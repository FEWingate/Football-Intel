"""
BUILD_DFS.PY
============
Server-side port of dfs_center.html's scoring engine (computeAll() and its
supporting name-matching functions). This exists so DFS Center's own numbers
and Coeus's DFS Report numbers come from ONE source of truth instead of two
independent implementations quietly drifting apart over a season.

Ported EXACTLY from dfs_center.html — same formulas, same normalization,
same name-matching fallback logic, same fallback rules for thin samples.
Where the JS and this file disagree, that's a bug to fix, not a design
choice to make twice.

NOT YET PORTED: the LP-based lineup optimizer (buildLineupModel() in
dfs_center.html). That's needed for Section 21 of the DFS Intelligence
Report Standard (the full slate-wide tournament lineup) — a later step,
once per-game generation is proven out. This script currently covers
per-player scoring only, which is what the per-game DFS Breakdown needs.

INPUT:
  matchup/current.json     season+week pointer (never hardcode a week)
  matchup/wkNN.json        opponent defense-vs-position ranks
  players/latest.json      season stats, splits vs tier, ceiling data
  data/dfs/DKSalaries.csv  weekly DraftKings salary export (manual, same
                           convention as build_evidence_package.py)

OUTPUT:
  dfs/wkNN.json — every player from the DK slate, fully scored, matched to
  Football Intel data where possible. This is what build_evidence_package.py
  should read from for the "dfs" block in each game's evidence bundle.
"""

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


def load_json(path):
    if not os.path.exists(path):
        return None
    with open(path) as f:
        return json.load(f)


# ── Name matching, ported EXACTLY from dfs_center.html's normalizeName() /
# buildNameIndex() / firstNamesSimilar() / matchSiteData(). ────────────────
SUFFIX_RE = re.compile(r"\b(jr|sr|ii|iii|iv|v)\b\.?\s*$")


def normalize_name(name):
    n = str(name).lower().strip()
    n = n.replace(".", "").replace("'", "")
    n = SUFFIX_RE.sub("", n).strip()
    return re.sub(r"\s+", " ", n)


def build_name_index(playerstats):
    exact, lastname = {}, {}
    for pos in ("QB", "RB", "WR", "TE"):
        for p in playerstats.get("players", {}).get(pos, []):
            norm = normalize_name(p["name"])
            exact[f"{norm}|{pos}"] = p
            last = norm.split(" ")[-1] if norm else ""
            lastname.setdefault(f"{last}|{pos}", []).append(p)
    return {"exact": exact, "lastname": lastname}


def first_names_similar(norm_a, norm_b):
    a = norm_a.split(" ")[0] if norm_a else ""
    b = norm_b.split(" ")[0] if norm_b else ""
    if not a or not b:
        return False
    n = min(3, len(a), len(b))
    return a[:n] == b[:n]


def match_site_data(dk_player, name_index):
    norm = normalize_name(dk_player["name"])
    pos = dk_player["pos"]
    exact_hit = name_index["exact"].get(f"{norm}|{pos}")
    if exact_hit:
        return exact_hit
    last = norm.split(" ")[-1] if norm else ""
    candidates = name_index["lastname"].get(f"{last}|{pos}", [])
    if len(candidates) != 1:
        return None
    # Last name alone isn't safe — see dfs_center.html's own comment on this
    # exact line: two different "Henry"s at the same position would
    # otherwise wrongly merge a deep-bench player into a star's stats.
    cand = candidates[0]
    return cand if first_names_similar(norm, normalize_name(cand["name"])) else None


def tier_of(rank):
    if rank <= 10:
        return "top"
    if rank <= 22:
        return "mid"
    return "bot"


def opponent_of(team, game_info):
    m = re.match(r"^([A-Z]+)@([A-Z]+)", str(game_info))
    if not m:
        return None
    away, home = m.group(1), m.group(2)
    if away == team:
        return home
    if home == team:
        return away
    return None


def normalize_row(row):
    return {
        "name": row.get("Name"), "pos": row.get("Position"), "team": row.get("TeamAbbrev"),
        "salary": int(row["Salary"]) if pd.notna(row.get("Salary")) else 0,
        "avg_pts": float(row["AvgPointsPerGame"]) if pd.notna(row.get("AvgPointsPerGame")) else 0.0,
        "status": str(row["Status"]).strip() if pd.notna(row.get("Status")) else "",
        "game_info": row.get("Game Info") or "",
    }


def norm(v, lo, hi):
    return ((v - lo) / (hi - lo)) * 100 if hi > lo else 50.0


