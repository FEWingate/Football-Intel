"""
BUILD_FANDUEL_PROPS.PY
========================
Fetches real game lines (h2h/spreads/totals + alternates) and player
props (passing/rushing/receiving yards, receptions, anytime TD — both
the plain line where FanDuel has one, and every real alt-line/milestone
rung), filtered to FanDuel specifically, from parlay-api.com. Writes
one normalized JSON, grouped by real game then by real stat concept,
that both generate_props_report.py and prop_center.html read from —
same "one source of truth" pattern as build_dfs.py for DraftKings data.

REQUIRES: export PARLAY_API_KEY=... in ~/.bashrc (never commit it)

REAL BUG FIX (2026-09-12): the original version of this script used
parlay-api.com's flat /props extension endpoint. Two real, confirmed
problems with that endpoint, found by testing against real live data,
not assumed from docs:
  1. Prices came back in American format (-115, -113, +104...) —
     inconsistent with every other price in this whole pipeline, which
     is decimal (confirmed for /odds). A decimal price can never be
     negative, so this wasn't ambiguous once checked directly.
  2. A single flat call covered only 3 of 12+ real games in testing —
     nowhere close to comprehensive weekly coverage. Real FanDuel
     single-line passing/rushing yards props (confirmed live on
     FanDuel's own site via screenshot) were WRONGLY concluded to not
     exist, purely because the incomplete sample didn't happen to
     include the game being checked.
This version uses the standard /odds endpoint instead, passing player
prop market keys directly in the markets param — a real, confirmed-
working usage pattern for this API (verified via a real SDK's
documented usage, then independently confirmed with a live test call:
13 of 14 real events returned real FanDuel player-prop data, all in
clean decimal, for 28 credits covering 5 markets). Same endpoint
that already reliably covers every game for h2h/spreads/totals, same
clean pricing — no separate price-format handling needed anywhere
downstream.

REAL MARKET-KEY MAPPING (confirmed live 2026-09-12, not assumed):
FanDuel currently has a real plain Over/Under line for passing yards,
rushing yards, receiving yards, and receptions — the "no single line,
only ladders" conclusion in the original OPEN ISSUES was wrong, caused
by the flat-endpoint's incomplete coverage, not a real gap in what
FanDuel offers. Every one of the four stats ALSO has a real alt-line
ladder alongside its plain line. Anytime TD (player_anytime_touchdown_
scorer) is real but different in shape: a "Yes" side per player with a
real price, no "Under"/"No" side — you can't bet against a player
scoring, only for it.

Real credit cost: reported directly from x-requests-used after every
run, not estimated — do not assume last run's number still holds.

USAGE:
    python3 build_fanduel_props.py
"""

import glob
import copy
import json
import os
import re
import sys
import time
from datetime import datetime, timezone

import requests

PARLAY_API_KEY = os.environ.get("PARLAY_API_KEY")
BASE_URL = "https://api.parlay-api.com/v1"
NFL_SPORT_KEY = "americanfootball_nfl"
AUTH_HEADER = "X-API-Key"
OUTPUT_PATH = "fanduel_props/latest.json"
STALE_MAX_AGE_SECONDS = 6 * 60 * 60

# Standard, stable NFL team name/code mapping — used only to cross-
# reference parlay-api.com's full team names against this project's
# real current-week slate (evidence_bootstrap/*.json filenames), not
# used anywhere else in this pipeline.
TEAM_NAME_TO_CODE = {
    "Arizona Cardinals": "ARI", "Atlanta Falcons": "ATL", "Baltimore Ravens": "BAL",
    "Buffalo Bills": "BUF", "Carolina Panthers": "CAR", "Chicago Bears": "CHI",
    "Cincinnati Bengals": "CIN", "Cleveland Browns": "CLE", "Dallas Cowboys": "DAL",
    "Denver Broncos": "DEN", "Detroit Lions": "DET", "Green Bay Packers": "GB",
    "Houston Texans": "HOU", "Indianapolis Colts": "IND", "Jacksonville Jaguars": "JAX",
    "Kansas City Chiefs": "KC", "Las Vegas Raiders": "LV", "Los Angeles Chargers": "LAC",
    "Los Angeles Rams": "LAR", "Miami Dolphins": "MIA", "Minnesota Vikings": "MIN",
    "New England Patriots": "NE", "New Orleans Saints": "NO", "New York Giants": "NYG",
    "New York Jets": "NYJ", "Philadelphia Eagles": "PHI", "Pittsburgh Steelers": "PIT",
    "San Francisco 49ers": "SF", "Seattle Seahawks": "SEA", "Tampa Bay Buccaneers": "TB",
    "Tennessee Titans": "TEN", "Washington Commanders": "WAS",
}


