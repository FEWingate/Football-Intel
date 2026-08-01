"""
FOOTBALL INTEL — Matchup Statistics builder
Team + positional offense vs. that week's opponent's defense-allowed-to-position.

Same data-horizon rule as the Coeus snapshots: week N uses ONLY weeks 1..N-1.

Usage:
  python3 build_matchup_stats.py            # builds WEEK (default 10)
  python3 build_matchup_stats.py 12         # builds week 12
Output:
  matchup/wk{NN}.json
"""

import datetime
import json
import os
import sys
import pandas as pd
import requests
from io import StringIO

def default_season():
    """NFL season year: 2026 season spans Sep 2026 - Feb 2027."""
    now = datetime.date.today()
    return now.year if now.month >= 3 else now.year - 1


# Override with NFL_SEASON=2025 in the environment (used for replaying old seasons).
SEASON = int(os.environ.get("NFL_SEASON", default_season()))
DEFAULT_WEEK = 10
FIRST_BUILDABLE_WEEK = 3   # weeks 1-2 have too little prior data to rank

PLAYER_STATS_URLS = [
    f"https://github.com/nflverse/nflverse-data/releases/download/stats_player/stats_player_week_{SEASON}.csv",
    f"https://github.com/nflverse/nflverse-data/releases/download/player_stats/player_stats_{SEASON}.csv",
]
GAMES_URL = "https://raw.githubusercontent.com/nflverse/nfldata/master/data/games.csv"

POS_MAP = {"QB": "QB", "RB": "RB", "FB": "RB", "WR": "WR", "TE": "TE"}
POSITIONS = ["QB", "RB", "WR", "TE"]

# metric -> (label, decimals, offense_higher_is_better)
# Defensive direction is always the inverse: a defence wants to allow less of
# what an offence wants more of, and wants MORE of sacks / interceptions.
TEAM_OFF = {
    "ppg":       ("Points / game", 1, True),
    "total_ypg": ("Total yards / game", 1, True),
    "pass_ypg":  ("Pass yards / game", 1, True),
    "rush_ypg":  ("Rush yards / game", 1, True),
    "fd_pg":     ("First downs / game", 1, True),
}
TEAM_DEF = {
    "ppg":       ("Points allowed / game", 1),
    "total_ypg": ("Total yards allowed / game", 1),
    "pass_ypg":  ("Pass yards allowed / game", 1),
    "rush_ypg":  ("Rush yards allowed / game", 1),
    "fd_pg":     ("First downs allowed / game", 1),
}

# (label, decimals, offense_higher_better, group)
POS_METRICS = {
    "QB": {
        "pass_yds":   ("Passing yards", 0, True, "Volume"),
        "pass_ypg":   ("Passing yards / game", 1, True, "Volume"),
        "completions":("Completions", 0, True, "Volume"),
        "comp_pg":    ("Completions / game", 1, True, "Volume"),
        "attempts":   ("Attempts", 0, True, "Volume"),
        "att_pg":     ("Attempts / game", 1, True, "Volume"),
        "pass_td":    ("Passing TDs", 0, True, "Volume"),
        "comp_pct":   ("Completion %", 1, True, "Efficiency"),
        "ypc":        ("Yards / completion", 1, True, "Efficiency"),
        "fd_pg":      ("Passing first downs / game", 1, True, "Efficiency"),
        "p10_pg":     ("10+ yd completions / game", 1, True, "Explosive"),
        "p16_pg":     ("16+ yd completions / game", 1, True, "Explosive"),
        "p20_pg":     ("20+ yd completions / game", 1, True, "Explosive"),
        "p40_pg":     ("40+ yd completions / game", 2, True, "Explosive"),
        "sacks_pg":   ("Sacks taken / game", 1, False, "Protection"),
        "int_pg":     ("Interceptions / game", 1, False, "Protection"),
    },
    "RB": {
        "rush_yds":   ("Rushing yards", 0, True, "Volume"),
        "rush_ypg":   ("Rushing yards / game", 1, True, "Volume"),
        "carries":    ("Carries", 0, True, "Volume"),
        "car_pg":     ("Carries / game", 1, True, "Volume"),
        "rec_yds":    ("Receiving yards", 0, True, "Volume"),
        "rec":        ("Receptions", 0, True, "Volume"),
        "td":         ("Total TDs", 0, True, "Volume"),
        "fd_pg":      ("Rushing first downs / game", 1, True, "Efficiency"),
        "r10_pg":     ("10+ yd runs / game", 1, True, "Explosive"),
        "r12_pg":     ("12+ yd runs / game", 1, True, "Explosive"),
        "r20_pg":     ("20+ yd runs / game", 1, True, "Explosive"),
        "r40_pg":     ("40+ yd runs / game", 2, True, "Explosive"),
    },
    "WR": {
        "rec_yds":    ("Receiving yards", 0, True, "Volume"),
        "rec_ypg":    ("Receiving yards / game", 1, True, "Volume"),
        "rec":        ("Receptions", 0, True, "Volume"),
        "td":         ("Receiving TDs", 0, True, "Volume"),
        "ypr":        ("Yards / reception", 1, True, "Efficiency"),
        "air_pg":     ("Air yards / game", 1, True, "Efficiency"),
        "yac_pg":     ("Yards after catch / game", 1, True, "Efficiency"),
        "fd_pg":      ("Receiving first downs / game", 1, True, "Efficiency"),
        "c10_pg":     ("10+ yd catches / game", 1, True, "Explosive"),
        "c16_pg":     ("16+ yd catches / game", 1, True, "Explosive"),
        "c20_pg":     ("20+ yd catches / game", 1, True, "Explosive"),
        "c40_pg":     ("40+ yd catches / game", 2, True, "Explosive"),
    },
}
POS_METRICS["TE"] = dict(POS_METRICS["WR"])


