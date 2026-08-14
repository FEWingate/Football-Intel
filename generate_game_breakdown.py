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
GAME_BREAKDOWN_STANDARD_PATH = f"{PROMPTS_DIR}/Coeus_Game_Breakdown_Report_Standard_v1.2.md"

DEFAULT_MODEL = "claude-sonnet-5"

TASK_INSTRUCTION = """\
Generate the full Game Breakdown for this game, following the Game \
Breakdown Report Standard exactly. Produce, in this order:

1. Game Overview
2. Team Unit Breakdown
3. Positional Matchups
4. Coverage & Scheme Notes
5. Hidden Intelligence
6. Threats to Watch
7. Injury & Availability Report
8. Keys to the Game
9. Bottom Line

This report is market-neutral — no DraftKings salaries, no DFS role or \
risk labels, no betting lines framing. Pure football analysis for BOTH \
teams, both sides of the ball.

Every raw statistic cited must carry its league rank; every rank cited \
must carry its raw statistic — in both directions, every time, per the \
Stat-Rank Pairing Rule. Section 3 (Hidden Intelligence) is REQUIRED and \
must be its own clearly labeled section — never a phrase dropped inside \
another section or a forward-reference resolved elsewhere.

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
        out_dir = "game_breakdowns/bootstrap"
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

    system = [
        {"type": "text", "text": master_prompt, "cache_control": {"type": "ephemeral"}},
        {"type": "text", "text": gb_standard, "cache_control": {"type": "ephemeral"}},
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
        "system_char_count": len(master_prompt) + len(gb_standard),
        "user_char_count": len(user_content),
    }
    with open(f"{out_stem}_prompt.json", "w") as f:
        json.dump(prompt_record, f, indent=2)

    approx_input_tokens = (len(master_prompt) + len(gb_standard) + len(user_content)) // 4
    print(f"Evidence: {evidence_path} (frozen at {evidence.get('generated_at')})")
    print(f"System prompt: {prompt_record['system_char_count']:,} chars "
          f"(Master Prompt + Game Breakdown Standard, cached after first call this session)")
    print(f"Evidence payload: {len(user_content):,} chars")
    print(f"Rough input size: ~{approx_input_tokens:,} tokens (estimate only, not exact)")

    if args.dry_run:
        with open(f"{out_stem}_prompt_full.txt", "w") as f:
            f.write("=== SYSTEM (Master Prompt) ===\n\n" + master_prompt +
                     "\n\n=== SYSTEM (Game Breakdown Standard) ===\n\n" + gb_standard +
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

    print(f"\nWrote {out_stem}.md")
    print(f"Actual usage: {usage.input_tokens:,} input tokens, {usage.output_tokens:,} output tokens")
    if getattr(usage, "cache_read_input_tokens", None):
        print(f"  ({usage.cache_read_input_tokens:,} of those input tokens served from cache)")


if __name__ == "__main__":
    main()
