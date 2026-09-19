"""
BUILD_EVIDENCE_PACKAGE_BOOTSTRAP.PY
====================================
Evidence assembly for an UPCOMING, not-yet-played slate — e.g. Week 1 2026,
before any current-season games exist. This is the DFS Report's actual real
use case, distinct from build_evidence_package.py's mode (which pairs a
week's team data with THAT SAME week's real, already-played game).

THE CORE IDEA: pair the REAL upcoming schedule (who actually plays whom,
extracted straight from the DK salary file's own Game Info column — DK only
builds slates for real, scheduled games) with the most recent season-FINAL
team/player/threat/intel data as the analytical foundation, since that's
the best real data that exists before the new season has been played.

This mirrors exactly how matchup/current.json already falls back to last
season's final week when no current-season data exists — this script does
the same thing, just for a REAL future pairing instead of matchup/current's
own (season, week), and explicitly WITHOUT fabricating a "game" box score,
since the game hasn't happened.

WHAT'S SAFE TO REUSE FROM THE BOOTSTRAP SEASON (per-team, season-cumulative,
doesn't depend on who actually played whom that week):
  matchup/wkNN.json      each team's own season off/def stats — safe
  threats/wkNN.json      each team's own starters' season convergence — safe
  context/wkNN.json      each team's own tier splits — safe
  players/latest.json    season/career player stats — safe (always-current,
                         not week-scoped in the first place)
  intel/*.json           Hidden Intelligence, keyed by team — safe
  intel/cb_rankings.json CB/DB rankings, keyed by team — safe

WHAT'S NOT REUSED (would be actively wrong to fabricate):
  games/wkNN.json box scores — that week's ACTUAL result, for a game that
  may not even be the same two teams. An upcoming game gets a "game" block
  built from the REAL schedule (kickoff date/time from the DK file) with an
  explicit "not yet played" flag, never a fake score.

USAGE:
  python3 build_evidence_package_bootstrap.py --bootstrap-week 18
  (--bootstrap-week defaults to matchup/current.json's week if omitted)

OUTPUT:
  evidence_bootstrap/{away}_{home}.json — one file per real scheduled game
  found in data/dfs/DKSalaries.csv, plus a manifest.
"""

import argparse
import copy
import json
import os
import re
import sys
from datetime import datetime, timezone

try:
    import pandas as pd
except ImportError:
    sys.exit("FATAL: pandas is required. pip install pandas --break-system-packages")

DK_SALARY_PATH = "data/dfs/DKSalaries.csv"

FI_TIERS = [
    {"key": "nuclear", "label": "Nuclear", "player_max": 3, "def_min": 30},
    {"key": "elite", "label": "Elite", "player_max": 5, "def_min": 28},
    {"key": "standard", "label": "Standard", "player_max": 10, "def_min": 23},
]


def fi_classify(cats):
    """Same port as build_evidence_package.py — see that file for the full
    explanation. Duplicated here deliberately rather than imported, so this
    script has no dependency on the other one and can run standalone."""
    assigned = {}
    for cat, c in (cats or {}).items():
        for t in FI_TIERS:
            if c["r"] <= t["player_max"] and c["dr"] >= t["def_min"]:
                assigned[cat] = t["key"]
                break
    out, used = [], set()
    for t in FI_TIERS:
        conv = [c for c in assigned if assigned[c] == t["key"]]
        if not conv:
            continue
        extra = [c for c, v in cats.items()
                 if c not in conv and c not in used and v["r"] <= t["player_max"]]
        used.update(conv); used.update(extra)
        out.append({"tier": t["key"], "tier_label": t["label"],
                     "type": "Quadruple" if len(conv) >= 2 else ("Triple" if extra else "Double"),
                     "categories_converged": conv, "categories_extra": extra})
    return out


def load_json(path):
    if not os.path.exists(path):
        return None
    with open(path) as f:
        return json.load(f)


DOWN_DIST_KEY = "Down/Distance"  # matches DOWN_DIST_SUBGROUP_NAME in build_matchup_stats.py
RED_ZONE_KEY = "Red Zone Play Calling"  # matches RED_ZONE_SUBGROUP_NAME in build_matchup_stats.py

def rank_teams_by(teamstats_json, side, field, subgroup=DOWN_DIST_KEY, ascending=False):
    """See build_evidence_package.py for full explanation — computes league
    ranks locally since teamstats/latest.json stores raw values with no
    rank included."""
    if not teamstats_json:
        return {}
    vals = {}
    for team, t in teamstats_json.get("teams", {}).items():
        v = t.get(side, {}).get(subgroup, {}).get(field, {}).get("avg")
        if v is not None:
            vals[team] = v
    ordered = sorted(vals, key=lambda t: vals[t], reverse=not ascending)
    return {team: {"v": vals[team], "r": i + 1} for i, team in enumerate(ordered)}

def down_distance_for_team(teamstats_json, team, off_ranks, def_ranks):
    """See build_evidence_package.py for full explanation."""
    if not teamstats_json or team not in teamstats_json.get("teams", {}):
        return None
    t = teamstats_json["teams"][team]
    off_dd = t.get("offense", {}).get(DOWN_DIST_KEY, {})
    def_dd = t.get("defense", {}).get(DOWN_DIST_KEY, {})
    def v(d, k): return d.get(k, {}).get("avg")
    return {
        "offense": {
            "third_down_attempts_per_game": v(off_dd, "d3_att"),
            "third_down_conversion_pct": off_ranks.get(team, {}),
            "fourth_down_situations_per_game": v(off_dd, "d4_situations"),
            "fourth_down_go_for_it_pct": v(off_dd, "d4_go_pct"),
            "fourth_down_conversion_pct": v(off_dd, "d4_conv_pct"),
        },
        "defense": {
            "third_down_attempts_faced_per_game": v(def_dd, "d3_att_faced"),
            "third_down_pct_allowed": def_ranks.get(team, {}),
            "third_down_stop_pct": v(def_dd, "d3_stop_pct"),
            "fourth_down_situations_faced_per_game": v(def_dd, "d4_situations_faced"),
            "fourth_down_go_for_it_pct_faced": v(def_dd, "d4_go_pct_faced"),
            "fourth_down_stop_pct": v(def_dd, "d4_stop_pct"),
        },
    }

