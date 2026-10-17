#!/usr/bin/env python3
"""
pff_facets.py - LOCAL, PRIVATE pull of PFF league-wide coverage leaderboards (man/zone + CB/DB).
Writes private/pff/facet_<name>.json (gitignored) and prints the column names so we can wire them into the evidence.

  python3 pff_facets.py                 # season 2026, season-to-date
  python3 pff_facets.py --season 2026
"""
import argparse, json, os, shutil, subprocess, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
PRIVATE = os.path.join(ROOT, "private", "pff")
FACETS = ["facet-defense-coverage", "facet-defense-coverage-scheme",
          "facet-receiving-scheme", "facet-receiving-coverage"]


def restish():
    p = shutil.which("restish") or os.path.expanduser("~/go/bin/restish")
    return p if p and os.path.exists(p) else sys.exit("restish not found")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--season", default="2026")
    a = ap.parse_args()
    rs = restish()
    os.makedirs(PRIVATE, exist_ok=True)
    for f in FACETS:
        r = subprocess.run([rs, "pff", f, "--league", "nfl", "--season", a.season],
                           capture_output=True, text=True, timeout=300)
        if r.returncode != 0:
            print("%-34s FAILED: %s" % (f, (r.stderr or r.stdout).strip()[:300]))
            continue
        try:
            d = json.loads(r.stdout)
        except ValueError:
            print("%-34s not JSON: %r" % (f, r.stdout[:200]))
            continue
        json.dump(d, open(os.path.join(PRIVATE, "%s.json" % f.replace("-", "_")), "w"))
        key = next((k for k, v in d.items() if isinstance(v, list) and v and isinstance(v[0], dict)), None)
        rows = d.get(key, []) if key else []
        cols = sorted({c for row in rows[:200] for c in row})
        print("\n=== %s  key=%s rows=%d  restricted=%s" % (f, key, len(rows), d.get("restricted")))
        print("columns (%d): %s" % (len(cols), ", ".join(cols)))
        if rows:
            ex = rows[0]
            print("example row:", json.dumps({k: ex[k] for k in list(ex)[:40]})[:900])
    print("\nSaved under private/pff/. Paste everything above to Claude.")


if __name__ == "__main__":
    main()
