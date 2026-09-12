"""Safely measure ParlayAPI FanDuel NFL player-prop coverage.

The API key is read only from PARLAY_API_KEY and is never printed or written.
The default probe costs 16 credits: 11 passing-family markets followed by five
plain player-prop markets. Use --request-shapes to run three additional
11-credit passing checks for hostname, bookmaker-filter, and event-filter A/Bs.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone


SPORT = "americanfootball_nfl"
PASSING_MARKETS = ["player_passing_yards"] + [
    f"player_passing_yards_milestones_{value}_or_more"
    for value in (150, 175, 200, 225, 250, 275, 300, 325, 350, 400)
]
PLAIN_MARKETS = [
    "player_passing_yards",
    "player_rushing_yards",
    "player_receiving_yards",
    "player_receptions",
    "player_anytime_touchdown_scorer",
]
SAFE_HEADERS = (
    "x-requests-last",
    "x-requests-remaining",
    "x-markets-served",
    "x-markets-unservable",
    "x-markets-served-elsewhere",
)


def fetch(markets, host, bookmaker=False, event_id=None):
    key = os.environ.get("PARLAY_API_KEY")
    if not key:
        raise SystemExit("PARLAY_API_KEY is not available to this process.")
    params = {
        "regions": "us",
        "markets": ",".join(markets),
        "oddsFormat": "decimal",
    }
    if bookmaker:
        params["bookmakers"] = "fanduel"
    if event_id:
        params["eventIds"] = event_id
    url = f"{host}/v1/sports/{SPORT}/odds?{urllib.parse.urlencode(params)}"
    request = urllib.request.Request(
        url,
        headers={
            "X-API-Key": key,
            "User-Agent": "FootballIntelReliabilityProbe/1.0",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            data = json.load(response)
            headers = {name.lower(): value for name, value in response.headers.items()}
    except urllib.error.HTTPError as error:
        body = error.read(500).decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {error.code}: {body}") from error
    return data, {name: headers.get(name) for name in SAFE_HEADERS}


def summarize(data, requested_markets, headers):
    coverage = {market: 0 for market in requested_markets}
    outcomes = {market: 0 for market in requested_markets}
    first_event_id = None
    fanduel_events = 0
    for event in data:
        first_event_id = first_event_id or event.get("canonical_event_id") or event.get("id")
        fanduel = next(
            (book for book in event.get("bookmakers", []) if book.get("key") == "fanduel"),
            None,
        )
        if not fanduel:
            continue
        fanduel_events += 1
        for market in fanduel.get("markets", []):
            key = market.get("key")
            rows = market.get("outcomes") or []
            if key in coverage and rows:
                coverage[key] += 1
                outcomes[key] += len(rows)
    return {
        "events_returned": len(data),
        "fanduel_events": fanduel_events,
        "event_coverage": coverage,
        "outcome_counts": outcomes,
        "response_headers": headers,
        "first_event_id": first_event_id,
    }


def run_probe(label, markets, host, bookmaker=False, event_id=None):
    data, headers = fetch(markets, host, bookmaker=bookmaker, event_id=event_id)
    result = summarize(data, markets, headers)
    safe_result = dict(result)
    safe_result.pop("first_event_id", None)
    print(f"{label}: {json.dumps(safe_result, sort_keys=True)}")
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--request-shapes",
        action="store_true",
        help="Also compare hosts, FanDuel filtering, and one-event filtering (33 extra credits).",
    )
    args = parser.parse_args()
    print(f"probe_started_at={datetime.now(timezone.utc).isoformat()}")
    baseline = run_probe(
        "passing_standard_host", PASSING_MARKETS, "https://parlay-api.com"
    )
    run_probe("plain_market_ab", PLAIN_MARKETS, "https://api.parlay-api.com")
    if args.request_shapes:
        run_probe(
            "passing_standard_host_fanduel",
            PASSING_MARKETS,
            "https://parlay-api.com",
            bookmaker=True,
        )
        run_probe(
            "passing_recommended_host_fanduel",
            PASSING_MARKETS,
            "https://api.parlay-api.com",
            bookmaker=True,
        )
        event_id = baseline.get("first_event_id")
        if event_id:
            run_probe(
                "passing_recommended_host_single_event",
                PASSING_MARKETS,
                "https://api.parlay-api.com",
                bookmaker=True,
                event_id=event_id,
            )


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"probe_failed={type(error).__name__}: {error}", file=sys.stderr)
        raise SystemExit(1)
