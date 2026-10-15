#!/usr/bin/env python3
"""
pff_pull.py - LOCAL, PRIVATE pull of PFF slot-coverage data -> team defense-vs-slot ranks.

Run from ~/football-intel on your own machine. It shells out to the `restish` CLI you already set up
(`restish pff signature-defense-slot-coverage nfl <season> <week>`), so your PFF key never touches this file.

Everything it writes goes under private/pff/, which is gitignored. Do NOT move that output into the
public repo until PFF's terms of service have been read.

  python3 pff_pull.py                 # all played weeks of the current season (skips weeks already saved)
  python3 pff_pull.py --refresh       # re-pull every week
  python3 pff_pull.py --season 2026 --through 5

Outputs
  private/pff/slot_wkNN.json          raw per-defender rows for one week (as PFF returns them)
  private/pff/slot_defense.json       per-team slot coverage allowed, season-to-date and last 3 games, with ranks
                                      (rank 1 = toughest defense, rank 32 = weakest - same as FI's matchup ranks)
"""
import argparse
import glob
import json
import os
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
PRIVATE = os.path.join(ROOT, "private", "pff")

# PFF's team abbreviations that differ from FI's (nflverse-style) codes.
PFF_TO_FI = {"ARZ": "ARI", "BLT": "BAL", "CLV": "CLE", "HST": "HOU", "JAC": "JAX", "WSH": "WAS", "LA": "LAR"}
SUM_FIELDS = ["coverage_snaps", "targets", "receptions", "yards", "yards_after_catch", "touchdowns", "interceptions"]


def find_restish():
    path = shutil.which("restish")
    if path:
        return path
    cand = os.path.expanduser("~/go/bin/restish")
    return cand if os.path.exists(cand) else None


def played_games(season_games_dir):
    """{week: {team: 1}} for every played game, from FI's own games/wkNN.json files."""
    out = {}
    for f in sorted(glob.glob(os.path.join(season_games_dir, "wk[0-9][0-9].json"))):
        d = json.load(open(f))
        wk = int(os.path.basename(f)[2:4])
        for g in d.get("games", []):
            if g.get("played"):
                out.setdefault(wk, {})
                out[wk][g["home"]] = 1
                out[wk][g["away"]] = 1
    return out


def pull_week(restish, season, week, refresh):
    path = os.path.join(PRIVATE, f"slot_wk{week:02d}.json")
    if os.path.exists(path) and not refresh:
        return json.load(open(path))
    r = subprocess.run([restish, "pff", "signature-defense-slot-coverage", "nfl", str(season), str(week)],
                       capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"restish failed for week {week}: {r.stderr.strip()[:400]}")
    try:
        data = json.loads(r.stdout)
    except ValueError:
        sys.exit(f"week {week}: response was not JSON: {r.stdout[:200]!r}")
    if "error" in data:
        sys.exit(f"week {week}: API error: {data['error']}")
    os.makedirs(PRIVATE, exist_ok=True)
    json.dump(data, open(path, "w"))
    return data


def aggregate(rows_by_week, games_by_week, weeks):
    """Sum slot-coverage numbers per team over `weeks`; returns {team: totals incl. games}."""
    teams = {}
    unmapped = set()
    for wk in weeks:
        for r in rows_by_week.get(wk, {}).get("slot_coverages", []):
            code = PFF_TO_FI.get(r.get("team"), r.get("team"))
            if not code:
                continue
            known = set().union(*[set(v) for v in games_by_week.values()]) if games_by_week else set()
            if known and code not in known:
                unmapped.add(r.get("team"))
                continue
            t = teams.setdefault(code, {k: 0 for k in SUM_FIELDS})
            for k in SUM_FIELDS:
                t[k] += r.get(k) or 0
    for code, t in teams.items():
        t["games"] = sum(1 for wk in weeks if code in games_by_week.get(wk, {}))
    return teams, unmapped


def finish(teams):
    """Per-game / per-target rates plus ranks (1 = toughest = fewest slot yards allowed per game)."""
    out = {}
    for code, t in teams.items():
        g = t["games"] or None
        out[code] = {
            "games": t["games"],
            "slot_yards": t["yards"], "slot_targets": t["targets"], "slot_receptions": t["receptions"],
            "slot_tds": t["touchdowns"], "slot_ints": t["interceptions"],
            "slot_yards_pg": round(t["yards"] / g, 1) if g else None,
            "slot_targets_pg": round(t["targets"] / g, 1) if g else None,
            "yards_per_target": round(t["yards"] / t["targets"], 2) if t["targets"] else None,
            "yards_per_coverage_snap": round(t["yards"] / t["coverage_snaps"], 3) if t["coverage_snaps"] else None,
            "catch_rate": round(100 * t["receptions"] / t["targets"], 1) if t["targets"] else None,
        }
    for key in ("slot_yards_pg", "yards_per_target", "yards_per_coverage_snap"):
        ranked = sorted([c for c in out if out[c][key] is not None], key=lambda c: out[c][key])
        for i, c in enumerate(ranked, 1):
            out[c]["rank_" + key.replace("slot_", "")] = i
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--season", type=int, default=2026)
    ap.add_argument("--through", type=int, help="last week to include (default: last week with a played game)")
    ap.add_argument("--refresh", action="store_true", help="re-pull weeks that are already saved")
    a = ap.parse_args()

    restish = find_restish()
    if not restish:
        sys.exit("restish not found. Is ~/go/bin on your PATH? (source ~/.bashrc)")
    games = played_games(os.path.join(ROOT, "games"))
    if not games:
        sys.exit("No played games found in games/wkNN.json - run `git pull` first.")
    through = a.through or max(games)
    weeks = [w for w in sorted(games) if w <= through]

    rows_by_week = {w: pull_week(restish, a.season, w, a.refresh) for w in weeks}
    season_teams, unmapped = aggregate(rows_by_week, games, weeks)
    last3 = weeks[-3:]
    last3_teams, _ = aggregate(rows_by_week, games, last3)

    if unmapped:
        print("WARNING: PFF team codes not recognised (skipped):", sorted(unmapped))
    result = {"season": a.season, "through_week": through, "weeks": weeks,
              "source": "PFF Premium Stats Pro API - PRIVATE, do not publish",
              "season_to_date": finish(season_teams),
              "last3": {"weeks": last3, "teams": finish(last3_teams)}}
    os.makedirs(PRIVATE, exist_ok=True)
    out_path = os.path.join(PRIVATE, "slot_defense.json")
    json.dump(result, open(out_path, "w"), indent=1)

    std = result["season_to_date"]
    print(f"Wrote {out_path}: {len(std)} teams through week {through}")
    print("Toughest vs slot (fewest yards allowed per game):")
    for c in sorted(std, key=lambda c: std[c].get("rank_yards_pg", 99))[:5]:
        print(f"  #{std[c]['rank_yards_pg']:>2} {c:<4} {std[c]['slot_yards_pg']} yds/g  {std[c]['yards_per_target']} yds/tgt")
    print("Weakest vs slot:")
    for c in sorted(std, key=lambda c: -std[c].get("rank_yards_pg", 0))[:5]:
        print(f"  #{std[c]['rank_yards_pg']:>2} {c:<4} {std[c]['slot_yards_pg']} yds/g  {std[c]['yards_per_target']} yds/tgt")


if __name__ == "__main__":
    main()
