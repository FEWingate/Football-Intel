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
    is inferred or guessed."""
    games = {}
    for info in dk_df["Game Info"].dropna().unique():
        m = re.match(r"^([A-Z]+)@([A-Z]+)\s+(\S+)\s+(\S+\s*[AP]M)\s*(\S*)", str(info))
        if not m:
            continue
        away, home, date, time, tz = m.groups()
        games[(away, home)] = {"away": away, "home": home, "date": date,
                                "time": time, "timezone": tz or "ET"}
    return games


def main():
    ap = argparse.ArgumentParser(description="Assemble evidence for an upcoming, not-yet-played slate.")
    ap.add_argument("--bootstrap-week", type=int, default=None,
                     help="Which season-final week's team data to use as the analytical "
                          "foundation. Defaults to matchup/current.json's week.")
    args = ap.parse_args()

    if not os.path.exists(DK_SALARY_PATH):
        sys.exit(f"FATAL: no DraftKings salary file at {DK_SALARY_PATH}.")
    dk_df = pd.read_csv(DK_SALARY_PATH)
    real_games = extract_real_schedule(dk_df)
    if not real_games:
        sys.exit("FATAL: couldn't parse any real games from the DK file's Game Info column.")

    if args.bootstrap_week is None:
        current = load_json("matchup/current.json")
        if not current:
            sys.exit("FATAL: matchup/current.json not found and no --bootstrap-week given.")
        bootstrap_season, bootstrap_week = current["season"], current["week"]
    else:
        current = load_json("matchup/current.json")
        bootstrap_season = current["season"] if current else None
        bootstrap_week = args.bootstrap_week
    bwk = f"wk{bootstrap_week:02d}"

    print(f"Bootstrap: using {bootstrap_season} season, week {bootstrap_week} team data "
          f"as the foundation for {len(real_games)} real upcoming game(s)")

    matchup_json = load_json(f"matchup/{bwk}.json")
    threats_json = load_json(f"threats/{bwk}.json")
    context_json = load_json(f"context/{bwk}.json")
    players_json = load_json("players/latest.json")
    intel_json = load_json("intel/latest.json")
    blitz_json = load_json("intel/blitz.json")
    coverage_json = load_json("intel/coverage.json")
    cbdb_json = load_json("intel/cb_rankings.json")
    dfs_json = load_json(f"dfs/{bwk}.json")

    required = {"matchup": matchup_json, "players": players_json}
    missing = [k for k, v in required.items() if v is None]
    if missing:
        sys.exit(f"FATAL: required bootstrap file(s) missing for {bwk}: {missing}.")

    global_notes = []
    if dfs_json is None:
        global_notes.append("No dfs/wkNN.json found — run build_dfs.py first. "
                            "DFS evidence will be unavailable.")

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

        threats_teams = (threats_json or {}).get("teams", {})
        threats_block = {}
        for side, team in (("away", away), ("home", home)):
            t = threats_teams.get(team)
            if not t:
                notes.append(f"no {bootstrap_season} threats data for {team}")
                continue
            starters_out = [{**s, "threat_classification": fi_classify(s.get("cats", {}))}
                             for s in t.get("starters", [])]
            threats_block[side] = {"team": team, "record": t.get("record"),
                                    "opp": t.get("opp"), "starters": starters_out}

        players_block = {"away": [], "home": []}
        for pos, plist in (players_json.get("players", {}) or {}).items():
            for p in plist:
                if p.get("team") == away:
                    players_block["away"].append(p)
                elif p.get("team") == home:
                    players_block["home"].append(p)

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
        }

        cbdb_block = []
        if cbdb_json and cbdb_json.get("available"):
            cbdb_block = [p for p in cbdb_json.get("players", []) if p.get("team") in teams]

        dfs_block = {"available": dfs_json is not None, "players": []}
        injuries_block = {"source": "DraftKings slate Status column (not a general "
                                     "injury feed)", "players": []}
        if dfs_json is not None:
            game_players = [p for p in dfs_json.get("players", []) if p.get("team") in teams]
            dfs_block["players"] = game_players
            for p in game_players:
                if p.get("status"):
                    injuries_block["players"].append({"name": p["name"], "team": p["team"],
                                                        "status": p["status"]})

        bundle = {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "evidence_type": "BOOTSTRAP — upcoming game, not yet played",
            "game": {
                "away": away, "home": home,
                "scheduled_date": sched["date"], "scheduled_time": sched["time"],
                "timezone": sched["timezone"], "played": False,
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
