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
from io import StringIO, BytesIO

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
TEAM_STATS_URL = f"https://github.com/nflverse/nflverse-data/releases/download/stats_team/stats_team_week_{SEASON}.csv"
PBP_URL = f"https://github.com/nflverse/nflverse-data/releases/download/pbp/play_by_play_{SEASON}.csv.gz"

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
        "rush_share": ("Rush share", 1, True, "Usage"),
        "target_share": ("Target share", 1, True, "Usage"),
        "rush_yds":   ("Rushing yards", 0, True, "Volume"),
        "rush_ypg":   ("Rushing yards / game", 1, True, "Volume"),
        "carries":    ("Carries", 0, True, "Volume"),
        "car_pg":     ("Carries / game", 1, True, "Volume"),
        "rec_yds":    ("Receiving yards", 0, True, "Volume"),
        "rec":        ("Receptions", 0, True, "Volume"),
        "rec_pg":     ("Receptions / game", 1, True, "Volume"),
        "rush_td":    ("Rushing TDs", 0, True, "Volume"),
        "rec_td":     ("Receiving TDs", 0, True, "Volume"),
        "fd_pg":      ("Rushing first downs / game", 1, True, "Efficiency"),
        "r10_pg":     ("10+ yd runs / game", 1, True, "Explosive"),
        "r12_pg":     ("12+ yd runs / game", 1, True, "Explosive"),
        "r20_pg":     ("20+ yd runs / game", 1, True, "Explosive"),
        "r40_pg":     ("40+ yd runs / game", 2, True, "Explosive"),
    },
    "WR": {
        "target_share": ("Target share", 1, True, "Usage"),
        "rec_yds":    ("Receiving yards", 0, True, "Volume"),
        "rec_ypg":    ("Receiving yards / game", 1, True, "Volume"),
        "rec":        ("Receptions", 0, True, "Volume"),
        "rec_pg":     ("Receptions / game", 1, True, "Volume"),
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

# The weekly build() below aggregates ALL players at a position into one
# team-position blob (e.g. "KC's WR corps this week") — rush/target share
# is a per-PLAYER usage concept (their slice of the team's looks) that
# doesn't mean anything at that aggregate level, and pos_metrics_from_sums()
# doesn't compute it there anyway (only build_player_stats() injects it,
# per-player, with the team-week denominator that requires). Weekly
# matchup/context/threats builders use this filtered view instead.
POS_METRICS_WEEKLY = {p: {k: v for k, v in metrics.items() if v[3] != "Usage"}
                       for p, metrics in POS_METRICS.items()}


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
           "rec": ("Receptions", 0), "rush_td": ("Rushing TDs", 0), "rec_td": ("Receiving TDs", 0)},
    "WR": {"rec_yds": ("Receiving yards", 0), "rec": ("Receptions", 0),
           "ypr": ("Yards / reception", 1), "td": ("Receiving TDs", 0)},
    "TE": {"rec_yds": ("Receiving yards", 0), "rec": ("Receptions", 0),
           "ypr": ("Yards / reception", 1), "td": ("Receiving TDs", 0)},
}
LOG_POS_DEFKEY = {
    "QB": {"pass_yds": "pass_yds", "comp_pct": "comp_pct", "ypc": "ypc", "pass_td": "pass_td"},
    "RB": {"rush_yds": "rush_yds", "rec_yds": "rec_yds", "rec": "rec", "rush_td": "rush_td", "rec_td": "rec_td"},
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
            "receiving_10", "receiving_16", "receiving_20", "receiving_40",
            "sack_fumbles_lost", "rushing_fumbles_lost", "receiving_fumbles_lost"]


