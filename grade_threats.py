#!/usr/bin/env python3
"""Grade Threats: did each tiered player reach his own average against the weak defense?

For every week N with threats/wkNN.json, take each starter whose stat clears a
tier (Standard/Elite/Nuclear: player rank <= playerMax AND defense rank >= defMin,
same rules as fiClassify in js/fi-shell.js), look up what he actually did in
Week N from players/latest.json (game log), and compare with the average shown
on the Threats page (cats[stat].v, built only from weeks before N).

HIT  = actual >= average      MISS = actual < average      VOID = did not play
Writes results/threats_graded.json and prints a summary.
Usage: python3 grade_threats.py [first_week last_week]   (default: every week with a threats file)
"""
import json, glob, os, re, sys, collections

TIERS = [("nuclear", 3, 30), ("elite", 5, 28), ("standard", 10, 23)]
STAT = {"pass_yds": "pass_yds", "pass_tds": "pass_td", "rush_yds": "rush_yds",
        "rec_yds": "rec_yds", "rec": "rec"}
CAT_LABEL = {"pass_yds": "Pass yds", "pass_tds": "Pass TDs", "rush_yds": "Rush yds",
             "rec_yds": "Rec yds", "rec": "Receptions"}

def tier_of(c):
    for key, pmax, dmin in TIERS:
        if c["r"] <= pmax and c["dr"] >= dmin:
            return key
    return None

def load_logs():
    d = json.load(open("players/latest.json"))
    logs = {}
    for pos, rows in d["players"].items():
        for p in rows:
            for g in p.get("log") or []:
                logs[(p["name"], g["week"])] = g.get("m") or {}
    return logs

def main():
    logs = load_logs()
    played = max((w for (_n, w) in logs), default=0)   # latest week with real games; later weeks are not graded
    files = sorted(glob.glob("threats/wk*.json"))
    lo, hi = (int(sys.argv[1]), int(sys.argv[2])) if len(sys.argv) >= 3 else (1, 99)
    rows = []
    for f in files:
        wk = int(re.search(r"wk(\d+)", f).group(1))
        if not (lo <= wk <= hi) or wk > played:
            continue
        t = json.load(open(f))
        carry = t.get("carryover_season")
        for team, info in t["teams"].items():
            for s in info.get("starters", []):
                for cat, c in (s.get("cats") or {}).items():
                    if cat not in STAT or c.get("v") is None:
                        continue
                    tier = tier_of(c)
                    m = logs.get((s["name"], wk))
                    if m is None or STAT[cat] not in m:
                        actual, res = None, "VOID"
                    else:
                        actual = float(m[STAT[cat]])
                        res = "HIT" if actual >= float(c["v"]) else "MISS"
                    rows.append({"week": wk, "team": team, "opp": info.get("opp"), "player": s["name"],
                                 "pos": s["pos"], "cat": cat, "avg": c["v"], "player_rank": c["r"],
                                 "def_allowed": c.get("dv"), "def_rank": c["dr"], "tier": tier,
                                 "actual": actual, "result": res, "carryover": bool(carry)})
    os.makedirs("results", exist_ok=True)
    json.dump({"rows": rows}, open("results/threats_graded.json", "w"))

    def tally(sel):
        h = sum(1 for r in sel if r["result"] == "HIT"); m = sum(1 for r in sel if r["result"] == "MISS")
        pct = f"{100*h/(h+m):.0f}%" if h + m else "-"
        over = [r["actual"] / r["avg"] - 1 for r in sel if r["result"] != "VOID" and r["avg"]]
        d = f"{100*sum(over)/len(over):+.0f}%" if over else "-"
        return f"{h}-{m} ({pct}), actual vs avg {d}"
    graded = [r for r in rows if r["result"] != "VOID"]
    print(f"Rows: {len(rows)}  graded: {len(graded)}  void: {len(rows)-len(graded)}\n")
    print("BASELINE (every starter stat, no tier):", tally([r for r in rows if r["tier"] is None]))
    print("ALL THREATS (any tier):               ", tally([r for r in rows if r["tier"]]))
    print("\nBY TIER")
    for k, _, _ in reversed(TIERS):
        print(f"  {k:9s}", tally([r for r in rows if r["tier"] == k]))
    print("\nBY STAT (threats only)")
    for cat in STAT:
        sel = [r for r in rows if r["tier"] and r["cat"] == cat]
        if sel: print(f"  {CAT_LABEL[cat]:11s}", tally(sel))
    print("\nBY POSITION (threats only)")
    for pos in ("QB", "RB", "WR", "TE"):
        sel = [r for r in rows if r["tier"] and r["pos"] == pos]
        if sel: print(f"  {pos:3s}", tally(sel))
    print("\nBY WEEK (threats only)")
    for wk in sorted({r["week"] for r in rows}):
        sel = [r for r in rows if r["tier"] and r["week"] == wk]
        print(f"  Wk {wk}", tally(sel))

if __name__ == "__main__":
    main()
