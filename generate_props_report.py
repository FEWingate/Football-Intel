"""
GENERATE_PROPS_REPORT.PY
==========================
Generates the real, structured content behind three of Prop Center's
five sub-sections: Coeus Prop Breakdown (3 favorite props per game,
plus one favorite per skill position, each with a suggested line or
alt), Favorite Overs and Unders for the week, and the existing 3/4/5/
6/7-team parlays. (Game Lines/Totals/ML and Player Props are pure,
real, live data display, built and read directly from
fanduel_props/latest.json — no LLM involved, see prop_center.html.)

REAL DESIGN CHANGE (2026-09-12): the original version of this script
only gave Coeus the FINISHED Game Breakdown text for each game — never
the original evidence packages behind them (Contextual Stats,
Matchup Intelligence, Threat Intelligence). Per Frank's explicit
instruction, Coeus's prop picks must be grounded in the SAME evidence
used to build the Game Breakdowns, especially Contextual Stats — not
just a prose summary of it. Both are now included: the Game Breakdown
text (trusted, already-vetted analysis) AND the raw evidence package
(the real underlying data) for every game on the slate.

REAL DESIGN CHANGE (2026-09-12): build_fanduel_props.py now tracks
real per-family coverage (current / stale_last_known_good /
unavailable) after a real, confirmed upstream reliability problem with
parlay-api.com (see PARLAY_API_RELIABILITY_INVESTIGATION.md). This
script reads that coverage metadata and tells Coeus explicitly, in
plain language, which stat families are live, which are stale (and
how old), and which have nothing at all — so it can caveat picks
honestly instead of presenting stale numbers as current, silently
skipping a category, or guessing. A stat family with zero real
coverage (live or stale) gets no pick at all — Coeus is told plainly
not to produce one, matching the Standard's "an honest gap is better
than a filled-in placeholder" rule already established for Game
Breakdowns and Contextual Stats.

REQUIRES: pip install anthropic --break-system-packages
          export ANTHROPIC_API_KEY=...   (never commit)
          fanduel_props/latest.json must already exist — run
          build_fanduel_props.py first.

USAGE:
    python3 generate_props_report.py
    python3 generate_props_report.py --dry-run
"""

import argparse
import copy
import json
import os
import re
import sys
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

from parlay_validator import validate_parlay, verify_legs_against_source, leg_key
from evidence_check_validator import verify_evidence_check


# REAL BUG FIX (2026-09-21), per Frank's direct, real catch: a real,
# already-played game (DET@BUF, Thursday) still generated real picks in
# a real run — confirmed directly the existing exclusion check only
# ever looks at whether FanDuel's OWN data still has an entry for a
# game, never independently at whether that game has actually kicked
# off yet. If FanDuel carries forward stale data for an already-played
# game rather than fully dropping it (a real, plausible provider
# behavior, not something this script controls), that check alone
# can't catch it. Real, independent kickoff-time check, ported from the
# same proven logic already used and tested on games.html/threats.html/
# stats_hub.html/injuries.html/coeus.html — checked against games/
# wkNN.json's own real kickoff data, not anything FanDuel reports.
def kickoff_has_passed(game_entry):
    gameday, gametime = game_entry.get("gameday"), game_entry.get("gametime")
    if not gameday or not gametime:
        return False
    hour, minute = (int(x) for x in gametime.split(":"))
    kickoff_et = datetime.strptime(gameday, "%Y-%m-%d").replace(
        hour=hour, minute=minute, tzinfo=ZoneInfo("America/New_York"))
    return datetime.now(timezone.utc) >= kickoff_et.astimezone(timezone.utc)


def already_played_games(games):
    """Returns the subset of (folder, away, home) whose REAL game has
    already kicked off, per games/wkNN.json — independent of whatever
    FanDuel's own data currently shows for that game."""
    played = []
    games_json_cache = {}
    for folder, away, home in games:
        if folder not in games_json_cache:
            games_json_cache[folder] = load_json(f"games/{folder}.json")
        wk_games = (games_json_cache[folder] or {}).get("games", [])
        real_entry = next((g for g in wk_games if g.get("away") == away and g.get("home") == home), None)
        if real_entry and kickoff_has_passed(real_entry):
            played.append((folder, away, home))
    return played

PROMPTS_DIR = "prompts"
MASTER_PROMPT_PATH = f"{PROMPTS_DIR}/Coeus_Master_Prompt_v1.1.md"
PROPS_STANDARD_PATH = f"{PROMPTS_DIR}/Coeus_Props_Parlay_Report_Standard_v2.0.md"
FANDUEL_DATA_PATH = "fanduel_props/latest.json"

DEFAULT_MODEL = "claude-sonnet-5"
PARLAY_SIZES = [3, 4, 5, 6, 7]
SKILL_POSITIONS = ["QB", "RB", "WR", "TE"]
STAT_LABELS = {"passing_yards": "Passing Yards", "rushing_yards": "Rushing Yards",
               "receiving_yards": "Receiving Yards", "receptions": "Receptions",
               "anytime_td": "Anytime TD"}