# ── Team Stats (Teams page modal) ──────────────────────────────────────
# Every column nflverse's stats_team_week file provides, bucketed into
# Offense / Defense / Special Teams / Penalties per subgroup.
# col -> (label, decimals, is_rate)
# is_rate columns aren't summable across weeks (percentages, CPOE) — they
# get an average-of-weeks instead of a season total.
# ── Down/Distance (drive sustainability + coach tendencies) ────────────
# These aren't raw stats_team_week columns — they're computed from the
# play-by-play file (down, ydstogo, third/fourth_down_converted flags),
# so build_team_stats() fills these in separately, not via the generic
# column-sum path the rest of TEAM_STATS_GROUPS uses.
DOWN_DIST_OFF_COLS = {
    "fd1_run": ("1st Down Run Plays", 0, False),
    "fd1_pass": ("1st Down Pass Plays", 0, False),
    "fd1_run_pct": ("1st Down Run %", 1, True),
    "fd1_pass_pct": ("1st Down Pass %", 1, True),
    "d3_att": ("3rd Down Attempts", 0, False),
    "d3_conv": ("3rd Down Conversions", 0, False),
    "d3_pct": ("3rd Down %", 1, True),
    "d4_situations": ("4th Down Situations", 0, False),
    "d4_go_att": ("4th Down Go-For-It Attempts", 0, False),
    "d4_go_pct": ("4th Down Go-For-It Rate", 1, True),
    "d4_conv": ("4th Down Conversions", 0, False),
    "d4_conv_pct": ("4th Down Conversion %", 1, True),
}
DOWN_DIST_DEF_COLS = {
    "fd1_run_faced": ("1st Down Run Plays Faced", 0, False),
    "fd1_pass_faced": ("1st Down Pass Plays Faced", 0, False),
    "fd1_run_pct_faced": ("Opponent 1st Down Run %", 1, True),
    "fd1_pass_pct_faced": ("Opponent 1st Down Pass %", 1, True),
    "d3_att_faced": ("3rd Down Attempts Faced", 0, False),
    "d3_conv_allowed": ("3rd Down Conversions Allowed", 0, False),
    "d3_pct_allowed": ("3rd Down % Allowed", 1, True),
    "d3_stop_pct": ("3rd Down Stop Rate", 1, True),
    "d4_situations_faced": ("4th Down Situations Faced", 0, False),
    "d4_go_att_faced": ("Opponent 4th Down Go-For-It Attempts", 0, False),
    "d4_go_pct_faced": ("Opponent 4th Down Go-For-It Rate", 1, True),
    "d4_conv_allowed": ("4th Down Conversions Allowed", 0, False),
    "d4_conv_pct_allowed": ("4th Down Conversion % Allowed", 1, True),
    "d4_stop_pct": ("4th Down Stop Rate", 1, True),
}
PASS_DEF_COLS = {
    "comp_allowed": ("Completions Allowed", 0, False),
    "att_faced": ("Attempts Faced", 0, False),
    "pass_yds_allowed": ("Passing Yards Allowed", 0, False),
    "pass_td_allowed": ("Passing TDs Allowed", 0, False),
    "comp_pct_allowed": ("Completion % Allowed", 1, True),
    "pass_air_yds_allowed": ("Air Yards Allowed", 0, False),
    "pass_yac_allowed": ("YAC Allowed", 0, False),
    "pass_fd_allowed": ("Passing First Downs Allowed", 0, False),
    "pass_epa_allowed": ("Passing EPA Allowed", 1, False),
    "def_pass10_allowed": ("10+ Yd Completions Allowed", 0, False),
    "def_pass16_allowed": ("16+ Yd Completions Allowed", 0, False),
    "def_pass20_allowed": ("20+ Yd Completions Allowed", 0, False),
    "def_pass40_allowed": ("40+ Yd Completions Allowed", 0, False),
    "def_sacks": ("Sacks", 0, False),
    "def_sack_yards": ("Sack Yards", 0, False),
    "def_qb_hits": ("QB Hits", 0, False),
    "def_pass_defended": ("Passes Defended", 0, False),
}
RUN_DEF_COLS = {
    "carries_faced": ("Carries Faced", 0, False),
    "rush_yds_allowed": ("Rushing Yards Allowed", 0, False),
    "rush_td_allowed": ("Rushing TDs Allowed", 0, False),
    "rush_fd_allowed": ("Rushing First Downs Allowed", 0, False),
    "rush_epa_allowed": ("Rushing EPA Allowed", 1, False),
    "def_rush10_allowed": ("10+ Yd Runs Allowed", 0, False),
    "def_rush12_allowed": ("12+ Yd Runs Allowed", 0, False),
    "def_rush20_allowed": ("20+ Yd Runs Allowed", 0, False),
    "def_rush40_allowed": ("40+ Yd Runs Allowed", 0, False),
    "def_tackles_for_loss": ("Tackles For Loss", 0, False),
    "def_tackles_for_loss_yards": ("TFL Yards", 0, False),
}
DOWN_DIST_SUBGROUP_NAME = "Down/Distance"
# subgroups that don't come from the plain team-column-sum path — Pass/Run
# Defense mix opponent-groupby yardage with play-by-play explosive-play
# counts, Down/Distance is pure play-by-play. All handled specially in
# build_team_stats().
CUSTOM_SUBGROUPS = {"Pass Defense", "Run Defense", DOWN_DIST_SUBGROUP_NAME}

