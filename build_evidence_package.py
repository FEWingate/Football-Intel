"""
COEUS EVIDENCE PACKAGE ASSEMBLER
=================================
Gathers everything Coeus needs for one week into a "frozen" bundle: one JSON
file per game, plus a manifest. This is pure local processing — every input
already sits on disk after `build_matchup_stats.py` has run. No network calls.

WHY PER-GAME FILES, NOT ONE GIANT BUNDLE:
Coeus's DFS Report is generated one game at a time (see the DFS Intelligence
Report Standard, Section 19 — the per-game DFS Breakdown is the atomic unit
the slate-wide report is built from). One file per game keeps each generation
call properly scoped, keeps files independently regenerable/debuggable, and
avoids handing a single API call the entire week's data at once.

"FROZEN" MEANS: this snapshot doesn't shift once written. Every report
generated from a given week's Evidence Package used the exact same inputs —
reproducible, and safe to hand to multiple Coeus calls without the ground
shifting between them.

INPUTS (all read from disk, all already built by build_matchup_stats.py):
  games/wkNN.json        schedule, lines, box scores
  matchup/wkNN.json      team offense/defense season stats + positional splits
  threats/wkNN.json      raw convergence data (Coeus needs CLASSIFIED tiers,
                         so this script ports fiClassify() from fi-shell.js
                         to Python rather than handing Coeus raw numbers to
                         interpret itself — Coeus must never invent Threats)
  context/wkNN.json      production vs Top-10/Mid-12/Bottom-10 tiers faced
  teamstats/latest.json  always-current season team stats
  players/latest.json    always-current season/career player stats
  intel/latest.json      QB run-vs-pass, RB rush-vs-pass Hidden Intelligence
  intel/blitz.json       Blitz Impact Report
  intel/coverage.json    Coverage Breakdown (season retrospective)
  intel/cb_rankings.json CB/DB Coverage Rankings (live/weekly)
  dfs/wkNN.json          scored DK slate — built by build_dfs.py, which is
                         the single source of truth for DFS scoring/name-
                         matching. Run build_dfs.py BEFORE this script.

OUTPUT:
  evidence/wkNN/{AWAY}_{HOME}.json   one file per scheduled game
  evidence/wkNN/manifest.json        season, week, generated_at, game list,
                                      and a running log of any data gaps
"""

import json
import os
import sys
from datetime import datetime, timezone

def load_json(path):
    if not os.path.exists(path):
        return None
    with open(path) as f:
        return json.load(f)


DOWN_DIST_KEY = "Down/Distance"  # matches DOWN_DIST_SUBGROUP_NAME in build_matchup_stats.py

def rank_teams_by(teamstats_json, side, field, ascending=False):
    """teamstats/latest.json stores raw {"tot":.., "avg":..} pairs with NO
    rank included — every other stat category on this site pairs a value
    with a league rank (matching the Stat-Rank Pairing Rule), so this
    computes ranks locally rather than handing Coeus an unranked number.
    ascending=True for defensive "allowed" stats where LOWER is better."""
    if not teamstats_json:
        return {}
    vals = {}
    for team, t in teamstats_json.get("teams", {}).items():
        v = t.get(side, {}).get(DOWN_DIST_KEY, {}).get(field, {}).get("avg")
        if v is not None:
            vals[team] = v
    ordered = sorted(vals, key=lambda t: vals[t], reverse=not ascending)
    return {team: {"v": vals[team], "r": i + 1} for i, team in enumerate(ordered)}

def down_distance_for_team(teamstats_json, team, off_ranks, def_ranks):
    """Extract Down/Distance evidence for one team, translating the source
    file's internal abbreviations (d3_pct, d4_go_pct, etc.) into clear
    field names — the same kind of abbreviation-leak that caused the
    r7/dr31 rank-shorthand bug elsewhere in this project, avoided here by
    not exposing the raw internal keys at all."""
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


# ── Threat System classification, ported EXACTLY from fi-shell.js's
# FI_TIERS / fiClassify() so Coeus receives the same tier labels the site
# itself shows — never raw numbers for Coeus to classify on its own. ──────
FI_TIERS = [
    {"key": "nuclear", "label": "Nuclear", "player_max": 3, "def_min": 30},
    {"key": "elite", "label": "Elite", "player_max": 5, "def_min": 28},
    {"key": "standard", "label": "Standard", "player_max": 10, "def_min": 23},
]


def fi_classify(cats):
    """Python port of fi-shell.js's fiClassify(). Same tiering logic, same
    Double/Triple/Quadruple naming, so the Threat data Coeus sees always
    matches what a person looking at the live site would see."""
    assigned = {}
    for cat, c in (cats or {}).items():
        for t in FI_TIERS:
            if c["r"] <= t["player_max"] and c["dr"] >= t["def_min"]:
                assigned[cat] = t["key"]
                break

    out = []
    used = set()
    for t in FI_TIERS:
        conv = [c for c in assigned if assigned[c] == t["key"]]
        if not conv:
            continue
        extra = [c for c, v in cats.items()
                 if c not in conv and c not in used and v["r"] <= t["player_max"]]
        used.update(conv)
        used.update(extra)
        out.append({
            "tier": t["key"], "tier_label": t["label"],
            "type": "Quadruple" if len(conv) >= 2 else ("Triple" if extra else "Double"),
            "categories_converged": conv, "categories_extra": extra,
        })
    return out


