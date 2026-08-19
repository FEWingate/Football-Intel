"""
GENERATE_GAME_BREAKDOWN.PY
===========================
Generation harness for the NEW report type: Game Breakdown — the deep,
market-neutral, both-teams read for one game. This is now the SOLE
expensive generation per game; the DFS and Prop Intelligence Reports will
later extract cheaply from this report's finished text rather than
re-processing the raw Evidence Package each time.

Same proven architecture as generate_dfs_breakdown.py (streaming, prompt
caching, truncation diagnostics) — just pointed at the new Master Prompt +
Game Breakdown Standard pairing and the new section order.

REQUIRES: pip install anthropic --break-system-packages
          export ANTHROPIC_API_KEY=your_own_key   (never commit this)

USAGE:
  python3 generate_game_breakdown.py --away BUF --home HOU --bootstrap
  python3 generate_game_breakdown.py --away BUF --home HOU --bootstrap --dry-run

OUTPUT: game_breakdowns/{wk|bootstrap}/{AWAY}_{HOME}.md — the report,
plus a sibling _prompt.json for review/debugging.
"""

import argparse
import json
import os
import sys
from datetime import datetime, timezone

PROMPTS_DIR = "prompts"
MASTER_PROMPT_PATH = f"{PROMPTS_DIR}/Coeus_Master_Prompt_v1.1.md"
GAME_BREAKDOWN_STANDARD_PATH = f"{PROMPTS_DIR}/Coeus_Game_Breakdown_Report_Standard_v2.5.md"
GOLD_STANDARD_EXAMPLE_PATH = f"{PROMPTS_DIR}/Coeus_Game_Breakdown_Gold_Standard_Example.md"

DEFAULT_MODEL = "claude-sonnet-5"

