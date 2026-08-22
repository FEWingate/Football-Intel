"""
GENERATE_WEEKLY_DFS_REPORT.PY
==============================
Replaces reading individual per-game DFS Breakdowns entirely, per Frank's
direct feedback (Aug 2026) — one scannable, list-based report for the
whole slate, not another long-form report on top of the Game Breakdowns
already read. Reads every finished Game Breakdown for the slate plus the
full real DraftKings salary data, in one call.

The Lineup of the Week is genuinely checked, not just asserted: Coeus is
required to output it as a parseable JSON block (see the Standard), and
this script runs that block through dfs_lineup_validator.py — a real,
deterministic check against DraftKings' actual roster rules — after
generation. If Coeus's proposed lineup fails that check, this script
says so loudly rather than publishing it as if it were valid.

REQUIRES: pip install anthropic --break-system-packages
          export ANTHROPIC_API_KEY=your_own_key   (never commit this)

USAGE:
  python3 generate_weekly_dfs_report.py
  python3 generate_weekly_dfs_report.py --dry-run

OUTPUT: dfs_weekly/{season}_wk{NN}.md (or bootstrap/, matching whichever
folder(s) the Game Breakdowns were actually found in), plus a sibling
_prompt.json and a validator result printed directly to the terminal.
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone

from dfs_lineup_validator import validate_dk_lineup

PROMPTS_DIR = "prompts"
MASTER_PROMPT_PATH = f"{PROMPTS_DIR}/Coeus_Master_Prompt_v1.1.md"
WEEKLY_STANDARD_PATH = f"{PROMPTS_DIR}/Coeus_Weekly_DFS_Report_Standard_v1.2.md"

DEFAULT_MODEL = "claude-sonnet-5"

TASK_INSTRUCTION = """\
Generate this week's Weekly DFS Report for the FULL slate below, following \
the Coeus Weekly DFS Report Standard exactly — Top Plays by Position, \
Players to Fade, Stacks, and Coeus Lineup of the Week, in that order. \
Lists and short entries only, per the No Paragraphs Rule — never prose \
paragraphs. Every claim must come from one of the Game Breakdowns below; \
you do not have access to the original evidence packages behind them. \
Every salary and eligibility claim must come from the real DK slate data \
below. The Lineup of the Week MUST include the exact JSON block format \
specified in the Standard — this is not optional, a real program checks \
it after you finish.

