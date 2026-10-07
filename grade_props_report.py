"""
GRADE_PROPS_REPORT.PY
======================
Grades every real pick Coeus made in a week's Props/Parlay report(s)
against real final results, once those real games are actually over —
never simulated, never estimated. Real, independent sources of truth,
reused directly from the same modules the rest of this project already
trusts for this exact data (not re-derived here, so there's only ever
one real implementation of "what's the final score" / "what's a
player's real stat line" to keep correct):

  - Player props (passing/rushing/receiving yards, receptions) and
    Anytime TD picks: real nflverse weekly player stats, via
    build_matchup_stats.py's own fetch_csv()/norm_players()/RAW_COLS —
    same source, same team/name normalization the whole site already
    depends on.
  - Spread picks: real final scores from the same real schedule feed
    build_ats_records() itself uses (nflverse/nfldata games.csv).
  - Player-name matching between a pick's "player" string and the real
    stats file uses build_dfs.py's own proven normalize_name() — the
    same real name-matching logic already relied on for DFS Center and
    the DFS Report, not a second, independent guess at it.

REAL, IMPORTANT LIMITATION THIS SCRIPT SURFACES RATHER THAN HIDES: a
pick has no real line/threshold/point on file unless it was generated
by generate_props_report.py on or after 2026-09-28 (the date that data
started being saved — see verify_pick()/verify_legs_against_source()).
An older report's individual prop/O-U picks cannot be graded at all —
marked "ungraded" with a plain reason, never guessed at from Coeus's
prose. Anytime TD picks (a real binary yes/no) and Spread picks (which
already carried a real "point") are gradable regardless of when the
report was generated.

A parlay's own overall result is WON only if every real, gradable leg
in it WON (a leg that pushed is dropped from consideration, same as a
real sportsbook settles a push leg out of a parlay) — LOST if any real
leg LOST — and left ungraded if any leg can't be graded yet (game not
final) or ever (no stored line).

Usage:
    python3 grade_props_report.py 3            # grade every real report
                                                   file in props_reports/wk03/
    python3 grade_props_report.py 3 --force     # grade even games whose
                                                   real kickoff hasn't
                                                   technically passed yet
                                                   (only useful for testing)
Output:
    props_reports/wkNN/<same stem>_graded.json  — one per real report file
    results/season_record.json                  — rolling W/L/P totals,
                                                    by week and season-to-date
"""

import argparse
import glob
import json
import os
import re
import sys
from datetime import datetime, timezone

from build_dfs import normalize_name
from build_matchup_stats import (
    fetch_csv, norm_players, normalize_team_cols, normalize_team_code,
    GAMES_URL, PLAYER_STATS_URLS, SEASON,
)
from build_fanduel_props import TEAM_NAME_TO_CODE

REPORTS_DIR = "props_reports"
RESULTS_DIR = "results"
SEASON_RECORD_PATH = f"{RESULTS_DIR}/season_record.json"

MARKET_STAT_COL = {
    "player_passing_yards": "passing_yards",
    "player_rushing_yards": "rushing_yards",
    "player_receiving_yards": "receiving_yards",
    "player_receptions": "receptions",
}
ALT_MARKET_RE = re.compile(r"^player_(.+)_milestones_(\d+)_or_more$")

# Which report sections hold picks/legs, and how to walk each one.
SECTIONS = ["best_10", "prop_breakdown", "favorite_ou", "parlays", "td_parlays", "spread_parlays"]


def load_json(path):
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def write_json_atomic(payload, path):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    tmp = f"{path}.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
    os.replace(tmp, path)


