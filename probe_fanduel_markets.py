"""
PROBE_FANDUEL_MARKETS.PY — read-only diagnostic. Changes nothing on disk.

Why: FanDuel's own site shows full prop markets for Thursday's TB @ DAL, but
build_fanduel_props.py reports "no real market keys discovered" for passing,
rushing and receiving yards. This shows what parlay-api.com is actually
exposing, so we can tell whether the gap is in its market list (discovery) or
in its rows.

  python3 probe_fanduel_markets_v1.py              # free: lists market keys only
  python3 probe_fanduel_markets_v1.py --try-direct # 3 credits: asks /props for the
                                                   # plain yardage keys directly,
                                                   # skipping discovery
"""
import argparse
from collections import Counter

import build_fanduel_props as b

KEYWORDS = ("pass", "rush", "rec", "yds", "yard", "td", "touchdown")
DIRECT_KEYS = ["player_passing_yards", "player_rushing_yards", "player_receiving_yards"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--try-direct", action="store_true")
    args = ap.parse_args()

    print("Listing parlay-api.com's current NFL prop market keys (free)...")
    data = b._get(f"sports/{b.NFL_SPORT_KEY}/props/markets")
    markets = [m for m in data if isinstance(m, dict)]
    print(f"  {len(markets)} market entries total.")
    fd = [m for m in markets if "fanduel" in (m.get("bookmakers") or [])]
    print(f"  {len(fd)} of them list FanDuel as a bookmaker.\n")

    print("FanDuel keys that look like passing/rushing/receiving/TD markets:")
    shown = 0
    for m in sorted(fd, key=lambda x: x.get("key") or ""):
        key = m.get("key") or ""
        if any(k in key.lower() for k in KEYWORDS):
            print(f"  {key}")
            shown += 1
    if not shown:
        print("  (none)")

    print("\nKeys that look like yardage but do NOT list FanDuel (other books only):")
    other = sorted({(m.get("key") or "") for m in markets
                    if "fanduel" not in (m.get("bookmakers") or [])
                    and any(k in (m.get("key") or "").lower() for k in ("yds", "yard"))})
    for k in other[:40]:
        print(f"  {k}")
    if not other:
        print("  (none)")

    if args.try_direct:
        print(f"\nAsking /props directly for {DIRECT_KEYS} (3 credits)...")
        rows = b.fetch_props(DIRECT_KEYS)
        print(f"  {len(rows)} FanDuel rows came back.")
        by_market = Counter(r.get("market_key") for r in rows)
        for k, n in by_market.most_common():
            print(f"    {k}: {n} rows")
        events = Counter(r.get("canonical_event_id") for r in rows)
        print(f"  Rows span {len(events)} event(s).")
        for r in rows[:8]:
            print(f"    sample: {r.get('player')} | {r.get('market_key')} | line {r.get('line')} | "
                  f"over {r.get('over_price')} / under {r.get('under_price')}")


if __name__ == "__main__":
    main()