def filter_intel_by_teams(intel_json, key, teams):
    """intel/*.json report sections (qb_teams/rb_teams/wr_teams/te_teams) are
    dicts KEYED BY team abbreviation, not lists — confirmed against real
    2025 data (intel/latest.json, intel/blitz.json, intel/coverage.json all
    follow this pattern). Returns {team: entry} for just the two teams in
    this game."""
    if not intel_json or key not in intel_json:
        return {}
    section = intel_json[key]
    return {team: section[team] for team in teams if team in section}


def main():
    current = load_json("matchup/current.json")
    if not current:
        sys.exit("FATAL: matchup/current.json not found — run build_matchup_stats.py "
                  "first. The Evidence Package always reads from ITS pointer, never "
                  "a hardcoded week, for the same reason DFS Center does.")
    season, week = current["season"], current["week"]
    wk = f"wk{week:02d}"
    print(f"Assembling Evidence Package — season {season}, week {week}")

    games_json = load_json(f"games/{wk}.json")
    matchup_json = load_json(f"matchup/{wk}.json")
    threats_json = load_json(f"threats/{wk}.json")
    context_json = load_json(f"context/{wk}.json")
    teamstats_json = load_json("teamstats/latest.json")
    players_json = load_json("players/latest.json")
    intel_json = load_json("intel/latest.json")
    blitz_json = load_json("intel/blitz.json")
    coverage_json = load_json("intel/coverage.json")
    cbdb_json = load_json("intel/cb_rankings.json")
    dfs_json = load_json(f"dfs/{wk}.json")

    required = {"games": games_json, "matchup": matchup_json,
                "players": players_json}
    missing = [k for k, v in required.items() if v is None]
    if missing:
        sys.exit(f"FATAL: required file(s) missing for {wk}: {missing}. "
                  f"Run build_matchup_stats.py all first.")

    global_notes = []
    if dfs_json is None:
        global_notes.append(f"No dfs/{wk}.json found — run build_dfs.py before this "
                             f"script for DFS evidence to be available.")

    os.makedirs(f"evidence/{wk}", exist_ok=True)
    manifest_games = []

    # Computed once for the whole league, reused for every game below —
    # ranking is a full-league operation, not something to redo per game.
    dd_off_ranks = rank_teams_by(teamstats_json, "offense", "d3_pct", ascending=False)
    dd_def_ranks = rank_teams_by(teamstats_json, "defense", "d3_pct_allowed", ascending=True)
    if teamstats_json is None:
        global_notes.append("teamstats/latest.json not found — Down/Distance evidence "
                            "(3rd/4th down conversion rates) will be unavailable.")

    for g in games_json.get("games", []):
        away, home = g["away"], g["home"]
        teams = (away, home)
        notes = []

        # ── Matchup: both teams' own season off/def blocks, side by side —
        # matches exactly what matchup_stats.html itself shows in its modal.
        matchup_teams = matchup_json.get("teams", {})
        matchup_block = {}
        for side, team in (("away", away), ("home", home)):
            if team in matchup_teams:
                matchup_block[side] = {"team": team, **matchup_teams[team]}
            else:
                notes.append(f"no matchup/{wk}.json data for {team}")

        # ── Team context: production vs Top-10/Mid-12/Bottom-10 tiers faced
        context_teams = (context_json or {}).get("teams", {})
        context_block = {}
        for side, team in (("away", away), ("home", home)):
            if team in context_teams:
                context_block[side] = {"team": team, **context_teams[team]}
            else:
                notes.append(f"no context/{wk}.json data for {team}")

        # ── Threats: classified via the Python port of fiClassify(), never
        # raw numbers — Coeus must receive Threats pre-classified.
        threats_teams = (threats_json or {}).get("teams", {})
        threats_block = {}
        for side, team in (("away", away), ("home", home)):
            t = threats_teams.get(team)
            if not t:
                notes.append(f"no threats/{wk}.json data for {team}")
                continue
            starters_out = []
            for s in t.get("starters", []):
                classification = fi_classify(s.get("cats", {}))
                starters_out.append({**s, "threat_classification": classification})
            threats_block[side] = {"team": team, "record": t.get("record"),
                                    "opp": t.get("opp"), "starters": starters_out}

        # ── Players: full roster stat lines for both teams
        players_block = {"away": [], "home": []}
        for pos, plist in (players_json.get("players", {}) or {}).items():
            for p in plist:
                if p.get("team") == away:
                    players_block["away"].append(p)
                elif p.get("team") == home:
                    players_block["home"].append(p)

        # ── Raw material for Coeus to find genuine Hidden Intelligence in —
        # QB run-vs-pass, RB rush-vs-pass, Blitz, Coverage splits, filtered
        # to just the two teams in this game. Deliberately NOT named
        # "hidden_intelligence" as a JSON key: an earlier version used that
        # name, and Coeus treated it as a citable source ("per Hidden
        # Intelligence...") instead of a standing requirement to actually
        # produce a Hidden Intelligence finding — this is the raw data the
        # finding gets built FROM, not the finding itself.
        matchup_pattern_data = {
            # NOTE: intel/latest.json stores QB Run-vs-Pass data under the key
            # "teams" (not "qb_teams") — build_matchup_stats.py's
            # build_intel_reports() covers QB and RB together in one file and
            # named the QB half generically. RB Run-vs-Pass correctly uses
            # "rb_teams". Confirmed against the real source on 2026-08-13
            # after this exact mismatch silently produced an empty QB
            # Run-vs-Pass section in every evidence bundle built before this.
            "qb_run_vs_pass": filter_intel_by_teams(intel_json, "teams", teams),
            "rb_rush_vs_pass": filter_intel_by_teams(intel_json, "rb_teams", teams),
            "blitz_qb": filter_intel_by_teams(blitz_json, "qb_teams", teams),
            "blitz_wr": filter_intel_by_teams(blitz_json, "wr_teams", teams),
            "coverage_qb": filter_intel_by_teams(coverage_json, "qb_teams", teams),
            "coverage_wr": filter_intel_by_teams(coverage_json, "wr_teams", teams),
            "coverage_te": filter_intel_by_teams(coverage_json, "te_teams", teams),
        }

        # ── CB/DB Coverage Rankings for defenders on both teams
        cbdb_block = []
        if cbdb_json and cbdb_json.get("available"):
            cbdb_block = [p for p in cbdb_json.get("players", []) if p.get("team") in teams]
        elif cbdb_json is not None:
            notes.append("CB/DB rankings present but marked unavailable for this build")

        # ── DFS: read from dfs/wkNN.json — built by build_dfs.py, which
        # ports dfs_center.html's EXACT scoring and name-matching logic.
        # This script deliberately does NOT re-parse the DK CSV itself or
        # do its own name matching — two independent matchers for the same
        # problem is exactly the kind of drift this whole architecture
        # exists to avoid. Run build_dfs.py before this script.
        dfs_block = {"available": dfs_json is not None, "players": []}
        injuries_block = {"source": "DraftKings slate Status column (not a "
                                     "general injury feed)", "players": []}
        if dfs_json is not None:
            game_players = [p for p in dfs_json.get("players", []) if p.get("team") in teams]
            dfs_block["players"] = game_players
            for p in game_players:
                if p.get("status"):
                    injuries_block["players"].append({
                        "name": p["name"], "team": p["team"], "status": p["status"],
                    })
            unmatched = sum(1 for p in game_players if not p.get("matched") and p.get("pos") != "DST"
                             and (p.get("avg_pts") or 0) >= 5)
            if unmatched:
                notes.append(f"{unmatched} relevant DK player(s) in this game did not match "
                             f"a Football Intel player record by name")
        else:
            notes.append("dfs/wkNN.json not found — run build_dfs.py before this script "
                         "for DFS evidence to be available")

        # ── Game info: schedule, lines, box score (from games/wkNN.json)
        game_info = dict(g)

        bundle = {
            "season": season, "week": week,
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "game": game_info,
            "matchup": matchup_block,
            "team_context": context_block,
            "down_distance": {
                "away": down_distance_for_team(teamstats_json, away, dd_off_ranks, dd_def_ranks),
                "home": down_distance_for_team(teamstats_json, home, dd_off_ranks, dd_def_ranks),
            },
            "threats": threats_block,
            "players": players_block,
            "matchup_pattern_data": matchup_pattern_data,
            "cb_db_rankings": cbdb_block,
            "dfs": dfs_block,
            "injuries": injuries_block,
            "data_notes": notes,
        }

        out_path = f"evidence/{wk}/{away}_{home}.json"
        with open(out_path, "w") as f:
            json.dump(bundle, f)
        manifest_games.append({"away": away, "home": home, "file": out_path,
                                "data_notes": notes})
        print(f"  Wrote {out_path}" + (f" — {len(notes)} note(s)" if notes else ""))

    manifest = {
        "season": season, "week": week,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "games": manifest_games,
        "global_notes": global_notes,
    }
    with open(f"evidence/{wk}/manifest.json", "w") as f:
        json.dump(manifest, f, indent=2)
    print(f"\nWrote evidence/{wk}/manifest.json — {len(manifest_games)} game(s)")
    if global_notes:
        print("Global notes:")
        for n in global_notes:
            print(f"  - {n}")


if __name__ == "__main__":
    main()