def current_week_game_codes():
    """Real (away, home) code pairs for THIS week's slate, read directly
    from evidence_bootstrap/*.json filenames — the same real files this
    project already uses as the source of truth for "what's this week's
    schedule", rather than trusting whatever date range parlay-api.com's
    /odds endpoint happens to return (confirmed real gap: that endpoint
    returned 27 games spanning two full weeks, not just this one)."""
    pairs = set()
    for path in glob.glob("evidence_bootstrap/*.json"):
        stem = os.path.splitext(os.path.basename(path))[0]
        if stem == "manifest":
            continue
        parts = stem.split("_")
        if len(parts) == 2:
            pairs.add((parts[0], parts[1]))
    return pairs

GAME_LINE_MARKETS = ["h2h", "spreads", "totals", "alternate_spreads", "alternate_totals"]

# Real, confirmed-existing FanDuel milestone thresholds per stat — read
# directly off a live /props taxonomy pull (inspect_parlay_props.py),
# not guessed at a round-number pattern. A book can add/drop a rung at
# any time; this list reflects what was real as of 2026-09-12.
PASSING_YARDS_THRESHOLDS = (150, 175, 200, 225, 250, 275, 300, 325, 350, 400)
RUSHING_YARDS_THRESHOLDS = (10, 15, 20, 25, 30, 40, 50, 60, 70, 75, 80, 90, 100, 110)
RECEIVING_YARDS_THRESHOLDS = (10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100, 110, 125, 150)
RECEPTIONS_THRESHOLDS = (2, 3, 4, 5, 6, 7, 8, 9, 10)

PLAIN_KEY_TO_STAT = {
    "player_passing_yards": "passing_yards",
    "player_rushing_yards": "rushing_yards",
    "player_receiving_yards": "receiving_yards",
    "player_receptions": "receptions",
}
ALT_LISTS = {
    "passing_yards": [f"player_passing_yards_milestones_{n}_or_more" for n in PASSING_YARDS_THRESHOLDS],
    "rushing_yards": [f"player_rushing_yards_milestones_{n}_or_more" for n in RUSHING_YARDS_THRESHOLDS],
    "receiving_yards": [f"player_receiving_yards_milestones_{n}_or_more" for n in RECEIVING_YARDS_THRESHOLDS],
    "receptions": [f"player_receptions_milestones_{n}_or_more" for n in RECEPTIONS_THRESHOLDS],
}
ANYTIME_TD_KEY = "player_anytime_touchdown_scorer"

PLAYER_PROP_MARKETS = (
    list(PLAIN_KEY_TO_STAT.keys())
    + [k for alts in ALT_LISTS.values() for k in alts]
    + [ANYTIME_TD_KEY]
)


def classify_market(key):
    """Returns (stat, kind, threshold) for a real market_key. kind is
    'line' (the plain O/U), 'alt' (one rung of the milestone ladder),
    'anytime_td' (yes-only), or (None, None, None) if this key isn't
    one this script asked for (shouldn't happen, but never silently
    misclassify an unexpected key as something it isn't)."""
    if key == ANYTIME_TD_KEY:
        return ("anytime_td", "anytime_td", None)
    if key in PLAIN_KEY_TO_STAT:
        return (PLAIN_KEY_TO_STAT[key], "line", None)
    for stat, alts in ALT_LISTS.items():
        if key in alts:
            threshold = int(key.split("_")[-3])
            return (stat, "alt", threshold)
    return (None, None, None)