# ── Real final scores, this week only ───────────────────────────────────
def load_final_scores(season, week):
    """team_code -> {"own": real points scored, "opp": real points
    allowed, "final": bool}, for every real REG game in this week that
    has actually finished (a real final score on file)."""
    games = fetch_csv(GAMES_URL)
    games = normalize_team_cols(games, "home_team", "away_team")
    wk = games[(games["season"] == season) & (games["week"] == week) & (games["game_type"] == "REG")]
    out = {}
    for _, g in wk.iterrows():
        final = bool(g["home_score"] == g["home_score"] and g["away_score"] == g["away_score"])  # not NaN
        home, away = g["home_team"], g["away_team"]
        if final:
            out[home] = {"own": float(g["home_score"]), "opp": float(g["away_score"]), "final": True}
            out[away] = {"own": float(g["away_score"]), "opp": float(g["home_score"]), "final": True}
        else:
            out.setdefault(home, {"final": False})
            out.setdefault(away, {"final": False})
    return out


# ── Real final player stats, this week only ─────────────────────────────
def load_player_stats(season, week):
    """normalize_name(player) -> {stat_col: real value, ...}. A player
    with more than one real row this week (shouldn't happen, but real
    data has surprised this project before) keeps the first — logged,
    not silently overwritten twice."""
    df = norm_players(fetch_csv(PLAYER_STATS_URLS), season=season)
    wk = df[df["week"] == week]
    out = {}
    dupes = 0
    for _, r in wk.iterrows():
        key = normalize_name(r["name"])
        if key in out:
            dupes += 1
            continue
        out[key] = r.to_dict()
    if dupes:
        print(f"  NOTE: {dupes} duplicate real player-name row(s) this week — kept the first, "
              f"ignored the rest.")
    return out


# ── Per-pick grading ─────────────────────────────────────────────────────
def grade_ou(real_value, line, side):
    if real_value is None or line is None:
        return None, "no real stat or no real line on file"
    if real_value == line:
        return "P", None
    hit = (real_value > line) if side == "over" else (real_value < line)
    return ("W", None) if hit else ("L", None)


def grade_td(td_count):
    if td_count is None:
        return None, "player not found in real weekly stats"
    return ("W", None) if td_count > 0 else ("L", None)


def grade_spread(team_code, point, scores):
    if point is None:
        return None, "no real spread point on file"
    entry = scores.get(team_code)
    if not entry:
        return None, f"'{team_code}' not found in this week's real schedule"
    if not entry.get("final"):
        return None, "game not final yet"
    margin = entry["own"] - entry["opp"]
    if margin > -point:
        return "W", None
    if margin < -point:
        return "L", None
    return "P", None


def grade_pick(pick, player_stats, scores):
    """Returns (grade, reason_if_ungraded) — grade is 'W'/'L'/'P'/None."""
    market_key = pick.get("market_key")

    if market_key == "player_anytime_td":
        row = player_stats.get(normalize_name(pick.get("player", "")))
        if row is None:
            return None, "game not final yet, or player not found in real weekly stats"
        td_count = float(row.get("rushing_tds", 0) or 0) + float(row.get("receiving_tds", 0) or 0)
        return grade_td(td_count)

    if market_key == "spreads":
        code = TEAM_NAME_TO_CODE.get(pick.get("player"), pick.get("player"))
        code = normalize_team_code(code)
        return grade_spread(code, pick.get("point"), scores)

    stat_col = MARKET_STAT_COL.get(market_key)
    line = pick.get("line")
    if stat_col is None:
        alt = ALT_MARKET_RE.match(market_key or "")
        if alt:
            stat_col = MARKET_STAT_COL.get(f"player_{alt.group(1)}")
            line = pick.get("threshold")
    if stat_col is None:
        return None, f"don't know how to grade market '{market_key}'"

    row = player_stats.get(normalize_name(pick.get("player", "")))
    real_value = float(row.get(stat_col, 0) or 0) if row is not None else None
    if row is None:
        return None, "game not final yet, or player not found in real weekly stats"
    return grade_ou(real_value, line, pick.get("side", "over"))


