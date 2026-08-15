"""
GENERATE_DFS_BREAKDOWN.PY
=========================
The actual Coeus generation harness — proof-of-concept scope: ONE game at a
time, per the agreed build sequence (prove the pipeline on one game before
scaling to a full slate).

Loads the Master Prompt + DFS Intelligence Report Standard as Coeus's system
prompt, loads one game's frozen Evidence Package, and calls the Claude API
to produce that game's DFS Breakdown (Section 19 of the DFS standard):
Executive DFS Summary, Featured DFS Plays, Recommended Stacks, Bring-Back
Candidates, Tournament Leverage Plays, Players to Avoid, DFS Risk Assessment,
DFS Takeaway.

REQUIRES: pip install anthropic --break-system-packages
          export ANTHROPIC_API_KEY=your_own_key   (never commit this)

USAGE:
  python3 generate_dfs_breakdown.py --away DET --home CHI
  python3 generate_dfs_breakdown.py --away DET --home CHI --dry-run
  python3 generate_dfs_breakdown.py --away DET --home CHI --model claude-haiku-4-5-20251001

PROMPT CACHING: the Master Prompt + DFS Standard (~55KB combined) are marked
as an ephemeral cache breakpoint. They're byte-for-byte identical across all
16 games every week, so caching means you're not paying full input-token
cost on that ~55KB sixteen separate times per week — only the per-game
evidence bundle (the part that actually changes) is priced fresh each call.
Verify current caching mechanics/pricing against Anthropic's docs before
assuming exact savings — this changes over time and isn't hardcoded here.

OUTPUT: dfs_breakdowns/wkNN/{AWAY}_{HOME}.md — the report itself, plus a
sibling _prompt.json with exactly what was sent, for review/debugging.
This is a proof-of-concept: nothing here auto-publishes anywhere. You read
it, you decide if the voice and reasoning are right, before we talk about
scaling to the full slate.
"""

import argparse
import json
import os
import sys
from datetime import datetime, timezone

PROMPTS_DIR = "prompts"
MASTER_PROMPT_PATH = f"{PROMPTS_DIR}/Coeus_Master_Prompt_v1.1.md"
DFS_STANDARD_PATH = f"{PROMPTS_DIR}/Coeus_DFS_Intelligence_Report_Standard_v1.4.md"

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
labeled section — not a phrase dropped inside another section, not a \
forward-reference resolved elsewhere. See the DFS Standard for the exact \
required shape of a Hidden Intelligence finding.

Base every claim ONLY on the evidence package below — Football Intel data \
first, per the Master Prompt's Evidence Permission and Web Search Fallback \
rules. If a required fact isn't in the evidence package and you cannot find \
it via web search, say so explicitly rather than filling the gap. Do not \
invent salaries, ownership, injuries, or matchup data not present below.

