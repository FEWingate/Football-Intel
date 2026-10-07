"""
ANALYZE_PROPS_PICKS.PY
======================
Read-only diagnostic: slices every graded Coeus pick (props_reports/wk*/
*_graded.json, written by grade_props_report.py) to show WHERE the losses
are, instead of just the overall W-L record. Changes nothing on disk.

Why this exists: the Results tab's Overall record counts the same real
pick once per section it appears in (a pick that is in the Prop Breakdown,
the Favorite O/U list AND two parlays is four tally entries for one real
result), so it overstates the real sample size. This script reports both:
every tally entry (matches the Results tab) and UNIQUE picks (deduped).

Also reports units at each pick's own stored price (flat 1 unit/pick),
because win% alone doesn't say whether a pick type makes or loses money:
at a typical 1.885 decimal price, break-even is 53.1%.

Usage:
    python3 analyze_props_picks.py             # all weeks found
    python3 analyze_props_picks.py 4           # one week
    python3 analyze_props_picks.py --margins   # also fetch real final stats
                                                 and show how far each O/U
                                                 pick missed/hit by (needs
                                                 network, same source the
                                                 grader already uses)
"""

import argparse
import glob
import json
import os
import re
import sys
from collections import defaultdict

REPORTS_DIR = "props_reports"


def flatten(graded, week, source_file):
    """Every individual graded pick/leg in one report, tagged by section."""
    rows = []

    def add(p, section, extra=None):
        if not isinstance(p, dict) or "grade" not in p:
            return
        r = dict(p)
        r["_section"] = section
        r["_week"] = week
        r["_file"] = os.path.basename(source_file)
        if extra:
            r.update(extra)
        rows.append(r)

    pb = graded.get("prop_breakdown") or {}
    for game in pb.get("per_game") or []:
        for p in game.get("picks") or []:
            add(p, "prop_breakdown", {"_game": f"{game.get('away')}@{game.get('home')}"})
    for pos, p in (pb.get("per_position") or {}).items():
        add(p, "prop_breakdown", {"_pos": pos})
    for p in (graded.get("best_10") or {}).get("picks") or []:
        add(p, "best_10")
    fou = graded.get("favorite_ou") or {}
    for p in fou.get("overs") or []:
        add(p, "favorite_ou")
    for p in fou.get("unders") or []:
        add(p, "favorite_ou")
    for section in ("parlays", "td_parlays", "spread_parlays"):
        for size, parlay in (graded.get(section) or {}).items():
            if not parlay or not parlay.get("legs"):
                continue
            for leg in parlay["legs"]:
                add(leg, section, {"_parlay_size": size})
    return rows


def pick_key(r):
    return (r["_week"], r.get("player"), r.get("market_key"), r.get("side"),
            r.get("line", r.get("threshold", r.get("point"))))


def units(r):
    g = r.get("grade")
    price = r.get("price")
    if g == "W":
        return (price - 1.0) if isinstance(price, (int, float)) else None
    if g == "L":
        return -1.0
    return 0.0 if g == "P" else None


def summarize(rows):
    w = sum(1 for r in rows if r["grade"] == "W")
    l = sum(1 for r in rows if r["grade"] == "L")
    p = sum(1 for r in rows if r["grade"] == "P")
    ung = sum(1 for r in rows if r["grade"] is None)
    us = [units(r) for r in rows if r["grade"] in ("W", "L", "P")]
    us = [u for u in us if u is not None]
    return w, l, p, ung, (sum(us) if us else None)


def fmt(label, rows, width=34):
    w, l, p, ung, u = summarize(rows)
    n = w + l
    pct = f"{100*w/n:5.1f}%" if n else "  n/a "
    unit_s = f"{u:+7.2f}u" if u is not None else "    n/a"
    ung_s = f"  ({ung} ungraded)" if ung else ""
    print(f"  {label:<{width}} {w:>3}-{l:<3}{('-'+str(p)) if p else '  '}  {pct}  {unit_s}{ung_s}")