def _get(path, params=None):
    if not PARLAY_API_KEY:
        sys.exit("FATAL: PARLAY_API_KEY not set. Add `export PARLAY_API_KEY=...` "
                 "to ~/.bashrc, then `source ~/.bashrc`.")
    url = f"{BASE_URL}/{path}"
    for attempt in range(3):
        resp = requests.get(
            url,
            headers={AUTH_HEADER: PARLAY_API_KEY},
            params=params or {},
            timeout=45,
        )
        if resp.status_code == 200:
            break
        if resp.status_code == 429 or 500 <= resp.status_code < 600:
            delay = min(int(resp.headers.get("Retry-After", 2 ** attempt)), 30)
            print(f"  WARNING: {path} returned HTTP {resp.status_code}; retrying in {delay}s")
            time.sleep(delay)
            continue
        sys.exit(f"FATAL: {url} returned HTTP {resp.status_code}: {resp.text[:300]}")
    else:
        sys.exit(f"FATAL: {url} did not recover after three attempts: {resp.text[:300]}")
    print(
        f"  {path} -> HTTP 200 (last-cost={resp.headers.get('x-requests-last')}, "
        f"remaining={resp.headers.get('x-requests-remaining')}, "
        f"served={resp.headers.get('x-markets-served')}, "
        f"unservable={resp.headers.get('x-markets-unservable')})"
    )
    return resp.json()


def fetch_odds(markets):
    """Real /odds call for the given market keys, filtered to FanDuel.
    Same endpoint and shape for game lines and player props — the only
    difference is which market keys get requested."""
    data = _get(
        f"sports/{NFL_SPORT_KEY}/odds",
        {
            "regions": "us",
            "markets": ",".join(markets),
            "oddsFormat": "decimal",
        },
    )
    events = []
    for event in data:
        fd = next((bk for bk in event.get("bookmakers", []) if bk.get("key") == "fanduel"), None)
        if not fd:
            continue
        events.append({
            "canonical_event_id": event.get("canonical_event_id") or event.get("id"),
            "away_team": event.get("away_team"), "home_team": event.get("home_team"),
            "commence_time": event.get("commence_time"),
            "markets": {mkt.get("key"): mkt.get("outcomes", []) for mkt in fd.get("markets", [])},
        })
    return events


def reshape_player_props(prop_events):
    """Regroups the raw per-market-key event data into one entry per
    real player per stat, with their plain line (if FanDuel has one)
    and their full real alt-line ladder together — this is the shape
    both the report generator and the HTML page actually want, not the
    raw one-array-per-market-key shape the API returns."""
    # players[event_id][stat][player_name] = {"line": {...} or None, "alts": [...]}
    players = {}
    anytime_td = {}

    for event in prop_events:
        eid = event["canonical_event_id"]
        players.setdefault(eid, {stat: {} for stat in PLAIN_KEY_TO_STAT.values()})
        anytime_td.setdefault(eid, [])

        for market_key, outcomes in event["markets"].items():
            stat, kind, threshold = classify_market(market_key)
            if stat is None:
                continue

            if kind == "anytime_td":
                for o in outcomes:
                    name = o.get("description") or o.get("name")
                    if not name or name == "Defense":
                        continue
                    anytime_td[eid].append({"player": name, "price": o.get("price")})
                continue

            # Outcomes come as separate rows, one per side per player.
            # Two real, confirmed naming conventions exist in the actual
            # data (2026-09-12) — most use "Over X"/"Under X", but some
            # milestone markets use a bare "Yes" (semantically the same
            # as "Over" — "yes, they hit this threshold or more"), the
            # same way anytime_touchdown_scorer's "Yes" already works.
            # REAL BUG FIX: the original version only recognized names
            # starting with "Over" and silently misfiled every "Yes"
            # outcome as the Under side, dropping its real price and
            # leaving Over blank — confirmed directly against real data
            # (Jayden Daniels' passing_yards 250+ milestone) before
            # fixing this, not assumed.
            # REAL BUG FIX (2026-09-12): every player's real line was
            # being overwritten with outcomes[0]'s point value — the
            # FIRST row in the whole market's list, regardless of which
            # player the loop was actually on. Confirmed directly: every
            # QB in a game showed the identical passing-yards line, and
            # rushing yards showed QBs and RBs sharing one line, which
            # is not realistic sportsbook data. Receptions looked fine
            # by coincidence — 1.5 is naturally a common real threshold
            # across many real receivers — but the same bug was silently
            # there too, just masked by real data happening to agree.
            # Each player's own point value is now captured alongside
            # their own price in the same pass, not borrowed from
            # whichever row happened to be first in the list.
            by_player = {}
            for o in outcomes:
                name = o.get("description")
                if not name:
                    continue
                by_player.setdefault(name, {"over": None, "under": None, "point": o.get("point")})
                label = (o.get("name") or "").lower()
                side = "over" if label.startswith("over") or label == "yes" else "under"
                by_player[name][side] = o.get("price")

            for name, sides in by_player.items():
                bucket = players[eid][stat].setdefault(name, {"line": None, "alts": []})
                if kind == "line":
                    bucket["line"] = {"point": sides["point"],
                                       "over_price": sides["over"], "under_price": sides["under"]}
                elif kind == "alt":
                    bucket["alts"].append({"threshold": threshold, "over_price": sides["over"],
                                            "under_price": sides["under"]})

    # Sort each player's alt ladder by threshold so consumers don't have to.
    for eid, stats in players.items():
        for stat, by_player in stats.items():
            for name, bucket in by_player.items():
                bucket["alts"].sort(key=lambda a: a["threshold"])

    return players, anytime_td


