"""
CHECK_SUNDAY_FULL_MARKET.PY
============================
Comprehensive real-data check: does parlay-api.com actually deliver every
requested bet type (moneyline, spread, total, alternate spread/total,
player props) for FanDuel, for the real games happening this Sunday?

This re-checks and extends the original test from a few days ago in two
real ways:
  1. alternate_spreads and alternate_totals were NEVER tested before —
     confirmed as real, separate, requestable market keys directly from
     the current docs (fetched 2026-09-10), not assumed.
  2. Standard spreads came back EMPTY for FanDuel in the original test,
     days before kickoff. Worth re-checking now that it's genuinely
     closer to game time — lines that hadn't posted yet may exist now.

Uses the real /events endpoint first (0 credits, per the docs) to find
this Sunday's actual real games via real date filtering, rather than
guessing which events are "this week's" from a broader pull.

Also uses /props' own bookmakers= filter to request ONLY FanDuel's rows
directly (documented as supported), instead of pulling all books and
filtering client-side like the earlier test did — cheaper and cleaner,
though the endpoint still bills its flat 3 credits regardless.

REQUIRES: export PARLAY_API_KEY=... in ~/.bashrc

USAGE:
    python3 check_sunday_full_market.py
"""

import datetime
import os
import sys

import requests

BASE_URL = "https://parlay-api.com/v1"
NFL_SPORT_KEY = "americanfootball_nfl"
AUTH_HEADER = "X-API-Key"
BOOKMAKER = "fanduel"


def get_api_key():
    key = os.environ.get("PARLAY_API_KEY")
    if not key:
        sys.exit("FATAL: PARLAY_API_KEY not set. Add `export PARLAY_API_KEY=...` "
                 "to ~/.bashrc, then `source ~/.bashrc`.")
    return key


def this_sundays_window():
    """Real, computed 'this Sunday' — not hardcoded, so this script stays
    correct regardless of which real day it's actually run on. If today
    IS Sunday, uses today; otherwise the upcoming one."""
    today = datetime.datetime.now(datetime.timezone.utc)
    days_until_sunday = (6 - today.weekday()) % 7  # Monday=0 ... Sunday=6
    sunday = (today + datetime.timedelta(days=days_until_sunday)).date()
    start = datetime.datetime.combine(sunday, datetime.time(0, 0), tzinfo=datetime.timezone.utc)
    end = start + datetime.timedelta(days=1)
    return sunday, start.isoformat().replace("+00:00", "Z"), end.isoformat().replace("+00:00", "Z")


def show_credit_headers(resp):
    for h in ("x-requests-used", "x-requests-remaining", "x-markets-served", "x-markets-unservable"):
        if h in resp.headers:
            print(f"    {h}: {resp.headers[h]}")


def main():
    api_key = get_api_key()
    headers = {AUTH_HEADER: api_key}
    sunday, start_iso, end_iso = this_sundays_window()

    print("=" * 70)
    print(f"STEP 1 — Real Sunday games (free, 0 credits): {sunday}")
    print("=" * 70)
    resp = requests.get(
        f"{BASE_URL}/sports/{NFL_SPORT_KEY}/events", headers=headers,
        params={"commenceTimeFrom": start_iso, "commenceTimeTo": end_iso}, timeout=20,
    )
    if resp.status_code != 200:
        sys.exit(f"FATAL: /events returned HTTP {resp.status_code}: {resp.text[:300]}")
    events = resp.json()
    print(f"Found {len(events)} real game(s) on {sunday}:")
    for e in events:
        print(f"  {e['away_team']} @ {e['home_team']} — {e['commence_time']}")
    if not events:
        print("\nNo real games found for this exact date — either the slate hasn't "
              "posted event records yet, or this script's Sunday-window math is off "
              "relative to what you expected. Worth checking by hand before trusting "
              "the rest of this run.")
        return
    event_ids = ",".join(e["id"] for e in events)

    print()
    print("=" * 70)
    print("STEP 2 — Real /odds: h2h, spreads, totals, alternate_spreads, "
          "alternate_totals — FanDuel only, this Sunday's games only")
    print("=" * 70)
    markets = "h2h,spreads,totals,alternate_spreads,alternate_totals"
    resp = requests.get(
        f"{BASE_URL}/sports/{NFL_SPORT_KEY}/odds", headers=headers,
        params={"regions": "us", "markets": markets, "bookmakers": BOOKMAKER,
                "eventIds": event_ids},
        timeout=30,
    )
    print(f"HTTP {resp.status_code}")
    show_credit_headers(resp)
    market_counts = {}
    if resp.status_code == 200:
        odds_data = resp.json()
        for event in odds_data:
            fd = next((b for b in event.get("bookmakers", []) if b.get("key") == BOOKMAKER), None)
            if not fd:
                continue
            for mkt in fd.get("markets", []):
                market_counts[mkt["key"]] = market_counts.get(mkt["key"], 0) + 1
        print(f"\nReal FanDuel market coverage across {len(events)} Sunday games:")
        for m in ["h2h", "spreads", "totals", "alternate_spreads", "alternate_totals"]:
            n = market_counts.get(m, 0)
            status = "OK" if n > 0 else "MISSING for FanDuel this run"
            print(f"  {m:20s}: {n} of {len(events)} games — {status}")
    else:
        print(f"Response body: {resp.text[:500]}")

    print()
    print("=" * 70)
    print("STEP 3 — Real /props: FanDuel only, this Sunday's games only")
    print("=" * 70)
    resp = requests.get(
        f"{BASE_URL}/sports/{NFL_SPORT_KEY}/props", headers=headers,
        params={"bookmakers": BOOKMAKER}, timeout=30,
    )
    print(f"HTTP {resp.status_code}")
    show_credit_headers(resp)
    if resp.status_code == 200:
        props_data = resp.json()
        sunday_event_ids = {e["id"] for e in events} | {e.get("canonical_event_id") for e in events}
        sunday_props = [r for r in props_data
                         if r.get("event_id") in sunday_event_ids
                         or r.get("canonical_event_id") in sunday_event_ids]
        print(f"\n{len(props_data)} total FanDuel prop rows returned; "
              f"{len(sunday_props)} of them match a real game on {sunday}.")
        market_keys = sorted(set(r.get("market_key") for r in sunday_props if r.get("market_key")))
        print(f"Distinct FanDuel market_key values for Sunday's games: {len(market_keys)}")
        for k in market_keys:
            print(f"  {k}")
        milestone = [k for k in market_keys if "_milestones_" in k]
        if market_keys and len(milestone) == len(market_keys):
            print("\nEvery single FanDuel market here is an alt-line ladder "
                  "(_milestones_) — same real pattern confirmed in the earlier test. "
                  "No plain single-line prop exists for FanDuel via this endpoint.")
    else:
        print(f"Response body: {resp.text[:500]}")

    print()
    print("=" * 70)
    print("DONE. Read the real per-market coverage above — don't assume "
          "'the API supports X' means FanDuel specifically has X posted "
          "right now. A market genuinely can be supported and still be "
          "empty for one book on one day.")
    print("=" * 70)


if __name__ == "__main__":
    main()
