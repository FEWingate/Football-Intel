"""
BUILD_FANDUEL_PROPS.PY
========================
Fetches real game lines (h2h/spreads/totals + alternates, via /odds) and
player props (passing/rushing/receiving yards, receptions, anytime TD —
both the plain line where FanDuel has one, and every real alt-line/
milestone rung, via /props), filtered to FanDuel specifically, from
parlay-api.com. Writes one normalized JSON, grouped by real game then by
real stat concept, that both generate_props_report.py and
prop_center.html read from — same "one source of truth" pattern as
build_dfs.py for DraftKings data.

REQUIRES: export PARLAY_API_KEY=... in ~/.bashrc (never commit it)

REAL HISTORY, for whoever reads this next — two prior approaches were
tried and replaced, each for a real, confirmed reason, not a guess:
  1. The original version used the flat /props endpoint with no markets
     param. Confirmed problems: American-format prices (inconsistent
     with the rest of this pipeline) and incomplete per-game coverage
     (a single call covered only 3 of 12+ real games).
  2. The next version moved player props onto /odds instead, passing
     prop market keys directly. This worked for a while, but a real
     support ticket to parlay-api.com (2026-09-13) revealed why passing
     yards specifically kept going empty: /odds only shows prop lines
     that moved in the last 10 minutes. A real, unchanged line falls
     out of that view entirely — it isn't a provider outage, it's the
     wrong endpoint for this use case.
  3. THIS version (current): player props are back on /props, but
     called correctly per parlay-api.com support's direct guidance —
     explicit markets=, oddsFormat=decimal, and a real limit, with the
     real market-key list discovered fresh every run via the free (0-
     credit) /props/markets endpoint rather than trusted from a
     hardcoded snapshot. Confirmed flat 3 credits per /props call,
     regardless of market count — cheaper and more reliable than either
     prior approach. Game lines stay on /odds, unaffected by any of
     this — that side was never broken.

REAL, CONFIRMED QUIRKS OF /props SPECIFICALLY (2026-09-13, not assumed):
  - Market-key spellings for the same real stat differ by book (e.g.
    receiving yards: player_receiving_yards for most books,
    player_receiving_yds for pick6). Only FanDuel's real spellings
    matter here, discovered fresh via /props/markets each run.
  - The key requested and the key a response row is labeled with can
    differ: requesting player_anytime_touchdown_scorer via /props
    returns FanDuel rows labeled player_anytime_td — a real, confirmed
    quirk of this endpoint specifically, not true of /odds, which does
    use player_anytime_touchdown_scorer for the same real market.
  - limit=20000 is rejected outright (HTTP 422); 5000 is a real,
    confirmed-safe value — direct testing showed FanDuel's real
    coverage was identical at limit=5000 and limit=10000 for a 5-market
    request, meaning 5000 is enough to avoid other books' volume
    crowding FanDuel's rows out, at least at the per-stat-family
    request size this script uses.

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
BASE_URL = "https://parlay-api.com/v1"
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

# REAL REWRITE (2026-09-13): per direct guidance from parlay-api.com's own
# support team (replying to a real support ticket about the passing-yards
# outage), the player-props side of this script was rebuilt around their
# actual recommended usage, confirmed against real live tests before
# shipping:
#   1. Player props belong on the dedicated /props endpoint, not /odds.
#      /odds only shows lines that moved in the last 10 minutes — a real,
#      unchanged line can fall out of that view entirely, which is what
#      actually caused the passing-yards "outage" this whole pipeline
#      built a stale-data fallback around. /props looks back 60 minutes
#      and returns the full real board.
#   2. /props must be called with an explicit, real markets= list — an
#      earlier version of this project called it with no markets param
#      at all, which support confirmed returns "a mixed page across every
#      prop market", explaining the incomplete per-game coverage found
#      then.
#   3. Real cost is a FLAT 3 credits per /props call, confirmed directly —
#      NOT scaled by market count the way /odds is. The old approach of
#      combining everything into one /odds call at ~53 credits was
#      needlessly expensive as well as unreliable.
#   4. Real market-key spellings are confirmed to DIFFER by book (e.g.
#      receiving yards: player_receiving_yards for most books,
#      player_receiving_yds for pick6, player_rec_yds for some others) —
#      and, confirmed by direct testing, can also differ between what
#      /props accepts as a request param and what it labels the response
#      row with (anytime TD: requesting player_anytime_touchdown_scorer
#      via /props actually returns rows labeled player_anytime_td for
#      FanDuel — a real, confirmed quirk of this specific endpoint, not
#      true of /odds, which does use player_anytime_touchdown_scorer).
#   5. The real, current list of market keys — including which alt-line
#      milestone rungs actually exist right now — is discovered fresh
#      every run via the free (0-credit) /props/markets endpoint, rather
#      than a hardcoded threshold list. Confirmed necessary: rushing
#      yards' 75-or-more rung was present in one real check and absent
#      from another the same day — a fixed list would silently go stale.
STAT_FAMILIES = ["passing_yards", "rushing_yards", "receiving_yards", "receptions"]
# Confirmed via direct testing against the real /props endpoint — this is
# the actual key FanDuel's rows come back labeled with there, DIFFERENT
# from the player_anytime_touchdown_scorer key /odds uses for the same
# real market. Using the wrong one here silently returns zero rows.
ANYTIME_TD_KEY = "player_anytime_td"
# Real cap confirmed by direct testing: limit=20000 is rejected outright
# (HTTP 422); limit=5000 vs 10000 returned identical real FanDuel coverage
# for a 5-market combined request, meaning 5000 already captures FanDuel's
# real data for a single stat family's plain+alt markets without other
# books' volume crowding it out — confirmed, not assumed.
PROPS_ROW_LIMIT = 5000


def discover_fanduel_markets():
    """Real, current FanDuel market keys per stat family, discovered fresh
    via the free /props/markets endpoint (0 credits) — confirmed real
    market data, not a hardcoded snapshot that can silently go stale.
    Returns {stat: {"plain": key_or_None, "alts": [(threshold, key), ...]}}."""
    data = _get(f"sports/{NFL_SPORT_KEY}/props/markets")
    result = {stat: {"plain": None, "alts": []} for stat in STAT_FAMILIES}
    for m in data:
        if not isinstance(m, dict) or "fanduel" not in (m.get("bookmakers") or []):
            continue
        key = m.get("key") or ""
        for stat in STAT_FAMILIES:
            if key == f"player_{stat}":
                result[stat]["plain"] = key
            elif key.startswith(f"player_{stat}_milestones_") and key.endswith("_or_more"):
                try:
                    threshold = int(key.split("_")[-3])
                except (ValueError, IndexError):
                    continue
                result[stat]["alts"].append((threshold, key))
    for stat in STAT_FAMILIES:
        result[stat]["alts"].sort()
    return result


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


def fetch_props(markets):
    """Real /props call for the given market keys, filtered to FanDuel.
    Confirmed flat 3-credit cost regardless of how many market keys are
    requested (per parlay-api.com support, 2026-09-13) — unlike /odds,
    where cost scales with market count. Returns a flat list of real
    rows, one per real player per real market — NOT the nested
    event/outcomes shape /odds uses. Each row already carries its own
    player, line, over_price, and under_price together, confirmed
    directly against real data, so no Over/Under pairing is needed here
    the way it was for the old /odds-based approach."""
    data = _get(f"sports/{NFL_SPORT_KEY}/props",
                {"markets": ",".join(markets), "oddsFormat": "decimal", "limit": PROPS_ROW_LIMIT})
    return [r for r in data if isinstance(r, dict) and r.get("bookmaker") == "fanduel"]


def reshape_props_rows(rows, market_to_stat_kind):
    """Regroups real flat /props rows into one entry per real player per
    stat, with their plain line (if FanDuel has one) and their full real
    alt-line ladder together — the same output shape reshape_player_props()
    used to produce, so nothing downstream (coverage protection, the
    report generator, prop_center.html) needs to change.
    market_to_stat_kind: {market_key: (stat, kind, threshold_or_None)},
    built from discover_fanduel_markets()."""
    players = {}
    anytime_td = {}
    for row in rows:
        eid = row.get("canonical_event_id")
        name = row.get("player")
        market_key = row.get("market_key")
        if not eid or not name or not market_key or name == "Defense":
            continue
        classification = market_to_stat_kind.get(market_key)
        if classification is None:
            continue
        stat, kind, threshold = classification
        if kind == "anytime_td":
            anytime_td.setdefault(eid, []).append({"player": name, "price": row.get("over_price")})
            continue
        players.setdefault(eid, {s: {} for s in STAT_FAMILIES})
        bucket = players[eid][stat].setdefault(name, {"line": None, "alts": []})
        if kind == "line":
            bucket["line"] = {"point": row.get("line"), "over_price": row.get("over_price"),
                               "under_price": row.get("under_price")}
        elif kind == "alt":
            bucket["alts"].append({"threshold": threshold, "over_price": row.get("over_price"),
                                    "under_price": row.get("under_price")})

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
    families = list(STAT_FAMILIES) + ["anytime_td"]
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

    # REAL REWRITE (2026-09-13): player props now use /props (not /odds),
    # per direct guidance from parlay-api.com support after a real
    # support ticket about the passing-yards outage — see the module
    # docstring and the comment above STAT_FAMILIES for the full real
    # findings behind this. One call per stat family (confirmed flat
    # 3 credits each) rather than one giant combined call, to keep each
    # individual call's total row volume well under the real, confirmed
    # 5000-row cap so other books' data doesn't crowd out FanDuel's.
    print("Discovering real, current FanDuel prop market keys (free)...")
    market_map = discover_fanduel_markets()

    market_to_stat_kind = {}
    for stat, info in market_map.items():
        if info["plain"]:
            market_to_stat_kind[info["plain"]] = (stat, "line", None)
        for threshold, key in info["alts"]:
            market_to_stat_kind[key] = (stat, "alt", threshold)
    market_to_stat_kind[ANYTIME_TD_KEY] = ("anytime_td", "anytime_td", None)

    all_rows = []
    for stat in STAT_FAMILIES:
        info = market_map[stat]
        markets_for_stat = ([info["plain"]] if info["plain"] else []) + [key for _, key in info["alts"]]
        if not markets_for_stat:
            print(f"  WARNING: no real FanDuel market keys discovered at all for {stat} right now — "
                  f"skipping this stat family for this run.")
            continue
        print(f"Fetching {stat} props ({len(markets_for_stat)} real market key(s), confirmed FanDuel)...")
        all_rows.extend(fetch_props(markets_for_stat))

    print("Fetching anytime TD props...")
    all_rows.extend(fetch_props([ANYTIME_TD_KEY]))

    players, anytime_td = reshape_props_rows(all_rows, market_to_stat_kind)

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
            "player_props": players.get(eid, {stat: {} for stat in STAT_FAMILIES}),
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