def grade_pick_list(picks, player_stats, scores):
    graded = []
    for p in picks:
        grade, reason = grade_pick(p, player_stats, scores)
        entry = dict(p)
        entry["grade"] = grade
        if reason:
            entry["ungraded_reason"] = reason
        graded.append(entry)
    return graded


def grade_parlay_sizes(parlay_by_size, player_stats, scores):
    out = {}
    for size, p in (parlay_by_size or {}).items():
        if not p or not p.get("legs"):
            out[size] = p
            continue
        graded_legs = grade_pick_list(p["legs"], player_stats, scores)
        grades = [l["grade"] for l in graded_legs]
        if any(g == "L" for g in grades):
            overall = "L"
        elif any(g is None for g in grades):
            overall = None
        elif all(g == "P" for g in grades):
            overall = "P"
        else:
            overall = "W"
        new_p = dict(p)
        new_p["legs"] = graded_legs
        new_p["overall_grade"] = overall
        out[size] = new_p
    return out


def tally(counter, grade, units=None):
    if grade == "W":
        counter["w"] += 1
    elif grade == "L":
        counter["l"] += 1
    elif grade == "P":
        counter["p"] += 1
    else:
        counter["ungraded"] += 1
    if units is not None:
        counter["units"] = round(counter.get("units", 0.0) + units, 2)


def blank_tally():
    return {"w": 0, "l": 0, "p": 0, "ungraded": 0, "units": 0.0}


def pick_units(grade, price):
    """Flat 1-unit stake at the pick's own stored decimal price: a win
    returns price-1, a loss -1, a push 0. None when ungraded or when no
    real price is on file — never guessed."""
    if grade == "L":
        return -1.0
    if grade == "P":
        return 0.0
    if grade == "W" and isinstance(price, (int, float)):
        return price - 1.0
    return None


def grade_report(report, player_stats, scores):
    """Returns (graded_report, week_tallies) — week_tallies: {section:
    blank_tally()} plus "overall" (every individual pick/leg, all
    sections combined)."""
    graded = dict(report)
    tallies = {s: blank_tally() for s in SECTIONS}
    tallies["overall"] = blank_tally()

    pb = report.get("prop_breakdown")
    if pb:
        new_pb = dict(pb)
        new_per_game = []
        for game in (pb.get("per_game") or []):
            picks = grade_pick_list(game.get("picks") or [], player_stats, scores)
            for p in picks:
                tally(tallies["prop_breakdown"], p["grade"], pick_units(p["grade"], p.get("price")))
                tally(tallies["overall"], p["grade"])
            new_per_game.append({**game, "picks": picks})
        new_pb["per_game"] = new_per_game
        new_per_position = {}
        for pos, pick in (pb.get("per_position") or {}).items():
            grade, reason = grade_pick(pick, player_stats, scores)
            entry = dict(pick)
            entry["grade"] = grade
            if reason:
                entry["ungraded_reason"] = reason
            new_per_position[pos] = entry
            tally(tallies["prop_breakdown"], grade, pick_units(grade, pick.get("price")))
            tally(tallies["overall"], grade)
        new_pb["per_position"] = new_per_position
        graded["prop_breakdown"] = new_pb

    b10 = report.get("best_10")
    if b10 and b10.get("picks"):
        b10_picks = grade_pick_list(b10["picks"], player_stats, scores)
        for p in b10_picks:
            tally(tallies["best_10"], p["grade"], pick_units(p["grade"], p.get("price")))
            tally(tallies["overall"], p["grade"])
        graded["best_10"] = {**b10, "picks": b10_picks}

    fou = report.get("favorite_ou")
    if fou:
        overs = grade_pick_list(fou.get("overs") or [], player_stats, scores)
        unders = grade_pick_list(fou.get("unders") or [], player_stats, scores)
        for p in overs + unders:
            tally(tallies["favorite_ou"], p["grade"], pick_units(p["grade"], p.get("price")))
            tally(tallies["overall"], p["grade"])
        graded["favorite_ou"] = {**fou, "overs": overs, "unders": unders}

    for section in ("parlays", "td_parlays", "spread_parlays"):
        block = report.get(section)
        if block:
            graded_block = grade_parlay_sizes(block, player_stats, scores)
            for p in graded_block.values():
                if p and p.get("legs"):
                    for leg in p["legs"]:
                        tally(tallies["overall"], leg["grade"])
                    # A whole parlay's own units: a win pays its real
                    # combined decimal price minus the stake, a loss is -1.
                    combined = (p.get("result") or {}).get("combined_decimal")
                    tally(tallies[section], p.get("overall_grade"),
                          pick_units(p.get("overall_grade"), combined))
            graded[section] = graded_block

    graded["graded_at"] = datetime.now(timezone.utc).isoformat()
    return graded, tallies


