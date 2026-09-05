"""
BUILD_FANDUEL_PROPS.PY
========================
Fetches real props + odds (h2h/spreads/totals) from parlay-api.com,
filtered to FanDuel only — per Frank's actual need (props, spreads,
and lines from FanDuel specifically, not all 17 books this API
carries). Writes one normalized JSON that generate_props_report.py
reads from — same "one source of truth" pattern as build_dfs.py for
DraftKings data.

REQUIRES: export PARLAY_API_KEY=... in ~/.bashrc (never commit it)

KNOWN, CONFIRMED GAPS as of 2026-09-05 (full write-up in the Props &
Parlay Report Standard's OPEN ISSUES section):
  - A real test call requesting h2h+spreads+totals got h2h and totals
    back for FanDuel but ZERO spreads. Cause unconfirmed (real gap vs.
    not-yet-posted this far from kickoff). This script does NOT treat
    an empty spreads list as fatal — it logs a clear warning and
    proceeds, since the actual fix is either time (re-test closer to
    kickoff) or a support question to parlay-api, not something this
    script can work around on its own.
  - FanDuel's real player props are ALT-LINE LADDERS
    (player_receiving_yards_milestones_50_or_more, _100_or_more, etc.),
    not single-line props. This script passes through whatever real
    thresholds exist — it does not invent or collapse them into a
    single line.

This is a live odds/props snapshot, not season-stat data, so it does
NOT go through write_with_archive() the way the stats pipeline's
season-namespaced outputs do — there's no "season" concept for odds
that change by the minute, just "latest," overwritten every run.

Real credit cost per run: 3 (odds: h2h+spreads+totals, 1 region, per
the docs' markets x regions formula) + 3 (props, flat) = 6 credits.

USAGE:
    python3 build_fanduel_props.py
"""

import json
import os
import sys
from datetime import datetime, timezone

import requests

PARLAY_API_KEY = os.environ.get("PARLAY_API_KEY")
BASE_URL = "https://parlay-api.com/v1"
NFL_SPORT_KEY = "americanfootball_nfl"
AUTH_HEADER = "X-API-Key"


def _get(path, params=None):
    if not PARLAY_API_KEY:
        sys.exit("FATAL: PARLAY_API_KEY not set. Add `export PARLAY_API_KEY=...` "
                 "to ~/.bashrc, then `source ~/.bashrc`.")
    url = f"{BASE_URL}/{path}"
    resp = requests.get(url, headers={AUTH_HEADER: PARLAY_API_KEY}, params=params or {}, timeout=30)
    if resp.status_code != 200:
        sys.exit(f"FATAL: {url} returned HTTP {resp.status_code}: {resp.text[:300]}")
    print(f"  {path} -> HTTP 200 (x-requests-used={resp.headers.get('x-requests-used')}, "
          f"remaining={resp.headers.get('x-requests-remaining')})")
    return resp.json()


def fetch_fanduel_odds():
    """Real h2h/spreads/totals, filtered to the FanDuel book only,
    reshaped into one row per event with markets keyed by type."""
    data = _get(f"sports/{NFL_SPORT_KEY}/odds", {"regions": "us", "markets": "h2h,spreads,totals"})
    out = []
    for event in data:
        fd = next((bk for bk in event.get("bookmakers", []) if bk.get("key") == "fanduel"), None)
        if not fd:
            continue
        row = {
            "canonical_event_id": event.get("canonical_event_id") or event.get("id"),
            "home_team": event.get("home_team"), "away_team": event.get("away_team"),
            "commence_time": event.get("commence_time"),
            "markets": {mkt.get("key"): mkt.get("outcomes", []) for mkt in fd.get("markets", [])},
        }
        out.append(row)

    seen = set()
    for row in out:
        seen |= set(row["markets"].keys())
    for expected in ("h2h", "spreads", "totals"):
        if expected not in seen:
            print(f"  WARNING: FanDuel returned NO '{expected}' markets this run. "
                  f"Confirmed missing for spreads specifically as of 2026-09-05 — "
                  f"re-test closer to kickoff before assuming this is permanent.")
    return out


def fetch_fanduel_props():
    data = _get(f"sports/{NFL_SPORT_KEY}/props")
    fd_rows = [r for r in data if r.get("bookmaker") == "fanduel"]
    print(f"  {len(fd_rows)} of {len(data)} total prop rows are FanDuel.")
    if not fd_rows:
        print("  WARNING: zero FanDuel prop rows returned. Either FanDuel truly has "
              "no props posted right now, or something changed since 2026-09-05's "
              "confirmed real test — don't assume either without checking.")
    return fd_rows


def main():
    print(f"Building FanDuel-only props/odds — {datetime.now(timezone.utc).isoformat()}")
    odds = fetch_fanduel_odds()
    props = fetch_fanduel_props()

    os.makedirs("fanduel_props", exist_ok=True)
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "bookmaker": "fanduel",
        "odds_events": odds,
        "props": props,
    }
    path = "fanduel_props/latest.json"
    with open(path, "w") as f:
        json.dump(payload, f)
    print(f"Wrote {path} — {len(odds)} events with FanDuel odds, {len(props)} FanDuel prop rows")


if __name__ == "__main__":
    main()