TASK_INSTRUCTION = """\
Generate this week's Props report for the FULL slate below, following the \
Props & Parlay Report Standard exactly, in this order:

1. Coeus Prop Breakdown — 3 favorite props for EACH game on the slate, \
plus one favorite prop for each of QB/RB/WR/TE league-wide across the \
whole slate. For every pick, name the real line FanDuel has posted AND \
suggest a specific line or alt-line threshold from the real data — \
never an invented number.
2. Favorite Overs and Unders for the week — your best Over picks and \
best Under picks across the ENTIRE slate, ranked by conviction, not \
grouped by game.
3. Five separate parlays (3, 4, 5, 6, and 7 team).

Lists and short entries only, per the No Paragraphs Rule — never prose \
paragraphs. Every football claim must come from the Game Breakdowns \
and/or the real evidence packages below (Contextual Stats especially) \
— never from outside knowledge. Every market, line, and price must \
come from the real FanDuel data below — never invent one. The REAL \
DATA COVERAGE section below tells you which stat families are live, \
which are stale, and which have no real data at all right now — a \
stat family with no real data (live or stale) gets no pick; say so \
plainly rather than skipping it silently or guessing. Every JSON block \
specified in the Standard is required, not optional — a real program \
checks every one of them after you finish.

=== REAL DATA COVERAGE (what you can actually trust right now) ===
"""


def load_text(path):
    if not os.path.exists(path):
        sys.exit(f"FATAL: {path} not found.")
    with open(path) as f:
        return f.read()


def load_json(path):
    if not os.path.exists(path):
        return None
    with open(path) as f:
        return json.load(f)


def discover_all_games():
    """Same lookup as generate_weekly_dfs_report.py's — every finished
    Game Breakdown, deduplicated across every game_breakdowns/*/manifest.json."""
    base = "game_breakdowns"
    if not os.path.isdir(base):
        return []
    seen = {}
    for folder in sorted(os.listdir(base)):
        manifest = load_json(os.path.join(base, folder, "manifest.json"))
        for key, g in (manifest.get("games") or {}).items() if manifest else []:
            if key not in seen:
                seen[key] = (folder, g["away"], g["home"])
    return list(seen.values())


def load_evidence_for_game(away, home):
    """Real evidence package for this game — bootstrap or regular,
    whichever actually exists, same lookup order the Game Breakdown
    generation itself uses. Returns (None, None) if neither exists,
    which is a real, reportable gap for this specific game, not
    something to silently paper over."""
    for path in (f"evidence_bootstrap/{away}_{home}.json", f"evidence/current/{away}_{home}.json"):
        data = load_json(path)
        if data:
            return data, path
    return None, None


def trim_evidence_for_props(evidence, multi_game=False):
    """REAL BUG FIX (2026-09-14): confirmed directly against real evidence
    files that a single game's full evidence package can run anywhere
    from ~23K to ~430K real characters — dominated almost entirely by
    each player's own "log" field: a full, real week-by-week game log
    (one detailed entry per week already played) sitting alongside that
    same player's already-aggregated "season" and "career" totals in the
    same record. For 5 real games this pushed the whole props prompt to
    ~375,000 tokens — a real, serious cost problem caught before it was
    ever run for real, not after.

    UPDATED (2026-09-15), per Frank's direct pushback: the original fix
    dropped "log" entirely. That went too far — a player's own recent
    games (who they actually played, what they actually did, and that
    opponent's real defensive tier/rank that week) is real, correctly-
    attributed evidence a season average can't give: whether they're
    actually hitting today's real posted line over their last 3/5/10
    games, against what caliber of defense. So "log" is now trimmed to
    the most recent 10 real entries per player, not removed — keeping
    that real recency and opponent-quality evidence while still
    avoiding the original cost problem (confirmed up to ~84% of one
    real game's entire evidence size in the worst case, from keeping
    all 17 weeks for every player on both rosters).

    This trim is props-specific — it does NOT touch the real evidence
    package on disk, and Game Breakdown generation (which can genuinely
    use the full week-by-week trend detail for its own deeper analysis)
    is completely unaffected.

    REAL CHANGE (2026-09-15), per Frank's direct request, for a
    different reason than cost — data correctness. A prop is a bet on
    one specific player producing one specific stat; it has nothing to
    do with which team wins or by how much. Several evidence blocks
    exist specifically to support real GAME-outcome narrative (Game
    Breakdown's whole purpose), not player-specific prop reasoning, and
    keeping them in the props prompt risks exactly what happened with
    the real, confirmed Mahomes Week 17 misattribution: team-level or
    schematic data getting reasoned into a specific player's stat line
    it was never actually about. Removed entirely for props:
      - team_context: both its per-game "log" and its "splits" are
        team-level, QB/RB/WR/TE POSITION-GROUP aggregates, never an
        individual player's own real production — the same real
        category of data that caused the Mahomes misattribution.
      - dfs: DraftKings salary/ownership data has zero real bearing on
        whether a FanDuel yardage or reception prop hits.
      - down_distance, red_zone_play_calling: real, but these describe
        team-level play-calling tendency and game script, not whether
        a specific named player reaches a specific number — the kind
        of evidence that supports a Game Breakdown's account of how a
        game is likely to unfold, not a prop pick's reasoning.
    Real, individual player evidence (threats, players.season/career/
    splits/ceiling, matchup's team_off/team_def category rankings —
    the actual opponent-side half of a real Threat-style convergence —
    and the player-specific slices of matchup_pattern_data) is
    untouched by this trim.

    REAL ADDITION (2026-09-21), per Frank's direct, real, confirmed
    problem: a genuine 16-game props run hit the API's hard 1,000,000
    token ceiling at 1,501,538 real tokens — confirmed directly (a real
    dry-run measurement, no API cost) that evidence alone was ~69% of
    the whole prompt at that scale, over 1,000,000 real tokens by
    itself even with the trim above already applied. The trim above was
    tuned and proven at single-game scale (~47K tokens); it was never
    enough at 16-game scale, and no amount of per-game data is going to
    fit comfortably once multiplied by that many games. When
    multi_game is true, three further, real cuts apply, calibrated to
    real per-game evidence roughly halving: log capped at 5 entries
    instead of 10 (still keeps real head-to-head meetings against
    today's opponent regardless, same as the single-game case — recency
    matters more than depth once evidence is being sent 16 times over);
    each remaining log entry's "_split_m" sub-block dropped (a more
    detailed, larger real duplicate of the same entry's own "m" block —
    "m" alone still carries the real per-game numbers this trim is
    built to preserve); and "career" dropped entirely (season,
    season_2025, and splits already give three real, DISTINCT windows —
    this year, last year, and opponent-tier — without career's more
    diluted, multi-year blend on top). Single-game runs are completely
    unaffected — multi_game defaults to False, so nothing here changes
    unless the real games list passed in genuinely warrants it."""
    trimmed = copy.deepcopy(evidence)
    game_info = trimmed.get("game") or {}
    away_team, home_team = game_info.get("away"), game_info.get("home")
    players = trimmed.get("players")
    log_cap = 5 if multi_game else 10
    if isinstance(players, dict):
        for side_name, side in players.items():
            # REAL BUG FIX (2026-09-15), per Frank's direct request: a
            # division rival plays this same real opponent twice a real
            # season, and how a player has actually performed in those
            # specific past meetings is real, directly relevant
            # evidence — not just general recent form. A pure "last 10
            # games" trim could accidentally cut a real division
            # meeting that happened earlier in a season. This player's
            # real opponent TODAY (the other team in this game — away
            # players face home, home players face away) is checked
            # explicitly, and any of their real past log entries
            # against that same opponent are kept regardless of
            # whether they'd otherwise fall outside the most recent 10
            # — capped at the 3 most recent such meetings, since that's
            # the real, relevant window for head-to-head history, not
            # every meeting a multi-season log might ever contain.
            todays_opponent = home_team if side_name == "away" else away_team
            if isinstance(side, list):
                for p in side:
                    if isinstance(p, dict) and isinstance(p.get("log"), list):
                        sorted_log = sorted(p["log"], key=lambda e: e.get("week", 0))
                        recentN = sorted_log[-log_cap:]
                        vs_opponent = [e for e in sorted_log if e.get("opp") == todays_opponent][-3:]
                        merged = {id(e): e for e in recentN}
                        for e in vs_opponent:
                            merged.setdefault(id(e), e)
                        final_log = sorted(merged.values(), key=lambda e: e.get("week", 0))
                        if multi_game:
                            for e in final_log:
                                if isinstance(e, dict):
                                    e.pop("_split_m", None)
                        p["log"] = final_log
                    if multi_game and isinstance(p, dict):
                        p.pop("career", None)
    for key in ("team_context", "dfs", "down_distance", "red_zone_play_calling"):
        trimmed.pop(key, None)
    return trimmed