def iter_graded_picks(graded):
    """Every individual graded pick/leg in one graded report, regardless
    of which section it sits in."""
    pb = graded.get("prop_breakdown") or {}
    for game in pb.get("per_game") or []:
        for p in game.get("picks") or []:
            yield p
    for p in (pb.get("per_position") or {}).values():
        yield p
    for p in (graded.get("best_10") or {}).get("picks") or []:
        yield p
    fou = graded.get("favorite_ou") or {}
    for p in (fou.get("overs") or []) + (fou.get("unders") or []):
        yield p
    for section in ("parlays", "td_parlays", "spread_parlays"):
        for parlay in (graded.get(section) or {}).values():
            for leg in (parlay or {}).get("legs") or []:
                yield leg


def unique_pick_key(p):
    return (p.get("player"), p.get("market_key"), p.get("side"),
            p.get("line", p.get("threshold", p.get("point"))))


def unique_tally(graded_reports):
    """W/L/P and units over UNIQUE real picks — the same pick appearing in
    several sections (Prop Breakdown, Favorite O/U, a parlay leg...) is one
    real result, counted once. Units are flat 1-unit stakes at each pick's
    own stored price."""
    seen = {}
    for graded in graded_reports:
        for p in iter_graded_picks(graded):
            if "grade" in p:
                seen.setdefault(unique_pick_key(p), p)
    t = blank_tally()
    for p in seen.values():
        tally(t, p["grade"], pick_units(p["grade"], p.get("price")))
    return t


def legs_tally(graded_reports, section):
    """Unique legs inside one parlay section (e.g. spread_parlays): each
    distinct pick counted once however many parlays it sits in."""
    seen = {}
    for graded in graded_reports:
        for parlay in (graded.get(section) or {}).values():
            for leg in (parlay or {}).get("legs") or []:
                if "grade" in leg:
                    seen.setdefault(unique_pick_key(leg), leg)
    t = blank_tally()
    for p in seen.values():
        tally(t, p["grade"], pick_units(p["grade"], p.get("price")))
    return t