# Per-GAME metrics for the contextual game log. "/game" rates are omitted here
# because for a single game they are identical to the raw total.
LOG_TEAM = {
    "pts":       ("Points", 0),
    "total_yds": ("Total yards", 0),
    "pass_yds":  ("Pass yards", 0),
    "rush_yds":  ("Rush yards", 0),
}
# maps a log metric -> the season-level defensive metric whose rank sets the tier
LOG_TEAM_DEFKEY = {"pts": "ppg", "total_yds": "total_ypg",
                   "pass_yds": "pass_ypg", "rush_yds": "rush_ypg"}
LOG_POS = {
    "QB": {"pass_yds": ("Passing yards", 0), "comp_pct": ("Completion %", 1),
           "ypc": ("Yards / completion", 1), "pass_td": ("Passing TDs", 0)},
    "RB": {"rush_yds": ("Rushing yards", 0), "rec_yds": ("Receiving yards", 0),
           "rec": ("Receptions", 0), "td": ("Total TDs", 0)},
    "WR": {"rec_yds": ("Receiving yards", 0), "rec": ("Receptions", 0),
           "ypr": ("Yards / reception", 1), "td": ("Receiving TDs", 0)},
    "TE": {"rec_yds": ("Receiving yards", 0), "rec": ("Receptions", 0),
           "ypr": ("Yards / reception", 1), "td": ("Receiving TDs", 0)},
}
LOG_POS_DEFKEY = {
    "QB": {"pass_yds": "pass_yds", "comp_pct": "comp_pct", "ypc": "ypc", "pass_td": "pass_td"},
    "RB": {"rush_yds": "rush_yds", "rec_yds": "rec_yds", "rec": "rec", "td": "td"},
    "WR": {"rec_yds": "rec_yds", "rec": "rec", "ypr": "ypr", "td": "td"},
    "TE": {"rec_yds": "rec_yds", "rec": "rec", "ypr": "ypr", "td": "td"},
}


RAW_COLS = ["completions", "attempts", "passing_yards", "passing_tds",
            "passing_interceptions", "sacks_suffered", "passing_first_downs",
            "passing_10", "passing_16", "passing_20", "passing_40",
            "carries", "rushing_yards", "rushing_tds", "rushing_first_downs",
            "rushing_10", "rushing_12", "rushing_20", "rushing_40",
            "receptions", "targets", "receiving_yards", "receiving_tds",
            "receiving_first_downs", "receiving_air_yards",
            "receiving_yards_after_catch",
            "receiving_10", "receiving_16", "receiving_20", "receiving_40"]

def tier_of(rank):
    """Defensive strength faced, by season rank in that category.
    1-10 = toughest (top), 11-22 = middle 12, 23-32 = softest (bottom)."""
    if rank <= 10:
        return "top"
    if rank <= 22:
        return "mid"
    return "bot"


_CSV_CACHE = {}


def fetch_csv(urls):
    if isinstance(urls, str):
        urls = [urls]
    key = urls[0]
    if key in _CSV_CACHE:
        return _CSV_CACHE[key].copy()
    for url in urls:
        print(f"  fetching {url}")
        try:
            r = requests.get(url, timeout=90)
            if r.status_code == 200:
                df = pd.read_csv(StringIO(r.text), low_memory=False)
                _CSV_CACHE[key] = df
                return df.copy()
            print(f"    -> HTTP {r.status_code}, trying next candidate")
        except Exception as e:
            print(f"    -> {e}, trying next candidate")
    sys.exit("FATAL: could not download player stats. Check nflverse release paths.")


def norm_players(df):
    team_col = "team" if "team" in df.columns else "recent_team"
    name_col = ("player_display_name" if "player_display_name" in df.columns
                else "player_name")
    df = df.rename(columns={team_col: "team", name_col: "name"})
    if "season_type" in df.columns:
        df = df[df["season_type"] == "REG"]
    if "season" in df.columns:
        df = df[df["season"] == SEASON]
    cols = ["name", "position", "team", "opponent_team", "week"] + RAW_COLS
    for c in cols:
        if c not in df.columns:
            df[c] = 0
    df = df[cols].copy()
    num = [c for c in cols if c not in ("name", "position", "team", "opponent_team")]
    df[num] = df[num].fillna(0)
    df["pos"] = df["position"].map(POS_MAP)
    return df[df["pos"].notna()]


def safe_div(a, b):
    return float(a) / float(b) if b else 0.0