=== GAME BREAKDOWNS (every finished game on this slate) ===
"""


def load_text(path):
    if not os.path.exists(path):
        sys.exit(f"FATAL: {path} not found.")
    with open(path) as f:
        return f.read()


def load_json(path):
    if not os.path.exists(path):
        return None
    with open(path) as f:
        return json.load(f)


def discover_all_games():
    """Same lookup as generate_dfs_breakdown.py's --all — every (folder,
    away, home) with a finished Game Breakdown, deduplicated across every
    game_breakdowns/*/manifest.json."""
    base = "game_breakdowns"
    if not os.path.isdir(base):
        return []
    seen = {}
    for folder in sorted(os.listdir(base)):
        manifest = load_json(os.path.join(base, folder, "manifest.json"))
        for key, g in (manifest.get("games") or {}).items() if manifest else []:
            if key not in seen:
                seen[key] = (folder, g["away"], g["home"])
    return list(seen.values())


def extract_lineup_json(report_text):
    """Pull the LINEUP_OF_THE_WEEK JSON block out of the response. Returns
    a list of 9 player dicts, or None if the block wasn't found/parseable
    — a missing block is a real failure to report, not something to
    silently skip past."""
    match = re.search(r"LINEUP_OF_THE_WEEK\s*\n(\[.*?\])", report_text, re.DOTALL)
    if not match:
        return None
    try:
        return json.loads(match.group(1))
    except json.JSONDecodeError:
        return None


def enrich_lineup_with_game_info(lineup, dfs_json):
    """The JSON block only has name/pos/team/salary — the validator's
    multi-game check needs game_info too, so look each player up in the
    real DK slate data by name+team to attach it, rather than trust
    whatever Coeus may or may not have included."""
    by_key = {(p.get("name"), p.get("team")): p for p in dfs_json.get("players", [])}
    for entry in lineup:
        real = by_key.get((entry.get("name"), entry.get("team")))
        if real:
            entry["game_info"] = real.get("game_info")
            # Trust the real salary from the slate data over whatever
            # Coeus wrote, in case of a transcription slip — the
            # validator should check the real number, not a copy of it.
            entry["salary"] = real.get("salary", entry.get("salary"))
    return lineup


def main():
    ap = argparse.ArgumentParser(description="Generate the full-slate Weekly DFS Report.")
    ap.add_argument("--dfs-week", type=int, default=None,
                     help="Which dfs/wkNN.json (real DK salary data) to use. Defaults to "
                          "matchup/current.json's week.")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--max-tokens", type=int, default=48000,
                     help="16000 was tried first and hit the ceiling before producing any "
                          "output at all — covering 5 positions, fades, several stacks, and "
                          "a full validated lineup across the whole slate needs real room "
                          "even in list format. Matches the Game Breakdown's proven-safe "
                          "ceiling; you only pay for tokens actually generated, not this "
                          "number, so there's no cost downside to headroom here.")
    ap.add_argument("--dry-run", action="store_true",
                     help="Build and save the exact prompt without calling the API.")
    args = ap.parse_args()

    games = discover_all_games()
    if not games:
        sys.exit("FATAL: no finished Game Breakdowns found anywhere in game_breakdowns/*/"
                 "manifest.json — nothing to build a slate report from yet.")

    if args.dfs_week is None:
        current = load_json("matchup/current.json")
        if not current:
            sys.exit("FATAL: matchup/current.json not found and no --dfs-week given.")
        dfs_week = current["week"]
    else:
        dfs_week = args.dfs_week
    dfs_path = f"dfs/wk{dfs_week:02d}.json"
    dfs_json = load_json(dfs_path)
    if dfs_json is None:
        sys.exit(f"FATAL: {dfs_path} not found. Run build_dfs.py first.")

    # A finished Game Breakdown existing is NOT the same as a game being on
    # the current DK Classic slate — e.g. Sunday/Monday night games added
    # via generate_game_breakdown.py's --extra-away/--extra-home have real
    # analysis but no DK salary data at all. Sending Coeus a full Game
    # Breakdown it can never actually build DFS content from is wasted
    # input cost, not just a missing feature — filter those out here,
    # same DK-Classic-slate scope the per-game extraction already respects.
    teams_on_slate = {p.get("team") for p in dfs_json.get("players", [])}
    slate_games, dropped_games = [], []
    for folder, away, home in games:
        if away in teams_on_slate or home in teams_on_slate:
            slate_games.append((folder, away, home))
        else:
            dropped_games.append((away, home))
    games = slate_games
    if not games:
        sys.exit(f"FATAL: none of the {len(dropped_games)} finished Game Breakdown(s) have "
                 f"any players in {dfs_path} — nothing to build a slate report from.")
    if dropped_games:
        print(f"Excluded {len(dropped_games)} game(s) with a Game Breakdown but no DK "
              f"Classic slate data (not part of this week's main slate): "
              f"{', '.join(f'{a}/{h}' for a, h in dropped_games)}")

    gb_texts = []
    folders_used = set()
    for folder, away, home in games:
        gb_path = os.path.join("game_breakdowns", folder, f"{away}_{home}.md")
        gb_texts.append(f"--- {away} @ {home} ---\n{load_text(gb_path)}")
        folders_used.add(folder)
    combined_breakdowns = "\n\n".join(gb_texts)

    master_prompt = load_text(MASTER_PROMPT_PATH)
    weekly_standard = load_text(WEEKLY_STANDARD_PATH)
    system = [
        {"type": "text", "text": master_prompt, "cache_control": {"type": "ephemeral"}},
        {"type": "text", "text": weekly_standard, "cache_control": {"type": "ephemeral"}},
    ]

    salary_json = json.dumps(dfs_json.get("players", []), separators=(",", ":"))
    user_content = (TASK_INSTRUCTION + combined_breakdowns +
                     "\n\n=== FULL DK SLATE DATA (every player on the current slate) ===\n" +
                     salary_json)

    # Output folder: if every Game Breakdown came from one folder, use it;
    # a mixed slate (some bootstrap, some real wkNN) is a real edge case
    # worth its own clear label rather than silently picking one.
    out_dir = f"dfs_weekly/{list(folders_used)[0]}" if len(folders_used) == 1 else "dfs_weekly/mixed"
    os.makedirs(out_dir, exist_ok=True)
    out_stem = f"{out_dir}/wk{dfs_week:02d}"

    prompt_record = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "model": args.model, "max_tokens": args.max_tokens,
        "games_included": [f"{a}_{h}" for _, a, h in games],
        "dfs_salary_source": dfs_path,
        "system_char_count": len(master_prompt) + len(weekly_standard),
        "user_char_count": len(user_content),
    }
    with open(f"{out_stem}_prompt.json", "w") as f:
        json.dump(prompt_record, f, indent=2)

    approx_input_tokens = (len(master_prompt) + len(weekly_standard) + len(user_content)) // 4
    print(f"Games included: {len(games)} — {', '.join(f'{a}/{h}' for _, a, h in games)}")
    print(f"DK salary data: {dfs_path}, {len(dfs_json.get('players', []))} total players")
    print(f"Rough input size: ~{approx_input_tokens:,} tokens (estimate only, not exact)")

    if args.dry_run:
        with open(f"{out_stem}_prompt_full.txt", "w") as f:
            f.write("=== SYSTEM (Master Prompt) ===\n\n" + master_prompt +
                     "\n\n=== SYSTEM (Weekly DFS Standard) ===\n\n" + weekly_standard +
                     "\n\n=== USER MESSAGE ===\n\n" + user_content)
        print(f"\nDRY RUN — no API call made. Prompt written to {out_stem}_prompt_full.txt")
        return

    try:
        import anthropic
    except ImportError:
        sys.exit("FATAL: pip install anthropic --break-system-packages")
    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("FATAL: ANTHROPIC_API_KEY not set. export ANTHROPIC_API_KEY=your_own_key")

    client = anthropic.Anthropic()
    print(f"\nCalling {args.model} (streaming)...\n")
    with client.messages.stream(
        model=args.model,
        max_tokens=args.max_tokens,
        system=system,
        messages=[{"role": "user", "content": user_content}],
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)
        response = stream.get_final_message()
    print()

    report_text = "".join(block.text for block in response.content if block.type == "text")
    print(f"stop_reason: {response.stop_reason}")
    if response.stop_reason == "max_tokens":
        print("WARNING: hit the max_tokens ceiling before finishing — INCOMPLETE. "
              "Re-run with a higher --max-tokens value.")
    if not report_text.strip():
        sys.exit("FATAL: empty response, nothing written.")

    with open(f"{out_stem}.md", "w") as f:
        f.write(report_text)

    usage = response.usage
    prompt_record["usage"] = {
        "input_tokens": usage.input_tokens, "output_tokens": usage.output_tokens,
        "cache_read_input_tokens": getattr(usage, "cache_read_input_tokens", None),
    }
    with open(f"{out_stem}_prompt.json", "w") as f:
        json.dump(prompt_record, f, indent=2)
    print(f"\nWrote {out_stem}.md — {usage.input_tokens:,} input / {usage.output_tokens:,} output tokens")

    # The real check — independent of whatever Coeus asserted in prose.
    lineup = extract_lineup_json(report_text)
    print("\n" + "=" * 60)
    if lineup is None:
        print("LINEUP VALIDATION: FAILED — could not find or parse a "
              "LINEUP_OF_THE_WEEK JSON block in the response. The report "
              "was still written, but its proposed lineup has NOT been "
              "checked against DraftKings' real rules. Do not trust it "
              "as legal without checking by hand.")
    else:
        lineup = enrich_lineup_with_game_info(lineup, dfs_json)
        is_valid, errors, total_salary = validate_dk_lineup(lineup)
        if is_valid:
            print(f"LINEUP VALIDATION: PASSED — real, legal DraftKings lineup, "
                  f"${total_salary:,} of $50,000 used (${50000 - total_salary:,} unused).")
        else:
            print(f"LINEUP VALIDATION: FAILED — Coeus's proposed lineup is NOT a "
                  f"legal DraftKings lineup as written:")
            for e in errors:
                print(f"  - {e}")
            print("Do not submit this lineup as-is. This is exactly the failure mode "
                  "the validator exists to catch before it reaches you.")
    print("=" * 60)


if __name__ == "__main__":
    main()
