"""
TEST_PARLAY_API.PY — throwaway integration test, not a site feature
=====================================================================
Confirms parlay-api.com actually delivers what it claims, against
Frank's real paid account, before any Prop Center UI gets built around
it. Per the docs (https://parlay-api.com/docs, fetched and read in full
2026-09-05 — NOT taken from the PyPI package description, which
disagrees with the live docs on the URL prefix):

  - Base path is /v1/ (the docs' own "Migration from the-odds-api"
    section is explicit: TOA's /v4 maps to parlay-api's /v1). The PyPI
    README's /v4 references look like a copy-paste error from TOA's own
    docs — not the real, current API surface. /v1/ is documented as
    stable; breaking changes only ever ship under /v2/.
  - NFL sport key: americanfootball_nfl (confirmed in their Sport Keys
    reference table).
  - Auth: X-API-Key header (recommended) or ?apiKey= query param.
  - /odds costs (markets x regions) credits, floor 1 — this script asks
    for exactly 1 market x 1 region, so this costs 1 credit.
  - /props costs a flat 3 credits regardless of how much data comes
    back (all books, all markets, one call).
  - There's also a free, no-auth SANDBOX with deterministic fake data
    (/v1/sandbox/...) — hit first, costs nothing, and proves basic
    connectivity/shape before spending a single real credit.

Total real cost of running this script once: ~4 credits (1 + 3) against
the 20,000/month Starter balance. Trivial.

NEVER hardcode the key. Matching how ANTHROPIC_API_KEY is already
handled in this project:

    export PARLAY_API_KEY="the-real-key-here"    # add to ~/.bashrc

then this script reads it via os.environ.get() — nothing else. No .env
file is used here at all, which sidesteps the whole "did I gitignore it
before or after creating it" risk entirely — there's no file to leak.

USAGE:
    export PARLAY_API_KEY="your key"
    python3 test_parlay_api.py

This does NOT write to any part of the site. It only prints. Delete it
once you've confirmed what you needed to confirm, or keep it around
purely as a diagnostic — either way, it's not meant to be imported by
build_matchup_stats.py or anything else.
"""

import json
import os
import sys

import requests

# ── Provider config, deliberately isolated ──────────────────────────────
# If parlay-api.com doesn't work out, switching to the-odds-api.com is
# meant to be "swap these four lines," not a rewrite — that's the whole
# point of parlay-api mirroring TOA's shape. Nothing below this block
# should need to change for that swap.
PROVIDER = {
    "name": "parlay-api.com",
    "base_url": "https://parlay-api.com/v1",
    "sandbox_base_url": "https://parlay-api.com/v1/sandbox",
    "api_key_env": "PARLAY_API_KEY",
    "auth_header": "X-API-Key",
}
NFL_SPORT_KEY = "americanfootball_nfl"


def get_api_key():
    key = os.environ.get(PROVIDER["api_key_env"])
    if not key:
        sys.exit(
            f"FATAL: {PROVIDER['api_key_env']} is not set in this shell's environment.\n"
            f"Add this to ~/.bashrc, then open a new terminal (or `source ~/.bashrc`):\n\n"
            f'    export {PROVIDER["api_key_env"]}="the-real-key-here"\n'
        )
    return key


def show_credit_headers(resp):
    """Every real response carries these three headers per the docs —
    print them every time so real credit consumption is visible, not
    assumed."""
    for h in ("x-requests-used", "x-requests-remaining", "x-requests-last"):
        if h in resp.headers:
            print(f"    {h}: {resp.headers[h]}")


def pretty(data, limit=1500):
    s = json.dumps(data, indent=2)
    if len(s) > limit:
        return s[:limit] + f"\n... [truncated, {len(s)} chars total]"
    return s


def test_sandbox():
    """No auth, no credits, deterministic fake data. Pure connectivity
    and shape check — run this first, always."""
    print("=" * 70)
    print("STEP 1 — Sandbox (no key, no credits): confirm the service")
    print("responds at all and the response SHAPE matches what the docs")
    print("describe, before spending anything real.")
    print("=" * 70)
    url = f"{PROVIDER['sandbox_base_url']}/sports/{NFL_SPORT_KEY}/odds"
    try:
        resp = requests.get(url, timeout=20)
    except requests.RequestException as e:
        print(f"FAILED — could not reach {url} at all: {e}")
        return False
    print(f"GET {url}")
    print(f"HTTP {resp.status_code}")
    if resp.status_code != 200:
        print(f"Response body: {resp.text[:500]}")
        return False
    data = resp.json()
    print(f"Response type: {type(data).__name__}, "
          f"{'length ' + str(len(data)) if isinstance(data, list) else ''}")
    print(pretty(data[:2] if isinstance(data, list) else data))
    return True