def merge_tallies(a, b):
    out = {}
    for key in set(a) | set(b):
        ta, tb = a.get(key, blank_tally()), b.get(key, blank_tally())
        out[key] = {k: ta.get(k, 0) + tb.get(k, 0) for k in ("w", "l", "p", "ungraded")}
        out[key]["units"] = round(ta.get("units", 0.0) + tb.get("units", 0.0), 2)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("week", type=int)
    ap.add_argument("--force", action="store_true",
                     help="grade even games whose real kickoff hasn't passed yet (testing only)")
    args = ap.parse_args()

    week_folder = f"wk{args.week:02d}"
    report_dir = f"{REPORTS_DIR}/{week_folder}"
    if not os.path.isdir(report_dir):
        sys.exit(f"FATAL: {report_dir} not found — no real reports for week {args.week}.")

    report_paths = sorted(
        p for p in glob.glob(f"{report_dir}/*.json")
        if not p.endswith("_prompt.json") and not p.endswith("manifest.json")
        # REAL BUG FIX (2026-10-07): this glob also matched the *_graded.json files
        # a previous run wrote into the same folder, so every rerun graded its own
        # earlier output (creating *_graded_graded.json) and merged those picks into
        # the week's tallies again — inflating the Results tab with each rerun.
        and not p.endswith("_graded.json")
    )
    if not report_paths:
        sys.exit(f"FATAL: no real report files in {report_dir}.")

    print(f"Loading real final scores and real weekly player stats for {SEASON} week {args.week}...")
    scores = load_final_scores(SEASON, args.week)
    if args.force:
        for entry in scores.values():
            entry["final"] = True
    not_final = [t for t, e in scores.items() if not e.get("final")]
    if not_final and not args.force:
        print(f"  NOTE: {len(not_final)} team(s) this week have no real final score yet: "
              f"{sorted(not_final)} — their picks will grade as ungraded, not guessed at.")
    player_stats = load_player_stats(SEASON, args.week)
    print(f"  {len(player_stats)} real player(s) with a stat line this week.")

    week_totals = {s: blank_tally() for s in SECTIONS}
    week_totals["overall"] = blank_tally()

    graded_reports = []
    for path in report_paths:
        report = load_json(path)
        graded, tallies = grade_report(report, player_stats, scores)
        graded_reports.append(graded)
        week_totals = merge_tallies(week_totals, tallies)
        out_path = path[:-len(".json")] + "_graded.json"
        write_json_atomic(graded, out_path)
        overall = tallies["overall"]
        print(f"  {os.path.basename(path)}: {overall['w']}-{overall['l']}-{overall['p']} "
              f"({overall['ungraded']} ungraded) -> wrote {os.path.basename(out_path)}")

    season_record = load_json(SEASON_RECORD_PATH) or {"weeks": {}}
    week_totals["unique"] = unique_tally(graded_reports)
    # v4 (2026-10-07): the headline "Overall" is the real-pick record (each
    # pick once), not a count of every place a pick appears. The old
    # multi-count figure is kept as "entries" for reference only.
    week_totals["entries"] = week_totals["overall"]
    week_totals["overall"] = dict(week_totals["unique"])
    for sec in ("parlays", "td_parlays", "spread_parlays"):
        week_totals[sec + "_legs"] = legs_tally(graded_reports, sec)
    season_record["weeks"][week_folder] = week_totals
    season_record["season_totals"] = {s: blank_tally() for s in SECTIONS}
    season_record["season_totals"]["overall"] = blank_tally()
    season_record["season_totals"]["unique"] = blank_tally()
    season_record["season_totals"]["entries"] = blank_tally()
    for sec in ("parlays", "td_parlays", "spread_parlays"):
        season_record["season_totals"][sec + "_legs"] = blank_tally()
    for wk_totals in season_record["weeks"].values():
        season_record["season_totals"] = merge_tallies(season_record["season_totals"], wk_totals)
    season_record["generated_at"] = datetime.now(timezone.utc).isoformat()
    write_json_atomic(season_record, SEASON_RECORD_PATH)

    overall = week_totals["overall"]
    print(f"\nWeek {args.week} overall (unique picks): {overall['w']}-{overall['l']}-{overall['p']} "
          f"({overall['ungraded']} ungraded)")
    for sec in ("parlays", "td_parlays", "spread_parlays"):
        lg = week_totals[sec + "_legs"]; wp = week_totals[sec]
        print(f"  {sec}: whole parlays {wp['w']}-{wp['l']}, unique legs {lg['w']}-{lg['l']}-{lg['p']}")
    uq = week_totals["unique"]
    print(f"Week {args.week} UNIQUE picks: {uq['w']}-{uq['l']}-{uq['p']}  {uq['units']:+.2f}u")
    season = season_record["season_totals"]["overall"]
    print(f"Season to date: {season['w']}-{season['l']}-{season['p']} "
          f"({season['ungraded']} ungraded) — wrote {SEASON_RECORD_PATH}")


if __name__ == "__main__":
    main()