def coverage_summary_text(coverage):
    """Real, human-readable summary of which stat families Coeus can
    actually trust right now — built directly from build_fanduel_props.py's
    real coverage metadata (current / stale_last_known_good /
    unavailable), not re-derived or guessed at from the raw game data."""
    lines = []
    for stat, label in STAT_LABELS.items():
        meta = (coverage or {}).get(stat, {})
        status = meta.get("status", "unavailable")
        real_key = f"player_{stat}"
        if status == "current":
            lines.append(f"- {label} (real market_key: `{real_key}`): LIVE, current data "
                         f"({meta.get('current_event_count', 0)} real game(s)).")
        elif status == "stale_last_known_good":
            age_min = round((meta.get("source_age_seconds") or 0) / 60)
            lines.append(f"- {label} (real market_key: `{real_key}`): STALE — the live provider "
                         f"feed dropped out; showing the last real data from about {age_min} "
                         f"minute(s) ago, for {meta.get('carried_event_count', 0)} game(s). Say so "
                         f"plainly wherever this data is used — do not present it as live.")
        else:
            lines.append(f"- {label} (real market_key: `{real_key}`): UNAVAILABLE — no real data "
                         f"at all right now, live or stale. Do not produce a pick for this stat; "
                         f"say plainly that none is available.")
    # REAL BUG FIX (2026-09-14): confirmed directly that even with the
    # exact market_key instruction already in the Standard, Coeus
    # occasionally still wrote a shortened, plausible-sounding but real,
    # confirmed-wrong key ("player_pass_yards" instead of the real
    # "player_passing_yards") — a real hallucination the validator
    # correctly caught, failing every parlay that used it. This explicit,
    # short, copy-ready list — right where the prompt is read first, not
    # buried inside a large JSON blob — gives Coeus a real, unambiguous
    # reference for exactly these five strings, reducing reliance on
    # recalling them correctly from memory.
    lines.append("")
    lines.append("The five real, exact market_key strings this project ever uses (copy exactly, "
                 "never shorten or paraphrase): " +
                 ", ".join(f"`player_{stat}`" for stat in STAT_LABELS))
    return "\n".join(lines)


