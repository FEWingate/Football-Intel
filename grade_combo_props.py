#!/usr/bin/env python3
"""
GRADE_COMBO_PROPS.PY
====================
Grades the picks saved by build_combo_props.py (results/combo_picks.json) against real nflverse
weekly player stats once the games are final (nflverse usually posts them by Tuesday).

For each saved pick it records the real combined total, then whether the MODEL's side (STRONG/LEAN
only) and COEUS's pick (OVER/UNDER only) won, plus profit in units at the saved price (1 unit risked).
NEUTRAL and CHECK (amber) rows are tracked but not counted as model plays.

USAGE:  python3 grade_combo_props.py          # grade everything that is final
        python3 grade_combo_props.py --week 6 # only one week
"""
import argparse, json, os, re, sys
from io import StringIO
import pandas as pd
import requests

ROOT = os.path.dirname(os.path.abspath(__file__))
PICKS = os.path.join(ROOT, "results", "combo_picks.json")
URL = "https://github.com/nflverse/nflverse-data/releases/download/stats_player/stats_player_week_%d.csv"
HALVES = {"pass_rush": ("passing_yards", "rushing_yards"), "rush_rec": ("rushing_yards", "receiving_yards")}


def norm(n):
    return re.sub(r"\s+", " ", re.sub(r"[^a-z ]", " ", re.sub(r"[.'’]", "", str(n or "").lower()))).strip()


def profit(price):
    p = -113.0 if price is None else float(price)
    if abs(p) >= 100:
        return 100 / -p if p < 0 else p / 100
    return p - 1 if p > 1 else 0.88


def settle(side, actual, line, over_price, under_price):
    if actual == line:
        return "PUSH", 0.0
    won = (actual > line) if side == "OVER" else (actual < line)
    return ("WIN", profit(over_price if side == "OVER" else under_price)) if won else ("LOSS", -1.0)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--week", type=int)
    a = ap.parse_args()
    try:
        data = json.load(open(PICKS))
    except (OSError, ValueError):
        sys.exit("No results/combo_picks.json yet - run build_combo_props.py first.")
    cache = {}
    done = 0
    for p in data["picks"]:
        if p.get("graded") or (a.week and p["week"] != a.week):
            continue
        s = p["season"]
        if s not in cache:
            r = requests.get(URL % s, timeout=120)
            cache[s] = pd.read_csv(StringIO(r.text), low_memory=False) if r.status_code == 200 else None
        df = cache[s]
        if df is None:
            continue
        x = df[(df["week"] == p["week"]) & (df["season_type"] == "REG")]
        x = x[x["player_display_name"].map(norm) == norm(p["player"])]
        if x.empty:
            print("  not final yet: %s week %s" % (p["player"], p["week"]))
            continue
        c1, c2 = HALVES[p["market"]]
        actual = float(x[c1].sum() + x[c2].sum())
        p["actual"] = actual
        res, units = settle(p["model_side"], actual, p["line"], p.get("over_price"), p.get("under_price"))
        p["model_result"], p["model_units"] = res, round(units, 3)
        if p.get("coeus_pick") in ("OVER", "UNDER"):
            r2, u2 = settle(p["coeus_pick"], actual, p["line"], p.get("over_price"), p.get("under_price"))
            p["coeus_result"], p["coeus_units"] = r2, round(u2, 3)
        p["graded"] = True
        done += 1
        print("  %-22s %-9s actual %-6s line %-6s model %s %s | coeus %s %s" % (
            p["player"], p["market"], actual, p["line"], p["model_side"], res, p.get("coeus_pick"), p.get("coeus_result", "-")))
    with open(PICKS, "w") as f:
        json.dump(data, f, indent=1)

    g = [p for p in data["picks"] if p.get("graded")]

    def tally(rows, key, ukey):
        w = sum(1 for r in rows if r.get(key) == "WIN")
        l = sum(1 for r in rows if r.get(key) == "LOSS")
        ps = sum(1 for r in rows if r.get(key) == "PUSH")
        return "%d-%d%s  %+.2f units" % (w, l, ("-%d" % ps) if ps else "", sum(r.get(ukey, 0) for r in rows))

    print("\nGraded this run: %d | graded overall: %d" % (done, len(g)))
    plays = [r for r in g if r.get("model_lean") in ("STRONG", "LEAN")]
    print("Model STRONG/LEAN plays: %s" % tally(plays, "model_result", "model_units"))
    print("Coeus OVER/UNDER picks : %s" % tally([r for r in g if r.get("coeus_result")], "coeus_result", "coeus_units"))
    print("(NEUTRAL and amber-flagged rows are saved and graded but not counted as model plays)")


if __name__ == "__main__":
    main()