TEAM_STATS_GROUPS = {
    "offense": {
        "Passing": {
            "completions": ("Completions", 0, False),
            "attempts": ("Attempts", 0, False),
            "passing_yards": ("Passing Yards", 0, False),
            "passing_tds": ("Passing TDs", 0, False),
            "passing_interceptions": ("Interceptions Thrown", 0, False),
            "sacks_suffered": ("Sacks Taken", 0, False),
            "sack_yards_lost": ("Sack Yards Lost", 0, False),
            "sack_fumbles": ("Sack Fumbles", 0, False),
            "sack_fumbles_lost": ("Sack Fumbles Lost", 0, False),
            "passing_air_yards": ("Air Yards", 0, False),
            "passing_yards_after_catch": ("YAC (Passing)", 0, False),
            "passing_first_downs": ("Passing First Downs", 0, False),
            "passing_epa": ("Passing EPA", 1, False),
            "passing_cpoe": ("CPOE (pts)", 1, True),
            "passing_2pt_conversions": ("Passing 2PT Conversions", 0, False),
            "passing_10": ("10+ Yd Completions", 0, False),
            "passing_16": ("16+ Yd Completions", 0, False),
            "passing_20": ("20+ Yd Completions", 0, False),
            "passing_40": ("40+ Yd Completions", 0, False),
        },
        "Rushing": {
            "carries": ("Carries", 0, False),
            "rushing_yards": ("Rushing Yards", 0, False),
            "rushing_tds": ("Rushing TDs", 0, False),
            "rushing_fumbles": ("Rushing Fumbles", 0, False),
            "rushing_fumbles_lost": ("Rushing Fumbles Lost", 0, False),
            "rushing_first_downs": ("Rushing First Downs", 0, False),
            "rushing_epa": ("Rushing EPA", 1, False),
            "rushing_2pt_conversions": ("Rushing 2PT Conversions", 0, False),
            "rushing_10": ("10+ Yd Runs", 0, False),
            "rushing_12": ("12+ Yd Runs", 0, False),
            "rushing_20": ("20+ Yd Runs", 0, False),
            "rushing_40": ("40+ Yd Runs", 0, False),
        },
        "Receiving": {
            "receptions": ("Receptions", 0, False),
            "targets": ("Targets", 0, False),
            "receiving_yards": ("Receiving Yards", 0, False),
            "receiving_tds": ("Receiving TDs", 0, False),
            "receiving_fumbles": ("Receiving Fumbles", 0, False),
            "receiving_fumbles_lost": ("Receiving Fumbles Lost", 0, False),
            "receiving_air_yards": ("Receiving Air Yards", 0, False),
            "receiving_yards_after_catch": ("YAC (Receiving)", 0, False),
            "receiving_first_downs": ("Receiving First Downs", 0, False),
            "receiving_epa": ("Receiving EPA", 1, False),
            "receiving_2pt_conversions": ("Receiving 2PT Conversions", 0, False),
            "receiving_10": ("10+ Yd Catches", 0, False),
            "receiving_16": ("16+ Yd Catches", 0, False),
            "receiving_20": ("20+ Yd Catches", 0, False),
            "receiving_40": ("40+ Yd Catches", 0, False),
        },
        "Down/Distance": DOWN_DIST_OFF_COLS,
        "Ball Security": {
            "fumbles_total": ("Total Fumbles", 0, False),
            "fumbles_lost_total": ("Fumbles Lost", 0, False),
            "fumbles_not_forced": ("Unforced Fumbles", 0, False),
            "fumbles_out_of_bounds": ("Fumbles Out of Bounds", 0, False),
            "fumbles_forced_by_opp": ("Fumbles Forced By Opponent", 0, False),
            "fumble_recovery_own": ("Own Fumbles Recovered", 0, False),
            "fumble_recovery_yards_own": ("Own Fumble Recovery Yards", 0, False),
        },
    },
    "defense": {
        "Pass Defense": PASS_DEF_COLS,
        "Run Defense": RUN_DEF_COLS,
        "Tackling": {
            "def_tackles_solo": ("Solo Tackles", 0, False),
            "def_tackles_with_assist": ("Assisted Tackles", 0, False),
            "def_tackle_assists": ("Tackle Assists", 0, False),
        },
        "Turnovers Forced": {
            "def_interceptions": ("Interceptions", 0, False),
            "def_interception_yards": ("INT Return Yards", 0, False),
            "def_fumbles_forced": ("Fumbles Forced", 0, False),
            "def_fumbles": ("Defensive Fumbles", 0, False),
            "fumble_recovery_opp": ("Opponent Fumbles Recovered", 0, False),
            "fumble_recovery_yards_opp": ("Opp Fumble Recovery Yards", 0, False),
            "fumble_recovery_tds": ("Fumble Recovery TDs", 0, False),
        },
        "Scoring": {
            "def_tds": ("Defensive TDs", 0, False),
            "def_safeties": ("Safeties", 0, False),
        },
        "Down/Distance": DOWN_DIST_DEF_COLS,
    },
    "special_teams": {
        "Kicking": {
            "fg_made": ("FG Made", 0, False),
            "fg_att": ("FG Attempts", 0, False),
            "fg_missed": ("FG Missed", 0, False),
            "fg_blocked": ("FG Blocked", 0, False),
            "fg_long": ("Longest FG", 0, False),
            "fg_pct": ("FG %", 1, True),
            "fg_made_0_19": ("FG Made 0-19", 0, False),
            "fg_made_20_29": ("FG Made 20-29", 0, False),
            "fg_made_30_39": ("FG Made 30-39", 0, False),
            "fg_made_40_49": ("FG Made 40-49", 0, False),
            "fg_made_50_59": ("FG Made 50-59", 0, False),
            "fg_made_60_": ("FG Made 60+", 0, False),
            "fg_missed_0_19": ("FG Missed 0-19", 0, False),
            "fg_missed_20_29": ("FG Missed 20-29", 0, False),
            "fg_missed_30_39": ("FG Missed 30-39", 0, False),
            "fg_missed_40_49": ("FG Missed 40-49", 0, False),
            "fg_missed_50_59": ("FG Missed 50-59", 0, False),
            "fg_missed_60_": ("FG Missed 60+", 0, False),
            "fg_made_distance": ("Made FG Total Yards", 0, False),
            "fg_missed_distance": ("Missed FG Total Yards", 0, False),
            "fg_blocked_distance": ("Blocked FG Total Yards", 0, False),
            "pat_made": ("PAT Made", 0, False),
            "pat_att": ("PAT Attempts", 0, False),
            "pat_missed": ("PAT Missed", 0, False),
            "pat_blocked": ("PAT Blocked", 0, False),
            "pat_pct": ("PAT %", 1, True),
            "gwfg_made": ("Game-Winning FG Made", 0, False),
            "gwfg_att": ("Game-Winning FG Att", 0, False),
            "gwfg_missed": ("Game-Winning FG Missed", 0, False),
            "gwfg_blocked": ("Game-Winning FG Blocked", 0, False),
            "gwfg_distance": ("Game-Winning FG Distance", 0, False),
        },
        "Punting": {
            "pt_att": ("Punts", 0, False),
            "pt_blocked": ("Punts Blocked", 0, False),
            "pt_long": ("Longest Punt", 0, False),
            "pt_yards": ("Punt Yards", 0, False),
            "pt_net_yards": ("Net Punt Yards", 0, False),
            "pt_inside_20": ("Punts Inside 20", 0, False),
            "pt_out_of_bounds": ("Punts Out of Bounds", 0, False),
            "pt_downed": ("Punts Downed", 0, False),
            "pt_touchback": ("Punt Touchbacks", 0, False),
            "pt_fair_caught": ("Opponent Fair Catches", 0, False),
            "pt_returned": ("Opponent Punt Returns", 0, False),
            "pt_return_yards": ("Opponent Punt Return Yards", 0, False),
            "pt_return_tds": ("Opponent Punt Return TDs", 0, False),
        },
        "Returns": {
            "punt_returns": ("Punt Returns", 0, False),
            "punt_return_yards": ("Punt Return Yards", 0, False),
            "kickoff_returns": ("Kickoff Returns", 0, False),
            "kickoff_return_yards": ("Kickoff Return Yards", 0, False),
            "special_teams_tds": ("Special Teams TDs", 0, False),
            "misc_yards": ("Misc Yards", 0, False),
        },
    },
    "penalties": {
        "Discipline": {
            "penalties": ("Penalties", 0, False),
            "penalty_yards": ("Penalty Yards", 0, False),
            "timeouts": ("Timeouts Used", 0, False),
        },
    },
}


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
    cols = ["player_id", "name", "position", "team", "opponent_team", "week"] + RAW_COLS
    for c in cols:
        if c not in df.columns:
            df[c] = 0
    df = df[cols].copy()
    num = [c for c in cols if c not in ("player_id", "name", "position", "team", "opponent_team")]
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
            "rec_pg":   safe_div(g("receptions"), gp),
            "rush_td":  g("rushing_tds"),
            "rec_td":   g("receiving_tds"),
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
        "rec_pg":  safe_div(g("receptions"), gp),
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
        for m, (_lbl, dec, off_hb, _grp) in POS_METRICS_WEEKLY[p].items():
            out_pos_off[p][m] = pack({t: pos_off[p][t][m] for t in all_teams}, off_hb, dec)
            out_pos_def[p][m] = pack({t: pos_def[p][t][m] for t in all_teams}, not off_hb, dec)

    teams = {}
    for t in all_teams:
        teams[t] = {
            "record": records[t], "gp": len(wl.get(t, [])),
            "team_off": {m: out_team_off[m][t] for m in TEAM_OFF},
            "team_def": {m: out_team_def[m][t] for m in TEAM_DEF},
            "off": {p: {m: out_pos_off[p][m][t] for m in POS_METRICS_WEEKLY[p]} for p in POSITIONS},
            "def": {p: {m: out_pos_def[p][m][t] for m in POS_METRICS_WEEKLY[p]} for p in POSITIONS},
        }

    payload = {
        "season": SEASON,
        "week": week,
        "data_horizon": f"weeks 1-{week - 1}",
        "labels": {
            "team_off": {m: TEAM_OFF[m][0] for m in TEAM_OFF},
            "team_def": {m: TEAM_DEF[m][0] for m in TEAM_DEF},
            "pos": {p: {m: {"l": POS_METRICS_WEEKLY[p][m][0], "g": POS_METRICS_WEEKLY[p][m][3],
                            "inv": not POS_METRICS_WEEKLY[p][m][2]}
                        for m in POS_METRICS_WEEKLY[p]} for p in POSITIONS},
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


def fetch_pbp():
    """Play-by-play is gzipped and much bigger than the other feeds, so it
    gets its own fetch path rather than reusing fetch_csv()'s text/StringIO
    handling."""
    if PBP_URL in _CSV_CACHE:
        return _CSV_CACHE[PBP_URL].copy()
    print(f"  fetching {PBP_URL}")
    r = requests.get(PBP_URL, timeout=180)
    if r.status_code != 200:
        sys.exit(f"FATAL: could not download play-by-play (HTTP {r.status_code}).")
    df = pd.read_csv(BytesIO(r.content), compression="gzip", low_memory=False)
    _CSV_CACHE[PBP_URL] = df
    return df.copy()


def compute_pbp_stats(games_played):
    """Offense/defense splits that need play-by-play, not just the season
    team-stats file: Down/Distance and Explosive Plays Allowed. Loaded once
    and shared so we don't re-download pbp twice."""
    pbp = fetch_pbp()
    reg = pbp[pbp["season_type"] == "REG"]

    def pct(n, d):
        return round(100 * n / d, 1) if d else 0.0

    d1 = reg[(reg["down"] == 1) & (reg["play_type"].isin(["run", "pass"]))]
    off1 = d1.groupby(["posteam", "play_type"]).size().unstack(fill_value=0)
    def1 = d1.groupby(["defteam", "play_type"]).size().unstack(fill_value=0)

    d3 = reg[reg["down"] == 3]
    off3 = d3.groupby("posteam").agg(conv=("third_down_converted", "sum"),
                                      fail=("third_down_failed", "sum"))
    def3 = d3.groupby("defteam").agg(conv=("third_down_converted", "sum"),
                                      fail=("third_down_failed", "sum"))

    d4 = reg[reg["down"] == 4]
    d4_go = d4[d4["play_type"].isin(["run", "pass"])]
    off4_go = d4_go.groupby("posteam").agg(att=("play_id", "count"),
                                            conv=("fourth_down_converted", "sum"))
    off4_tot = d4.groupby("posteam").size()
    def4_go = d4_go.groupby("defteam").agg(att=("play_id", "count"),
                                            conv=("fourth_down_converted", "sum"))
    def4_tot = d4.groupby("defteam").size()

    # explosive plays allowed: completions/runs faced by each defense, by
    # the same yardage thresholds nflverse uses on the offense side.
    pass_faced = reg[(reg["play_type"] == "pass") & (reg["complete_pass"] == 1)]
    rush_faced = reg[reg["play_type"] == "run"]
    pass_bucket = {}
    for thresh in (10, 16, 20, 40):
        pass_bucket[thresh] = pass_faced[pass_faced["yards_gained"] >= thresh].groupby("defteam").size()
    rush_bucket = {}
    for thresh in (10, 12, 20, 40):
        rush_bucket[thresh] = rush_faced[rush_faced["yards_gained"] >= thresh].groupby("defteam").size()

    def get(df_, t, col, default=0):
        return int(df_.loc[t, col]) if (df_ is not None and t in df_.index and col in df_.columns) else default

    out = {}
    for t, gp in games_played.items():
        run1 = get(off1, t, "run"); pass1 = get(off1, t, "pass")
        run1d = get(def1, t, "run"); pass1d = get(def1, t, "pass")
        c3 = int(off3.loc[t, "conv"]) if t in off3.index else 0
        f3 = int(off3.loc[t, "fail"]) if t in off3.index else 0
        c3d = int(def3.loc[t, "conv"]) if t in def3.index else 0
        f3d = int(def3.loc[t, "fail"]) if t in def3.index else 0
        goA = int(off4_go.loc[t, "att"]) if t in off4_go.index else 0
        goC = int(off4_go.loc[t, "conv"]) if t in off4_go.index else 0
        totA = int(off4_tot.get(t, 0))
        goAd = int(def4_go.loc[t, "att"]) if t in def4_go.index else 0
        goCd = int(def4_go.loc[t, "conv"]) if t in def4_go.index else 0
        totAd = int(def4_tot.get(t, 0))

        def tavg(tot, dec=0):
            return {"tot": tot, "avg": round(tot / gp, max(dec, 1)) if gp else 0}
        def ravg(val):
            return {"tot": None, "avg": val}

        off_dd = {
            "fd1_run": tavg(run1), "fd1_pass": tavg(pass1),
            "fd1_run_pct": ravg(pct(run1, run1 + pass1)),
            "fd1_pass_pct": ravg(pct(pass1, run1 + pass1)),
            "d3_att": tavg(c3 + f3), "d3_conv": tavg(c3), "d3_pct": ravg(pct(c3, c3 + f3)),
            "d4_situations": tavg(totA), "d4_go_att": tavg(goA),
            "d4_go_pct": ravg(pct(goA, totA)),
            "d4_conv": tavg(goC), "d4_conv_pct": ravg(pct(goC, goA)),
        }
        def_dd = {
            "fd1_run_faced": tavg(run1d), "fd1_pass_faced": tavg(pass1d),
            "fd1_run_pct_faced": ravg(pct(run1d, run1d + pass1d)),
            "fd1_pass_pct_faced": ravg(pct(pass1d, run1d + pass1d)),
            "d3_att_faced": tavg(c3d + f3d), "d3_conv_allowed": tavg(c3d),
            "d3_pct_allowed": ravg(pct(c3d, c3d + f3d)), "d3_stop_pct": ravg(pct(f3d, c3d + f3d)),
            "d4_situations_faced": tavg(totAd), "d4_go_att_faced": tavg(goAd),
            "d4_go_pct_faced": ravg(pct(goAd, totAd)),
            "d4_conv_allowed": tavg(goCd), "d4_conv_pct_allowed": ravg(pct(goCd, goAd)),
            "d4_stop_pct": ravg(pct(goAd - goCd, goAd)),
        }
        out[t] = {
            "offense": {DOWN_DIST_SUBGROUP_NAME: off_dd},
            "defense": {DOWN_DIST_SUBGROUP_NAME: def_dd},
            "explosive_pass_allowed": {th: int(pass_bucket[th].get(t, 0)) for th in (10, 16, 20, 40)},
            "explosive_rush_allowed": {th: int(rush_bucket[th].get(t, 0)) for th in (10, 12, 20, 40)},
        }
    return out


def compute_pass_run_defense(df, games_played, pbp_stats):
    """Pass/Run Defense subgroups: yardage allowed comes from re-aggregating
    the team-stats file by opponent_team (each row already holds what the
    opposing offense did that week); sacks/QB hits/TFL/passes-defended are
    this team's own def_* columns; explosive-play counts come from the
    play-by-play pass computed above. All three get merged into one dict
    per subgroup here since TEAM_STATS_GROUPS treats them as a single
    'custom' subgroup."""
    opp_pass_cols = ["completions", "attempts", "passing_yards", "passing_tds",
                      "passing_air_yards", "passing_yards_after_catch",
                      "passing_first_downs", "passing_epa"]
    opp_rush_cols = ["carries", "rushing_yards", "rushing_tds",
                      "rushing_first_downs", "rushing_epa"]
    own_cols = ["def_sacks", "def_sack_yards", "def_qb_hits", "def_pass_defended",
                "def_tackles_for_loss", "def_tackles_for_loss_yards"]
    for c in opp_pass_cols + opp_rush_cols + own_cols:
        if c not in df.columns:
            df[c] = 0
    opp_sums = df.groupby("opponent_team")[opp_pass_cols + opp_rush_cols].sum(numeric_only=True)
    own_sums = df.groupby("team")[own_cols].sum(numeric_only=True)

    def tavg(tot, gp, dec=0):
        tot = round(float(tot), dec)
        tot = int(tot) if dec == 0 else tot
        return {"tot": tot, "avg": round(tot / gp, max(dec, 1)) if gp else 0}
    def ravg(val):
        return {"tot": None, "avg": round(val, 1)}
    def pct(n, d):
        return round(100 * n / d, 1) if d else 0.0

    out = {}
    for t, gp in games_played.items():
        o = opp_sums.loc[t] if t in opp_sums.index else opp_sums.iloc[0] * 0
        s = own_sums.loc[t] if t in own_sums.index else own_sums.iloc[0] * 0
        expl_p = pbp_stats.get(t, {}).get("explosive_pass_allowed", {10: 0, 16: 0, 20: 0, 40: 0})
        expl_r = pbp_stats.get(t, {}).get("explosive_rush_allowed", {10: 0, 12: 0, 20: 0, 40: 0})

        pass_def = {
            "comp_allowed": tavg(o["completions"], gp),
            "att_faced": tavg(o["attempts"], gp),
            "pass_yds_allowed": tavg(o["passing_yards"], gp),
            "pass_td_allowed": tavg(o["passing_tds"], gp),
            "comp_pct_allowed": ravg(pct(o["completions"], o["attempts"])),
            "pass_air_yds_allowed": tavg(o["passing_air_yards"], gp),
            "pass_yac_allowed": tavg(o["passing_yards_after_catch"], gp),
            "pass_fd_allowed": tavg(o["passing_first_downs"], gp),
            "pass_epa_allowed": tavg(o["passing_epa"], gp, dec=1),
            "def_pass10_allowed": tavg(expl_p[10], gp),
            "def_pass16_allowed": tavg(expl_p[16], gp),
            "def_pass20_allowed": tavg(expl_p[20], gp),
            "def_pass40_allowed": tavg(expl_p[40], gp),
            "def_sacks": tavg(s["def_sacks"], gp),
            "def_sack_yards": tavg(s["def_sack_yards"], gp),
            "def_qb_hits": tavg(s["def_qb_hits"], gp),
            "def_pass_defended": tavg(s["def_pass_defended"], gp),
        }
        run_def = {
            "carries_faced": tavg(o["carries"], gp),
            "rush_yds_allowed": tavg(o["rushing_yards"], gp),
            "rush_td_allowed": tavg(o["rushing_tds"], gp),
            "rush_fd_allowed": tavg(o["rushing_first_downs"], gp),
            "rush_epa_allowed": tavg(o["rushing_epa"], gp, dec=1),
            "def_rush10_allowed": tavg(expl_r[10], gp),
            "def_rush12_allowed": tavg(expl_r[12], gp),
            "def_rush20_allowed": tavg(expl_r[20], gp),
            "def_rush40_allowed": tavg(expl_r[40], gp),
            "def_tackles_for_loss": tavg(s["def_tackles_for_loss"], gp),
            "def_tackles_for_loss_yards": tavg(s["def_tackles_for_loss_yards"], gp),
        }
        out[t] = {"Pass Defense": pass_def, "Run Defense": run_def}
    return out


def build_career_base():
    """One-time (or rarely re-run) historical aggregation: every season from
    1999 through the season before SEASON, summed per player_id. This is
    deliberately NOT part of the regular weekly build — refetching 25+
    seasons every run would be slow and pointless since history doesn't
    change. Run this manually (python3 build_matchup_stats.py --career-base)
    when you want to refresh it; the regular build just reads the resulting
    file and layers the current season on top of it at render/build time."""
    years = range(1999, SEASON)
    totals = {}  # player_id -> {name, pos, team, games, raw: {col: sum}}
    for year in years:
        urls = [
            f"https://github.com/nflverse/nflverse-data/releases/download/stats_player/stats_player_week_{year}.csv",
            f"https://github.com/nflverse/nflverse-data/releases/download/player_stats/player_stats_{year}.csv",
        ]
        df = None
        for url in urls:
            print(f"  fetching {url}")
            try:
                r = requests.get(url, timeout=90)
                if r.status_code != 200:
                    print(f"    -> HTTP {r.status_code}, trying next candidate")
                    continue
                df = pd.read_csv(StringIO(r.text), low_memory=False)
                break
            except Exception as e:
                print(f"    -> {e}, trying next candidate")
        if df is None:
            print(f"    -> no source found for {year}, skipping")
            continue

        df = df[df.get("season_type", "REG") == "REG"] if "season_type" in df.columns else df
        df["pos"] = df["position"].map(POS_MAP)
        df = df[df["pos"].notna()]
        for c in RAW_COLS:
            if c not in df.columns:
                df[c] = 0
        df[RAW_COLS] = df[RAW_COLS].fillna(0)

        grouped = df.groupby(["player_id", "pos"])
        sums = grouped[RAW_COLS].sum(numeric_only=True)
        games = grouped.size()
        last_name = grouped["player_display_name"].last() if "player_display_name" in df.columns else grouped["player_name"].last()
        last_team_col = "recent_team" if "recent_team" in df.columns else "team"
        last_team = grouped[last_team_col].last()

        for (pid, pos), gp in games.items():
            key = (pid, pos)
            if key not in totals:
                totals[key] = {"name": last_name.get((pid, pos), ""), "pos": pos,
                                "team": last_team.get((pid, pos), ""), "games": 0,
                                "raw": {c: 0.0 for c in RAW_COLS}}
            t = totals[key]
            t["games"] += int(gp)
            t["name"] = last_name.get((pid, pos), t["name"])  # keep most recent
            t["team"] = last_team.get((pid, pos), t["team"])
            for c in RAW_COLS:
                t["raw"][c] += float(sums.loc[(pid, pos), c])

    payload = {
        "through_season": SEASON - 1,
        "players": {f"{pid}|{pos}": v for (pid, pos), v in totals.items()},
    }
    os.makedirs("players", exist_ok=True)
    path = "players/career_base.json"
    with open(path, "w") as f:
        json.dump(payload, f)
    print(f"Wrote {path} — {len(totals)} player-position entries, "
          f"1999-{SEASON-1}, {os.path.getsize(path) / 1024:.0f} KB")


def dk_points_for_game(s):
    """Standard DraftKings Classic scoring (full PPR), computed directly
    from RAW_COLS — works the same for any offensive position since
    non-applicable fields are just 0 (a QB's receiving_yards is 0, etc).
    Doesn't include 2pt conversions (not in the player-week source data) —
    a minor, disclosed gap; rare enough not to meaningfully move rankings."""
    pts = 0.0
    pts += s.get("passing_yards", 0) * 0.04
    pts += s.get("passing_tds", 0) * 4
    pts += s.get("passing_interceptions", 0) * -1
    if s.get("passing_yards", 0) >= 300:
        pts += 3
    pts += s.get("rushing_yards", 0) * 0.1
    pts += s.get("rushing_tds", 0) * 6
    if s.get("rushing_yards", 0) >= 100:
        pts += 3
    pts += s.get("receptions", 0) * 1
    pts += s.get("receiving_yards", 0) * 0.1
    pts += s.get("receiving_tds", 0) * 6
    if s.get("receiving_yards", 0) >= 100:
        pts += 3
    fumbles_lost = (s.get("sack_fumbles_lost", 0) + s.get("rushing_fumbles_lost", 0)
                     + s.get("receiving_fumbles_lost", 0))
    pts -= fumbles_lost * 1
    return pts


def build_player_log(player_df, pos, latest_matchup):
    """One player's game-by-game log, each game tagged with the tier
    (top/mid/bot) of the defense-vs-position rank their opponent held that
    week, plus average production split by tier. The Volume-group stats
    only, to keep a game row readable at a glance.

    Counting stats (Passing Yards, Completions, Attempts...) show that
    single game's total. Rate stats (_pg/_ypg suffix, e.g. Passing Yards /
    Game) show the running season-to-date average THROUGH that week, not
    that game's own total divided by 1 — otherwise "yards" and "yards /
    game" are identical and the per-game column is meaningless."""
    volume_keys = [k for k, (_l, _d, _hb, grp) in POS_METRICS[pos].items() if grp == "Volume"]
    rate_keys = {k for k in volume_keys if k.endswith("_pg") or k.endswith("_ypg")}
    primary_key = volume_keys[0]

    log = []
    tier_rows = {"top": [], "mid": [], "bot": []}
    cum_raw = {c: 0.0 for c in RAW_COLS}
    cum_games = 0
    dk_scores = []
    for _, row in player_df.sort_values("week").iterrows():
        opp = row.get("opponent_team")
        s = {c: row[c] for c in RAW_COLS}
        game_metrics = pos_metrics_from_sums(pos, s, 1)  # this game's own totals
        dk_pts = dk_points_for_game(s)
        dk_scores.append(dk_pts)

        cum_games += 1
        for c in RAW_COLS:
            cum_raw[c] += s[c]
        cum_metrics = pos_metrics_from_sums(pos, cum_raw, cum_games)  # through this week

        tier = None
        if latest_matchup and opp in latest_matchup.get("teams", {}):
            def_block = latest_matchup["teams"][opp].get("def", {}).get(pos, {})
            rank = def_block.get(primary_key, {}).get("r")
            if rank is not None:
                tier = tier_of(rank)

        entry = {
            "week": int(row["week"]), "opp": opp, "tier": tier,
            "m": {k: round(game_metrics.get(k, 0), 1) for k in volume_keys},
            "cum": {k: round(cum_metrics.get(k, 0), 1) for k in rate_keys},
            "dk": round(dk_pts, 1),
        }
        log.append(entry)
        if tier:
            tier_rows[tier].append(entry["m"])

    dk_scores_sorted = sorted(dk_scores, reverse=True)
    ceiling = {
        "games": len(dk_scores),
        "best": round(dk_scores_sorted[0], 1) if dk_scores_sorted else 0,
        "top3avg": round(sum(dk_scores_sorted[:3]) / min(3, len(dk_scores_sorted)), 1) if dk_scores_sorted else 0,
    }

    splits = {}
    for tier, rows in tier_rows.items():
        if not rows:
            splits[tier] = {"games": 0, "m": {}}
            continue
        splits[tier] = {
            "games": len(rows),
            "m": {k: round(sum(r[k] for r in rows) / len(rows), 1) for k in volume_keys},
        }
    return log, splits, ceiling


def build_player_stats():
    """Season-to-date individual player leaderboards, grouped by position
    then by the same Volume/Efficiency/Explosive/Protection categories
    POS_METRICS already tags each stat with. Reuses norm_players() (already
    fetched for Matchup Stats) and pos_metrics_from_sums() (already used for
    team-position aggregates) — a player is just a group-by of one. Always-
    current, not week-gated, same as team stats.

    Also layers in career totals (from the separately-built career_base.json,
    if present) and a per-game log classified by the opponent's defense-vs-
    position tier that week, reusing tier_of() — same Top10/Mid12/Bottom10
    convention as the Contextual Stats page, using the most recently built
    matchup/wkNN.json as the current defense-vs-position ranking (a single
    current snapshot applied across the season's games, matching how
    Contextual Stats already classifies team-position logs)."""
    stats = norm_players(fetch_csv(PLAYER_STATS_URLS))
    if stats.empty:
        raise SystemExit(f"no {SEASON} player stats available yet")

    career_base = {}
    if os.path.exists("players/career_base.json"):
        with open("players/career_base.json") as f:
            cb = json.load(f)
        career_base = cb.get("players", {})
        career_through = cb.get("through_season", SEASON - 1)
    else:
        career_through = SEASON - 1

    # latest built matchup week on disk -> current defense-vs-position ranks
    latest_matchup = None
    if os.path.isdir("matchup"):
        wk_files = sorted(int(f[2:4]) for f in os.listdir("matchup")
                           if f.startswith("wk") and f.endswith(".json"))
        if wk_files:
            with open(f"matchup/wk{wk_files[-1]:02d}.json") as f:
                latest_matchup = json.load(f)

    games_played = stats.groupby(["player_id", "pos"]).size().to_dict()
    sums = stats.groupby(["player_id", "pos"])[RAW_COLS].sum(numeric_only=True)
    latest_name = (stats.sort_values("week")
                    .groupby(["player_id", "pos"])["name"].last().to_dict())
    latest_team = (stats.sort_values("week")
                    .groupby(["player_id", "pos"])["team"].last().to_dict())
    player_weeks = {key: sub for key, sub in stats.groupby(["player_id", "pos"])}

    # Team-week totals for carries/targets, used to compute each player's
    # rush/target share. nflverse ships target_share pre-computed per game,
    # but not season-level or rush_share at all — both are simple enough to
    # derive ourselves the same way: player's total over their games /
    # the matching team-week totals for those SAME (team, week) pairs,
    # which correctly handles a player traded mid-season.
    team_week_totals = stats.groupby(["team", "week"])[["carries", "targets"]].sum()

    def season_share(player_df, col):
        player_total = player_df[col].sum()
        team_total = 0.0
        for _, row in player_df.iterrows():
            key = (row["team"], row["week"])
            if key in team_week_totals.index:
                team_total += team_week_totals.loc[key, col]
        if team_total <= 0:
            return None
        return round(100 * player_total / team_total, 1)

    players_out = {p: [] for p in POSITIONS}
    for (pid, pos), gp in games_played.items():
        name = latest_name.get((pid, pos), "")
        team = latest_team.get((pid, pos), "")
        s = sums.loc[(pid, pos)].to_dict()
        season_metrics = pos_metrics_from_sums(pos, s, gp)

        pdf = player_weeks[(pid, pos)]
        if pos == "RB":
            season_metrics["rush_share"] = season_share(pdf, "carries")
            season_metrics["target_share"] = season_share(pdf, "targets")
        elif pos in ("WR", "TE"):
            season_metrics["target_share"] = season_share(pdf, "targets")

        cb_key = f"{pid}|{pos}"
        cb_entry = career_base.get(cb_key)
        career_gp = gp + (cb_entry["games"] if cb_entry else 0)
        career_raw = dict(s)
        if cb_entry:
            for c in RAW_COLS:
                career_raw[c] = career_raw.get(c, 0) + cb_entry["raw"].get(c, 0)
        career_metrics = pos_metrics_from_sums(pos, career_raw, career_gp)
        # Usage share is deliberately season-only, not career — aggregating
        # target share across team changes and different offenses over many
        # years isn't a meaningful number the way a season snapshot is.

        log, splits_acc, ceiling = build_player_log(player_weeks[(pid, pos)], pos, latest_matchup)

        players_out[pos].append({
            "name": name, "team": team, "games": gp,
            "season": {"games": gp, "m": {k: (round(v, 2) if v is not None else None)
                                           for k, v in season_metrics.items()}},
            "career": {"games": career_gp, "through": career_through,
                       "m": {k: round(v, 2) for k, v in career_metrics.items()}},
            "log": log, "splits": splits_acc, "ceiling": ceiling,
        })
    for p in POSITIONS:
        players_out[p].sort(key=lambda r: r["games"], reverse=True)

    labels = {}
    for pos, metrics in POS_METRICS.items():
        by_group = {}
        for k, (lbl, dec, hb, grp) in metrics.items():
            by_group.setdefault(grp, {})[k] = {"l": lbl, "inv": not hb}
        labels[pos] = by_group

    payload = {
        "season": SEASON,
        "data_horizon": f"through {max(games_played.values())} games played",
        "labels": labels,
        "players": players_out,
    }
    os.makedirs("players", exist_ok=True)
    path = "players/latest.json"
    with open(path, "w") as f:
        json.dump(payload, f)
    total = sum(len(v) for v in players_out.values())
    print(f"Wrote {path} — {total} players across {len(POSITIONS)} positions, "
          f"{os.path.getsize(path) / 1024:.0f} KB")


def build_team_stats():
    """Season-to-date team stats — every offense/defense/special-teams/penalty
    column nflverse's stats_team_week file provides, as both a season total
    and a per-game average. Not week-horizon-gated like the ranking pages;
    this is just 'what's true right now', so it always uses every played
    week. Writes a single file, overwritten on every build run."""
    df = fetch_csv(TEAM_STATS_URL)
    df = df[(df["season"] == SEASON) & (df["season_type"] == "REG")]
    if df.empty:
        raise SystemExit(f"no {SEASON} team stats available yet")

    games_played = df.groupby("team").size().to_dict()
    all_cols = [c for section, grp in TEAM_STATS_GROUPS.items()
                for sub, cols in grp.items() if sub not in CUSTOM_SUBGROUPS
                for c in cols]
    for c in all_cols:
        if c not in df.columns:
            df[c] = 0
    sums = df.groupby("team")[all_cols].sum(numeric_only=True)
    means = df.groupby("team")[all_cols].mean(numeric_only=True)
    pbp_stats = compute_pbp_stats(games_played)
    pass_run_def = compute_pass_run_defense(df, games_played, pbp_stats)

    teams_out = {}
    for t in sorted(games_played.keys()):
        gp = games_played[t]
        entry = {"games": gp}
        for section, subgroups in TEAM_STATS_GROUPS.items():
            entry[section] = {}
            for sub, cols in subgroups.items():
                if sub in ("Pass Defense", "Run Defense"):
                    entry[section][sub] = pass_run_def.get(t, {}).get(sub, {})
                    continue
                if sub == DOWN_DIST_SUBGROUP_NAME:
                    entry[section][sub] = pbp_stats.get(t, {}).get(section, {}).get(sub, {})
                    continue
                entry[section][sub] = {}
                for col, (_label, dec, is_rate) in cols.items():
                    if is_rate:
                        tot = None
                        avg = float(means.loc[t, col]) if t in means.index else 0
                        if col in ("fg_pct", "pat_pct"):
                            avg *= 100
                        avg = round(avg, dec)
                    else:
                        tot = round(float(sums.loc[t, col]), dec) if t in sums.index else 0
                        avg = round(tot / gp, max(dec, 1)) if gp else 0
                        tot = int(tot) if dec == 0 else tot
                    entry[section][sub][col] = {"tot": tot, "avg": avg}
        teams_out[t] = entry

    labels = {
        section: {sub: {c: v[0] for c, v in cols.items()} for sub, cols in subgroups.items()}
        for section, subgroups in TEAM_STATS_GROUPS.items()
    }
    payload = {
        "season": SEASON,
        "data_horizon": f"through {max(games_played.values())} games played",
        "labels": labels,
        "teams": teams_out,
    }
    os.makedirs("teamstats", exist_ok=True)
    path = "teamstats/latest.json"
    with open(path, "w") as f:
        json.dump(payload, f)
    print(f"Wrote {path} — {len(teams_out)} teams, "
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
    if arg == "--career-base":
        build_career_base()
        sys.exit(0)
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

    # 3. Team stats: always-current season totals for the Teams page modal.
    try:
        build_team_stats()
    except SystemExit as e:
        print(f"  team stats: skipped — {e}")

    # 4. Player leaderboards: always-current, for Stats Hub.
    try:
        build_player_stats()
    except SystemExit as e:
        print(f"  player stats: skipped — {e}")