def pos_metrics_from_sums(pos, s, gp):
    """s = dict of summed raw stats, gp = games played."""
    g = lambda k: float(s.get(k, 0) or 0)
    if pos == "QB":
        return {
            "pass_yds":    g("passing_yards"),
            "pass_ypg":    safe_div(g("passing_yards"), gp),
            "completions": g("completions"),
            "comp_pg":     safe_div(g("completions"), gp),
            "attempts":    g("attempts"),
            "att_pg":      safe_div(g("attempts"), gp),
            "pass_td":     g("passing_tds"),
            "comp_pct":    safe_div(g("completions"), g("attempts")) * 100,
            "ypc":         safe_div(g("passing_yards"), g("completions")),
            "fd_pg":       safe_div(g("passing_first_downs"), gp),
            "p10_pg":      safe_div(g("passing_10"), gp),
            "p16_pg":      safe_div(g("passing_16"), gp),
            "p20_pg":      safe_div(g("passing_20"), gp),
            "p40_pg":      safe_div(g("passing_40"), gp),
            "sacks_pg":    safe_div(g("sacks_suffered"), gp),
            "int_pg":      safe_div(g("passing_interceptions"), gp),
        }
    if pos == "RB":
        return {
            "rush_yds": g("rushing_yards"),
            "rush_ypg": safe_div(g("rushing_yards"), gp),
            "carries":  g("carries"),
            "car_pg":   safe_div(g("carries"), gp),
            "rec_yds":  g("receiving_yards"),
            "rec":      g("receptions"),
            "td":       g("rushing_tds") + g("receiving_tds"),
            "fd_pg":    safe_div(g("rushing_first_downs"), gp),
            "r10_pg":   safe_div(g("rushing_10"), gp),
            "r12_pg":   safe_div(g("rushing_12"), gp),
            "r20_pg":   safe_div(g("rushing_20"), gp),
            "r40_pg":   safe_div(g("rushing_40"), gp),
        }
    return {  # WR / TE
        "rec_yds": g("receiving_yards"),
        "rec_ypg": safe_div(g("receiving_yards"), gp),
        "rec":     g("receptions"),
        "td":      g("receiving_tds"),
        "ypr":     safe_div(g("receiving_yards"), g("receptions")),
        "air_pg":  safe_div(g("receiving_air_yards"), gp),
        "yac_pg":  safe_div(g("receiving_yards_after_catch"), gp),
        "fd_pg":   safe_div(g("receiving_first_downs"), gp),
        "c10_pg":  safe_div(g("receiving_10"), gp),
        "c16_pg":  safe_div(g("receiving_16"), gp),
        "c20_pg":  safe_div(g("receiving_20"), gp),
        "c40_pg":  safe_div(g("receiving_40"), gp),
    }


