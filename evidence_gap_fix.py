#!/usr/bin/env python3
"""
evidence_gap_fix.py - flags report sentences that claim data is missing from "the evidence package".

Frank's rule: no report may say the evidence package lacks something. Real gaps are expressed as football
facts ("no games yet against a bottom-5 defense", n=0), never as statements about the package.

  python3 evidence_gap_fix.py              # scan latest game_breakdowns/wk*/*.md and props_reports/wk*/ md/json
  python3 evidence_gap_fix.py file1 file2  # scan specific files
Library:  from evidence_gap_fix import scan_gaps, summarize_gaps
"""
import glob
import json
import os
import re
import sys

NEG = r"(not|n't|no\b|none|without|lack|lacks|lacking|missing|empty|absent|unavailable|cannot|can't|isn't|aren't|doesn't|does not)"
PATTERNS = [
    ("says package lacks data", re.compile(
        r"[^.\n|]*\b(evidence package|evidence bundle|this week's package|the package)\b[^.\n|]*", re.I)),
    ("says data not available", re.compile(
        r"[^.\n|]*\bnot available in (this|the) [^.\n|]*", re.I)),
    ("says split/ranking empty", re.compile(
        r"[^.\n|]*\b(splits?|rankings?|man/zone|contextual statistics)\b[^.\n|]*\b(are|is) (both )?(empty|unavailable|missing)[^.\n|]*", re.I)),
]


def scan_gaps(text):
    """Returns [{line, kind, snippet}] for sentences claiming missing data / mentioning the package negatively."""
    out = []
    for ln, line in enumerate(text.splitlines(), 1):
        seen = set()
        for kind, pat in PATTERNS:
            for m in pat.finditer(line):
                snip = m.group(0).strip()
                if kind == "says package lacks data" and not re.search(NEG, snip, re.I):
                    continue
                if snip in seen:
                    continue
                seen.add(snip)
                out.append({"line": ln, "kind": kind, "snippet": snip[:220]})
    return out


def summarize_gaps(recs, label=""):
    if not recs:
        return "EVIDENCE-GAP CHECK: clean - no 'not in the evidence package' statements.%s" % (" " + label if label else "")
    lines = ["EVIDENCE-GAP CHECK: %d sentence(s) claim data is missing - regenerate or edit by hand:" % len(recs)]
    for r in recs[:25]:
        lines.append("  line %d [%s] %s" % (r["line"], r["kind"], r["snippet"]))
    return "\n".join(lines)


def default_files():
    files = []
    for pat in ("game_breakdowns", "props_reports"):
        wks = sorted(glob.glob(pat + "/wk*"))
        if wks:
            for ext in ("*.md", "*.json"):
                files += glob.glob(os.path.join(wks[-1], ext))
    return [f for f in files if not f.endswith("manifest.json")]


def main():
    files = sys.argv[1:] or default_files()
    total = 0
    for f in files:
        txt = open(f, encoding="utf-8", errors="ignore").read()
        if f.endswith(".json"):
            try:
                d = json.load(open(f))
                txt = "\n".join(str(v) for v in d.values() if isinstance(v, str)) or txt
            except ValueError:
                pass
        recs = scan_gaps(txt)
        total += len(recs)
        if recs:
            print("\n%s" % f)
            print(summarize_gaps(recs))
    print("\nTotal flagged: %d across %d file(s)" % (total, len(files)))


if __name__ == "__main__":
    main()