def compute_all(players, matchup_json, name_index):
    """Direct port of computeAll() in dfs_center.html. Mutates each player
    dict in place, exactly mirroring the JS version's field names (in
    snake_case) so anyone comparing the two side by side can follow along."""
    by_pos = {}
    for p in players:
        p["opp"] = opponent_of(p["team"], p["game_info"])
        p["value"] = (p["avg_pts"] / (p["salary"] / 1000)) if p["salary"] else 0.0
        p["site_data"] = match_site_data(p, name_index) if p["pos"] != "DST" else None
        by_pos.setdefault(p["pos"], []).append(p)

    for pos, group in by_pos.items():
        values = [p["value"] for p in group]
        pts = [p["avg_pts"] for p in group]
        v_lo, v_hi = min(values), max(values)
        p_lo, p_hi = min(pts), max(pts)

        pos_labels = (matchup_json or {}).get("labels", {}).get("pos", {}).get(pos)
        primary_key = next(iter(pos_labels), None) if pos_labels else None

        for p in group:
            p["value_score"] = norm(p["value"], v_lo, v_hi)
            p["perf_score"] = norm(p["avg_pts"], p_lo, p_hi)
            p["opp_score"], p["opp_rank_label"], p["opp_tier"] = None, None, None

            if matchup_json and p["opp"] and p["opp"] in matchup_json.get("teams", {}):
                opp_team = matchup_json["teams"][p["opp"]]
                if pos == "DST":
                    r = (opp_team.get("team_off") or {}).get("ppg", {}).get("r")
                    if r:
                        p["opp_score"] = ((r - 1) / 31) * 100
                        p["opp_rank_label"] = f"Opp offense #{r}"
                        p["opp_tier"] = tier_of(r)
                elif primary_key:
                    r = ((opp_team.get("def") or {}).get(pos, {}).get(primary_key, {}) or {}).get("r")
                    if r:
                        p["opp_score"] = ((r - 1) / 31) * 100
                        p["opp_rank_label"] = f"Def vs {pos} #{r}"
                        p["opp_tier"] = tier_of(r)

            has_opp = p["opp_score"] is not None
            p["composite"] = (0.4 * p["opp_score"] + 0.3 * p["value_score"] + 0.3 * p["perf_score"]
                               if has_opp else 0.5 * p["value_score"] + 0.5 * p["perf_score"])
            p["quality"] = (0.5 * p["opp_score"] + 0.5 * p["perf_score"]) if has_opp else p["perf_score"]

            # Matchup History: this player's own history vs. the tier their
            # actual opponent belongs to. 2+ qualifying games required, or
            # fall back to season average — a 1-game sample is too noisy.
            p["matchup_history_games"] = 0
            if p["site_data"] and p["opp_tier"] and primary_key:
                split = (p["site_data"].get("splits") or {}).get(p["opp_tier"])
                games_for_key = (split.get("games", {}) or {}).get(primary_key, 0) if split else 0
                m_val = (split.get("m", {}) or {}).get(primary_key) if split else None
                if split and games_for_key >= 2 and m_val is not None:
                    p["matchup_history_raw"] = m_val
                    p["matchup_history_games"] = games_for_key
                else:
                    p["matchup_history_raw"] = p["avg_pts"]
            else:
                p["matchup_history_raw"] = p["avg_pts"]

            # Ceiling: average of this player's top-3 DK-scored games this
            # season. 2+ games logged required, else falls back to season avg.
            ceiling = (p["site_data"] or {}).get("ceiling") if p["site_data"] else None
            if ceiling and ceiling.get("games", 0) >= 2:
                p["ceiling_raw"] = ceiling["top3avg"]
                p["ceiling_games"] = ceiling["games"]
                p["ceiling_best"] = ceiling.get("best")
            else:
                p["ceiling_raw"] = p["avg_pts"]
                p["ceiling_games"] = 0
                p["ceiling_best"] = None

        mh_vals = [p["matchup_history_raw"] for p in group]
        ce_vals = [p["ceiling_raw"] for p in group]
        mh_lo, mh_hi = min(mh_vals), max(mh_vals)
        ce_lo, ce_hi = min(ce_vals), max(ce_vals)
        for p in group:
            p["matchup_history_score"] = norm(p["matchup_history_raw"], mh_lo, mh_hi)
            p["ceiling_score"] = norm(p["ceiling_raw"], ce_lo, ce_hi)

    return players


def main():
    current = load_json("matchup/current.json")
    if not current:
        sys.exit("FATAL: matchup/current.json not found — run build_matchup_stats.py first.")
    season, week = current["season"], current["week"]
    wk = f"wk{week:02d}"
    print(f"Building DFS scoring — season {season}, week {week}")

    if not os.path.exists(DK_SALARY_PATH):
        sys.exit(f"FATAL: no DraftKings salary file at {DK_SALARY_PATH}. "
                  f"Place this week's export there before running.")

    matchup_json = load_json(f"matchup/{wk}.json")
    playerstats = load_json("players/latest.json")
    if not matchup_json:
        print(f"  WARNING: no matchup/{wk}.json — opponent scoring will be unavailable "
              f"(value/performance scores still compute).")
    if not playerstats:
        print("  WARNING: no players/latest.json — Matchup History and Ceiling modes "
              "will fall back to season average for every player.")

    name_index = build_name_index(playerstats) if playerstats else {"exact": {}, "lastname": {}}

    df = pd.read_csv(DK_SALARY_PATH)
    players = [normalize_row(row) for _, row in df.iterrows()]
    players = [p for p in players if p["pos"]]

    compute_all(players, matchup_json, name_index)

    unmatched_relevant = [p for p in players if p["pos"] != "DST" and not p["site_data"] and p["avg_pts"] >= 5]

    # site_data is the full matched player record (season/career/log/splits/
    # ceiling) — large, and already available separately in players/latest.
    # Keep only what a report needs to reference without re-fetching, same
    # as dfs_center.html effectively does by holding it in memory client-side.
    for p in players:
        p["matched"] = p["site_data"] is not None
        p["football_intel_player_id"] = p["site_data"].get("player_id") if p["site_data"] else None
        p.pop("site_data", None)

    os.makedirs("dfs", exist_ok=True)
    out = {
        "season": season, "week": week,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "matchup_data_available": matchup_json is not None,
        "player_stats_available": playerstats is not None,
        "unmatched_relevant_count": len(unmatched_relevant),
        "unmatched_relevant": [p["name"] for p in unmatched_relevant[:25]],
        "players": players,
    }
    with open(f"dfs/{wk}.json", "w") as f:
        json.dump(out, f)
    print(f"Wrote dfs/{wk}.json — {len(players)} players scored, "
          f"{len(unmatched_relevant)} relevant unmatched")


if __name__ == "__main__":
    main()