def red_zone_for_team(teamstats_json, team, off_run_ranks, off_pass_ranks, def_run_ranks, def_pass_ranks):
    """See build_evidence_package.py for full explanation."""
    if not teamstats_json or team not in teamstats_json.get("teams", {}):
        return None
    t = teamstats_json["teams"][team]
    off_rz = t.get("offense", {}).get(RED_ZONE_KEY, {})
    def_rz = t.get("defense", {}).get(RED_ZONE_KEY, {})
    def v(d, k): return d.get(k, {}).get("avg")
    return {
        "offense": {
            "red_zone_plays_per_game": v(off_rz, "rz_plays"),
            "red_zone_run_pct": off_run_ranks.get(team, {}),
            "red_zone_pass_pct": off_pass_ranks.get(team, {}),
        },
        "defense": {
            "red_zone_plays_faced_per_game": v(def_rz, "rz_plays_faced"),
            "red_zone_run_pct_allowed": def_run_ranks.get(team, {}),
            "red_zone_pass_pct_allowed": def_pass_ranks.get(team, {}),
        },
    }

# Every category actually used across real threats.json starters (QB/RB/WR/TE),
# mapped to matchup.json's real field name for that stat, confirmed by direct
# inspection rather than assumed — the two files don't always use matching
# names (threats' "pass_tds" vs matchup's "pass_td", a raw season total that
# needs dividing by games-played to become the per-game rate threats.json
# actually stores). per_game=True marks fields needing that derivation.
THREAT_CATEGORY_FIELD = {
    "pass_yds": ("pass_ypg", False),
    "pass_tds": ("pass_td", True),
    "rush_yds": ("rush_ypg", False),
    "rec_yds": ("rec_ypg", False),
    "rec": ("rec_pg", False),
}

def def_stat_for_opponent(matchup_json, team, position, field, per_game=False):
    """matchup.json's def-by-position fields are already {"v":.., "r":..}
    pairs, same convention as team_off/team_def — confirmed by direct
    inspection, correcting an initial wrong assumption that these were
    raw numbers needing a rank computed from scratch. per_game=True
    divides v by games-played (needed for pass_tds specifically, which is
    a season total in matchup.json but a per-game rate in threats.json);
    the pre-existing rank is reused as-is in that case, since ranking a
    full season by total vs. by per-game rate produces the same order
    for teams that have all played the same number of games — true for
    every real NFL season, allowing for the rare mid-season game
    postponement, which this doesn't attempt to special-case."""
    t = (matchup_json or {}).get("teams", {}).get(team, {})
    cell = t.get("def", {}).get(position, {}).get(field)
    if not cell or "v" not in cell or "r" not in cell:
        return None
    v, r = cell["v"], cell["r"]
    if per_game:
        gp = t.get("gp") or 0
        if not gp:
            return None
        v = round(v / gp, 2)
    return {"v": v, "r": r}

def fix_threat_opponent_context(starters, real_opponent, matchup_json):
    """Threat Intelligence's per-category 'dv'/'dr' fields (the OPPONENT
    DEFENSE's value/rank in that category) are tagged to each team's real
    final-week-of-source-season opponent, not the bootstrap pairing —
    same root problem already fixed for rb_rush_vs_pass/qb_run_vs_pass,
    found here after Frank caught a real generated report citing a Threat
    tier that turned out to be computed against the wrong opponent
    entirely (Chicago instead of the real bootstrap opponent). Recomputes
    dv/dr against the real opponent's real, current matchup.json defensive
    data — the same source already used and trusted elsewhere in this
    evidence package — rather than leaving Coeus to manually catch and
    work around a wrong tier label every time."""
    for starter in starters:
        pos = starter.get("pos")
        cats = starter.get("cats", {})
        for cat_key, cat_val in cats.items():
            mapping = THREAT_CATEGORY_FIELD.get(cat_key)
            if not mapping:
                continue
            field, per_game = mapping
            result = def_stat_for_opponent(matchup_json, real_opponent, pos, field, per_game)
            if result:
                cat_val["dv"] = result["v"]
                cat_val["dr"] = result["r"]
                cat_val["opponent_context_recomputed_for_bootstrap"] = True
            else:
                cat_val["opponent_context_stale_note"] = (
                    f"Could not recompute dv/dr against {real_opponent} — "
                    f"treat this category's opponent comparison as unavailable "
                    f"for this bootstrap matchup, not as real evidence.")


def filter_intel_by_teams(intel_json, key, teams):
    if not intel_json or key not in intel_json:
        return {}
    section = intel_json[key]
    return {team: section[team] for team in teams if team in section}


def tier_of(rank):
    """Same convention as build_matchup_stats.py's tier_of() — 1-10 top,
    11-22 mid, 23-32 bottom. Kept in sync manually since this script has
    no import dependency on that file."""
    if rank <= 10:
        return "top"
    if rank <= 22:
        return "mid"
    return "bot"


def fix_bootstrap_opponent_context(entries, real_opponent_of, matchup_teams):
    """qb_run_vs_pass and rb_rush_vs_pass entries carry opponent-tagged
    fields (opp_run_def_rank, run_matchup_tier, upcoming_opponent, etc.)
    computed against each team's REAL final-week-of-source-season opponent
    — not the hypothetical bootstrap pairing. Left as-is, those fields are
    actively wrong for this matchup (e.g. tagged "NYJ" in a BUF-vs-HOU
    bootstrap game). Recompute them against the real bootstrap opponent
    using the same team_def ranks already validated elsewhere in this
    bundle, rather than leaving stale numbers for Coeus to have to notice
    and exclude on its own."""
    for team, entry in entries.items():
        opp = real_opponent_of.get(team)
        if not opp or opp not in matchup_teams:
            entry["bootstrap_opponent_context_note"] = (
                f"No {opp or 'opponent'} team_def data available to recompute "
                f"opponent context — treat opp_*_rank/tier fields as stale "
                f"(tagged to a different, real prior-season opponent) and do "
                f"not use them for this matchup.")
            continue
        opp_def = matchup_teams[opp].get("team_def", {})
        if "opp_run_def_rank" in entry and "rush_ypg" in opp_def:
            entry["opp_run_def_rank"] = opp_def["rush_ypg"]["r"]
            entry["run_matchup_tier"] = tier_of(opp_def["rush_ypg"]["r"])
        if "opp_pass_def_rank" in entry and "pass_ypg" in opp_def:
            entry["opp_pass_def_rank"] = opp_def["pass_ypg"]["r"]
            entry["pass_matchup_tier"] = tier_of(opp_def["pass_ypg"]["r"])
        entry["upcoming_opponent"] = opp
        entry["opponent_context_recomputed_for_bootstrap"] = True