def parse_timestamp(value):
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (TypeError, ValueError):
        return None


def family_value(game, family):
    if family == "anytime_td":
        return game.get("anytime_td") or []
    return (game.get("player_props") or {}).get(family) or {}


def set_family_value(game, family, value):
    if family == "anytime_td":
        game["anytime_td"] = copy.deepcopy(value)
    else:
        game.setdefault("player_props", {})[family] = copy.deepcopy(value)


def protect_against_coverage_collapse(games, previous_payload, generated_at):
    """Carry recent same-game data only after a catastrophic family drop.

    This is intentionally not a silent whole-file fallback. Each family gets
    explicit freshness metadata, and carried data expires six hours after the
    original successful fetch.
    """
    families = list(PLAIN_KEY_TO_STAT.values()) + ["anytime_td"]
    previous_games = {
        game.get("canonical_event_id"): game
        for game in (previous_payload or {}).get("games", [])
        if game.get("canonical_event_id")
    }
    previous_coverage = (previous_payload or {}).get("coverage", {})
    now = parse_timestamp(generated_at) or datetime.now(timezone.utc)
    coverage = {}
    warnings = []

    for family in families:
        current_count = sum(bool(family_value(game, family)) for game in games)
        matching_previous = [
            previous_games.get(game.get("canonical_event_id")) for game in games
        ]
        previous_count = sum(
            bool(family_value(game, family)) for game in matching_previous if game
        )
        prior_meta = previous_coverage.get(family, {})
        source_generated_at = prior_meta.get("source_generated_at") or (
            previous_payload or {}
        ).get("generated_at")
        source_time = parse_timestamp(source_generated_at)
        source_age = (now - source_time).total_seconds() if source_time else None
        collapsed = previous_count >= 2 and current_count * 2 < previous_count
        recent_enough = source_age is not None and 0 <= source_age <= STALE_MAX_AGE_SECONDS
        carried_count = 0

        if collapsed and recent_enough:
            for game in games:
                if family_value(game, family):
                    continue
                previous_game = previous_games.get(game.get("canonical_event_id"))
                previous_value = family_value(previous_game, family) if previous_game else None
                if previous_value:
                    set_family_value(game, family, previous_value)
                    carried_count += 1

        displayed_count = sum(bool(family_value(game, family)) for game in games)
        if carried_count:
            status = "stale_last_known_good"
            warnings.append(
                f"{family}: provider coverage fell from {previous_count} to {current_count} "
                f"same-game events; carrying {carried_count} recent event(s) from "
                f"{source_generated_at}."
            )
        elif current_count:
            status = "current"
            source_generated_at = generated_at
            source_age = 0
        else:
            status = "unavailable"
            source_generated_at = None
            source_age = None

        coverage[family] = {
            "status": status,
            "current_event_count": current_count,
            "displayed_event_count": displayed_count,
            "previous_event_count": previous_count,
            "carried_event_count": carried_count,
            "source_generated_at": source_generated_at,
            "source_age_seconds": int(source_age) if source_age is not None else None,
        }

    return coverage, warnings


def write_json_atomic(payload, path):
    temp_path = f"{path}.tmp"
    with open(temp_path, "w", encoding="utf-8") as output:
        json.dump(payload, output)
        output.flush()
        os.fsync(output.fileno())
    os.replace(temp_path, path)