def build(week):
    print(f"Building Matchup Statistics for {SEASON} week {week}...")
    stats = norm_players(fetch_csv(PLAYER_STATS_URLS))
    print("Downloading schedule/results...")
    games = fetch_csv(GAMES_URL)
    games = games[(games["season"] == SEASON) & (games["game_type"] == "REG")]

    prior_stats = stats[stats["week"] < week]
    prior_games = games[(games["week"] < week) & games["home_score"].notna()]
    week_games = games[games["week"] == week]
    if prior_stats.empty:
        raise SystemExit(f"no prior data for week {week} (data-horizon rule)")

    all_teams = sorted(set(games["home_team"]) | set(games["away_team"]))

    # ---- team scoring / record from completed games ----
    pts, pa, wl = {}, {}, {}
    for _, g in prior_games.iterrows():
        h, a = g["home_team"], g["away_team"]
        hs, as_ = int(g["home_score"]), int(g["away_score"])
        for t, pf, pag in [(h, hs, as_), (a, as_, hs)]:
            pts.setdefault(t, []).append(pf)
            pa.setdefault(t, []).append(pag)
            wl.setdefault(t, []).append("W" if pf > pag else ("L" if pf < pag else "T"))

    gp = {t: max(len(wl.get(t, [])), 1) for t in all_teams}
    records = {}
    for t in all_teams:
        r = wl.get(t, [])
        records[t] = f"{r.count('W')}-{r.count('L')}" + (f"-{r.count('T')}" if r.count("T") else "")

    # ---- team totals: offense (by team) and defense allowed (by opponent_team) ----
    raw_cols = RAW_COLS
    off_tot = prior_stats.groupby("team")[raw_cols].sum()
    def_tot = prior_stats.groupby("opponent_team")[raw_cols].sum()

    team_off, team_def = {}, {}
    for t in all_teams:
        o = off_tot.loc[t] if t in off_tot.index else None
        d = def_tot.loc[t] if t in def_tot.index else None
        team_off[t] = {
            "ppg":       safe_div(sum(pts.get(t, [])), gp[t]),
            "pass_ypg":  safe_div(o["passing_yards"], gp[t]) if o is not None else 0,
            "rush_ypg":  safe_div(o["rushing_yards"], gp[t]) if o is not None else 0,
            "total_ypg": safe_div((o["passing_yards"] + o["rushing_yards"]), gp[t]) if o is not None else 0,
            "fd_pg":     safe_div((o["passing_first_downs"] + o["rushing_first_downs"]), gp[t]) if o is not None else 0,
        }
        team_def[t] = {
            "ppg":       safe_div(sum(pa.get(t, [])), gp[t]),
            "pass_ypg":  safe_div(d["passing_yards"], gp[t]) if d is not None else 0,
            "rush_ypg":  safe_div(d["rushing_yards"], gp[t]) if d is not None else 0,
            "total_ypg": safe_div((d["passing_yards"] + d["rushing_yards"]), gp[t]) if d is not None else 0,
            "fd_pg":     safe_div((d["passing_first_downs"] + d["rushing_first_downs"]), gp[t]) if d is not None else 0,
        }

    # ---- positional offense / defense-allowed ----
    off_pos = prior_stats.groupby(["team", "pos"])[raw_cols].sum()
    def_pos = prior_stats.groupby(["opponent_team", "pos"])[raw_cols].sum()

    pos_off = {p: {} for p in POSITIONS}
    pos_def = {p: {} for p in POSITIONS}
    for t in all_teams:
        for p in POSITIONS:
            so = off_pos.loc[(t, p)].to_dict() if (t, p) in off_pos.index else {c: 0 for c in raw_cols}
            sd = def_pos.loc[(t, p)].to_dict() if (t, p) in def_pos.index else {c: 0 for c in raw_cols}
            pos_off[p][t] = pos_metrics_from_sums(p, so, gp[t])
            pos_def[p][t] = pos_metrics_from_sums(p, sd, gp[t])

    # ---- ranking helpers (1 = best) ----
    def rank(values, higher_better):
        order = sorted(all_teams, key=lambda t: values[t], reverse=higher_better)
        return {t: i + 1 for i, t in enumerate(order)}

    def pack(values, higher_better, dec):
        rk = rank(values, higher_better)
        return {t: {"v": round(values[t], dec), "r": rk[t]} for t in all_teams}

    out_team_off, out_team_def = {}, {}
    for m, (_lbl, dec, off_hb) in TEAM_OFF.items():
        out_team_off[m] = pack({t: team_off[t][m] for t in all_teams}, off_hb, dec)
    for m, (_lbl, dec) in TEAM_DEF.items():
        off_hb = TEAM_OFF[m][2]
        out_team_def[m] = pack({t: team_def[t][m] for t in all_teams}, not off_hb, dec)

    out_pos_off, out_pos_def = {}, {}
    for p in POSITIONS:
        out_pos_off[p], out_pos_def[p] = {}, {}
        for m, (_lbl, dec, off_hb, _grp) in POS_METRICS[p].items():
            out_pos_off[p][m] = pack({t: pos_off[p][t][m] for t in all_teams}, off_hb, dec)
            out_pos_def[p][m] = pack({t: pos_def[p][t][m] for t in all_teams}, not off_hb, dec)

    teams = {}
    for t in all_teams:
        teams[t] = {
            "record": records[t], "gp": len(wl.get(t, [])),
            "team_off": {m: out_team_off[m][t] for m in TEAM_OFF},
            "team_def": {m: out_team_def[m][t] for m in TEAM_DEF},
            "off": {p: {m: out_pos_off[p][m][t] for m in POS_METRICS[p]} for p in POSITIONS},
            "def": {p: {m: out_pos_def[p][m][t] for m in POS_METRICS[p]} for p in POSITIONS},
        }

    payload = {
        "season": SEASON,
        "week": week,
        "data_horizon": f"weeks 1-{week - 1}",
        "labels": {
            "team_off": {m: TEAM_OFF[m][0] for m in TEAM_OFF},
            "team_def": {m: TEAM_DEF[m][0] for m in TEAM_DEF},
            "pos": {p: {m: {"l": POS_METRICS[p][m][0], "g": POS_METRICS[p][m][3],
                            "inv": not POS_METRICS[p][m][2]}
                        for m in POS_METRICS[p]} for p in POSITIONS},
        },
        "games": [{
            "game_id": f"{SEASON}_{week:02d}_{g['away_team']}_{g['home_team']}",
            "away": g["away_team"], "home": g["home_team"],
            "away_record": records[g["away_team"]], "home_record": records[g["home_team"]],
        } for _, g in week_games.iterrows()],
        "teams": teams,
    }

    os.makedirs("matchup", exist_ok=True)
    path = f"matchup/wk{week:02d}.json"
    with open(path, "w") as f:
        json.dump(payload, f)
    size = os.path.getsize(path) / 1024
    print(f"Wrote {path} — {len(payload['games'])} games, {len(all_teams)} teams, {size:.0f} KB")

    build_context(week, all_teams, records, prior_stats, prior_games,
                  out_team_def, out_pos_def)
    build_threats(week, all_teams, records, prior_stats, week_games, gp)
    build_games(week, all_teams, records, week_games, prior_games, stats)
    print("Serve the folder and open matchup_stats.html / contextual_stats.html")


# ==========================================================================
# GAMES — the week's slate: schedule, lines, venue, rest, results.
# Everything here comes straight from the nflverse schedule file.
# ==========================================================================

def _num(v):
    import math
    try:
        f = float(v)
        return None if math.isnan(f) else f
    except (TypeError, ValueError):
        return None


def _int(v):
    f = _num(v)
    return None if f is None else int(f)