def build_real_index(fanduel_data):
    """Real (canonical_event_id, market_key, player) -> real row index,
    built from the current games[]-based fanduel_props schema. Uses the
    exact same real market_key naming convention build_fanduel_props.py
    itself uses (e.g. "player_passing_yards",
    "player_passing_yards_milestones_250_or_more") so this matches
    leg_key()'s expected identity with no changes needed to
    parlay_validator.py."""
    index = {}
    for g in fanduel_data.get("games", []):
        eid = g["canonical_event_id"]
        for mkey in ("h2h", "spreads", "totals"):
            for o in g.get("game_lines", {}).get(mkey, []):
                index[(eid, mkey, o.get("name"))] = {
                    "canonical_event_id": eid, "market_key": mkey,
                    "player": o.get("name"), "price": o.get("price"), "point": o.get("point"),
                }
        for stat, by_player in (g.get("player_props") or {}).items():
            for name, p in by_player.items():
                if p.get("line"):
                    plain_key = f"player_{stat}"
                    index[(eid, plain_key, name)] = {
                        "canonical_event_id": eid, "market_key": plain_key,
                        "player": name, "price": p["line"]["over_price"],
                        "under_price": p["line"]["under_price"], "point": p["line"]["point"],
                    }
                for alt in (p.get("alts") or []):
                    alt_key = f"player_{stat}_milestones_{alt['threshold']}_or_more"
                    index[(eid, alt_key, name)] = {
                        "canonical_event_id": eid, "market_key": alt_key,
                        "player": name, "price": alt.get("over_price") or alt.get("under_price"),
                        "threshold": alt["threshold"],
                    }
        # REAL BUG FIX (2026-09-14): this was hardcoded to the OLD market
        # key from before build_fanduel_props.py switched to the /props
        # endpoint's real, confirmed key for this market. Confirmed
        # directly as the real cause of every parlay containing an
        # anytime-TD leg failing validation tonight — Coeus correctly
        # used "player_anytime_td" (the real key actually present in the
        # FanDuel data it was shown), but this index was still only
        # storing entries under the stale "player_anytime_touchdown_scorer"
        # key, so a completely real, accurate pick looked like a
        # hallucinated one. The pick was never wrong — this lookup table
        # was.
        for p in (g.get("anytime_td") or []):
            index[(eid, "player_anytime_td", p["player"])] = {
                "canonical_event_id": eid, "market_key": "player_anytime_td",
                "player": p["player"], "price": p["price"],
            }
    return index


def extract_json_block(report_text, tag):
    """Pulls one named JSON block (a JSON object, not a bare array —
    the parlay blocks use arrays, these use objects) out of the
    response. Returns None if the tag is missing or the JSON is
    unparseable — a real failure for that specific block, not something
    to silently paper over with an empty result."""
    match = re.search(rf"{tag}\s*\n(\{{.*?\n\}})", report_text, re.DOTALL)
    if not match:
        return None
    try:
        return json.loads(match.group(1))
    except json.JSONDecodeError:
        return None


def extract_parlay_blocks(report_text):
    """Pulls all five PARLAY_N_TEAM JSON blocks out of the response.
    Returns {size: legs_list_or_None} — a missing or unparseable block
    for a given size is a real failure to report for THAT size, not
    something to silently skip past; the other sizes are unaffected."""
    result = {}
    for size in PARLAY_SIZES:
        tag = f"PARLAY_{size}_TEAM"
        match = re.search(rf"{tag}\s*\n(\[.*?\])", report_text, re.DOTALL)
        if not match:
            result[size] = None
            continue
        try:
            result[size] = json.loads(match.group(1))
        except json.JSONDecodeError:
            result[size] = None
    return result


# verify_evidence_check() is now imported from the shared evidence_check_validator.py
# module above — see that module for the real reasoning and the confirmed failure
# case behind it.



def verify_pick(pick, real_by_key, evidence_by_game=None):
    """Cross-checks one proposed pick (player/market_key/canonical_event_id)
    against the real source data — same principle as
    verify_legs_against_source() for parlay legs. Returns (verified_pick,
    is_real) — verified_pick has its price overwritten with the REAL
    price wherever a match is found, in case of a transcription slip;
    is_real is False when the pick doesn't exist in the real data at
    all, which is a real problem (Coeus referenced something not
    actually on the board), not a rounding difference to shrug off.

    ALSO runs verify_evidence_check() against this pick's own real,
    structured evidence_check claims (see that function's own real
    reasoning above) when evidence_by_game is provided — appending any
    real mismatches to verified_pick["evidence_mismatches"] rather than
    silently dropping them, so a downstream caller can decide how to
    treat a factually-wrong reasoning claim (fail the pick, fail the
    whole report, or simply surface it) without this function making
    that call unilaterally."""
    key = leg_key(pick)
    real = real_by_key.get(key)
    if real is None:
        return pick, False
    merged = dict(pick)
    merged["price"] = real.get("price")
    if evidence_by_game is not None:
        ev_mismatches = verify_evidence_check(pick.get("evidence_check"), evidence_by_game)
        if ev_mismatches:
            merged["evidence_mismatches"] = ev_mismatches
    return merged, True


def verify_pick_list(picks, real_by_key, evidence_by_game=None):
    verified, mismatches, evidence_errors = [], [], []
    for p in picks:
        vp, is_real = verify_pick(p, real_by_key, evidence_by_game)
        verified.append(vp)
        if not is_real:
            mismatches.append(p)
        elif vp.get("evidence_mismatches"):
            evidence_errors.append((vp.get("player"), vp["evidence_mismatches"]))
    return verified, mismatches, evidence_errors


def verify_prop_breakdown(raw, real_by_key, evidence_by_game=None):
    if not raw:
        return None, ["Could not parse the PROP_BREAKDOWN JSON block."]
    errors = []
    per_game = []
    for game in (raw.get("per_game") or []):
        picks, mismatches, ev_errors = verify_pick_list(game.get("picks") or [], real_by_key, evidence_by_game)
        if mismatches:
            errors.append(f"{game.get('away')}@{game.get('home')}: {len(mismatches)} pick(s) "
                           f"don't exist in the real FanDuel data.")
        for player, msgs in ev_errors:
            for m in msgs:
                errors.append(f"{game.get('away')}@{game.get('home')} — {player}: {m}")
        per_game.append({"away": game.get("away"), "home": game.get("home"), "picks": picks,
                          "mismatch_count": len(mismatches)})
    per_position = {}
    for pos in SKILL_POSITIONS:
        pick = (raw.get("per_position") or {}).get(pos)
        if not pick:
            continue
        vp, is_real = verify_pick(pick, real_by_key, evidence_by_game)
        if not is_real:
            errors.append(f"{pos} favorite pick doesn't exist in the real FanDuel data.")
        elif vp.get("evidence_mismatches"):
            for m in vp["evidence_mismatches"]:
                errors.append(f"{pos} favorite ({vp.get('player')}): {m}")
        per_position[pos] = vp
    return {"per_game": per_game, "per_position": per_position}, errors