def main():
    generated_at = datetime.now(timezone.utc).isoformat()
    print(f"Building FanDuel game lines + player props - {generated_at}")

    previous_payload = None
    if os.path.exists(OUTPUT_PATH):
        try:
            with open(OUTPUT_PATH, encoding="utf-8") as previous_file:
                previous_payload = json.load(previous_file)
        except (OSError, json.JSONDecodeError) as error:
            print(f"  WARNING: could not read prior snapshot for coverage protection: {error}")

    print("Fetching game lines (h2h/spreads/totals/alternates)...")
    line_events = fetch_odds(GAME_LINE_MARKETS)
    seen_markets = set()
    for e in line_events:
        seen_markets |= set(e["markets"].keys())
    for expected in GAME_LINE_MARKETS:
        if expected not in seen_markets:
            print(f"  WARNING: FanDuel returned NO '{expected}' this run. Confirmed a real, "
                  f"unexplained gap for 'spreads' specifically as of 2026-09-05 — if that's "
                  f"still true this close to kickoff, that's now a real, not just early-week, gap.")

    # Passing remains isolated so its coverage and credit cost are observable
    # independently. A 2026-09-12 investigation disproved the earlier belief
    # that isolation itself fixes missing data: the isolated call later stayed
    # empty across both API hostnames, with and without a FanDuel filter, and
    # for a single event. Coverage protection below is therefore the safeguard;
    # this split is diagnostic, not a claimed upstream workaround.
    passing_yards_markets = [k for k in PLAYER_PROP_MARKETS
                              if k == "player_passing_yards" or k.startswith("player_passing_yards_milestones_")]
    other_prop_markets = [k for k in PLAYER_PROP_MARKETS if k not in passing_yards_markets]

    print("Fetching passing yards props (isolated — confirmed dropped when combined with other markets)...")
    passing_events = fetch_odds(passing_yards_markets)

    print("Fetching remaining player props (rushing/receiving/receptions/anytime TD + alts)...")
    other_events = fetch_odds(other_prop_markets)

    # Merge the two fetches back together by event, since both cover the
    # same real games — just different market subsets each.
    merged_by_id = {}
    for e in passing_events + other_events:
        eid = e["canonical_event_id"]
        if eid not in merged_by_id:
            merged_by_id[eid] = e
        else:
            merged_by_id[eid]["markets"].update(e["markets"])
    prop_events = list(merged_by_id.values())

    players, anytime_td = reshape_player_props(prop_events)

    games = []
    week_codes = current_week_game_codes()
    excluded = 0
    for e in line_events:
        eid = e["canonical_event_id"]
        away_code = TEAM_NAME_TO_CODE.get(e["away_team"])
        home_code = TEAM_NAME_TO_CODE.get(e["home_team"])
        if (away_code, home_code) not in week_codes:
            excluded += 1
            continue
        games.append({
            "canonical_event_id": eid, "away_team": e["away_team"], "home_team": e["home_team"],
            "away_code": away_code, "home_code": home_code,
            "commence_time": e["commence_time"],
            "game_lines": {k: e["markets"].get(k, []) for k in GAME_LINE_MARKETS},
            "player_props": players.get(eid, {stat: {} for stat in PLAIN_KEY_TO_STAT.values()}),
            "anytime_td": anytime_td.get(eid, []),
        })
    if excluded:
        print(f"  Excluded {excluded} real event(s) outside this week's slate (confirmed against "
              f"evidence_bootstrap/*.json) — a later week's lines had already opened for betting.")
    if len(games) != len(week_codes):
        missing = week_codes - {(TEAM_NAME_TO_CODE.get(g["away_team"]), TEAM_NAME_TO_CODE.get(g["home_team"]))
                                 for g in games}
        print(f"  {len(week_codes) - len(games)} of this week's {len(week_codes)} real game(s) have no live "
              f"betting line right now: {missing}. Expected, not a bug, for any game that's already been "
              f"played — sportsbooks correctly pull a line once there's nothing left to bet on. Worth a "
              f"second look only if one of these hasn't actually kicked off yet.")

    coverage, warnings = protect_against_coverage_collapse(
        games, previous_payload, generated_at
    )
    for warning in warnings:
        print(f"  WARNING: {warning}")

    os.makedirs("fanduel_props", exist_ok=True)
    payload = {
        "generated_at": generated_at,
        "bookmaker": "fanduel",
        "coverage": coverage,
        "warnings": warnings,
        "games": games,
    }
    path = OUTPUT_PATH
    write_json_atomic(payload, path)

    real_players_count = sum(
        len(by_player) for g in games for by_player in g["player_props"].values()
    )
    real_td_count = sum(len(g["anytime_td"]) for g in games)
    print(f"Wrote {path} — {len(games)} games, {real_players_count} real player-stat entries "
          f"(line + alts combined), {real_td_count} real anytime-TD entries")


if __name__ == "__main__":
    main()