This is a single-game proof-of-concept generation, not the full slate-wide \
report — do not attempt to reference or compare against other games on the \
slate, since you don't have their evidence packages in this call.

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
    ap = argparse.ArgumentParser(description="Generate one game's Coeus DFS Breakdown.")
    ap.add_argument("--away", required=True, help="Away team code, e.g. DET")
    ap.add_argument("--home", required=True, help="Home team code, e.g. CHI")
    ap.add_argument("--week", type=int, default=None,
                     help="Week override. Defaults to whatever matchup/current.json says. "
                          "Ignored when --bootstrap is set.")
    ap.add_argument("--bootstrap", action="store_true",
                     help="Read from evidence_bootstrap/{away}_{home}.json instead of "
                          "evidence/wkNN/ — use this for an upcoming, not-yet-played game "
                          "assembled by build_evidence_package_bootstrap.py.")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--max-tokens", type=int, default=48000,
                     help="32000 was tested and still hit the ceiling once the required "
                          "Hidden Intelligence section was added — the report needed more "
                          "than that to finish 9 full sections. You only pay for tokens "
                          "actually generated, not the ceiling, so there's no cost downside "
                          "to real headroom here.")
    ap.add_argument("--dry-run", action="store_true",
                     help="Build and save the exact prompt without calling the API. "
                          "Use this to review what Coeus would actually see first.")
    args = ap.parse_args()

    if args.bootstrap:
        evidence_path = f"evidence_bootstrap/{args.away}_{args.home}.json"
        evidence = load_json(evidence_path)
        if evidence is None:
            sys.exit(f"FATAL: {evidence_path} not found. Run "
                      f"build_evidence_package_bootstrap.py first, and confirm "
                      f"{args.away}/{args.home} is a real game in the DK file.")
        wk = "bootstrap"
        week = evidence["bootstrap_source"]["week"]
        out_dir = "dfs_breakdowns/bootstrap"
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
        out_dir = f"dfs_breakdowns/{wk}"

    master_prompt = load_text(MASTER_PROMPT_PATH)
    dfs_standard = load_text(DFS_STANDARD_PATH)

    system = [
        {"type": "text", "text": master_prompt, "cache_control": {"type": "ephemeral"}},
        {"type": "text", "text": dfs_standard, "cache_control": {"type": "ephemeral"}},
    ]
    task = TASK_INSTRUCTION
    if args.bootstrap:
        task += ("\n\nIMPORTANT: this is a BOOTSTRAP evidence package for an UPCOMING game "
                 "that has NOT been played (see the 'game' and 'bootstrap_source' blocks "
                 "below). All team/player analytics are from the most recent completed "
                 "season, used as the best available foundation — this is NOT a review of "
                 "a past game. Write this as genuine pre-kickoff DFS analysis for a real "
                 "upcoming slate, not a retrospective.\n")
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
        "system_char_count": len(master_prompt) + len(dfs_standard),
        "user_char_count": len(user_content),
    }
    with open(f"{out_stem}_prompt.json", "w") as f:
        json.dump(prompt_record, f, indent=2)

    approx_input_tokens = (len(master_prompt) + len(dfs_standard) + len(user_content)) // 4
    print(f"Evidence: {evidence_path} (frozen at {evidence.get('generated_at')})")
    print(f"System prompt: {prompt_record['system_char_count']:,} chars "
          f"(Master Prompt + DFS Standard, cached after first call this session)")
    print(f"Evidence payload: {len(user_content):,} chars")
    print(f"Rough input size: ~{approx_input_tokens:,} tokens (estimate only, not exact)")

    if args.dry_run:
        with open(f"{out_stem}_prompt_full.txt", "w") as f:
            f.write("=== SYSTEM (Master Prompt) ===\n\n" + master_prompt +
                     "\n\n=== SYSTEM (DFS Standard) ===\n\n" + dfs_standard +
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
    print(f"\nCalling {args.model} (streaming — this can take a few minutes for a "
          f"report this size)...\n")
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

    # A truncated or empty response is a real failure, not a quiet edge case —
    # this is exactly what silently produced a 0-byte file before. Surface it
    # loudly instead of writing an empty .md and looking like success.
    block_types = [b.type for b in response.content]
    print(f"stop_reason: {response.stop_reason}")
    print(f"response content blocks: {block_types}")
    if response.stop_reason == "max_tokens":
        print("\nWARNING: response hit the max_tokens ceiling before finishing. "
              "The report below (if any) is INCOMPLETE. Re-run with a higher "
              "--max-tokens value.")
    if not report_text.strip():
        print("\nFATAL: no text content in the response — nothing written. "
              "This usually means max_tokens was hit before any report text was "
              "produced (all budget went to reasoning). Re-run with a higher "
              "--max-tokens value rather than trusting this as a real result.")
        # Still write what we have for debugging, but don't claim success.
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
    print("\nThis is a proof-of-concept single-game output. Read it, check the voice "
          "and reasoning against the Master Prompt's standard, before we talk about "
          "scaling to the full slate.")


if __name__ == "__main__":
    main()
