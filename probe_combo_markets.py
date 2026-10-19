#!/usr/bin/env python3
"""
PROBE_COMBO_MARKETS.PY - read-only diagnostic. Changes nothing on disk.

Question: does parlay-api.com return FanDuel's COMBINED yardage markets
(Rushing + Receiving, Passing + Rushing) for a real game, under any key?

  1. FREE: lists every market key (any book) that looks like a combined-yardage market and which
     books carry it, plus FanDuel's own pass/rush/rec keys.
  2. 3 credits per call: asks /props directly for the candidate keys with bookmakers=fanduel,
     prints the response headers and the exact rows for the players you name, unmodified.

  python3 probe_combo_markets.py                       # free part only
  python3 probe_combo_markets.py --fetch               # + direct /props calls (about 3-6 credits)
  python3 probe_combo_markets.py --fetch --players "Christian McCaffrey,Brock Purdy,Jayden Daniels"

Nothing is ever added together or inferred: rows are printed exactly as the provider returns them.
"""
import argparse, json, os, sys
import requests
import build_fanduel_props as b

CANDIDATES = ["player_rush_reception_yds", "player_rushing_receiving_yards", "player_passing_rushing_yards",
              "player_pass_rush_yds", "player_rush_rec_yds"]
SHOW = ("market_key", "market", "player", "line", "over_price", "under_price", "period", "bookmaker",
        "canonical_event_id", "last_update")
HDRS = ("x-result-has-more", "x-next-offset", "x-result-truncated", "x-source-degraded", "x-source-errors",
        "x-request-id", "x-requests-last", "x-requests-remaining", "x-markets-served", "x-markets-unservable")


def get(path, params):
    r = requests.get(f"{b.BASE_URL}/{path}", headers={b.AUTH_HEADER: b.PARLAY_API_KEY}, params=params, timeout=90)
    return r


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fetch", action="store_true")
    ap.add_argument("--players", default="Christian McCaffrey,Brock Purdy,Jayden Daniels")
    a = ap.parse_args()
    if not b.PARLAY_API_KEY:
        sys.exit("PARLAY_API_KEY not set (source ~/.bashrc).")
    want = [p.strip().lower() for p in a.players.split(",") if p.strip()]

    print("== 1) market list (free) ==")
    r = get(f"sports/{b.NFL_SPORT_KEY}/props/markets", {})
    print("HTTP", r.status_code)
    data = [m for m in r.json() if isinstance(m, dict)]
    print(len(data), "market entries")
    print("\nKeys that look like COMBINED yardage (any book):")
    hit = False
    for m in sorted(data, key=lambda x: x.get("key") or ""):
        k = (m.get("key") or "").lower()
        if (("rush" in k and ("rec" in k or "pass" in k)) or "combined" in k) and "___alt_" not in k:
            hit = True
            print("  %-45s books: %s" % (m.get("key"), ", ".join(m.get("bookmakers") or [])))
    if not hit:
        print("  (none listed)")
    print("\nFanDuel keys that mention pass/rush/rec (non-alt):")
    for m in sorted(data, key=lambda x: x.get("key") or ""):
        k = m.get("key") or ""
        if "fanduel" in (m.get("bookmakers") or []) and any(w in k for w in ("pass", "rush", "rec")) and "___alt_" not in k:
            print("  ", k)
    alts = sorted({m.get("key") for m in data if "fanduel" in (m.get("bookmakers") or []) and "___alt_" in (m.get("key") or "")
                   and any(n.split()[-1].lower() in (m.get("key") or "") for n in want)})
    print("\nPer-player FanDuel alt keys for your players:", alts or "(none)")

    cov = get("meta/parser-coverage", {"window_hours": 72})
    print("\n== parser coverage endpoint == HTTP", cov.status_code)
    try:
        txt = json.dumps(cov.json())
        import re
        for m in sorted(set(re.findall(r'player_[a-z_]*(?:rush|reception|pass)[a-z_]*', txt))):
            print("  ", m)
    except Exception as e:
        print("  could not read:", e)

    if not a.fetch:
        print("\n(add --fetch to ask /props directly for the candidate keys)")
        return

    print("\n== 2) direct /props requests (bookmakers=fanduel) ==")
    for keys in (CANDIDATES,):
        params = {"markets": ",".join(keys), "oddsFormat": "decimal", "limit": 5000, "bookmakers": "fanduel"}
        offset = None
        rows_all, page = [], 0
        while True:
            p = dict(params)
            if offset:
                p["offset"] = offset
            r = get(f"sports/{b.NFL_SPORT_KEY}/props", p)
            print("\nHTTP", r.status_code, "page", page)
            for h in HDRS:
                if h in r.headers:
                    print("  %s: %s" % (h, r.headers[h]))
            if r.status_code != 200:
                print("  body:", r.text[:400])
                break
            rows = r.json()
            rows_all += [x for x in rows if isinstance(x, dict)]
            page += 1
            if str(r.headers.get("x-result-has-more", "")).lower() == "true" and r.headers.get("x-next-offset") and page < 6:
                offset = r.headers["x-next-offset"]
                continue
            break
        print("\n%d rows total; market keys returned: %s" % (len(rows_all), sorted({x.get("market_key") for x in rows_all})))
        print("bookmakers returned:", sorted({x.get("bookmaker") for x in rows_all}))
        found = 0
        for x in rows_all:
            if (x.get("player") or "").lower() in want or any(w in (x.get("player") or "").lower() for w in want):
                found += 1
                print(json.dumps({k: x.get(k) for k in SHOW}))
        if not found:
            print("No rows for", a.players, "- showing first 3 rows of whatever came back:")
            for x in rows_all[:3]:
                print(json.dumps({k: x.get(k) for k in SHOW}))
    print("\nPaste everything above back to Claude.")


if __name__ == "__main__":
    main()