def test_real_odds(api_key):
    """Real call, real key, minimal cost (1 market x 1 region = 1
    credit per the docs' own cost formula)."""
    print()
    print("=" * 70)
    print("STEP 2 — Real /odds call against your real account.")
    print("Requesting exactly 1 market x 1 region on purpose — this")
    print("should cost 1 real credit, per the docs' own cost formula.")
    print("=" * 70)
    url = f"{PROVIDER['base_url']}/sports/{NFL_SPORT_KEY}/odds"
    params = {"regions": "us", "markets": "h2h"}
    headers = {PROVIDER["auth_header"]: api_key}
    try:
        resp = requests.get(url, headers=headers, params=params, timeout=20)
    except requests.RequestException as e:
        print(f"FAILED — could not reach {url} at all: {e}")
        return None
    print(f"GET {url}?{requests.compat.urlencode(params)}")
    print(f"HTTP {resp.status_code}")
    show_credit_headers(resp)
    if resp.status_code == 401:
        print("401 — the key is missing or invalid. Double-check "
              f"{PROVIDER['api_key_env']} is the real key, not a placeholder.")
        return None
    if resp.status_code == 403:
        print("403 — credit limit exceeded. Check your dashboard balance "
              "before retrying.")
        return None
    if resp.status_code != 200:
        print(f"Unexpected status. Response body: {resp.text[:500]}")
        return None
    data = resp.json()
    print(f"Response type: {type(data).__name__}, "
          f"{'length ' + str(len(data)) if isinstance(data, list) else ''}")
    if isinstance(data, list) and data:
        print("First real event:")
        print(pretty(data[0]))
    else:
        print(pretty(data))
        print("\nNOTE: an empty list here is a REAL possible outcome if "
              "there are no NFL games in the near-term window right now — "
              "not necessarily a failure. Check the dashboard / try again "
              "closer to a real slate if this comes back empty.")
    return data


def test_real_props(api_key):
    """Real call, real key. Flat 3 credits per the docs, regardless of
    how much comes back — this is the endpoint Football Intel's actual
    Prop Center use case cares about."""
    print()
    print("=" * 70)
    print("STEP 3 — Real /props call against your real account.")
    print("Flat 3 credits per the docs, all books/markets in one call.")
    print("=" * 70)
    url = f"{PROVIDER['base_url']}/sports/{NFL_SPORT_KEY}/props"
    headers = {PROVIDER["auth_header"]: api_key}
    try:
        resp = requests.get(url, headers=headers, timeout=20)
    except requests.RequestException as e:
        print(f"FAILED — could not reach {url} at all: {e}")
        return None
    print(f"GET {url}")
    print(f"HTTP {resp.status_code}")
    show_credit_headers(resp)
    if resp.status_code != 200:
        print(f"Response body: {resp.text[:500]}")
        return None
    data = resp.json()
    print(f"Response type: {type(data).__name__}, "
          f"{'length ' + str(len(data)) if isinstance(data, list) else ''}")
    if isinstance(data, list) and data:
        print("First real prop row (confirm this matches the documented shape "
              "— bookmaker/player/market_key/line/over_price/under_price):")
        print(pretty(data[0]))
        markets_seen = sorted(set(row.get("market_key") for row in data))
        books_seen = sorted(set(row.get("bookmaker") for row in data))
        print(f"\n{len(data)} total prop rows across {len(books_seen)} books "
              f"and {len(markets_seen)} market types.")
        print(f"Markets seen: {markets_seen}")
        print(f"Books seen: {books_seen}")
    else:
        print(pretty(data))
        print("\nNOTE: an empty list is a real possible outcome outside game "
              "week / far from kickoff, same caveat as /odds above.")
    return data


if __name__ == "__main__":
    sandbox_ok = test_sandbox()
    if not sandbox_ok:
        print("\nSandbox check failed — something is wrong with basic "
              "connectivity to parlay-api.com before real credits are even "
              "involved. Worth resolving this before spending anything real.")
        sys.exit(1)

    api_key = get_api_key()
    odds_data = test_real_odds(api_key)
    props_data = test_real_props(api_key)

    print()
    print("=" * 70)
    print("DONE. Real findings from this run — read these, don't assume:")
    print(f"  /odds  returned real data: {bool(odds_data)}")
    print(f"  /props returned real data: {bool(props_data)}")
    print("If either came back empty, that alone doesn't mean it's broken —")
    print("check the x-requests-used header above against your dashboard,")
    print("and re-run closer to a real NFL slate if today's window is thin.")
    print("=" * 70)