def extract_real_schedule(dk_df):
    """Pull the REAL upcoming schedule straight from the DK file's own Game
    Info column — 'AWAY@HOME MM/DD/YYYY HH:MMAM/PM ET'. This is genuine
    schedule data DK only publishes for real, confirmed games; nothing here
    is inferred or guessed.

    REAL CHANGE (2026-09-16): no longer called by main() — see
    extract_real_schedule_from_games_json() below, which replaced this as
    the real schedule source per Frank's direct question about why a
    manually-downloaded, main-slate-only DK file should matter for
    schedule discovery at all when a more complete source already exists.
    Left defined, unused, rather than deleted outright, in case DK's raw
    schedule text is ever needed again for some other real reason."""
    games = {}
    for info in dk_df["Game Info"].dropna().unique():
        m = re.match(r"^([A-Z]+)@([A-Z]+)\s+(\S+)\s+(\S+\s*[AP]M)\s*(\S*)", str(info))
        if not m:
            continue
        away, home, date, time, tz = m.groups()
        games[(away, home)] = {"away": away, "home": home, "date": date,
                                "time": time, "timezone": tz or "ET"}
    return games


def extract_real_schedule_from_games_json(games_json):
    """REAL CHANGE (2026-09-16), replacing DK-based schedule discovery
    entirely, per Frank's direct question: why should a DK salary file
    matter for finding out which teams are playing, now that DK is no
    longer this project's injury source? It shouldn't, and confirmed
    directly it was actively causing real problems beyond that — DK's
    file only ever covers its own main Sunday slate (Thursday/Monday
    games like DET@BUF were never in it at all, requiring the
    --extra-away/--extra-home workaround every single week just to
    include them), and it depends on someone remembering to
    re-download it fresh — confirmed directly as the real cause of a
    stale September 5th file silently causing real Week 1 matchups
    (TB_CIN, GB_MIN) to be misidentified as Week 2's upcoming games.

    games/wkNN.json has neither problem: it's nflverse's own real,
    complete schedule (via build_matchup_stats.py), covering every real
    game for the week regardless of time slot, and it's already
    rebuilt as part of the normal pipeline Frank runs regularly — not a
    separate, easy-to-forget manual download. This is also the exact
    same file already loaded elsewhere in this script for the
    div_game lookup; the caller reuses that one load for both purposes
    rather than loading it twice."""
    games = {}
    for g in games_json.get("games", []) if games_json else []:
        away, home = g.get("away"), g.get("home")
        gameday, gametime = g.get("gameday"), g.get("gametime")
        if not (away and home and gameday and gametime):
            continue
        real_dt = datetime.strptime(f"{gameday} {gametime}", "%Y-%m-%d %H:%M")
        games[(away, home)] = {
            "away": away, "home": home,
            "date": real_dt.strftime("%m/%d/%Y"),
            "time": real_dt.strftime("%I:%M%p"),
            "timezone": "ET",
        }
    return games


def determine_real_bootstrap_week():
    """REAL BUG FIX (2026-09-16): bootstrap_week previously came straight
    from matchup/current.json's own "week" field. Confirmed directly this
    is unreliable for the same real reason already found and fixed in
    games.html's week selector the night before: that field doesn't track
    "the real current NFL week" — it tracks "the highest week number
    build_matchup_stats.py has ever built." A real, separate fix from two
    nights ago deliberately makes that script build ahead through the
    carryover window (week 3) early in the season, which wrote week: 3
    into that file while the real season was still in week 1 or 2 — long
    before week 3 actually started. Confirmed directly: this caused a
    real Week 2 bootstrap run to use week 3 as its target, pulling the
    wrong week's team data and evidence entirely.

    Computed independently here instead, the same real principle as the
    games.html fix: scan games/wkNN.json in order and return the first
    real week that has at least one game not yet marked played. This
    reflects the real, actual state of the season as of the last real
    data rebuild, not a stale build-time label."""
    for week in range(1, 19):
        wk_data = load_json(f"games/wk{week:02d}.json")
        if not wk_data:
            break  # that week isn't built yet — nothing further to check
        games = wk_data.get("games", [])
        if any(not g.get("played") for g in games):
            return week
    return 1  # real fallback: no games/wkNN.json exists at all yet


