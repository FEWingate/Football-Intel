#!/usr/bin/env python3
"""
pff_weekly.py - one-line weekly PFF refresh (LOCAL, PRIVATE).

  python3 pff_weekly.py            # slot data + man/zone + CB/DB + receivers, then rebuild coverage_context.json
  python3 pff_weekly.py --refresh  # also re-pull every saved slot week

Run it Tuesday (or whenever PFF has posted the weekend's charting). Everything lands in the gitignored private/pff/.
Stops at the first step that fails, so you never end up with half-updated files.
"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
refresh = ["--refresh"] if "--refresh" in sys.argv else []
steps = [("PFF slot coverage + receivers", ["pff_pull.py"] + refresh),
         ("PFF man/zone + CB/DB leaderboards", ["pff_facets.py"]),
         ("Building coverage_context.json", ["pff_coverage.py"])]
for i, (label, cmd) in enumerate(steps, 1):
    print("\n[%d/%d] %s" % (i, len(steps), label))
    r = subprocess.run([sys.executable] + cmd, cwd=ROOT)
    if r.returncode != 0:
        sys.exit("\nSTOPPED at step %d (%s). Fix that and rerun." % (i, " ".join(cmd)))
print("\nPFF refresh complete. Hard refresh (Ctrl+Shift+R) any open Football Intel page.")
