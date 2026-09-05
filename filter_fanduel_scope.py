"""
FILTER_FANDUEL_SCOPE.PY — re-measure quality, scoped to FanDuel only
========================================================================
Frank only needs props, spreads, and lines (moneyline) from FanDuel —
not all 17 books. The prior quality report (264 market keys, 6.7% blank
team names, mixed odds formats) was measured across EVERY book,
including DFS pick'em apps (PrizePicks, Underdog, Sleeper) that are the
likely source of the player-name-embedded markets and milestone
ladders. Scoped to just FanDuel, the real picture could be much
cleaner — or could not be. This measures it rather than assuming.

Two parts:
  1. FREE — re-reads the already-saved parlay_props_sample.json from
     the prior run and filters to bookmaker == "fanduel" only. No new
     API credits spent; this data is already on disk.
  2. ONE NEW CALL — the prior /odds test only requested markets=h2h.
     Spreads and totals were never actually fetched or checked. This
     makes one real call for markets=h2h,spreads,totals (3 markets x
     1 region = 3 credits) since that's genuinely new ground, not
     something already answered.

USAGE:
    python3 filter_fanduel_scope.py
"""

import json
import os
import sys
from collections import Counter

import requests

from inspect_parlay_props import (
    PROVIDER, NFL_SPORT_KEY, classify_price, CANONICAL_STAT_PROBES,
)

PROPS_SAMPLE_PATH = "parlay_props_sample.json"


def get_api_key():
    key = os.environ.get(PROVIDER["api_key_env"])
    if not key:
        sys.exit(f"FATAL: {PROVIDER['api_key_env']} is not set.")
    return key


def fetch_full_odds(api_key):
    """The prior test only asked for markets=h2h. Spreads/totals were
    never fetched — this is genuinely new, not a re-check."""
    url = f"{PROVIDER['base_url']}/sports/{NFL_SPORT_KEY}/odds"
    resp = requests.get(
        url, headers={PROVIDER["auth_header"]: api_key},
        params={"regions": "us", "markets": "h2h,spreads,totals"}, timeout=30,
    )
    resp.raise_for_status()
    print("    x-requests-used:", resp.headers.get("x-requests-used"))
    print("    x-requests-remaining:", resp.headers.get("x-requests-remaining"))
    return resp.json()


def main():
    if not os.path.exists(PROPS_SAMPLE_PATH):
        sys.exit(f"FATAL: {PROPS_SAMPLE_PATH} not found — run inspect_parlay_props.py "
                  f"first (that's what wrote it).")
    with open(PROPS_SAMPLE_PATH) as f:
        all_props = json.load(f)

    fanduel_props = [r for r in all_props if r.get("bookmaker") == "fanduel"]
    print("=" * 70)
    print(f"FANDUEL-ONLY /props — from already-saved data, 0 new credits")
    print("=" * 70)
    print(f"{len(fanduel_props)} of {len(all_props)} total prop rows are FanDuel "
          f"({100*len(fanduel_props)/len(all_props):.1f}%).")
    if not fanduel_props:
        print("ZERO FanDuel rows in the props response at all. Worth confirming "
              "directly with parlay-api support whether FanDuel is included in "
              "/props for NFL, or only for certain sports/markets.")
    else:
        blank = sum(1 for r in fanduel_props if not r.get("home_team") or not r.get("away_team"))
        print(f"Blank team names (FanDuel only): {blank} of {len(fanduel_props)} "
              f"({100*blank/len(fanduel_props):.1f}%)")

        keys = sorted(set(r.get("market_key") for r in fanduel_props if r.get("market_key")))
        print(f"\nDistinct market_key values FanDuel actually offers: {len(keys)}")
        for k in keys:
            print(f"  {k}")

        milestone = [k for k in keys if "_milestones_" in k]
        player_embedded = [k for k in keys if "_to_score_" in k or "_to_rush_for_" in k]
        print(f"\nOf those, milestone-ladder keys: {len(milestone)}")
        print(f"Of those, player-name-embedded keys: {len(player_embedded)}")
        if not milestone and not player_embedded:
            print("FanDuel's real market set looks like standard sportsbook props, "
                  "not DFS-style milestone/player-embedded markets — consistent "
                  "with those being a DFS-app (PrizePicks/Underdog/Sleeper) pattern, "
                  "not a FanDuel one. Confirmed from real data, not assumed.")

    print()
    print("=" * 70)
    print("FANDUEL /odds — spreads + totals (NEW: 1 real call, 3 credits)")
    print("=" * 70)
    api_key = get_api_key()
    odds_data = fetch_full_odds(api_key)
    with open("parlay_odds_full_sample.json", "w") as f:
        json.dump(odds_data, f, indent=2)
    print(f"Saved {len(odds_data)} events to parlay_odds_full_sample.json")

    fd_market_counts = Counter()
    fd_price_formats = Counter()
    events_with_fd = 0
    for event in odds_data:
        fd_book = next((bk for bk in event.get("bookmakers", [])
                         if bk.get("key") == "fanduel"), None)
        if not fd_book:
            continue
        events_with_fd += 1
        for mkt in fd_book.get("markets", []):
            fd_market_counts[mkt.get("key")] += 1
            for outcome in mkt.get("outcomes", []):
                fd_price_formats[classify_price(outcome.get("price"))] += 1

    print(f"\nFanDuel present in {events_with_fd} of {len(odds_data)} events.")
    print(f"Market types FanDuel actually returned: {dict(fd_market_counts)}")
    print(f"Price format(s): {dict(fd_price_formats)}")
    missing = {"h2h", "spreads", "totals"} - set(fd_market_counts.keys())
    if missing:
        print(f"\nFanDuel did NOT return these requested market types: {missing} "
              f"— worth checking if that's a real gap or just this moment's slate.")
    else:
        print("\nAll three requested market types (h2h, spreads, totals) came back "
              "for FanDuel.")


if __name__ == "__main__":
    main()
