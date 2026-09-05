"""
INSPECT_PARLAY_PROPS.PY — measure the real data quality, not another demo
============================================================================
Follow-up to test_parlay_api.py. That script proved connectivity and
correct credit costs (1 + 3 = 4 credits, confirmed against the real
x-requests-used headers). But its console output truncated both real
responses at 1500 characters, which is why three real problems only
became visible on manual inspection of what DID print:

  1. /odds came back in DECIMAL format (1.543, 2.54...) even with no
     oddsFormat param — the docs say American is the default. The
     sandbox response (Step 1 of the prior run) WAS American-format,
     so this isn't "the API only does decimal" — something about the
     real endpoint's default disagrees with docs or with the sandbox.
  2. The first real /props row had "home_team": "" and "away_team": ""
     — blank strings, not missing keys.
  3. 5000 prop rows spanned 275 distinct market_key values against a
     docs table showing ~10 core NFL markets — a lot of that looked
     like the same real stat spelled multiple ways, milestone ladders,
     and player-name-embedded keys.

This script makes ONE fresh /odds call and ONE fresh /props call (same
1 + 3 = 4 credit cost as before — the prior run's data was never saved,
only printed and truncated, so re-fetching is the only way to inspect
it fully), saves the COMPLETE raw JSON to disk, then runs real counts
against the full data instead of a hunch from a truncated scroll.

This does NOT decide whether to proceed with Prop Center. It measures,
so that decision gets made from real numbers.

USAGE:
    python3 inspect_parlay_props.py

OUTPUT:
    parlay_odds_sample.json   — complete raw /odds response
    parlay_props_sample.json — complete raw /props response
    (both printed findings AND written to parlay_quality_report.txt)
"""

import json
import os
import re
import sys
from collections import Counter

import requests

PROVIDER = {
    "base_url": "https://parlay-api.com/v1",
    "api_key_env": "PARLAY_API_KEY",
    "auth_header": "X-API-Key",
}
NFL_SPORT_KEY = "americanfootball_nfl"


def get_api_key():
    key = os.environ.get(PROVIDER["api_key_env"])
    if not key:
        sys.exit(f"FATAL: {PROVIDER['api_key_env']} is not set.")
    return key


def fetch_odds(api_key):
    url = f"{PROVIDER['base_url']}/sports/{NFL_SPORT_KEY}/odds"
    resp = requests.get(url, headers={PROVIDER["auth_header"]: api_key},
                         params={"regions": "us", "markets": "h2h"}, timeout=30)
    resp.raise_for_status()
    return resp.json()


def fetch_props(api_key):
    url = f"{PROVIDER['base_url']}/sports/{NFL_SPORT_KEY}/props"
    resp = requests.get(url, headers={PROVIDER["auth_header"]: api_key}, timeout=30)
    resp.raise_for_status()
    return resp.json()


# ── Analysis functions — kept separate from the fetch calls above so ──────
# they can be unit-tested against a saved sample without spending credits
# on every run.

def classify_price(p):
    """American odds are always |price| >= 100 (and typically an
    integer). Decimal odds are typically in (1.0, ~20) for anything
    resembling a real game price. This is a real, defensible
    heuristic, not a guess — the two ranges don't overlap for
    realistic sports prices."""
    try:
        p = float(p)
    except (TypeError, ValueError):
        return "unparseable"
    if abs(p) >= 100 and p == int(p):
        return "american"
    if 1.0 < p < 20.0:
        return "decimal"
    return "other"


def analyze_odds_format(odds_data):
    """Walks every bookmaker/market/outcome price in a real /odds
    response and reports which format(s) actually came back, broken
    out per bookmaker (in case some books are consistent and others
    aren't)."""
    per_book = {}
    overall = Counter()
    for event in odds_data:
        for bk in event.get("bookmakers", []):
            book = bk.get("key", "unknown")
            per_book.setdefault(book, Counter())
            for mkt in bk.get("markets", []):
                for outcome in mkt.get("outcomes", []):
                    fmt = classify_price(outcome.get("price"))
                    per_book[book][fmt] += 1
                    overall[fmt] += 1
    return overall, per_book


def analyze_props_team_names(props_data):
    blank = sum(1 for r in props_data
                if not r.get("home_team") or not r.get("away_team"))
    return blank, len(props_data)


CANONICAL_STAT_PROBES = {
    "receiving_yards": ["rec_yds", "receiving_yards", "reception_yds"],
    "rushing_yards": ["rush_yds", "rushing_yards"],
    "passing_yards": ["pass_yds", "passing_yards"],
    "receptions": ["receptions", "rec_targets"],
    "passing_tds": ["pass_tds", "passing_tds", "passing_touchdowns", "touchdown_passes"],
}


