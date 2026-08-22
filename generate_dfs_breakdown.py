"""
GENERATE_DFS_BREAKDOWN.PY
=========================
REWRITTEN for the extraction architecture (see DFS Standard v1.5's
changelog for the full reasoning). This script no longer reads a raw
Evidence Package — it reads two things only:

  1. The finished Game Breakdown for this exact game (wherever it
     actually lives — bootstrap/ or a real wkNN/ folder, auto-detected
     from every game_breakdowns/*/manifest.json, same lookup pattern
     already proven working in intel_reports.html's Coeus Game
     Breakdowns tab).
  2. Real DraftKings salary/slate data for this game's players, from
     dfs/wkNN.json (built by build_dfs.py from the current DK export).

This is what makes it cheap: the expensive reasoning already happened
once, in the Game Breakdown (~90-100K input tokens). This script's
input is a few thousand words of already-written analysis plus a
filtered player list — a small fraction of that cost.

REQUIRES: pip install anthropic --break-system-packages
          export ANTHROPIC_API_KEY=your_own_key   (never commit this)

USAGE:
  python3 generate_dfs_breakdown.py --away DET --home CHI
  python3 generate_dfs_breakdown.py --away DET --home CHI --dry-run

OUTPUT: dfs_breakdowns/{same folder the Game Breakdown was found in}/
{AWAY}_{HOME}.md, plus a sibling _prompt.json for review/debugging.
"""

import argparse
import json
import os
import sys
from datetime import datetime, timezone

PROMPTS_DIR = "prompts"
MASTER_PROMPT_PATH = f"{PROMPTS_DIR}/Coeus_Master_Prompt_v1.1.md"
DFS_STANDARD_PATH = f"{PROMPTS_DIR}/Coeus_DFS_Intelligence_Report_Standard_v1.5.md"

DEFAULT_MODEL = "claude-sonnet-5"