def group(rows, keyfn):
    out = defaultdict(list)
    for r in rows:
        out[keyfn(r)].append(r)
    return out


def section_print(title, rows, keyfn, order=None):
    print(f"\n{title}")
    g = group(rows, keyfn)
    keys = order or sorted(g, key=lambda k: -len(g[k]))
    for k in keys:
        if k in g:
            fmt(str(k), g[k])


def price_bucket(r):
    p = r.get("price")
    if not isinstance(p, (int, float)):
        return "no price"
    if p < 1.80:
        return "heavy fav (<1.80)"
    if p < 2.00:
        return "standard (1.80-1.99)"
    if p < 3.00:
        return "plus money (2.00-2.99)"
    return "long shot (3.00+)"


def line_kind(r):
    mk = r.get("market_key") or ""
    if "milestones" in mk:
        return "alt/milestone line"
    if mk in ("player_anytime_td",):
        return "anytime TD"
    if mk == "spreads":
        return "spread"
    return "main O/U line"


def cites_prior_season(r):
    """Does the stated reason lean on last season's numbers? (Coeus's own
    words, matched loosely — a rough flag, not a guarantee.)"""
    txt = (r.get("reason") or "")
    return bool(re.search(r"\b2025\b", txt))


def fetch_margins(rows):
    """Adds _real and _margin to graded O/U rows by pulling the same real
    weekly stats the grader uses. Network required."""
    from grade_props_report import load_player_stats, MARKET_STAT_COL, ALT_MARKET_RE
    from build_dfs import normalize_name
    from build_matchup_stats import SEASON
    cache = {}
    for r in rows:
        wk = r["_week"]
        if wk not in cache:
            try:
                cache[wk] = load_player_stats(SEASON, wk)
            except SystemExit:
                cache[wk] = {}
        mk = r.get("market_key") or ""
        stat_col = MARKET_STAT_COL.get(mk)
        line = r.get("line")
        alt = ALT_MARKET_RE.match(mk)
        if stat_col is None and alt:
            stat_col = MARKET_STAT_COL.get(f"player_{alt.group(1)}")
            line = r.get("threshold")
        if stat_col is None or line is None:
            continue
        row = cache[wk].get(normalize_name(r.get("player", "")))
        if row is None:
            continue
        try:
            real = float(row.get(stat_col, 0) or 0)
        except (TypeError, ValueError):
            continue
        r["_real"] = real
        r["_margin"] = real - float(line)
        r["_margin_pct"] = (real - float(line)) / float(line) if float(line) else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("week", nargs="?", type=int)
    ap.add_argument("--margins", action="store_true")
    args = ap.parse_args()

    pattern = f"{REPORTS_DIR}/wk{args.week:02d}/*_graded.json" if args.week else f"{REPORTS_DIR}/wk*/*_graded.json"
    files = sorted(glob.glob(pattern))
    if not files:
        sys.exit(f"No graded files found for {pattern}. Run grade_props_report.py first.")

    all_rows = []
    for f in files:
        m = re.search(r"wk(\d+)", f)
        week = int(m.group(1)) if m else 0
        with open(f, encoding="utf-8") as fh:
            all_rows.extend(flatten(json.load(fh), week, f))

    graded_rows = [r for r in all_rows if r["grade"] in ("W", "L", "P")]
    print(f"Files: {len(files)}   tally entries: {len(all_rows)}   gradable: {len(graded_rows)}")

    # Unique picks: same real pick repeated across sections counts once.
    seen = {}
    for r in graded_rows:
        seen.setdefault(pick_key(r), r)
    unique = list(seen.values())
    print(f"Unique real picks (deduped): {len(unique)}  "
          f"(the Results tab Overall counts each repeat separately)")

    print("\n=== OVERALL ===")
    fmt("every tally entry (Results tab)", graded_rows)
    fmt("UNIQUE picks", unique)
    print("  Break-even at a 1.885 price is 53.1% (this is a real, priced bet, not a coin flip).")

    section_print("=== BY SECTION (every tally entry) ===", graded_rows, lambda r: r["_section"])
    section_print("=== BY WEEK (unique picks) ===", unique, lambda r: r["_week"],
                  order=sorted({r["_week"] for r in unique}))
    section_print("=== BY MARKET (unique picks) ===", unique, lambda r: r.get("market_key"))
    section_print("=== OVER vs UNDER (unique O/U picks) ===",
                  [r for r in unique if r.get("side") in ("over", "under")],
                  lambda r: r.get("side"))
    section_print("=== LINE TYPE (unique picks) ===", unique, line_kind)
    section_print("=== PRICE BUCKET (unique picks) ===", unique, price_bucket)
    section_print("=== REASON LEANS ON 2025 NUMBERS? (unique picks) ===", unique,
                  lambda r: "cites 2025" if cites_prior_season(r) else "no 2025 cited")

    # Side x market is where a systematic lean usually shows up.
    ou = [r for r in unique if r.get("side") in ("over", "under")]
    section_print("=== MARKET x SIDE (unique O/U picks) ===", ou,
                  lambda r: f"{r.get('market_key')} / {r.get('side')}")

    # Parlay leg sizes: how do the legs perform vs the whole parlay?
    parlay_legs = [r for r in graded_rows if r["_section"] in ("parlays", "td_parlays", "spread_parlays")]
    section_print("=== PARLAY LEGS BY PARLAY SIZE (individual legs) ===", parlay_legs,
                  lambda r: f"{r['_section']} / {r.get('_parlay_size')}-leg")

    # Worst repeat offenders.
    by_player = group(unique, lambda r: r.get("player"))
    rep = [(k, v) for k, v in by_player.items() if len(v) >= 2]
    rep.sort(key=lambda kv: (summarize(kv[1])[4] or 0))
    if rep:
        print("\n=== PLAYERS PICKED 2+ TIMES (worst units first, unique picks) ===")
        for k, v in rep[:12]:
            fmt(str(k), v)

    if args.margins:
        print("\nFetching real final stats for margin analysis...")
        try:
            fetch_margins(ou)
        except Exception as e:  # network / import issues shouldn't kill the report above
            print(f"  margins unavailable: {e}")
        with_m = [r for r in ou if "_margin" in r]
        if with_m:
            def avg(xs):
                return sum(xs) / len(xs) if xs else float("nan")
            print(f"\n=== MARGINS (unique O/U picks with a real stat, n={len(with_m)}) ===")
            print("  Signed margin is real stat minus line, flipped so POSITIVE always means")
            print("  Coeus was right (over: real-line, under: line-real).")
            for label, rows in (("all", with_m),
                                ("losses", [r for r in with_m if r['grade'] == 'L']),
                                ("wins", [r for r in with_m if r['grade'] == 'W'])):
                signed = [(r["_margin"] if r["side"] == "over" else -r["_margin"]) for r in rows]
                pct = [((r["_margin_pct"] if r["side"] == "over" else -r["_margin_pct"]) * 100)
                       for r in rows if r.get("_margin_pct") is not None]
                print(f"  {label:<7} n={len(rows):>3}  avg margin {avg(signed):+7.2f}   avg margin% {avg(pct):+6.1f}%")
            near = [r for r in with_m if r["grade"] == "L" and
                    abs(r.get("_margin_pct") or 9) <= 0.10]
            print(f"  losses within 10% of the line: {near and len(near) or 0} of "
                  f"{sum(1 for r in with_m if r['grade']=='L')} "
                  f"(close misses = variance; big misses = a real modeling problem)")
            print("\n  Worst 10 misses (biggest wrong-side margin):")
            losses = [r for r in with_m if r["grade"] == "L"]
            losses.sort(key=lambda r: (r["_margin"] if r["side"] == "over" else -r["_margin"]))
            for r in losses[:10]:
                print(f"    wk{r['_week']} {r.get('player')} {r.get('side')} {r.get('line', r.get('threshold'))} "
                      f"{r.get('market_key')}: real {r['_real']:.1f}")


if __name__ == "__main__":
    main()
