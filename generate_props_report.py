"""
GENERATE_PROPS_REPORT.PY
==========================
Generates the Props & Parlay Report: 3 favorite props per game, plus
five separate parlays (3/4/5/6/7-team), from real FanDuel data only.
Same architecture as generate_weekly_dfs_report.py — reads every
finished Game Breakdown for the slate plus real bookmaker data, one
API call for the whole slate, then runs the model's proposed parlays
through parlay_validator.py (a real, deterministic check) rather than
trusting Coeus's own arithmetic.

REQUIRES: pip install anthropic --break-system-packages
          export ANTHROPIC_API_KEY=...   (never commit)
          fanduel_props/latest.json must already exist — run
          build_fanduel_props.py first.

BLOCKED as of 2026-09-05 — see the Props & Parlay Report Standard's
OPEN ISSUES section: FanDuel spreads are currently absent from the
real data, and FanDuel's real player props are alt-line ladders, not
single-line props. This script will still RUN against whatever real
data exists (it does not invent what's missing), but the resulting
report inherits those same real gaps until a re-test closer to kickoff
resolves them.

USAGE:
    python3 generate_props_report.py
    python3 generate_props_report.py --dry-run
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone

from parlay_validator import validate_parlay, verify_legs_against_source, leg_key

PROMPTS_DIR = "prompts"
MASTER_PROMPT_PATH = f"{PROMPTS_DIR}/Coeus_Master_Prompt_v1.1.md"
PROPS_STANDARD_PATH = f"{PROMPTS_DIR}/Coeus_Props_Parlay_Report_Standard_v1.0.md"
FANDUEL_DATA_PATH = "fanduel_props/latest.json"

DEFAULT_MODEL = "claude-sonnet-5"
PARLAY_SIZES = [3, 4, 5, 6, 7]

TASK_INSTRUCTION = """\
Generate this week's Props & Parlay Report for the FULL slate below, \
following the Props & Parlay Report Standard exactly — 3 Favorite Props \
per game, then five separate parlays (3, 4, 5, 6, and 7 team), in that \
order. Lists and short entries only, per the No Paragraphs Rule — never \
prose paragraphs. Every football claim must come from one of the Game \
Breakdowns below; you do not have access to the original evidence \
packages behind them. Every market, line, and price must come from the \
real FanDuel data below — never invent a market or a single-line price \
where only ladder thresholds exist. Each of the five parlays MUST include \
its exact JSON block as specified in the Standard — this is not optional, \
a real program checks every parlay after you finish.

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
    """Same lookup as generate_weekly_dfs_report.py's — every finished
    Game Breakdown, deduplicated across every game_breakdowns/*/manifest.json."""
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


def extract_parlay_blocks(report_text):
    """Pulls all five PARLAY_N_TEAM JSON blocks out of the response.
    Returns {size: legs_list_or_None} — a missing or unparseable block
    for a given size is a real failure to report for THAT size, not
    something to silently skip past; the other sizes are unaffected."""
    result = {}
    for size in PARLAY_SIZES:
        tag = f"PARLAY_{size}_TEAM"
        match = re.search(rf"{tag}\s*\n(\[.*?\])", report_text, re.DOTALL)
        if not match:
            result[size] = None
            continue
        try:
            result[size] = json.loads(match.group(1))
        except json.JSONDecodeError:
            result[size] = None
    return result