def _leaders_and_box(df, team, pts=None):
    """df = player rows for one team (one game, or a season slice)."""
    g = lambda r, k: float(r.get(k, 0) or 0)
    box = {
        "pts": pts,
        "pass_yds": int(df["passing_yards"].sum()),
        "rush_yds": int(df["rushing_yards"].sum()),
        "total_yds": int(df["passing_yards"].sum() + df["rushing_yards"].sum()),
        "first_downs": int(df["passing_first_downs"].sum() + df["rushing_first_downs"].sum()),
        "turnovers": int(df["passing_interceptions"].sum()),
        "sacks_taken": int(df["sacks_suffered"].sum()),
        "comp": int(df["completions"].sum()), "att": int(df["attempts"].sum()),
        "tds": int(df["passing_tds"].sum() + df["rushing_tds"].sum()),
    }
    qb_rows = df[df["attempts"] > 0].sort_values("attempts", ascending=False)
    qb = None
    if len(qb_rows):
        r = qb_rows.iloc[0]
        qb = {"name": r["name"], "comp": int(r["completions"]), "att": int(r["attempts"]),
              "yds": int(r["passing_yards"]), "td": int(r["passing_tds"]),
              "int": int(r["passing_interceptions"]), "rush_yds": int(r["rushing_yards"])}
    rush = [{"name": r["name"], "car": int(r["carries"]), "yds": int(r["rushing_yards"]),
             "td": int(r["rushing_tds"])}
            for _, r in df[df["carries"] > 0].nlargest(2, "rushing_yards").iterrows()]
    rec = [{"name": r["name"], "rec": int(r["receptions"]), "tgt": int(r["targets"]),
            "yds": int(r["receiving_yards"]), "td": int(r["receiving_tds"])}
           for _, r in df[df["receptions"] > 0].nlargest(3, "receiving_yards").iterrows()]
    return box, {"qb": qb, "rush": rush, "rec": rec}


def build_games(week, all_teams, records, week_games, prior_games, stats=None):
    # last-3 form per team, for a quick read on each card
    form = {}
    for _, g in prior_games.sort_values("week").iterrows():
        hs, as_ = int(g["home_score"]), int(g["away_score"])
        for t, pf, pa in [(g["home_team"], hs, as_), (g["away_team"], as_, hs)]:
            form.setdefault(t, []).append("W" if pf > pa else ("L" if pf < pa else "T"))

    rows = []
    for _, g in week_games.iterrows():
        away, home = g["away_team"], g["home_team"]
        hs, as_ = _int(g.get("home_score")), _int(g.get("away_score"))
        played = hs is not None and as_ is not None
        rows.append({
            "game_id": f"{SEASON}_{week:02d}_{away}_{home}",
            "away": away, "home": home,
            "away_record": records.get(away, ""), "home_record": records.get(home, ""),
            "away_form": "".join(form.get(away, [])[-3:]),
            "home_form": "".join(form.get(home, [])[-3:]),
            "gameday": str(g.get("gameday", "")), "weekday": str(g.get("weekday", "")),
            "gametime": str(g.get("gametime", "")) if pd.notna(g.get("gametime")) else "",
            "stadium": str(g.get("stadium", "")) if pd.notna(g.get("stadium")) else "",
            "roof": str(g.get("roof", "")) if pd.notna(g.get("roof")) else "",
            "surface": str(g.get("surface", "")) if pd.notna(g.get("surface")) else "",
            "div_game": bool(_int(g.get("div_game")) or 0),
            "away_rest": _int(g.get("away_rest")), "home_rest": _int(g.get("home_rest")),
            "spread_line": _num(g.get("spread_line")),
            "total_line": _num(g.get("total_line")),
            "away_ml": _int(g.get("away_moneyline")), "home_ml": _int(g.get("home_moneyline")),
            "played": played,
            "away_score": as_, "home_score": hs,
        })

        # box score for a completed game; season-to-date leaders before kickoff
        if stats is not None:
            entry = rows[-1]
            src_df = stats[stats["week"] == week] if played else stats[stats["week"] < week]
            entry["leader_scope"] = "game" if played else "season"
            box, lead = {}, {}
            for side, t, pts in [("away", away, as_), ("home", home, hs)]:
                sub = src_df[src_df["team"] == t]
                if len(sub):
                    b, l = _leaders_and_box(sub, t, pts)
                    box[side], lead[side] = b, l
            entry["box"], entry["leaders"] = box, lead

    # sort by kickoff so the page reads like a real slate
    rows.sort(key=lambda r: (r["gameday"], r["gametime"]))

    payload = {
        "season": SEASON, "week": week,
        "data_horizon": f"weeks 1-{week - 1}" if week > 1 else "season opener",
        "games": rows,
    }
    os.makedirs("games", exist_ok=True)
    path = f"games/wk{week:02d}.json"
    with open(path, "w") as f:
        json.dump(payload, f)
    lines = sum(1 for r in rows if r["spread_line"] is not None)
    kind = "schedule only" if stats is None else "with box scores"
    print(f"Wrote {path} — {len(rows)} games, {lines} with lines, {kind}, "
          f"{os.path.getsize(path)/1024:.0f} KB")