def verify_favorite_ou(raw, real_by_key, evidence_by_game=None):
    if not raw:
        return None, ["Could not parse the FAVORITE_OU JSON block."]
    errors = []
    overs, over_mismatches, over_ev_errors = verify_pick_list(raw.get("overs") or [], real_by_key, evidence_by_game)
    unders, under_mismatches, under_ev_errors = verify_pick_list(raw.get("unders") or [], real_by_key, evidence_by_game)
    if over_mismatches:
        errors.append(f"{len(over_mismatches)} favorite Over(s) don't exist in the real FanDuel data.")
    if under_mismatches:
        errors.append(f"{len(under_mismatches)} favorite Under(s) don't exist in the real FanDuel data.")
    for player, msgs in over_ev_errors + under_ev_errors:
        for m in msgs:
            errors.append(f"{player}: {m}")
    return {"overs": overs, "unders": unders}, errors


def main():
    ap = argparse.ArgumentParser(description="Generate the Props & Parlay Report.")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--max-tokens", type=int, default=48000)
    ap.add_argument("--stake", type=float, default=100,
                     help="Hypothetical per-parlay stake used to compute a real "
                          "payout figure in the validator output. Default $100.")
    ap.add_argument("--dry-run", action="store_true",
                     help="Build and save the exact prompt without calling the API.")
    ap.add_argument("--away", default=None,
                     help="Restrict this run to a single game (requires --home too) — e.g. "
                          "for a real, time-sensitive slate like tonight's TNF game alone, "
                          "rather than paying for and waiting on the whole week's props.")
    ap.add_argument("--home", default=None,
                     help="Paired with --away — see above.")
    ap.add_argument("--games", default=None,
                     help="Restrict this run to a specific, real subset of games — e.g. running "
                          "a 16-game slate as two real batches of 8 to stay well under the API's "
                          "token ceiling. Comma-separated AWAY-HOME pairs, e.g. "
                          "'DET-BUF,CAR-ATL,CIN-HOU'. Mutually exclusive with --away/--home.")
    args = ap.parse_args()
    if (args.away is None) != (args.home is None):
        sys.exit("FATAL: --away and --home must be given together, or not at all.")
    if args.games and (args.away or args.home):
        sys.exit("FATAL: --games can't be combined with --away/--home — use one or the other.")

    games = discover_all_games()
    if not games:
        sys.exit("FATAL: no finished Game Breakdowns found — nothing to build "
                 "a props report from yet.")

    # REAL ADDITION (2026-09-17), per Frank's direct request for a
    # single-game run on a real, time-sensitive night (tonight's TNF):
    # restricts the full, multi-game slate down to exactly one real
    # matchup, before any FanDuel matching, evidence loading, or prompt
    # assembly happens below — everything downstream already treats
    # "games" as the full source of truth for what this run covers, so
    # narrowing it here is sufficient and touches nothing else.
    if args.away and args.home:
        away, home = args.away.strip().upper(), args.home.strip().upper()
        games = [g for g in games if g[1] == away and g[2] == home]
        if not games:
            sys.exit(f"FATAL: no finished Game Breakdown found for {away}@{home} — "
                      f"run generate_game_breakdown.py for that game first.")
        print(f"Restricting this run to {away} @ {home} only, per --away/--home.")

    # REAL ADDITION (2026-09-21), per Frank's direct request for a real
    # way to run a full slate as two (or more) real, separate batches —
    # e.g. to keep each batch comfortably under the real 1,000,000 token
    # ceiling confirmed as a genuine problem at full 16-game scale. Each
    # pair is self-contained (AWAY-HOME together), unlike a pair of
    # separate --away/--home LISTS would be — no risk of the two lists
    # silently drifting out of alignment with each other.
    if args.games:
        wanted_pairs = []
        for pair in args.games.split(","):
            pair = pair.strip()
            if not pair:
                continue
            if "-" not in pair:
                sys.exit(f"FATAL: '{pair}' isn't a real AWAY-HOME pair — expected a format like "
                          f"'DET-BUF'.")
            a, h = pair.split("-", 1)
            wanted_pairs.append((a.strip().upper(), h.strip().upper()))
        games = [g for g in games if (g[1], g[2]) in wanted_pairs]
        found_pairs = {(g[1], g[2]) for g in games}
        missing_pairs = [f"{a}-{h}" for a, h in wanted_pairs if (a, h) not in found_pairs]
        if missing_pairs:
            sys.exit(f"FATAL: no finished Game Breakdown found for: {', '.join(missing_pairs)} — "
                      f"run generate_game_breakdown.py for {'that game' if len(missing_pairs)==1 else 'those games'} first.")
        print(f"Restricting this run to {len(games)} real game(s), per --games: "
              f"{', '.join(f'{g[1]}@{g[2]}' for g in games)}")

    fanduel_data = load_json(FANDUEL_DATA_PATH)
    if fanduel_data is None:
        sys.exit(f"FATAL: {FANDUEL_DATA_PATH} not found. Run build_fanduel_props.py first.")
    coverage = fanduel_data.get("coverage") or {}
    if not any((coverage.get(s) or {}).get("status") != "unavailable" for s in STAT_LABELS):
        sys.exit("FATAL: every real stat family is unavailable (no live or stale data at all) — "
                 "nothing real to build picks from. Re-run build_fanduel_props.py once the "
                 "provider's coverage recovers.")

    # REAL BUG FIX (2026-09-12): fanduel_props/latest.json covers the
    # WHOLE week's slate (14+ games), but this run only has finished
    # Game Breakdowns for a handful of them. Sending every other game's
    # full prop data (every player, every real alt-line rung) for no
    # reason was confirmed directly to balloon a 4-game run to ~308,000
    # input tokens — real, billed cost for data Coeus was never even
    # asked about. Filtered down to only the games actually relevant to
    # this run, before it's built into the prompt OR the verification
    # index — Coeus can't reference a game it was never shown, so
    # restricting both consistently loses nothing real.
    relevant_codes = {(away, home) for _, away, home in games}
    fanduel_data = dict(fanduel_data)
    fanduel_data["games"] = [
        g for g in fanduel_data.get("games", [])
        if (g.get("away_code"), g.get("home_code")) in relevant_codes
    ]
    if len(fanduel_data["games"]) < len(games):
        missing_fd = relevant_codes - {(g.get("away_code"), g.get("home_code")) for g in fanduel_data["games"]}
        print(f"  NOTE: {len(missing_fd)} game(s) with a finished breakdown have no real FanDuel "
              f"data at all right now: {missing_fd}.")

    # REAL BUG FIX (2026-09-14): confirmed directly that most of a real
    # 5-game run's cost was evidence/breakdown text for games with ZERO
    # real FanDuel data — games already played, with no live line left
    # to bet on. Coeus cannot produce a real prop pick for a game with no
    # real prop data, no matter how much evidence it's given for that
    # game — so sending full evidence and breakdown text for those games
    # was pure cost with no possible benefit. Narrowing `games` itself
    # here (not just fanduel_data, which was already filtered above)
    # means this reduction cascades naturally into the evidence loop,
    # the breakdown-text loop, and games_included below, instead of
    # needing a separate fix in each place.
    live_codes = {(g.get("away_code"), g.get("home_code")) for g in fanduel_data["games"]}
    games_with_no_real_props = [(folder, away, home) for folder, away, home in games
                                  if (away, home) not in live_codes]
    games = [(folder, away, home) for folder, away, home in games if (away, home) in live_codes]
    if games_with_no_real_props:
        print(f"  Excluding {len(games_with_no_real_props)} game(s) from evidence/breakdown "
              f"text entirely — no real prop data exists for them right now, so there's "
              f"nothing a pick could be grounded in regardless of how much evidence is sent.")

    # REAL BUG FIX (2026-09-21), per Frank's direct, real catch — see
    # already_played_games() above for the real reasoning. Runs SECOND,
    # after the "no live FanDuel data" filter above, so this only ever
    # narrows further — a game that already failed the first check is
    # already gone and doesn't need checking twice.
    already_played = already_played_games(games)
    if already_played:
        played_set = set(already_played)
        games = [g for g in games if g not in played_set]
        print(f"  Excluding {len(already_played)} game(s) whose real kickoff has already "
              f"passed — {', '.join(f'{a}@{h}' for _, a, h in already_played)} — even though "
              f"FanDuel's own data still had an entry for it, a real, already-played game has "
              f"no real prop to pick regardless.")

    if not games:
        sys.exit("FATAL: none of the finished Game Breakdowns have any real, live FanDuel "
                 "prop data right now — nothing real to build picks from.")

    real_by_key = build_real_index(fanduel_data)

    gb_texts, evidence_texts, folders_used, missing_evidence = [], [], set(), []
    evidence_by_game = {}   # REAL ADDITION (2026-09-21): retains each real
    # game's real, structured evidence (not just its stringified prompt
    # text) so a real rank-verification pass can run AFTER the API call
    # returns — see verify_evidence_check() below for why.
    # REAL threshold (2026-09-21): 4 games is comfortably inside real,
    # confirmed single-game-trim territory (a real 4-game run stays
    # well under the 1,000,000 token ceiling even before this); 5+ is
    # where the real, confirmed 16-game overflow started to matter, so
    # the more aggressive trim engages there rather than waiting until
    # a run is already close to the real hard limit.
    multi_game = len(games) > 4
    for folder, away, home in games:
        gb_path = os.path.join("game_breakdowns", folder, f"{away}_{home}.md")
        gb_texts.append(f"--- {away} @ {home} ---\n{load_text(gb_path)}")
        folders_used.add(folder)
        evidence, ev_path = load_evidence_for_game(away, home)
        if evidence:
            trimmed_evidence = trim_evidence_for_props(evidence, multi_game=multi_game)
            evidence_by_game[(away, home)] = trimmed_evidence
            evidence_texts.append(f"--- {away} @ {home} (from {ev_path}, per-player week-by-week "
                                    f"logs trimmed — real season/career/splits/ceiling totals kept) ---\n" +
                                    json.dumps(trimmed_evidence, separators=(",", ":")))
        else:
            missing_evidence.append(f"{away}_{home}")
    combined_breakdowns = "\n\n".join(gb_texts)
    combined_evidence = "\n\n".join(evidence_texts)
    if missing_evidence:
        print(f"  NOTE: no evidence package found for {len(missing_evidence)} game(s) — "
              f"{', '.join(missing_evidence)} — Coeus will rely on their Game Breakdown text alone.")

    master_prompt = load_text(MASTER_PROMPT_PATH)
    props_standard = load_text(PROPS_STANDARD_PATH)
    system = [
        {"type": "text", "text": master_prompt, "cache_control": {"type": "ephemeral"}},
        {"type": "text", "text": props_standard, "cache_control": {"type": "ephemeral"}},
    ]

    fanduel_json = json.dumps(fanduel_data, separators=(",", ":"))
    user_content = (
        TASK_INSTRUCTION + coverage_summary_text(coverage) +
        "\n\n=== GAME BREAKDOWNS (every finished game on this slate) ===\n" + combined_breakdowns +
        "\n\n=== REAL EVIDENCE PACKAGES (Contextual Stats, Matchup Intelligence, Threat "
        "Intelligence — the same underlying data the Game Breakdowns above were built from) ===\n" +
        combined_evidence +
        "\n\n=== REAL FANDUEL GAME LINES + PROPS DATA (this slate only) ===\n" + fanduel_json
    )

    out_dir = f"props_reports/{list(folders_used)[0]}" if len(folders_used) == 1 else "props_reports/mixed"
    os.makedirs(out_dir, exist_ok=True)
    out_stem = f"{out_dir}/props_parlay_report"
    # REAL BUG FIX (2026-09-21), caught by Frank's own direct question
    # before any real run happened: --games splits a slate into real,
    # separate batches specifically so each stays under the token
    # ceiling — but out_dir/out_stem above only ever key off which real
    # WEEK a game belongs to, not which specific games are actually in
    # THIS run. Every batch from the same real week would resolve to
    # the identical output path, so a second batch would silently
    # overwrite the first real batch's output rather than sitting
    # alongside it. Appends a real, deterministic, readable suffix
    # whenever --games is used, built from the real game count and the
    # first real away team in this batch — distinct batches get
    # distinct real files.
    if args.games:
        out_stem += f"_batch{len(games)}_{games[0][1]}"

    prompt_record = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "model": args.model, "max_tokens": args.max_tokens,
        "games_included": [f"{a}_{h}" for _, a, h in games],
        "fanduel_data_source": FANDUEL_DATA_PATH,
        "evidence_missing_for": missing_evidence,
        "system_char_count": len(master_prompt) + len(props_standard),
        "user_char_count": len(user_content),
    }
    with open(f"{out_stem}_prompt.json", "w") as f:
        json.dump(prompt_record, f, indent=2)

    # REAL BUG FIX (2026-09-21), per Frank's direct, real, confirmed
    # problem: this estimate said ~656,171 tokens for a run that the
    # real API rejected at 1,501,538 real tokens — confirmed directly
    # (a real dry-run measurement) that "chars/4" badly undercounts
    # dense, minified JSON (evidence_texts, fanduel_json): punctuation-
    # and-number-heavy text tokenizes far less efficiently than English
    # prose, which is what "/4" is actually calibrated for. The real,
    # measured ratio from that same real run was ~1.75 chars/token
    # overall; solving separately for the JSON-heavy share (evidence +
    # FanDuel, which dominate at real scale) against the prose share
    # (breakdowns, master prompt, standard) gives ~1.5 chars/token for
    # the JSON portions specifically — used here rather than one single
    # ratio for the whole prompt, so this estimate stays meaningfully
    # accurate whether a run is JSON-heavy (many games) or prose-heavy
    # (few games, mostly breakdown text).
    json_chars = len(combined_evidence) + len(fanduel_json)
    prose_chars = len(master_prompt) + len(props_standard) + len(user_content) - json_chars
    approx_input_tokens = (prose_chars // 4) + (json_chars * 2 // 3)
    print(f"Games included: {len(games)}")
    print(f"Evidence packages found: {len(evidence_texts)} of {len(games)}")
    print(f"Rough input size: ~{approx_input_tokens:,} tokens (estimate only)")

    # REAL ADDITION (2026-09-21): fail fast and cheap, before the real
    # API call, rather than let a genuinely oversized prompt reach the
    # API and get rejected there — same real outcome (the run doesn't
    # happen), but with a clear, specific, actionable message instead
    # of a raw exception. 950,000 leaves real margin below the API's
    # real 1,000,000 hard ceiling — this estimate is accurate to within
    # ~1% against a real, confirmed run, but real margin still matters
    # since output tokens count against some limits too and estimates
    # are still estimates.
    if approx_input_tokens > 950_000 and not args.dry_run:
        sys.exit(f"FATAL: this run's real estimated size (~{approx_input_tokens:,} tokens) is too "
                  f"close to the API's real 1,000,000 token limit to safely attempt. Run fewer "
                  f"games at once (the --away/--home flag limits this to one specific game), or "
                  f"split this slate into two or more separate runs.")



    if args.dry_run:
        with open(f"{out_stem}_prompt_full.txt", "w") as f:
            f.write("=== SYSTEM (Master Prompt) ===\n\n" + master_prompt +
                     "\n\n=== SYSTEM (Props & Parlay Standard) ===\n\n" + props_standard +
                     "\n\n=== USER MESSAGE ===\n\n" + user_content)
        print(f"\nDRY RUN — no API call made. Prompt written to {out_stem}_prompt_full.txt")
        return

    try:
        import anthropic
    except ImportError:
        sys.exit("FATAL: pip install anthropic --break-system-packages")
    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("FATAL: ANTHROPIC_API_KEY not set.")

    client = anthropic.Anthropic()
    print(f"\nCalling {args.model} (streaming)...\n")
    with client.messages.stream(
        model=args.model, max_tokens=args.max_tokens, system=system,
        messages=[{"role": "user", "content": user_content}],
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)
        response = stream.get_final_message()
    print()

    report_text = "".join(block.text for block in response.content if block.type == "text")
    print(f"stop_reason: {response.stop_reason}")
    if response.stop_reason == "max_tokens":
        print("WARNING: hit the max_tokens ceiling before finishing — INCOMPLETE.")
    if not report_text.strip():
        sys.exit("FATAL: empty response, nothing written.")

    with open(f"{out_stem}.md", "w") as f:
        f.write(report_text)
    usage = response.usage
    prompt_record["usage"] = {"input_tokens": usage.input_tokens, "output_tokens": usage.output_tokens}
    with open(f"{out_stem}_prompt.json", "w") as f:
        json.dump(prompt_record, f, indent=2)
    print(f"\nWrote {out_stem}.md — {usage.input_tokens:,} input / {usage.output_tokens:,} output tokens")

    print("\n" + "=" * 60)

    prop_breakdown_raw = extract_json_block(report_text, "PROP_BREAKDOWN")
    prop_breakdown, pb_errors = verify_prop_breakdown(prop_breakdown_raw, real_by_key, evidence_by_game)
    print("\nPROP BREAKDOWN VALIDATION:")
    if pb_errors:
        for e in pb_errors:
            print(f"  ISSUE: {e}")
    else:
        print("  PASSED — every pick verified against real FanDuel data.")

    favorite_ou_raw = extract_json_block(report_text, "FAVORITE_OU")
    favorite_ou, fou_errors = verify_favorite_ou(favorite_ou_raw, real_by_key, evidence_by_game)
    print("\nFAVORITE OVERS/UNDERS VALIDATION:")
    if fou_errors:
        for e in fou_errors:
            print(f"  ISSUE: {e}")
    else:
        print("  PASSED — every pick verified against real FanDuel data.")

    parlays = extract_parlay_blocks(report_text)
    parlay_results = {}
    for size in PARLAY_SIZES:
        legs = parlays[size]
        print(f"\n{size}-TEAM PARLAY VALIDATION:")
        if legs is None:
            print(f"  FAILED — could not find or parse a PARLAY_{size}_TEAM JSON "
                  f"block. This parlay has NOT been checked. Do not trust it.")
            parlay_results[size] = {"valid": False, "errors": ["Could not parse this parlay's JSON block."],
                                     "warnings": [], "result": None, "legs": None, "mismatches": []}
            continue
        verified_legs, mismatches = verify_legs_against_source(legs, real_by_key)
        if mismatches:
            print(f"  {len(mismatches)} leg(s) do NOT exist in the real FanDuel data "
                  f"provided — Coeus referenced something not actually on the board:")
            for m in mismatches:
                print(f"    - {m}")
        is_valid, errors, warnings, result = validate_parlay(
            verified_legs, expected_size=size, stake=args.stake)
        # REAL ADDITION (2026-09-21): same real evidence_check verification
        # as every other pick type above — a parlay leg's reasoning is
        # just as capable of misstating a real rank as any other pick's,
        # and a leg with a real, confirmed-wrong evidence claim fails the
        # whole parlay here, the same way a leg with the wrong price does.
        for leg in verified_legs:
            leg_ev_mismatches = verify_evidence_check(leg.get("evidence_check"), evidence_by_game)
            if leg_ev_mismatches:
                for m in leg_ev_mismatches:
                    errors.append(f"{leg.get('player')}: {m}")
                is_valid = False
        passed = is_valid and not mismatches
        if passed:
            print(f"  PASSED — {result['legs']} real legs, combined odds "
                  f"{result['combined_decimal']} (American {result['combined_american']:+d}), "
                  f"${args.stake:.0f} stake -> ${result['payout']:.2f} payout.")
        else:
            print(f"  FAILED:")
            for e in errors:
                print(f"    - {e}")
        for w in warnings:
            print(f"  NOTE: {w}")
        parlay_results[size] = {
            "valid": passed, "errors": errors, "warnings": warnings,
            "result": result, "legs": verified_legs,
            "mismatches": [m for m in mismatches],
        }
    print("=" * 60)

    report_json = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "games_included": [f"{a}_{h}" for _, a, h in games],
        "coverage": coverage,
        "stake_used_for_payout_examples": args.stake,
        "markdown": report_text,
        "prop_breakdown": prop_breakdown, "prop_breakdown_errors": pb_errors,
        "favorite_ou": favorite_ou, "favorite_ou_errors": fou_errors,
        "parlays": {str(size): parlay_results[size] for size in PARLAY_SIZES},
    }
    with open(f"{out_stem}.json", "w") as f:
        json.dump(report_json, f)
    print(f"Wrote {out_stem}.json (structured, for the Prop Center page)")

    # REAL ADDITION (2026-09-21), per Frank's direct request to have
    # batch reports actually show up on the site: a browser's fetch()
    # can only check whether one SPECIFIC, already-known filename
    # exists — it can't list a folder's real contents. So Prop Center
    # needs a real, explicit record of which real batch files exist for
    # a given week, the same real reason game_breakdowns/wkNN/
    # manifest.json already exists for Game Breakdowns. Keyed by this
    # run's real out_stem filename, so re-running the SAME real batch
    # (same games, same games[0] away team) updates its own real entry
    # rather than accumulating duplicates — genuinely different batches
    # (different games) get their own real, separate entries.
    manifest_path = f"{out_dir}/manifest.json"
    manifest = load_json(manifest_path) or {"batches": {}}
    report_filename = os.path.basename(f"{out_stem}.json")
    manifest["batches"][report_filename] = {
        "games": [f"{a}_{h}" for _, a, h in games],
        "generated_at": report_json["generated_at"],
    }
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)
    print(f"Wrote {manifest_path} — {len(manifest['batches'])} real batch(es) on record for this week")

    os.makedirs("props_reports", exist_ok=True)
    with open("props_reports/latest.json", "w") as f:
        json.dump({
            "generated_at": report_json["generated_at"],
            "report_path": f"{out_stem}.json",
        }, f)
    print(f"Wrote props_reports/latest.json — points to {out_stem}.json")


if __name__ == "__main__":
    main()