def main():
    ap = argparse.ArgumentParser(description="Generate the Props & Parlay Report.")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--max-tokens", type=int, default=48000)
    ap.add_argument("--stake", type=float, default=100,
                     help="Hypothetical per-parlay stake used to compute a real "
                          "payout figure in the validator output. Default $100.")
    ap.add_argument("--dry-run", action="store_true",
                     help="Build and save the exact prompt without calling the API.")
    args = ap.parse_args()

    games = discover_all_games()
    if not games:
        sys.exit("FATAL: no finished Game Breakdowns found — nothing to build "
                 "a props report from yet.")

    fanduel_data = load_json(FANDUEL_DATA_PATH)
    if fanduel_data is None:
        sys.exit(f"FATAL: {FANDUEL_DATA_PATH} not found. Run build_fanduel_props.py first.")
    if not fanduel_data.get("props"):
        sys.exit("FATAL: fanduel_props/latest.json has zero FanDuel prop rows. "
                 "Nothing to build props/parlays from — re-run build_fanduel_props.py "
                 "closer to kickoff.")

    # Real-data-by-key index, for post-generation verification (same principle
    # as generate_weekly_dfs_report.py trusting the real slate data over
    # whatever the model wrote).
    real_by_key = {leg_key(r): r for r in fanduel_data["props"]}
    for event in fanduel_data.get("odds_events", []):
        for mkey, outcomes in event.get("markets", {}).items():
            for outcome in outcomes:
                row = {"canonical_event_id": event["canonical_event_id"],
                       "market_key": mkey, "player": outcome.get("name"),
                       "price": outcome.get("price")}
                real_by_key[leg_key(row)] = row

    gb_texts, folders_used = [], set()
    for folder, away, home in games:
        gb_path = os.path.join("game_breakdowns", folder, f"{away}_{home}.md")
        gb_texts.append(f"--- {away} @ {home} ---\n{load_text(gb_path)}")
        folders_used.add(folder)
    combined_breakdowns = "\n\n".join(gb_texts)

    master_prompt = load_text(MASTER_PROMPT_PATH)
    props_standard = load_text(PROPS_STANDARD_PATH)
    system = [
        {"type": "text", "text": master_prompt, "cache_control": {"type": "ephemeral"}},
        {"type": "text", "text": props_standard, "cache_control": {"type": "ephemeral"}},
    ]

    fanduel_json = json.dumps(fanduel_data, separators=(",", ":"))
    user_content = (TASK_INSTRUCTION + combined_breakdowns +
                     "\n\n=== REAL FANDUEL PROPS + ODDS DATA (this slate only) ===\n" +
                     fanduel_json)

    out_dir = f"props_reports/{list(folders_used)[0]}" if len(folders_used) == 1 else "props_reports/mixed"
    os.makedirs(out_dir, exist_ok=True)
    out_stem = f"{out_dir}/props_parlay_report"

    prompt_record = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "model": args.model, "max_tokens": args.max_tokens,
        "games_included": [f"{a}_{h}" for _, a, h in games],
        "fanduel_data_source": FANDUEL_DATA_PATH,
        "system_char_count": len(master_prompt) + len(props_standard),
        "user_char_count": len(user_content),
    }
    with open(f"{out_stem}_prompt.json", "w") as f:
        json.dump(prompt_record, f, indent=2)

    approx_input_tokens = (len(master_prompt) + len(props_standard) + len(user_content)) // 4
    print(f"Games included: {len(games)}")
    print(f"FanDuel data: {len(fanduel_data['props'])} prop rows, "
          f"{len(fanduel_data.get('odds_events', []))} odds events")
    print(f"Rough input size: ~{approx_input_tokens:,} tokens (estimate only)")

    if args.dry_run:
        with open(f"{out_stem}_prompt_full.txt", "w") as f:
            f.write("=== SYSTEM (Master Prompt) ===\n\n" + master_prompt +
                     "\n\n=== SYSTEM (Props & Parlay Standard) ===\n\n" + props_standard +
                     "\n\n=== USER MESSAGE ===\n\n" + user_content)
        print(f"\nDRY RUN — no API call made. Prompt written to {out_stem}_prompt_full.txt")
        return

    try:
        import anthropic
    except ImportError:
        sys.exit("FATAL: pip install anthropic --break-system-packages")
    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("FATAL: ANTHROPIC_API_KEY not set.")

    client = anthropic.Anthropic()
    print(f"\nCalling {args.model} (streaming)...\n")
    with client.messages.stream(
        model=args.model, max_tokens=args.max_tokens, system=system,
        messages=[{"role": "user", "content": user_content}],
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)
        response = stream.get_final_message()
    print()

    report_text = "".join(block.text for block in response.content if block.type == "text")
    print(f"stop_reason: {response.stop_reason}")
    if response.stop_reason == "max_tokens":
        print("WARNING: hit the max_tokens ceiling before finishing — INCOMPLETE.")
    if not report_text.strip():
        sys.exit("FATAL: empty response, nothing written.")

    with open(f"{out_stem}.md", "w") as f:
        f.write(report_text)
    usage = response.usage
    prompt_record["usage"] = {"input_tokens": usage.input_tokens, "output_tokens": usage.output_tokens}
    with open(f"{out_stem}_prompt.json", "w") as f:
        json.dump(prompt_record, f, indent=2)
    print(f"\nWrote {out_stem}.md — {usage.input_tokens:,} input / {usage.output_tokens:,} output tokens")

    # The real check — independent of whatever Coeus asserted in prose. Also
    # collected into structured form (not just printed) so the Prop Center
    # page can render real parlay cards from validated data, rather than
    # displaying Coeus's raw prose+JSON as-is.
    parlays = extract_parlay_blocks(report_text)
    parlay_results = {}
    print("\n" + "=" * 60)
    for size in PARLAY_SIZES:
        legs = parlays[size]
        print(f"\n{size}-TEAM PARLAY VALIDATION:")
        if legs is None:
            print(f"  FAILED — could not find or parse a PARLAY_{size}_TEAM JSON "
                  f"block. This parlay has NOT been checked. Do not trust it.")
            parlay_results[size] = {"valid": False, "errors": ["Could not parse this parlay's JSON block."],
                                     "warnings": [], "result": None, "legs": None, "mismatches": []}
            continue
        verified_legs, mismatches = verify_legs_against_source(legs, real_by_key)
        if mismatches:
            print(f"  {len(mismatches)} leg(s) do NOT exist in the real FanDuel data "
                  f"provided — Coeus referenced something not actually on the board:")
            for m in mismatches:
                print(f"    - {m}")
        is_valid, errors, warnings, result = validate_parlay(
            verified_legs, expected_size=size, stake=args.stake)
        passed = is_valid and not mismatches
        if passed:
            print(f"  PASSED — {result['legs']} real legs, combined odds "
                  f"{result['combined_decimal']} (American {result['combined_american']:+d}), "
                  f"${args.stake:.0f} stake -> ${result['payout']:.2f} payout.")
        else:
            print(f"  FAILED:")
            for e in errors:
                print(f"    - {e}")
        for w in warnings:
            print(f"  NOTE: {w}")
        parlay_results[size] = {
            "valid": passed, "errors": errors, "warnings": warnings,
            "result": result, "legs": verified_legs,
            "mismatches": [m for m in mismatches],
        }
    print("=" * 60)

    # Structured companion file — this is what the Prop Center page actually
    # reads. The raw markdown is included too (for a "full report" view) but
    # the parlay cards render from parlay_results, which is real, validated
    # data, not text the page would need to re-parse itself.
    report_json = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "games_included": [f"{a}_{h}" for _, a, h in games],
        "stake_used_for_payout_examples": args.stake,
        "markdown": report_text,
        "parlays": {str(size): parlay_results[size] for size in PARLAY_SIZES},
    }
    with open(f"{out_stem}.json", "w") as f:
        json.dump(report_json, f)
    print(f"Wrote {out_stem}.json (structured, for the Prop Center page)")

    os.makedirs("props_reports", exist_ok=True)
    with open("props_reports/latest.json", "w") as f:
        json.dump({
            "generated_at": report_json["generated_at"],
            "report_path": f"{out_stem}.json",
        }, f)
    print(f"Wrote props_reports/latest.json — points to {out_stem}.json")


if __name__ == "__main__":
    main()