TASK_INSTRUCTION = """\
Generate the DFS Breakdown for this single game, following Section 19 of the \
DFS Intelligence Report Standard exactly — this is the game-specific section, \
not the full slate-wide weekly report. Produce, in this order:

1. Executive DFS Summary
2. Featured DFS Plays
3. Hidden Intelligence
4. Recommended Stacks
5. Bring-Back Candidates
6. Tournament Leverage Plays
7. Players to Avoid
8. DFS Risk Assessment
9. DFS Takeaway

Section 3, Hidden Intelligence, is REQUIRED and must be its own clearly \
labeled section. Per the Standard's mechanism section: this report does NOT \
discover new Hidden Intelligence — select from what the Game Breakdown below \
already found, and explain what it changes for a DFS decision specifically.

Base every football claim ONLY on the Game Breakdown text below — you do not \
have access to the original evidence package, so you cannot verify or add to \
what it says. Base every salary/eligibility claim ONLY on the DK slate data \
below. If a required fact isn't in either source and you cannot find it via \
web search, say so explicitly rather than filling the gap. Do not invent \
salaries, ownership, injuries, or matchup data not present below.

This is a single-game generation, not the full slate-wide report — do not \
attempt to reference or compare against other games on the slate, since you \
don't have their material in this call.

=== GAME BREAKDOWN (the finished, already-vetted football analysis for this game) ===
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


def find_game_breakdown(away, home):
    """Check every game_breakdowns/*/manifest.json for this away/home pair,
    same lookup pattern already proven working in intel_reports.html's
    Coeus Game Breakdowns tab. Returns (folder, md_path) or (None, None)."""
    base = "game_breakdowns"
    if not os.path.isdir(base):
        return None, None
    key = f"{away}_{home}"
    for folder in sorted(os.listdir(base)):
        manifest_path = os.path.join(base, folder, "manifest.json")
        manifest = load_json(manifest_path)
        if manifest and key in (manifest.get("games") or {}):
            md_path = os.path.join(base, folder, f"{key}.md")
            if os.path.exists(md_path):
                return folder, md_path
    return None, None


def discover_all_games():
    """Every (away, home) pair with a finished Game Breakdown, across every
    game_breakdowns/*/manifest.json — deduplicated, since --all needs the
    full real slate, not just whichever folder happens to be checked."""
    base = "game_breakdowns"
    if not os.path.isdir(base):
        return []
    seen = {}
    for folder in sorted(os.listdir(base)):
        manifest = load_json(os.path.join(base, folder, "manifest.json"))
        for key, g in (manifest.get("games") or {}).items() if manifest else []:
            if key not in seen:
                seen[key] = (g["away"], g["home"])
    return list(seen.values())


def process_one_game(away, home, args, master_prompt, dfs_standard):
    """Everything needed for one game's DFS Breakdown. Returns True on a
    real, written report; False on any failure — --all uses this to keep
    going through the rest of the slate rather than stopping on one bad
    game, and prints a clear summary at the end."""
    folder, gb_path = find_game_breakdown(away, home)
    if not gb_path:
        print(f"[{away}/{home}] SKIPPED — no finished Game Breakdown found in any "
              f"game_breakdowns/*/manifest.json.")
        return False
    game_breakdown_text = load_text(gb_path)

    if args.dfs_week is None:
        current = load_json("matchup/current.json")
        if not current:
            print(f"[{away}/{home}] SKIPPED — matchup/current.json not found and no "
                  f"--dfs-week given.")
            return False
        dfs_week = current["week"]
    else:
        dfs_week = args.dfs_week
    dfs_path = f"dfs/wk{dfs_week:02d}.json"
    dfs_json = load_json(dfs_path)
    if dfs_json is None:
        print(f"[{away}/{home}] SKIPPED — {dfs_path} not found. Run build_dfs.py first.")
        return False

    teams = (away, home)
    game_players = [p for p in dfs_json.get("players", []) if p.get("team") in teams]
    if not game_players:
        print(f"[{away}/{home}] SKIPPED — no players found in {dfs_path}; this game may "
              f"not be part of the current DK Classic slate.")
        return False

    out_dir = f"dfs_breakdowns/{folder}"
    out_stem = f"{out_dir}/{away}_{home}"
    if os.path.exists(f"{out_stem}.md") and not args.force:
        print(f"[{away}/{home}] SKIPPED — {out_stem}.md already exists. Use --force to "
              f"regenerate (real cost — this re-spends on a game already done).")
        return False

    system = [
        {"type": "text", "text": master_prompt, "cache_control": {"type": "ephemeral"}},
        {"type": "text", "text": dfs_standard, "cache_control": {"type": "ephemeral"}},
    ]

    salary_json = json.dumps({"away": away, "home": home,
                               "players": game_players}, separators=(",", ":"))
    user_content = (TASK_INSTRUCTION + game_breakdown_text +
                     "\n\n=== DRAFTKINGS SLATE DATA (this game's players only) ===\n" +
                     salary_json)

    os.makedirs(out_dir, exist_ok=True)

    prompt_record = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "model": args.model, "max_tokens": args.max_tokens,
        "away": away, "home": home,
        "game_breakdown_source": gb_path, "dfs_salary_source": dfs_path,
        "system_char_count": len(master_prompt) + len(dfs_standard),
        "user_char_count": len(user_content),
    }
    with open(f"{out_stem}_prompt.json", "w") as f:
        json.dump(prompt_record, f, indent=2)

    approx_input_tokens = (len(master_prompt) + len(dfs_standard) + len(user_content)) // 4
    print(f"\n=== [{away}/{home}] ===")
    print(f"Game Breakdown: {gb_path} ({len(game_breakdown_text):,} chars)")
    print(f"DK salary data: {dfs_path}, {len(game_players)} players for this game")
    print(f"Rough input size: ~{approx_input_tokens:,} tokens (estimate only, not exact)")

    if args.dry_run:
        with open(f"{out_stem}_prompt_full.txt", "w") as f:
            f.write("=== SYSTEM (Master Prompt) ===\n\n" + master_prompt +
                     "\n\n=== SYSTEM (DFS Standard) ===\n\n" + dfs_standard +
                     "\n\n=== USER MESSAGE ===\n\n" + user_content)
        print(f"DRY RUN — no API call made. Prompt written to {out_stem}_prompt_full.txt")
        return True

    try:
        import anthropic
    except ImportError:
        sys.exit("FATAL: pip install anthropic --break-system-packages")
    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("FATAL: ANTHROPIC_API_KEY not set. export ANTHROPIC_API_KEY=your_own_key")

    client = anthropic.Anthropic()
    print(f"Calling {args.model} (streaming)...\n")
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
    block_types = [b.type for b in response.content]
    print(f"stop_reason: {response.stop_reason}")
    if response.stop_reason == "max_tokens":
        print("WARNING: hit the max_tokens ceiling before finishing — INCOMPLETE. "
              "Re-run this game alone with a higher --max-tokens value.")
    if not report_text.strip():
        print(f"[{away}/{home}] FAILED — empty response, nothing written.")
        with open(f"{out_stem}.md", "w") as f:
            f.write(f"[EMPTY RESPONSE — stop_reason={response.stop_reason}, "
                     f"content block types={block_types}. Not a valid report.]")
        return False

    with open(f"{out_stem}.md", "w") as f:
        f.write(report_text)

    usage = response.usage
    prompt_record["usage"] = {
        "input_tokens": usage.input_tokens, "output_tokens": usage.output_tokens,
        "cache_creation_input_tokens": getattr(usage, "cache_creation_input_tokens", None),
        "cache_read_input_tokens": getattr(usage, "cache_read_input_tokens", None),
    }
    with open(f"{out_stem}_prompt.json", "w") as f:
        json.dump(prompt_record, f, indent=2)

    print(f"Wrote {out_stem}.md — {usage.input_tokens:,} input / {usage.output_tokens:,} output tokens"
          + (f" ({usage.cache_read_input_tokens:,} cached)"
             if getattr(usage, "cache_read_input_tokens", None) else ""))
    return True


def main():
    ap = argparse.ArgumentParser(description="Generate Coeus DFS Breakdowns by extracting "
                                              "from finished Game Breakdowns.")
    ap.add_argument("--away", help="Away team code, e.g. DET. Required unless --all.")
    ap.add_argument("--home", help="Home team code, e.g. CHI. Required unless --all.")
    ap.add_argument("--all", action="store_true",
                     help="Run every game that has a finished Game Breakdown. Skips games "
                          "that already have a DFS Breakdown, unless --force is also given.")
    ap.add_argument("--force", action="store_true",
                     help="With --all, regenerate games that already have a DFS Breakdown too "
                          "— real cost, re-spends on games already done.")
    ap.add_argument("--dfs-week", type=int, default=None,
                     help="Which dfs/wkNN.json (real DK salary data) to use. Defaults to "
                          "matchup/current.json's week — the current, real DK export.")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--max-tokens", type=int, default=48000,
                     help="Game Breakdown needed this much for 7-10 full sections from raw "
                          "evidence; this report is shorter (extraction, not fresh analysis) "
                          "but kept at the same ceiling until real generations show a lower "
                          "one is safe — you only pay for tokens actually generated.")
    ap.add_argument("--dry-run", action="store_true",
                     help="Build and save the exact prompt(s) without calling the API.")
    args = ap.parse_args()

    if not args.all and not (args.away and args.home):
        sys.exit("FATAL: give --away and --home for one game, or --all for the whole slate.")

    master_prompt = load_text(MASTER_PROMPT_PATH)
    dfs_standard = load_text(DFS_STANDARD_PATH)

    if args.all:
        games = discover_all_games()
        if not games:
            sys.exit("FATAL: no finished Game Breakdowns found anywhere in game_breakdowns/*/"
                     "manifest.json — nothing to extract from yet.")
        print(f"Found {len(games)} game(s) with a finished Game Breakdown.\n")
        results = [process_one_game(away, home, args, master_prompt, dfs_standard)
                   for away, home in games]
        done, skipped = sum(results), len(results) - sum(results)
        print(f"\n=== DONE — {done} written, {skipped} skipped/failed out of {len(games)} ===")
    else:
        ok = process_one_game(args.away, args.home, args, master_prompt, dfs_standard)
        if not ok:
            sys.exit(1)


if __name__ == "__main__":
    main()