# ==========================================================================
# THREAT SYSTEM — offensive starters (QB, RB, WR, WR, TE) vs the positional
# defense they face. Emits raw ranks; classification happens in the browser
# so the tier rules stay tunable without rebuilding data.
# ==========================================================================

SNAPS_URL = ("https://github.com/nflverse/nflverse-data/releases/download/"
             "snap_counts/snap_counts_{season}.csv")

# Starters per team, by snap share.
LINEUP = [("QB", 1), ("RB", 1), ("WR", 2), ("TE", 1)]
SNAP_LOOKBACK = 4           # weeks of snap share used to identify starters
MIN_GAMES = 3               # games needed before a player can be ranked

# Prop categories only — the ones Frank actually bets.
# key -> (label, raw stat column, decimals)
THREAT_CATS = {
    "QB": {
        "pass_yds": ("Passing yards", "passing_yards", 1),
        "pass_tds": ("Passing TDs", "passing_tds", 2),
    },
    "RB": {
        "rush_yds": ("Rushing yards", "rushing_yards", 1),
        "rec_yds":  ("Receiving yards", "receiving_yards", 1),
        "rec":      ("Receptions", "receptions", 1),
    },
    "WR": {
        "rec_yds":  ("Receiving yards", "receiving_yards", 1),
        "rec":      ("Receptions", "receptions", 1),
    },
}
THREAT_CATS["TE"] = dict(THREAT_CATS["WR"])
THREAT_POS = ["QB", "RB", "WR", "TE"]


def build_threats(week, all_teams, records, prior_stats, week_games, gp):
    """prior_stats already respects the data horizon (weeks 1..week-1)."""
    import pandas as pd

    snaps = fetch_csv(SNAPS_URL.format(season=SEASON))
    snaps = snaps[(snaps["season"] == SEASON) & (snaps["game_type"] == "REG")
                  & (snaps["week"] < week)]
    lo = max(1, week - SNAP_LOOKBACK)
    snaps = snaps[snaps["week"] >= lo]
    snaps = snaps[snaps["position"].isin(THREAT_POS)]

    # ---- who starts: highest mean offensive snap share in the lookback ----
    share = (snaps.groupby(["team", "player", "position"])["offense_pct"]
             .mean().reset_index())
    starters = {}
    for t in all_teams:
        sub = share[share["team"] == t]
        picked = []
        for pos, n in LINEUP:
            rows = sub[sub["position"] == pos].nlargest(n, "offense_pct")
            for _, r in rows.iterrows():
                picked.append({"name": r["player"], "pos": pos,
                               "snap_pct": round(float(r["offense_pct"]) * 100, 1)})
        starters[t] = picked

    # ---- player production per game, ranked within position ----
    pl = prior_stats.copy()
    pl["posg"] = pl["position"].map(POS_MAP)
    pl = pl[pl["posg"].notna()]
    agg = (pl.groupby(["name", "posg", "team"])
             .agg(gp=("week", "nunique"),
                  **{c: (c, "sum") for c in
                     ["passing_yards", "passing_tds", "rushing_yards", "rushing_tds",
                      "receiving_yards", "receiving_tds", "receptions"]})
             .reset_index())
    # Early in the season there aren't MIN_GAMES to be had — fall back to what
    # exists so week 3 isn't a blank page, and flag the thin sample.
    min_games = min(MIN_GAMES, max(1, week - 1))
    agg = agg[agg["gp"] >= min_games]

    player_rank = {}     # (name, pos) -> {cat: {"v":pg, "r":rank}}
    for pos in THREAT_POS:
        sub = agg[agg["posg"] == pos].copy()
        for cat, (_lbl, col, dec) in THREAT_CATS[pos].items():
            sub[cat] = (sub[col] / sub["gp"]).round(dec)
            sub[cat + "_r"] = sub[cat].rank(ascending=False, method="min").astype(int)
        for _, r in sub.iterrows():
            player_rank[(r["name"], pos)] = {
                c: {"v": float(r[c]), "r": int(r[c + "_r"])}
                for c in THREAT_CATS[pos]}

    # ---- defense allowed to each position, per game, ranked ----
    dfn = {}
    for pos in THREAT_POS:
        sub = pl[pl["posg"] == pos]
        tot = sub.groupby("opponent_team")[
            ["passing_yards", "passing_tds", "rushing_yards", "rushing_tds",
             "receiving_yards", "receiving_tds", "receptions"]].sum()
        vals = {}
        for cat, (_lbl, col, dec) in THREAT_CATS[pos].items():
            vals[cat] = {t: round(float(tot.loc[t, col]) / gp[t], dec)
                         if t in tot.index else 0.0 for t in all_teams}
        dfn[pos] = {}
        for cat in THREAT_CATS[pos]:
            order = sorted(all_teams, key=lambda t: vals[cat][t])   # fewest allowed = rank 1
            ranks = {t: i + 1 for i, t in enumerate(order)}
            dfn[pos][cat] = {t: {"v": vals[cat][t], "r": ranks[t]} for t in all_teams}

    # ---- assemble: each starter with their ranks and the defense they face ----
    opp_of = {}
    for _, g in week_games.iterrows():
        opp_of[g["away_team"]] = g["home_team"]
        opp_of[g["home_team"]] = g["away_team"]

    teams_out = {}
    for t in all_teams:
        opp = opp_of.get(t)
        roster = []
        for s in starters.get(t, []):
            pr = player_rank.get((s["name"], s["pos"]))
            if not pr or not opp:
                roster.append({**s, "cats": {}, "unranked": True})
                continue
            cats = {}
            for cat in THREAT_CATS[s["pos"]]:
                d = dfn[s["pos"]][cat][opp]
                cats[cat] = {"v": pr[cat]["v"], "r": pr[cat]["r"],
                             "dv": d["v"], "dr": d["r"]}
            roster.append({**s, "cats": cats})
        teams_out[t] = {"record": records[t], "opp": opp, "starters": roster}

    payload = {
        "season": SEASON, "week": week, "data_horizon": f"weeks 1-{week - 1}",
        "min_games": min_games, "thin_sample": min_games < MIN_GAMES,
        "snap_lookback": SNAP_LOOKBACK,
        "labels": {p: {c: THREAT_CATS[p][c][0] for c in THREAT_CATS[p]} for p in THREAT_POS},
        "pos_cats": {p: list(THREAT_CATS[p].keys()) for p in THREAT_POS},
        "games": [{
            "game_id": f"{SEASON}_{week:02d}_{g['away_team']}_{g['home_team']}",
            "away": g["away_team"], "home": g["home_team"],
            "away_record": records[g["away_team"]], "home_record": records[g["home_team"]],
        } for _, g in week_games.iterrows()],
        "teams": teams_out,
    }
    os.makedirs("threats", exist_ok=True)
    path = f"threats/wk{week:02d}.json"
    with open(path, "w") as f:
        json.dump(payload, f)
    n = sum(len(v["starters"]) for v in teams_out.values())
    print(f"Wrote {path} — {n} starters, {os.path.getsize(path)/1024:.0f} KB")