def analyze_market_keys(props_data):
    keys = sorted(set(r.get("market_key") for r in props_data if r.get("market_key")))
    milestone_keys = [k for k in keys if "_milestones_" in k]
    player_specific_keys = [k for k in keys if re.search(r"_to_(score|rush_for)_", k)]
    core_variants = {}
    for concept, probes in CANONICAL_STAT_PROBES.items():
        matches = [k for k in keys if any(p in k for p in probes)]
        if matches:
            core_variants[concept] = matches
    accounted_for = set(milestone_keys) | set(player_specific_keys)
    for matches in core_variants.values():
        accounted_for |= set(matches)
    unaccounted = [k for k in keys if k not in accounted_for]
    return {
        "total_unique_keys": len(keys),
        "milestone_ladder_keys": len(milestone_keys),
        "player_name_embedded_keys": len(player_specific_keys),
        "core_stat_variants": core_variants,
        "unaccounted_keys_sample": unaccounted[:30],
        "unaccounted_count": len(unaccounted),
    }


def main():
    api_key = get_api_key()

    print("Fetching real /odds (1 credit)...")
    odds_data = fetch_odds(api_key)
    with open("parlay_odds_sample.json", "w") as f:
        json.dump(odds_data, f, indent=2)
    print(f"  Saved {len(odds_data)} events to parlay_odds_sample.json")

    print("Fetching real /props (3 credits)...")
    props_data = fetch_props(api_key)
    with open("parlay_props_sample.json", "w") as f:
        json.dump(props_data, f, indent=2)
    print(f"  Saved {len(props_data)} rows to parlay_props_sample.json")

    report_lines = []
    def p(line=""):
        print(line)
        report_lines.append(line)

    p()
    p("=" * 70)
    p("ODDS FORMAT CONSISTENCY (/odds)")
    p("=" * 70)
    overall, per_book = analyze_odds_format(odds_data)
    p(f"Overall price-format counts across all books/markets: {dict(overall)}")
    if len(overall) > 1:
        p("REAL ISSUE CONFIRMED: more than one price format present in a single "
          "response with no oddsFormat param set. Code cannot assume one format.")
    mixed_books = []
    for book, counts in sorted(per_book.items()):
        formats_seen = [k for k in counts if counts[k] > 0]
        tag = " <- MIXED WITHIN THIS BOOK" if len(formats_seen) > 1 else ""
        if tag:
            mixed_books.append(book)
        p(f"  {book:15s}: {dict(counts)}{tag}")
    if mixed_books:
        p(f"\nBooks with inconsistent formats WITHIN their own prices: {mixed_books}")
    else:
        p("\nEach individual book is internally consistent — the inconsistency "
          "(if any, see overall counts above) is BETWEEN books, not within one.")

    p()
    p("=" * 70)
    p("BLANK TEAM NAMES (/props)")
    p("=" * 70)
    blank, total = analyze_props_team_names(props_data)
    pct = 100 * blank / total if total else 0
    p(f"{blank} of {total} rows ({pct:.1f}%) have a blank home_team or away_team.")
    if blank == total:
        p("EVERY row is missing team names — this is systemic, not a one-off. "
          "Grouping props by game will need canonical_event_id, not team names.")
    elif blank == 0:
        p("Zero blank rows in this fetch — the earlier blank row may have been "
          "a one-off, not systemic. Worth treating as fixed-but-unconfirmed "
          "rather than fixed-for-sure off one clean sample.")
    else:
        p("Partial — some rows have real team names, some don't. Needs a "
          "fallback (e.g. resolve via canonical_event_id) for the blank ones.")

    p()
    p("=" * 70)
    p("MARKET KEY TAXONOMY (/props)")
    p("=" * 70)
    mk = analyze_market_keys(props_data)
    p(f"Total unique market_key values: {mk['total_unique_keys']}")
    p(f"Milestone-ladder keys (e.g. '..._or_more'): {mk['milestone_ladder_keys']}")
    p(f"Player-name-embedded keys (e.g. 'player_x_to_score_1__tds'): "
      f"{mk['player_name_embedded_keys']}")
    p(f"\nReal example — how many raw keys map to ONE actual stat concept:")
    for concept, variants in mk["core_stat_variants"].items():
        p(f"  '{concept}' is spelled {len(variants)} different way(s): {variants}")
    p(f"\nKeys not accounted for by any of the above categories: "
      f"{mk['unaccounted_count']} (sample: {mk['unaccounted_keys_sample']})")

    with open("parlay_quality_report.txt", "w") as f:
        f.write("\n".join(report_lines))
    print("\nFull report also saved to parlay_quality_report.txt")


if __name__ == "__main__":
    main()