TASK_INSTRUCTION = """\
Generate the full Game Breakdown for this game, following the Game \
Breakdown Report Standard exactly. Produce, in this order:

1. Pregame Briefing
2. Injury & Availability Report
3. Matchup Statistics
4. Matchup Intelligence
5. Threat Intelligence
6. Hidden Intelligence & Contextual Analysis
7. Coeus Final Read (closes with Coeus Cheat Sheet)

This report is market-neutral — no DraftKings salaries, no DFS role or \
risk labels, no betting lines framing. Pure football analysis for BOTH \
teams, both sides of the ball.

Every raw statistic cited must carry its league rank; every rank cited \
must carry its raw statistic — in both directions, every time, per the \
Stat-Rank Pairing Rule. Section 6 (Hidden Intelligence & Contextual \
Analysis) is REQUIRED and must be its own clearly labeled section — \
never a phrase dropped inside another section or a forward-reference \
resolved elsewhere; each finding requires the Context Expansion element \
per Section 7 of the Standard. Coeus Cheat Sheet, closing Section 7, is \
REQUIRED and must be a plain list, not paragraphs — the reader should be \
able to scan the game's key numbers in a few seconds without reading the \
rest of the report. Pregame Briefing (Section 1) must state a broad \
thesis only, not the actual verdict — see the Standard's Section 1a on \
how this differs from Coeus Final Read, and Section 7's reservation rule \
on not spoiling Hidden Intelligence material there.

This report is also the sole source material for later, cheaper DFS and \
Props extraction steps that will NOT re-read the raw evidence package — \
keep player names exact and consistent with the evidence package, keep \
numeric claims precise rather than paraphrased, and give every \
DFS/Props-relevant player enough standalone context to be extracted from \
this report alone.

Base every claim ONLY on the evidence package below — Football Intel data \
first, per the Evidence Permission and Web Search Fallback rules. If a \
required fact isn't in the evidence package and you cannot find it via \
web search, say so explicitly rather than filling the gap.

EVIDENCE PACKAGE (this game only, frozen at the timestamp shown inside it):
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


def main():
    ap = argparse.ArgumentParser(description="Generate one game's Coeus Game Breakdown.")
    ap.add_argument("--away", required=True, help="Away team code, e.g. BUF")
    ap.add_argument("--home", required=True, help="Home team code, e.g. HOU")
    ap.add_argument("--week", type=int, default=None,
                     help="Week override. Defaults to whatever matchup/current.json says. "
                          "Ignored when --bootstrap is set.")
    ap.add_argument("--bootstrap", action="store_true",
                     help="Read from evidence_bootstrap/{away}_{home}.json instead of "
                          "evidence/wkNN/ — use this for an upcoming, not-yet-played game.")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--max-tokens", type=int, default=64000,
                     help="Set higher than the DFS harness's 48000 — this report is expected "
                          "to run longer (both teams, all four units, deeper positional "
                          "detail, more Hidden Intelligence findings). You only pay for "
                          "tokens actually generated, not the ceiling.")
    ap.add_argument("--dry-run", action="store_true",
                     help="Build and save the exact prompt without calling the API.")
    args = ap.parse_args()

    if args.bootstrap:
        evidence_path = f"evidence_bootstrap/{args.away}_{args.home}.json"
        evidence = load_json(evidence_path)
        if evidence is None:
            sys.exit(f"FATAL: {evidence_path} not found. Run "
                      f"build_evidence_package_bootstrap.py first, and confirm "
                      f"{args.away}/{args.home} is a real game in the DK file.")
        week = evidence["bootstrap_source"]["week"]

        # Bootstrap mode means the EVIDENCE came from a prior season's data
        # (no current-season stats exist yet) — but the SCHEDULE itself
        # (who plays whom, when) is usually real and public well before a
        # season starts, and build_matchup_stats.py's games-only build step
        # has no dependency on stats existing. If a real games/wkNN.json
        # for the ACTUAL target season already lists this exact matchup,
        # file the output under that real week instead of "bootstrap" —
        # games.html only ever looks in game_breakdowns/wkNN/, so this is
        # what makes a Game Breakdown button actually work on a real,
        # upcoming game's card, without needing any change to that
        # already-tested page. Falls back to "bootstrap" if no real
        # schedule match is found.
        #
        # MUST check the season field, not just the team pairing — the
        # bootstrap evidence's own season (e.g. 2025) is the FOUNDATION
        # data, one season behind the actual target game (e.g. 2026).
        # Confirmed by testing: without this check, a real, ALREADY-PLAYED
        # prior-season game between the same two teams (e.g. the actual
        # 2025 GB@MIN game this evidence was bootstrapped from) can match
        # by team pairing alone, incorrectly filing a real upcoming
        # preview under a week folder that actually belongs to a
        # completed, unrelated game.
        target_season = evidence["bootstrap_source"]["season"] + 1
        real_week = None
        for wk_num in range(1, 23):
            g = load_json(f"games/wk{wk_num:02d}.json")
            if not g or g.get("season") != target_season:
                continue
            for game in g.get("games", []):
                if game.get("away") == args.away and game.get("home") == args.home:
                    real_week = wk_num
                    break
            if real_week:
                break
        out_dir = f"game_breakdowns/wk{real_week:02d}" if real_week else "game_breakdowns/bootstrap"
    else:
        if args.week is None:
            current = load_json("matchup/current.json")
            if not current:
                sys.exit("FATAL: matchup/current.json not found and no --week given.")
            week = current["week"]
        else:
            week = args.week
        wk = f"wk{week:02d}"
        evidence_path = f"evidence/{wk}/{args.away}_{args.home}.json"
        evidence = load_json(evidence_path)
        if evidence is None:
            sys.exit(f"FATAL: {evidence_path} not found. Run build_evidence_package.py "
                      f"for week {week} first, and confirm {args.away}/{args.home} is a "
                      f"real game that week.")
        out_dir = f"game_breakdowns/{wk}"

    master_prompt = load_text(MASTER_PROMPT_PATH)
    gb_standard = load_text(GAME_BREAKDOWN_STANDARD_PATH)
    gold_example = load_text(GOLD_STANDARD_EXAMPLE_PATH)
    gold_example_framed = (
        "GOLD STANDARD EXAMPLE — APPROVED REFERENCE REPORT\n\n"
        "The following is a real, human-approved Game Breakdown, approved for its "
        "writing quality, analytical depth, and rigor — study it for VOICE, DEPTH, "
        "and RIGOR, this is the quality bar every report should meet.\n\n"
        "IMPORTANT — its SECTION STRUCTURE IS OUTDATED. This example predates a "
        "structural redesign and still uses the OLD section order (Game Overview, "
        "Team Unit Breakdown, Positional Matchups, Coverage & Scheme Notes, Hidden "
        "Intelligence, Threats to Watch, Injury & Availability Report, Keys to the "
        "Game, Bottom Line, Key Statistics). DO NOT follow this structure. Follow "
        "ONLY the Frozen Section Order given in the Standard above (Pregame "
        "Briefing, Injury & Availability Report, Matchup Statistics, Matchup "
        "Intelligence, Threat Intelligence, Hidden Intelligence & Contextual "
        "Analysis, Coeus Final Read) for the actual report you write below — the "
        "Standard's structure always wins over this example's structure if the two "
        "ever conflict.\n\n"
        "This is also a DIFFERENT, UNRELATED game (Green Bay @ Minnesota). Do not "
        "reuse any team name, player name, stat, or specific claim from this "
        "example in the report you are about to write — it is a quality reference "
        "only, not source material. Every fact in your actual report must come "
        "from the real evidence package for the actual game below, not from this "
        "example.\n\n"
        f"{gold_example}"
    )

    system = [
        {"type": "text", "text": master_prompt, "cache_control": {"type": "ephemeral"}},
        {"type": "text", "text": gb_standard, "cache_control": {"type": "ephemeral"}},
        {"type": "text", "text": gold_example_framed, "cache_control": {"type": "ephemeral"}},
    ]
    task = TASK_INSTRUCTION
    if args.bootstrap:
        task += ("\n\nIMPORTANT: this is a BOOTSTRAP evidence package for an UPCOMING game "
                 "that has NOT been played (see the 'game' and 'bootstrap_source' blocks "
                 "below). All team/player analytics are from the most recent completed "
                 "season, used as the best available foundation — this is NOT a review of "
                 "a past game.\n")
    user_content = task + json.dumps(evidence, separators=(",", ":"))

    os.makedirs(out_dir, exist_ok=True)
    out_stem = f"{out_dir}/{args.away}_{args.home}"

    season = evidence["bootstrap_source"]["season"] if args.bootstrap else evidence["season"]
    prompt_record = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "model": args.model, "max_tokens": args.max_tokens,
        "away": args.away, "home": args.home, "season": season, "week": week,
        "bootstrap": args.bootstrap,
        "evidence_source": evidence_path,
        "evidence_generated_at": evidence.get("generated_at"),
        "system_char_count": len(master_prompt) + len(gb_standard) + len(gold_example_framed),
        "user_char_count": len(user_content),
    }
    with open(f"{out_stem}_prompt.json", "w") as f:
        json.dump(prompt_record, f, indent=2)

    approx_input_tokens = (len(master_prompt) + len(gb_standard) + len(gold_example_framed) + len(user_content)) // 4
    print(f"Evidence: {evidence_path} (frozen at {evidence.get('generated_at')})")
    print(f"System prompt: {prompt_record['system_char_count']:,} chars "
          f"(Master Prompt + Game Breakdown Standard + Gold Standard Example, "
          f"cached after first call this session)")
    print(f"Evidence payload: {len(user_content):,} chars")
    print(f"Rough input size: ~{approx_input_tokens:,} tokens (estimate only, not exact)")

    if args.dry_run:
        with open(f"{out_stem}_prompt_full.txt", "w") as f:
            f.write("=== SYSTEM (Master Prompt) ===\n\n" + master_prompt +
                     "\n\n=== SYSTEM (Game Breakdown Standard) ===\n\n" + gb_standard +
                     "\n\n=== SYSTEM (Gold Standard Example) ===\n\n" + gold_example_framed +
                     "\n\n=== USER MESSAGE ===\n\n" + user_content)
        print(f"\nDRY RUN — no API call made. Full prompt written to "
              f"{out_stem}_prompt_full.txt for review. Remove --dry-run to actually generate.")
        return

    try:
        import anthropic
    except ImportError:
        sys.exit("FATAL: pip install anthropic --break-system-packages")

    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("FATAL: ANTHROPIC_API_KEY not set. export ANTHROPIC_API_KEY=your_own_key")

    client = anthropic.Anthropic()
    print(f"\nCalling {args.model} (streaming — this report is expected to run long)...\n")
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
    print(f"response content blocks: {block_types}")
    if response.stop_reason == "max_tokens":
        print("\nWARNING: response hit the max_tokens ceiling before finishing. "
              "The report below (if any) is INCOMPLETE. Re-run with a higher "
              "--max-tokens value.")
    if not report_text.strip():
        print("\nFATAL: no text content in the response — nothing written.")
        with open(f"{out_stem}.md", "w") as f:
            f.write(f"[EMPTY RESPONSE — stop_reason={response.stop_reason}, "
                     f"content block types={block_types}. Not a valid report.]")
        sys.exit(1)

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

    # Update the shared manifest for this directory so games.html (or any
    # other page) can check "does a real report exist for this game" via a
    # single small fetch, rather than guessing or trying every filename.
    # Read-modify-write since multiple separate script runs share one file.
    manifest_path = f"{out_dir}/manifest.json"
    manifest = load_json(manifest_path) or {"games": {}}
    manifest["games"][f"{args.away}_{args.home}"] = {
        "away": args.away, "home": args.home, "season": season, "week": week,
        "generated_at": prompt_record["generated_at"],
    }
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)

    print(f"\nWrote {out_stem}.md")
    print(f"Updated {manifest_path}")
    print(f"Actual usage: {usage.input_tokens:,} input tokens, {usage.output_tokens:,} output tokens")
    if getattr(usage, "cache_read_input_tokens", None):
        print(f"  ({usage.cache_read_input_tokens:,} of those input tokens served from cache)")


if __name__ == "__main__":
    main()