# ==========================================================================
# CONTEXTUAL STATISTICS — per-game log, each game tagged by the defensive
# tier faced in that specific category.
# ==========================================================================
def build_context(week, all_teams, records, prior_stats, prior_games,
                  out_team_def, out_pos_def):
    raw_cols = RAW_COLS

    # opponent / venue / result per team per week
    sched = {}
    for _, g in prior_games.iterrows():
        h, a = g["home_team"], g["away_team"]
        hs, as_ = int(g["home_score"]), int(g["away_score"])
        wk = int(g["week"])
        sched[(h, wk)] = {"opp": a, "home": True,
                          "result": ("W" if hs > as_ else "L" if hs < as_ else "T"),
                          "score": f"{hs}-{as_}"}
        sched[(a, wk)] = {"opp": h, "home": False,
                          "result": ("W" if as_ > hs else "L" if as_ < hs else "T"),
                          "score": f"{as_}-{hs}"}

    wk_team = prior_stats.groupby(["team", "week"])[raw_cols].sum()
    wk_pos = prior_stats.groupby(["team", "pos", "week"])[raw_cols].sum()

    def team_game_metrics(s, pts):
        return {"pts": pts,
                "total_yds": s["passing_yards"] + s["rushing_yards"],
                "pass_yds": s["passing_yards"],
                "rush_yds": s["rushing_yards"]}

    def pos_game_metrics(pos, s):
        full = pos_metrics_from_sums(pos, s, 1)
        return {m: full[m] for m in LOG_POS[pos]}

    teams_out, sizes = {}, 0
    for t in all_teams:
        weeks = sorted({int(w) for (tt, w) in sched if tt == t})
        log = []
        for wk in weeks:
            info = sched[(t, wk)]
            opp = info["opp"]
            pts = int(info["score"].split("-")[0])
            s = (wk_team.loc[(t, wk)].to_dict() if (t, wk) in wk_team.index
                 else {c: 0 for c in raw_cols})

            entry = {"week": wk, "opp": opp, "home": info["home"],
                     "result": info["result"], "score": info["score"], "team": {}, "off": {}}

            tg = team_game_metrics(s, pts)
            for m, (_lbl, dec) in LOG_TEAM.items():
                drank = out_team_def[LOG_TEAM_DEFKEY[m]][opp]["r"]
                entry["team"][m] = {"v": round(tg[m], dec), "r": drank, "t": tier_of(drank)}

            for p in POSITIONS:
                sp = (wk_pos.loc[(t, p, wk)].to_dict() if (t, p, wk) in wk_pos.index
                      else {c: 0 for c in raw_cols})
                pg = pos_game_metrics(p, sp)
                entry["off"][p] = {}
                for m, (_lbl, dec) in LOG_POS[p].items():
                    drank = out_pos_def[p][LOG_POS_DEFKEY[p][m]][opp]["r"]
                    entry["off"][p][m] = {"v": round(pg[m], dec), "r": drank, "t": tier_of(drank)}
            log.append(entry)

        # ---- splits: average production against each defensive tier ----
        def split_for(getter, metrics):
            out = {}
            for m, (_lbl, dec) in metrics.items():
                buckets = {"top": [], "mid": [], "bot": []}
                for e in log:
                    cell = getter(e)[m]
                    buckets[cell["t"]].append(cell["v"])
                out[m] = {k: {"avg": round(sum(v) / len(v), max(dec, 1)) if v else None,
                              "n": len(v)} for k, v in buckets.items()}
            return out

        splits = {"team": split_for(lambda e: e["team"], LOG_TEAM), "off": {}}
        for p in POSITIONS:
            splits["off"][p] = split_for(lambda e, p=p: e["off"][p], LOG_POS[p])

        teams_out[t] = {"record": records[t], "log": log, "splits": splits}

    payload = {
        "season": SEASON, "week": week, "data_horizon": f"weeks 1-{week - 1}",
        "tier_note": "Defensive tier reflects the opponent's season rank in that "
                     "category through the data horizon, not their rank on game day.",
        "labels": {
            "team": {m: LOG_TEAM[m][0] for m in LOG_TEAM},
            "pos": {p: {m: LOG_POS[p][m][0] for m in LOG_POS[p]} for p in POSITIONS},
        },
        "teams": teams_out,
    }
    os.makedirs("context", exist_ok=True)
    path = f"context/wk{week:02d}.json"
    with open(path, "w") as f:
        json.dump(payload, f)
    print(f"Wrote {path} — {len(all_teams)} team logs, "
          f"{os.path.getsize(path) / 1024:.0f} KB")