def main():
    ap = argparse.ArgumentParser(description="Assemble evidence for an upcoming, not-yet-played slate.")
    ap.add_argument("--bootstrap-week", type=int, default=None,
                     help="Which season-final week's team data to use as the analytical "
                          "foundation. Defaults to matchup/current.json's week.")
    ap.add_argument("--extra-away", default=None,
                     help="Add one real game NOT in the DK Classic file — e.g. Sunday/Monday "
                          "night or a special-slot game that isn't part of the DK main slate. "
                          "Game Breakdown doesn't use DK salary data at all, so this works "
                          "fine; only the DFS/Injuries evidence for this specific game will "
                          "come back empty, which is honest (no DK data exists for it), not a "
                          "bug. Requires --extra-home too.")
    ap.add_argument("--extra-home", default=None)
    ap.add_argument("--extra-date", default="TBD", help="e.g. 09/13/2026")
    ap.add_argument("--extra-time", default="TBD", help="e.g. 08:20PM")
    args = ap.parse_args()

    if args.bootstrap_week is None:
        current = load_json("matchup/current.json")
        if not current:
            sys.exit("FATAL: matchup/current.json not found and no --bootstrap-week given.")
        # REAL BUG FIX (2026-09-16): current["week"] is a stale, build-time
        # label (see determine_real_bootstrap_week()'s own docstring for
        # the confirmed real cause) — the real, current week is computed
        # independently instead. current["season"] is untouched by this
        # fix; that field isn't the part that was wrong.
        bootstrap_season = current["season"]
        bootstrap_week = determine_real_bootstrap_week()
    else:
        current = load_json("matchup/current.json")
        bootstrap_season = current["season"] if current else None
        bootstrap_week = args.bootstrap_week
    bwk = f"wk{bootstrap_week:02d}"

    # REAL CHANGE (2026-09-16): real_games — the actual schedule
    # discovery this whole script depends on — now comes from
    # games/{bwk}.json instead of a raw DK CSV read. This is the same
    # real week's games file bootstrap_week above just resolved, and
    # the same one reused below for the div_game lookup — one real
    # load, two real uses, not two separate loads of the same data.
    games_json = load_json(f"games/{bwk}.json")
    real_games = extract_real_schedule_from_games_json(games_json)
    if not real_games:
        sys.exit(f"FATAL: no real games found in games/{bwk}.json — run "
                 f"build_matchup_stats.py to build it first.")

    if args.extra_away and args.extra_home:
        real_games[(args.extra_away, args.extra_home)] = {
            "away": args.extra_away, "home": args.extra_home,
            "date": args.extra_date, "time": args.extra_time, "timezone": "ET",
        }
        print(f"Added extra game not in games/{bwk}.json: {args.extra_away} @ {args.extra_home}")
    elif args.extra_away or args.extra_home:
        sys.exit("FATAL: --extra-away and --extra-home must both be given together.")


    matchup_json = load_json(f"matchup/{bwk}.json")

    # REAL BUG FIX (2026-09-09): bootstrap_season above comes straight from
    # matchup/current.json's "season" field — which, under the carryover
    # system added earlier this project, correctly reports the CURRENT
    # season (e.g. 2026) even while every stat underneath is actually
    # last season's data carried over (2026 has no games yet). Blindly
    # trusting that field here meant this script's own "season-FINAL
    # foundation data" label, and generate_game_breakdown.py's bootstrap-
    # mode folder routing (target_season = bootstrap_source.season + 1),
    # both silently assumed "2026" when the real foundation was "2025" —
    # producing a genuinely wrong "2027" target and a wrong narrative
    # claim that carried-over 2025 stats were "2026 season-FINAL data."
    # matchup/wkNN.json's own carryover_season field (added specifically
    # for this kind of honesty) is the real source of truth for what
    # season the data underneath actually reflects — use it whenever
    # present, since it's a real field on the exact file already loaded,
    # not a second guess.
    if matchup_json and matchup_json.get("carryover_season"):
        real_foundation_season = matchup_json["carryover_season"]
        if real_foundation_season != bootstrap_season:
            print(f"  NOTE: matchup/{bwk}.json is carryover data from "
                  f"{real_foundation_season} (matchup/current.json's season field says "
                  f"{bootstrap_season}, but that's the CURRENT season label, not what "
                  f"the stats underneath actually reflect). Using {real_foundation_season} "
                  f"as the real bootstrap_season.")
            # Real bug (2026-09-09): the context-file-selection fix below
            # needs to know whether bootstrap_season got corrected away
            # from the CURRENT actual season — this script has no module-
            # level SEASON constant the way build_matchup_stats.py does
            # (that was a wrong assumption in the first version of this
            # fix, caught by a real NameError on the first live run).
            # current["season"] read from matchup/current.json above is
            # the real "current season" value — save it before it's
            # overwritten below.
            current_actual_season = bootstrap_season
            bootstrap_season = real_foundation_season
        else:
            current_actual_season = bootstrap_season
    else:
        current_actual_season = bootstrap_season

    print(f"Bootstrap: using {bootstrap_season} season, week {bootstrap_week} team data "
          f"as the foundation for {len(real_games)} real upcoming game(s)")

    threats_json = load_json(f"threats/{bwk}.json")

    # REAL BUG FIX (2026-09-09): unlike matchup/threats (which carry their
    # own carryover_season field and stay populated even at "wk01" during
    # the preseason gap), context/wkNN.json has NO carryover mechanism at
    # all — it's built fresh each week from ONLY that season's own real
    # prior games, and archived separately per season under
    # archive/{season}/context/. Loading "context/wk01.json" here during a
    # real cross-season bootstrap (bootstrap_season != current_actual_season)
    # genuinely returns 2026's own near-empty file, not 2025's real,
    # complete data — exactly what Frank found: team-level Contextual
    # Stats came back "Unavailable" in a real Game Breakdown despite
    # contextual_stats.html itself showing real, populated Week 18 2025
    # data for the same team. Finds the real, highest archived week that
    # actually exists on disk for bootstrap_season, rather than
    # hardcoding "18" (right today, but not a real, checked fact — and
    # wrong the moment a season runs short or long for any real reason).
    if bootstrap_season != current_actual_season:
        context_json = None
        for wk_num in range(22, 0, -1):
            candidate = load_json(f"archive/{bootstrap_season}/context/wk{wk_num:02d}.json")
            if candidate:
                context_json = candidate
                print(f"  Using archive/{bootstrap_season}/context/wk{wk_num:02d}.json — the real "
                      f"final archived week of {bootstrap_season}'s Contextual Stats — since "
                      f"context/{bwk}.json has no carryover data at all this early in "
                      f"{current_actual_season}.")
                break
        if context_json is None:
            print(f"  WARNING: no archived context/*.json found for {bootstrap_season} at all — "
                  f"team-level Contextual Stats evidence will be unavailable.")
    else:
        context_json = load_json(f"context/{bwk}.json")

    # REAL BUG FIX (2026-09-13): same real cause, same fix shape as
    # context_json's cross-season handling just above. The comment below
    # ("teamstats/latest.json is always-current... safe to reuse directly
    # for a bootstrap pairing") was true when this was written, because
    # at that time the real season hadn't started yet, so "current" and
    # "2025" were the same thing. Now that the real season has started,
    # teamstats/latest.json reflects 2026 (genuinely thin — Week 1-2 of
    # a new season) instead, and this silently broke Down/Distance and
    # Red Zone evidence for every bootstrap pairing — confirmed directly
    # as the real cause Frank found tonight (these fields worked during
    # bootstrap, then came back "not available" once the season began).
    # teamstats/{bootstrap_season}.json now exists as a real, separate,
    # complete file (build_matchup_stats.py writes it alongside
    # teamstats/latest.json specifically for this purpose) — use it
    # whenever this is a real cross-season bootstrap.
    if bootstrap_season != current_actual_season:
        teamstats_json = load_json(f"teamstats/{bootstrap_season}.json")
        if teamstats_json is None:
            print(f"  WARNING: teamstats/{bootstrap_season}.json not found — falling back to "
                  f"teamstats/latest.json, which reflects {current_actual_season} instead and "
                  f"may be too thin this early in the season for real Down/Distance and Red "
                  f"Zone evidence.")
            teamstats_json = load_json("teamstats/latest.json")
        else:
            print(f"  Using teamstats/{bootstrap_season}.json — the real, complete "
                  f"{bootstrap_season} team stats — for Down/Distance and Red Zone evidence, "
                  f"since teamstats/latest.json now reflects {current_actual_season} instead.")
    else:
        teamstats_json = load_json("teamstats/latest.json")
    players_json = load_json("players/latest.json")
    # REAL ADDITION (2026-09-16), per Frank's direct request: real,
    # complete 2025 season-final stats for each player, genuinely
    # distinct from both the thin current-2026 "season" field and the
    # multi-season "career" field already on each player record.
    # Confirmed directly this gap was real — career is a blend across a
    # player's whole career (e.g. 83 games "through 2025" for a
    # established starter), not a clean single-season 2025 number, and
    # would be actively misleading if labeled "2025" in a report. This
    # reuses the same real, complete 2025 snapshot already proven out
    # for the Players page season dropdown — a real archived copy from
    # before the 2026 season started, not a new build step.
    players_2025_json = load_json("archive/2025/players/latest.json")
    players_2025_by_id = {}
    for pos_list in (players_2025_json.get("players", {}) or {}).values():
        for p25 in pos_list:
            if p25.get("gsis_id"):
                players_2025_by_id[p25["gsis_id"]] = p25.get("season")

    # REAL ADDITION (2026-09-20), per Frank's direct request: real
    # home/road splits AND real opponent-tier x home/road cross-tabs for
    # each player, so Coeus can cite the real, correct side (home or
    # road, whichever this player's real team actually is this week) the
    # first time each player is mentioned in a breakdown. Both fields
    # already live as top-level keys on players_json itself (written by
    # build_matchup_stats.py) — QB is keyed by TEAM (one real identified
    # QB1 per team); RB/WR/TE are keyed by real player id directly,
    # since those positions routinely have more than one real
    # fantasy-relevant player per team. Uses whichever real season is
    # most recent (home_road_splits_seasons is already sorted newest
    # first) — the one most relevant to "this week's game," not every
    # season this data happens to cover.
    _HR_FIELD_BY_POS = {"QB": "all_qb_home_road_by_season", "RB": "all_rb_home_road_by_season",
                         "WR": "all_wr_home_road_by_season", "TE": "all_te_home_road_by_season"}
    _TIER_HR_FIELD_BY_POS = {"QB": "qb_tier_home_road_by_season", "RB": "rb_tier_home_road_by_season",
                              "WR": "wr_tier_home_road_by_season", "TE": "te_tier_home_road_by_season"}
    _hr_seasons = players_json.get("home_road_splits_seasons") or []
    _hr_latest_season = _hr_seasons[0] if _hr_seasons else None

    def home_road_for_player(pos, team, gsis_id):
        """Returns (home_road_split, tier_home_road_buckets) for the most
        recent real season this data covers — either can be None if this
        specific real player/team has no real entry there."""
        if _hr_latest_season is None:
            return None, None
        hr_field = _HR_FIELD_BY_POS.get(pos)
        tier_field = _TIER_HR_FIELD_BY_POS.get(pos)
        hr_year_data = (players_json.get(hr_field) or {}).get(str(_hr_latest_season), {}) if hr_field else {}
        tier_year_data = (players_json.get(tier_field) or {}).get(str(_hr_latest_season), {}) if tier_field else {}
        if pos == "QB":
            hr_entry = hr_year_data.get(team)
            hr_entry = hr_entry if (hr_entry and hr_entry.get("gsis_id") == gsis_id) else None
            tier_entry = tier_year_data.get(team)
            tier_entry = tier_entry if (tier_entry and tier_entry.get("gsis_id") == gsis_id) else None
        else:
            hr_entry = hr_year_data.get(gsis_id)
            tier_entry = tier_year_data.get(gsis_id)
        return hr_entry, (tier_entry.get("buckets") if tier_entry else None)

    intel_json = load_json("intel/latest.json")
    blitz_json = load_json("intel/blitz.json")
    coverage_json = load_json("intel/coverage.json")
    cbdb_json = load_json("intel/cb_rankings.json")
    dfs_json = load_json(f"dfs/{bwk}.json")
    # REAL SWITCH (2026-09-13), per Frank's direct request: injury evidence
    # now comes from this real nflverse-backed source (built by Codex,
    # build_injuries() in build_matchup_stats.py) instead of reusing
    # dfs_json's DK Classic slate Status column. Confirmed real, concrete
    # limitation of the old source: DK Classic slate coverage only, so any
    # game outside that slate (a real, confirmed example: DEN @ KC) got
    # zero injury evidence at all, regardless of real injury status.
    injuries_json = load_json(f"injuries/{bwk}.json")

    # REAL BUG FIX (2026-09-15), per Frank's direct request: div_game is
    # a real field on games/{bwk}.json's own rows (confirmed directly —
    # DEN @ KC, a real AFC West matchup, carries div_game: true there),
    # but this bootstrap script never loaded that file at all — its own
    # "game" block below was hand-built from DK's separate schedule text
    # (extract_real_schedule), which never had this field to begin with.
    # A real division rival, playing this same opponent twice a real
    # season, is exactly the case where a player's specific head-to-head
    # history against THIS opponent is real, relevant evidence — not
    # just their general recent form.
    # REAL CHANGE (2026-09-16): games_json is no longer re-loaded here —
    # it's the same real file already loaded above for real_games'
    # schedule discovery, reused here rather than fetched a second time.
    div_game_by_matchup = {
        (g.get("away"), g.get("home")): g.get("div_game")
        for g in (games_json.get("games", []) if games_json else [])
    }

    # REAL BUG FIX (2026-09-09): players_json's own "team" field reflects
    # whichever team a player's STATS were last recorded under (2025
    # season, since 2026 has none yet) — NOT their real current roster.
    # Confirmed the real, concrete failure this caused: Kenneth Walker III
    # (signed with KC as a free agent, March 2026) still showed on SEA in
    # a real Game Breakdown, because nothing here ever cross-referenced
    # rosters/latest.json (built separately, stays accurate through the
    # whole offseason). This is the exact same class of bug already found
    # and fixed in coeus.html — same real gsis_id shared between both
    # files — just never applied to this script until now. Corrects every
    # player's team in-place before any away/home filtering happens below,
    # so every downstream use of players_json sees the real roster.
    rosters_json = load_json("rosters/latest.json")
    if rosters_json:
        current_team_of = {}
        for team, roster_players in (rosters_json.get("teams") or {}).items():
            for rp in roster_players:
                if rp.get("gsis_id"):
                    current_team_of[rp["gsis_id"]] = team
        corrected = 0
        for pos, plist in (players_json.get("players") or {}).items():
            for p in plist:
                real_team = current_team_of.get(p.get("gsis_id"))
                if real_team and real_team != p.get("team"):
                    p["team"] = real_team
                    corrected += 1
        if corrected:
            print(f"  Corrected {corrected} player(s) to their real current-roster team "
                  f"(rosters/latest.json) before building evidence.")
    else:
        print("  WARNING: rosters/latest.json not found — player team assignments will "
              "use players/latest.json's stats-based team, which may be stale during "
              "the offseason (trades/signings won't be reflected).")

    required = {"matchup": matchup_json, "players": players_json}
    missing = [k for k, v in required.items() if v is None]
    if missing:
        sys.exit(f"FATAL: required bootstrap file(s) missing for {bwk}: {missing}.")

    global_notes = []
    if dfs_json is None:
        global_notes.append("No dfs/wkNN.json found — run build_dfs.py first. "
                            "DFS evidence will be unavailable.")
    # teamstats_json above is now already the real, correct season for this
    # bootstrap (see the fix and comment just above where it's loaded).
    # Its Down/Distance data is each team's own self-stat, not opponent-
    # tagged — unlike rb_rush_vs_pass/blitz above, safe to reuse directly
    # for a bootstrap pairing with no recompute needed, now that it's
    # actually loading the right season's file.
    dd_off_ranks = rank_teams_by(teamstats_json, "offense", "d3_pct", ascending=False)
    dd_def_ranks = rank_teams_by(teamstats_json, "defense", "d3_pct_allowed", ascending=True)
    # Same "each team's own self-stat, not opponent-tagged" reasoning as
    # Down/Distance above — safe to reuse directly for a bootstrap pairing.
    rz_off_run_ranks = rank_teams_by(teamstats_json, "offense", "rz_run_pct",
                                      subgroup=RED_ZONE_KEY, ascending=False)
    rz_off_pass_ranks = rank_teams_by(teamstats_json, "offense", "rz_pass_pct",
                                       subgroup=RED_ZONE_KEY, ascending=False)
    rz_def_run_ranks = rank_teams_by(teamstats_json, "defense", "rz_run_pct_faced",
                                      subgroup=RED_ZONE_KEY, ascending=False)
    rz_def_pass_ranks = rank_teams_by(teamstats_json, "defense", "rz_pass_pct_faced",
                                       subgroup=RED_ZONE_KEY, ascending=False)
    if teamstats_json is None:
        global_notes.append(f"No real teamstats data found for {bootstrap_season} — "
                            "Down/Distance evidence (3rd/4th down conversion rates) and "
                            "Red Zone Play Calling will be unavailable.")

    matchup_teams = matchup_json.get("teams", {})
    unavailable_teams = set()
    for (away, home) in real_games:
        for t in (away, home):
            if t not in matchup_teams:
                unavailable_teams.add(t)
    if unavailable_teams:
        global_notes.append(f"No {bootstrap_season} season-final team data for: "
                            f"{sorted(unavailable_teams)} — these teams' evidence will "
                            f"be incomplete (likely relocated/renamed, or missing from "
                            f"the bootstrap season's build).")

    os.makedirs("evidence_bootstrap", exist_ok=True)
    manifest_games = []

    for (away, home), sched in real_games.items():
        teams = (away, home)
        notes = []

        matchup_block = {}
        for side, team in (("away", away), ("home", home)):
            if team in matchup_teams:
                matchup_block[side] = {"team": team, **matchup_teams[team]}
            else:
                notes.append(f"no {bootstrap_season} matchup data for {team}")

        context_teams = (context_json or {}).get("teams", {})
        context_block = {}
        for side, team in (("away", away), ("home", home)):
            if team in context_teams:
                context_block[side] = {"team": team, **context_teams[team]}
            else:
                notes.append(f"no {bootstrap_season} context data for {team}")

        real_opponent_of = {away: home, home: away}
        threats_teams = (threats_json or {}).get("teams", {})
        threats_block = {}
        for side, team in (("away", away), ("home", home)):
            t = threats_teams.get(team)
            if not t:
                notes.append(f"no {bootstrap_season} threats data for {team}")
                continue
            # Deep-copy before mutating — threats_json is one shared object
            # loaded once and reused for every game in this script run.
            starters_copy = copy.deepcopy(t.get("starters", []))
            fix_threat_opponent_context(starters_copy, real_opponent_of[team], matchup_json)
            # Classification MUST run AFTER the fix above, not before — it
            # reads dr directly from cats, so classifying first would still
            # produce a tier computed against the wrong (stale) opponent
            # even after the displayed numbers were corrected.
            starters_out = [{**s, "threat_classification": fi_classify(s.get("cats", {}))}
                             for s in starters_copy]
            threats_block[side] = {"team": team, "record": t.get("record"),
                                    "opp": real_opponent_of[team], "starters": starters_out}

        players_block = {"away": [], "home": []}
        for pos, plist in (players_json.get("players", {}) or {}).items():
            for p in plist:
                # REAL ADDITION (2026-09-16): a new dict, not a mutation
                # of p itself — players_json is one shared object loaded
                # once and reused for every game in this script run
                # (same real reason threats_json gets deep-copied above),
                # so mutating it here would leak season_2025 onto every
                # later game's use of the same player record.
                p_out = {**p, "season_2025": players_2025_by_id.get(p.get("gsis_id"))}
                if p.get("team") == away:
                    side = "road"
                elif p.get("team") == home:
                    side = "home"
                else:
                    side = None
                if side:
                    # REAL ADDITION (2026-09-20): only the side that's
                    # actually true for this player THIS WEEK — an away-
                    # team player gets their real road split/tier
                    # buckets, a home-team player gets their real home
                    # ones, never both, since only one is a real fact
                    # about this specific game.
                    hr_entry, tier_buckets = home_road_for_player(pos, p.get("team"), p.get("gsis_id"))
                    p_out["home_road_split"] = (hr_entry or {}).get(side)
                    p_out["home_road_side"] = side
                    if tier_buckets:
                        p_out["tier_home_road_split"] = {
                            tier: tier_buckets.get(f"{tier}_{side}")
                            for tier in ("top", "mid", "bot") if tier_buckets.get(f"{tier}_{side}")
                        }
                if p.get("team") == away:
                    players_block["away"].append(p_out)
                elif p.get("team") == home:
                    players_block["home"].append(p_out)

        real_opponent_of = {away: home, home: away}

        qb_rvp = filter_intel_by_teams(intel_json, "teams", teams)
        rb_rvp = filter_intel_by_teams(intel_json, "rb_teams", teams)
        fix_bootstrap_opponent_context(qb_rvp, real_opponent_of, matchup_teams)
        fix_bootstrap_opponent_context(rb_rvp, real_opponent_of, matchup_teams)

        blitz_qb = filter_intel_by_teams(blitz_json, "qb_teams", teams)
        blitz_wr = filter_intel_by_teams(blitz_json, "wr_teams", teams)
        # Blitz opponent-quality fields (opp_blitz_rate, opp_blitz_rank,
        # blitz_matchup_tier) are also tagged to each team's real prior
        # opponent, same problem as above — but recomputing them needs
        # each team's own blitz-rate-allowed data, which isn't loaded in
        # this script. Flag rather than silently leave wrong; recompute is
        # a follow-up once that data source is wired in here too.
        for entry in list(blitz_qb.values()) + list(blitz_wr.values()):
            entry["bootstrap_opponent_context_note"] = (
                "opp_blitz_rate/opp_blitz_rank/blitz_matchup_tier/"
                "upcoming_opponent below are tagged to this team's real "
                "prior-season opponent, NOT this bootstrap matchup — not yet "
                "recomputed for bootstrap pairings. Do not use these fields "
                "for this matchup; the player's own vs_blitz/vs_no_blitz "
                "splits above are still valid, opponent-independent data.")

        # Raw material for Coeus to find genuine Hidden Intelligence in — not
        # named "hidden_intelligence" itself, since that name collision
        # previously taught Coeus to cite this as a source rather than
        # produce an actual Hidden Intelligence finding from it. See
        # build_evidence_package.py for the full explanation.
        matchup_pattern_data = {
            "qb_run_vs_pass": qb_rvp,
            "rb_rush_vs_pass": rb_rvp,
            "blitz_qb": blitz_qb,
            "blitz_wr": blitz_wr,
            "coverage_qb": filter_intel_by_teams(coverage_json, "qb_teams", teams),
            "coverage_wr": filter_intel_by_teams(coverage_json, "wr_teams", teams),
            "coverage_te": filter_intel_by_teams(coverage_json, "te_teams", teams),
            # Each defense's OWN season-long man/zone play-calling rate —
            # different from coverage_qb/wr/te above (how a PLAYER performs
            # facing man vs. zone). This is team-level self-stat, not
            # opponent-tagged, so it's safe to reuse directly for a
            # bootstrap pairing — same reasoning as Down/Distance elsewhere
            # in this file.
            "team_coverage_rate": filter_intel_by_teams(coverage_json, "team_coverage_rate", teams),
        }

        cbdb_block = []
        if cbdb_json and cbdb_json.get("available"):
            cbdb_block = [p for p in cbdb_json.get("players", []) if p.get("team") in teams]

        dfs_block = {"available": dfs_json is not None, "players": []}
        if dfs_json is not None:
            game_players = [p for p in dfs_json.get("players", []) if p.get("team") in teams]
            dfs_block["players"] = game_players
            if not game_players:
                dfs_block["note"] = (f"{away}/{home} are not part of the DraftKings Classic "
                                      f"slate this file covers — no DFS salary data exists for "
                                      f"this game. This is a scope gap (this game simply isn't "
                                      f"in that slate), not a data error.")

        # REAL SWITCH (2026-09-13): injuries_block is now built entirely
        # separately from dfs_block, from the real nflverse-backed
        # injuries/{bwk}.json — covers every real NFL team regardless of
        # DK Classic slate inclusion, unlike the old DK-derived source.
        # Preserves a real, three-way honest distinction per team, not
        # collapsed into one generic "no data" case:
        #   1. The injuries file itself failed to load at all (a real
        #      data-source problem, flagged as such).
        #   2. The file loaded, but this team isn't in its own real
        #      teams_represented list — meaning nflverse's relevance
        #      filter (report_status populated, or practice status
        #      Limited/Did Not Participate) found nothing to report for
        #      this team this week. This is a real, honest "no
        #      qualifying injuries," not a gap — must not be phrased as
        #      unavailable data.
        #   3. Real players found — listed with the real, fuller field
        #      set nflverse provides (report + practice status and
        #      injury detail), not flattened down to a single "status"
        #      string the way the old DK-derived version was.
        if injuries_json is None:
            injuries_block = {"source": "nflverse (injuries/{bwk}.json)", "available": False,
                               "players": [],
                               "note": f"injuries/{bwk}.json not found — injury evidence is "
                                       f"genuinely unavailable for this game, not confirmed-healthy."}
        elif not injuries_json.get("teams_represented"):
            # REAL BUG FIX (2026-09-16), per Frank's direct question:
            # confirmed directly this real gap exists — a file can be
            # present but genuinely empty (teams_represented: [],
            # team_count: 0), which happens when nflverse's real
            # practice-week injury reports simply haven't been
            # published yet for a future week (confirmed as the real
            # cause here — the file existed, dated the night before,
            # with zero teams represented league-wide). Zero teams
            # represented across the entire league is not a real,
            # confirmed "everyone is healthy" result the way one or two
            # missing teams can honestly be — no NFL week has zero
            # reportable injuries across all 32 teams. This is
            # indistinguishable from a failed or premature fetch and
            # must be reported as genuinely unavailable, not silently
            # folded into the same "confirmed healthy" branch below
            # that's correct only when SOME real teams are present.
            injuries_block = {"source": "nflverse (injuries/{bwk}.json)", "available": False,
                               "players": [],
                               "note": f"injuries/{bwk}.json exists but reports zero teams "
                                       f"league-wide — the real practice-week injury data for "
                                       f"this week likely hadn't been published yet when this "
                                       f"file was built. Genuinely unavailable, not confirmed-"
                                       f"healthy; re-run build_matchup_stats.py closer to "
                                       f"kickoff for a real pull."}
        else:
            teams_represented = set(injuries_json.get("teams_represented", []))
            game_players = [p for p in injuries_json.get("players", []) if p.get("team") in teams]
            injuries_block = {
                "source": f"nflverse real injury report (status_policy: "
                          f"{injuries_json.get('status_policy')})",
                "available": True,
                "players": game_players,
            }
            missing_teams = [t for t in teams if t not in teams_represented]
            if missing_teams:
                injuries_block["note"] = (
                    f"{', '.join(missing_teams)} had no real nflverse-reported injury-relevant "
                    f"player(s) for {injuries_json.get('season')} week {injuries_json.get('week')} "
                    f"(no report_status, and no Limited/Did Not Participate practice status) — a "
                    f"real, confirmed result from the real injury file, not a missing-data gap.")

        bundle = {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "evidence_type": "BOOTSTRAP — upcoming game, not yet played",
            "game": {
                "away": away, "home": home,
                "scheduled_date": sched["date"], "scheduled_time": sched["time"],
                "timezone": sched["timezone"], "played": False,
                "div_game": div_game_by_matchup.get((away, home)),
                "note": ("This game has NOT been played. There is no box score, result, "
                         "or current-season line/spread available. All team-level analytics "
                         f"below are {bootstrap_season} season-FINAL data, used as the best "
                         f"available foundation until real current-season data exists."),
            },
            "bootstrap_source": {"season": bootstrap_season, "week": bootstrap_week,
                                  "note": (f"Every field below (matchup, team_context, threats, "
                                           f"players, matchup_pattern_data, cb_db_rankings) is "
                                           f"{bootstrap_season} season-final data for these two "
                                           f"teams — NOT specific to any {bootstrap_season} game "
                                           f"between them, which likely never happened as this "
                                           f"exact pairing.")},
            "matchup": matchup_block,
            "team_context": context_block,
            "down_distance": {
                "away": down_distance_for_team(teamstats_json, away, dd_off_ranks, dd_def_ranks),
                "home": down_distance_for_team(teamstats_json, home, dd_off_ranks, dd_def_ranks),
            },
            "red_zone_play_calling": {
                "away": red_zone_for_team(teamstats_json, away, rz_off_run_ranks, rz_off_pass_ranks,
                                           rz_def_run_ranks, rz_def_pass_ranks),
                "home": red_zone_for_team(teamstats_json, home, rz_off_run_ranks, rz_off_pass_ranks,
                                           rz_def_run_ranks, rz_def_pass_ranks),
            },
            "threats": threats_block,
            "players": players_block,
            "matchup_pattern_data": matchup_pattern_data,
            "cb_db_rankings": cbdb_block,
            "dfs": dfs_block,
            "injuries": injuries_block,
            "data_notes": notes,
        }

        out_path = f"evidence_bootstrap/{away}_{home}.json"
        with open(out_path, "w") as f:
            json.dump(bundle, f)
        manifest_games.append({"away": away, "home": home, "file": out_path,
                                "scheduled": f"{sched['date']} {sched['time']} {sched['timezone']}",
                                "data_notes": notes})
        print(f"  Wrote {out_path}" + (f" — {len(notes)} note(s)" if notes else ""))

    manifest = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "bootstrap_source": {"season": bootstrap_season, "week": bootstrap_week},
        "games": manifest_games,
        "global_notes": global_notes,
    }
    with open("evidence_bootstrap/manifest.json", "w") as f:
        json.dump(manifest, f, indent=2)
    print(f"\nWrote evidence_bootstrap/manifest.json — {len(manifest_games)} real upcoming game(s)")
    if global_notes:
        print("Global notes:")
        for n in global_notes:
            print(f"  - {n}")


if __name__ == "__main__":
    main()
