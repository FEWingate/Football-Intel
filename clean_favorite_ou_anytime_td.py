#!/usr/bin/env python3
"""
REAL ONE-OFF CLEANUP (2026-10-01), per Frank's direct catch: Prop
Center's Favorite O/U tab was showing real player_anytime_td picks
(Jahmyr Gibbs, Chris Olave, Bijan Robinson, Christian McCaffrey, etc.)
with no Over/Under badge at all, because the Favorite O/U section is
only supposed to hold real two-sided Over/Under markets — Anytime TD
has no real Under side, so it never belonged there. generate_props_
report.py's TASK_INSTRUCTION and verify_favorite_ou() are both fixed
now so this won't happen on any FUTURE batch run, but the already-
generated batch files for this week on disk still have the bad entries
baked into their JSON. Re-running all 4 batches through the real API
again just to strip this out would cost real money for no real benefit
— this is a pure data edit, not a re-analysis, so it's done directly
on the already-written files instead.

Usage: python3 clean_favorite_ou_anytime_td.py <week_folder>
  e.g. python3 clean_favorite_ou_anytime_td.py wk04

Edits every real batch file listed in props_reports/<week_folder>/
manifest.json (skips the whole-week parlay file, which has no
favorite_ou section at all) in place, removing any favorite_ou.overs/
unders entry whose market_key is player_anytime_td, and reports
exactly what it removed from where. Makes a real .bak copy of each
file it touches before writing, so nothing is lost if this needs to be
undone.
"""
import json
import os
import sys


def load_json(path):
    if not os.path.exists(path):
        return None
    with open(path) as f:
        return json.load(f)


def main():
    if len(sys.argv) != 2:
        sys.exit(f"Usage: python3 {sys.argv[0]} <week_folder>  (e.g. wk04)")
    week_folder = sys.argv[1]
    out_dir = f"props_reports/{week_folder}"
    manifest = load_json(f"{out_dir}/manifest.json")
    if not manifest:
        sys.exit(f"FATAL: no manifest.json found at {out_dir}/manifest.json")

    total_removed = 0
    for filename in sorted(manifest.get("batches") or {}):
        if filename == "props_parlay_report_WHOLEWEEK.json":
            continue  # no favorite_ou section — not a real target for this cleanup
        path = f"{out_dir}/{filename}"
        report = load_json(path)
        if not report or "favorite_ou" not in report:
            continue
        fou = report["favorite_ou"] or {}
        overs = fou.get("overs") or []
        unders = fou.get("unders") or []
        bad_overs = [p for p in overs if p.get("market_key") == "player_anytime_td"]
        bad_unders = [p for p in unders if p.get("market_key") == "player_anytime_td"]
        if not bad_overs and not bad_unders:
            print(f"{filename}: clean, nothing to remove.")
            continue
        with open(path + ".bak", "w") as f:
            json.dump(report, f, indent=2)
        fou["overs"] = [p for p in overs if p.get("market_key") != "player_anytime_td"]
        fou["unders"] = [p for p in unders if p.get("market_key") != "player_anytime_td"]
        report["favorite_ou"] = fou
        with open(path, "w") as f:
            json.dump(report, f, indent=2)
        removed_names = [p.get("player", "?") for p in bad_overs + bad_unders]
        total_removed += len(removed_names)
        print(f"{filename}: removed {len(removed_names)} Anytime TD entr{'y' if len(removed_names) == 1 else 'ies'} "
              f"from Favorite O/U — {', '.join(removed_names)}. Backup written to {filename}.bak")

    if total_removed == 0:
        print("\nNothing found to clean — all batch files already look correct.")
    else:
        print(f"\nDone — removed {total_removed} real Anytime TD entr{'y' if total_removed == 1 else 'ies'} "
              f"total across this week's batch files. Reload Prop Center to see the fix.")


if __name__ == "__main__":
    main()