def build_games_only(week):
    """Schedule, lines and venue — needs nothing but games.csv, so this works
    for a future season before any player stats exist."""
    games = fetch_csv(GAMES_URL)
    games = games[(games["season"] == SEASON) & (games["game_type"] == "REG")]
    if games.empty:
        raise SystemExit(f"no {SEASON} schedule available")
    week_games = games[games["week"] == week]
    if week_games.empty:
        raise SystemExit(f"no week {week} games in the {SEASON} schedule")
    prior_games = games[(games["week"] < week) & games["home_score"].notna()]

    wl = {}
    for _, g in prior_games.iterrows():
        hs, as_ = int(g["home_score"]), int(g["away_score"])
        for t, pf, pa in [(g["home_team"], hs, as_), (g["away_team"], as_, hs)]:
            wl.setdefault(t, []).append("W" if pf > pa else ("L" if pf < pa else "T"))
    all_teams = sorted(set(games["home_team"]) | set(games["away_team"]))
    records = {}
    for t in all_teams:
        r = wl.get(t, [])
        records[t] = f"{r.count('W')}-{r.count('L')}" + (f"-{r.count('T')}" if r.count("T") else "")

    # Box scores only need this week's own results, so load player stats if
    # they exist — a completed week gets a box score even when the ranking
    # pages sit out for want of prior data.
    stats = None
    try:
        stats = norm_players(fetch_csv(PLAYER_STATS_URLS))
    except SystemExit:
        pass                      # season hasn't started; schedule only
    build_games(week, all_teams, records, week_games, prior_games, stats)


def current_week(games):
    """The next week that hasn't been played yet — the one to preview."""
    reg = games[(games["season"] == SEASON) & (games["game_type"] == "REG")]
    if reg.empty:
        return None
    unplayed = reg[reg["home_score"].isna()]
    if unplayed.empty:
        return int(reg["week"].max())        # season complete
    return int(unplayed["week"].min())


def resolve_weeks(arg):
    """Returns a list of weeks to build. Downloads the schedule once to decide."""
    if arg not in ("auto", "all"):
        return [int(arg)]
    games = fetch_csv(GAMES_URL)
    wk = current_week(games)
    if wk is None:
        sys.exit(f"FATAL: no {SEASON} schedule found in nflverse yet.")
    if arg == "auto":
        return [wk]
    return list(range(1, wk + 1))


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else str(DEFAULT_WEEK)
    weeks = resolve_weeks(arg)
    if not weeks:
        print(f"Season {SEASON}: nothing buildable yet "
              f"(need week {FIRST_BUILDABLE_WEEK}+ for meaningful ranks). Exiting cleanly.")
        sys.exit(0)
    print(f"Season {SEASON} — building week(s): {', '.join(map(str, weeks))}")
    built, skipped, games_built = 0, [], 0

    # 1. Games: schedule only, so build every scheduled week regardless of
    #    how far the season has progressed.
    sched = fetch_csv(GAMES_URL)
    sched = sched[(sched["season"] == SEASON) & (sched["game_type"] == "REG")]
    game_weeks = sorted(int(w) for w in sched["week"].unique()) if not sched.empty else []
    if arg not in ("all",):
        game_weeks = [w for w in game_weeks if w in weeks]
    for w in game_weeks:
        try:
            build_games_only(w)
            games_built += 1
        except SystemExit as e:
            print(f"  week {w} games: skipped — {e}")

    # 2. Stats-dependent pages: need player data and enough prior weeks.
    for w in weeks:
        if w < FIRST_BUILDABLE_WEEK:
            skipped.append(w); continue
        try:
            build(w)
            built += 1
        except SystemExit as e:
            print(f"  week {w} stats: skipped — {e}")
            skipped.append(w)

    print(f"\nDone. {games_built} game file(s), {built} stat week(s)."
          + (f" Stats skipped: {skipped}" if skipped else ""))
