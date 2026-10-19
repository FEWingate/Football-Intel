#!/usr/bin/env python3
"""
PROBE_ALT_COVERAGE.PY - read-only diagnostic. Changes nothing on disk.

Question: are alt lines missing because parlay-api never LISTS them (provider gap),
or because we only ask for the keys it lists (our discovery gap)?

  1. FREE: every FanDuel '___alt_' key in /props/markets, counted by stat, plus any other
     FanDuel key containing alt/milestone/ladder.
  2. --fetch (about 3 credits, one call): builds per-player alt keys by name for players that
     have NO listed alt key (default: tonight's WAS@SF skill players), asks /props for them
     with bookmakers=fanduel, and prints which keys returned rows and which did not, plus the
     provider's x-markets-served / x-markets-unservable headers.

  python3 probe_alt_coverage.py
  python3 probe_alt_coverage.py --fetch
  python3 probe_alt_coverage.py --fetch --players "Christian McCaffrey,Terry McLaurin"
"""
import argparse, re, sys
from collections import Counter
import requests
import build_fanduel_props as b

STATS = ("passing", "rushing", "receiving")
HDRS = ("x-result-has-more", "x-result-truncated", "x-source-degraded", "x-source-errors", "x-request-id",
        "x-requests-last", "x-requests-remaining", "x-markets-served", "x-markets-unservable")


def get(path, params):
    return requests.get(f"{b.BASE_URL}/{path}", headers={b.AUTH_HEADER: b.PARLAY_API_KEY}, params=params, timeout=90)


def slug(name):
    s = re.sub(r"[.'’]", "", name.lower())
    return re.sub(r"[^a-z0-9]+", "_", s).strip("_")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fetch", action="store_true")
    ap.add_argument("--players", default="Christian McCaffrey,Terry McLaurin,George Kittle,Deebo Samuel,Jayden Daniels,Brock Purdy")
    a = ap.parse_args()
    if not b.PARLAY_API_KEY:
        sys.exit("PARLAY_API_KEY not set (source ~/.bashrc).")

    print("== 1) FanDuel alt keys currently listed (free) ==")
    r = get(f"sports/{b.NFL_SPORT_KEY}/props/markets", {})
    print("HTTP", r.status_code)
    fd = [m for m in r.json() if isinstance(m, dict) and "fanduel" in (m.get("bookmakers") or [])]
    print(len(fd), "FanDuel market entries")
    alts = sorted(m["key"] for m in fd if "___alt_" in (m.get("key") or ""))
    cnt = Counter(re.search(r"___alt_(\w+?)_yds$", k).group(1) if re.search(r"___alt_(\w+?)_yds$", k) else "other" for k in alts)
    print("per-player alt keys:", len(alts), dict(cnt))
    for k in alts:
        print("  ", k)
    print("\nOther FanDuel keys mentioning alt/milestone/ladder:")
    for m in sorted(fd, key=lambda x: x["key"]):
        k = m["key"].lower()
        if "___alt_" not in k and any(t in k for t in ("alt", "milestone", "ladder")):
            print("  ", m["key"])
    print("\nAll FanDuel non-alt keys:")
    for m in sorted(fd, key=lambda x: x["key"]):
        if "___alt_" not in m["key"]:
            print("  ", m["key"])

    if not a.fetch:
        print("\n(free part only; add --fetch to test constructed per-player alt keys)")
        return
    listed = set(alts)
    names = [p.strip() for p in a.players.split(",") if p.strip()]
    keys = []
    for n in names:
        for st in STATS:
            k = f"player_{slug(n)}___alt_{st}_yds"
            if k not in listed:
                keys.append((n, st, k))
    print("\n== 2) constructed keys NOT in the listing:", len(keys), "==")
    if not keys:
        print("nothing to test"); return
    resp = get(f"sports/{b.NFL_SPORT_KEY}/props", {"markets": ",".join(k for _, _, k in keys), "bookmakers": "fanduel",
                                                 "oddsFormat": "decimal", "limit": 10000})
    print("HTTP", resp.status_code)
    for h in HDRS:
        print(f"  {h}: {resp.headers.get(h)}")
    try:
        body = resp.json()
    except Exception:
        print(resp.text[:400]); return
    rows = body if isinstance(body, list) else body.get("props") or body.get("rows") or body.get("data") or []
    got = Counter(r.get("market_key") for r in rows if isinstance(r, dict))
    print(len(rows), "rows")
    for n, st, k in keys:
        print(f"  {'ROWS ' + str(got[k]) if got.get(k) else 'none     '}  {k}")
    for r_ in rows[:5]:
        print({x: r_.get(x) for x in ("market_key", "player", "line", "over_price", "under_price", "bookmaker", "last_update")})
    print("\nPaste everything above back to Claude.")


if __name__ == "__main__":
    main()
