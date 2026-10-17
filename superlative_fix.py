"""
SUPERLATIVE_FIX.PY
===================
Stops Coeus from calling a team "league-worst" / "worst in the NFL" /
"the league's best" when the rank printed right next to that claim says
otherwise (e.g. "a league-worst 48.4 rec yds/gm to RBs (30th)" — 30th is
the 3rd-worst, not the worst).

WHY A SCRIPT, NOT JUST A PROMPT RULE: the model writes the superlative from
the shape of a number ("big number -> league-worst") while the rank sits a
few words later in the same sentence. A prompt rule lowers how often that
happens (see the SUPERLATIVE LABELS rule added to the prompts) but cannot
guarantee zero. This module is the guarantee: it runs on the finished report
text, checks every absolute superlative against the rank cited beside it,
and rewrites the contradicted ones to the true ordinal ("3rd-worst").

THE RULE (ranks are 1 = best ... 32 = worst):
  * Absolute "worst"  (league-worst, NFL-worst, the league's worst,
    worst in the league/NFL)  needs the cited rank to be 32.
  * Absolute "best"   (league-best, NFL-best, the league's best,
    best in the league/NFL)   needs the cited rank to be 1.
  * Hedged forms ("one of the league's worst", "among the league's best",
    "nearly the league's worst") need rank >= 27 (worst) / <= 6 (best).
  * "tied", "but one", "-tier" and already-qualified forms ("3rd-worst",
    "2nd-best") are left alone.
  * A wrong ABSOLUTE is rewritten:  league-worst  ->  3rd-worst
                                    the league's worst -> the league's 3rd-worst
                                    worst in the NFL  -> 3rd-worst in the NFL
  * A wrong HEDGE is not rewritten (the sentence needs a human look); it is
    reported as REVIEW.
  * An absolute with no rank next to it can't be checked; reported as
    UNVERIFIED, never changed.

USE:
  python3 superlative_fix.py                 # dry run over this week's files
  python3 superlative_fix.py --apply         # rewrite those files in place
  python3 superlative_fix.py FILE [FILE...]  # specific files (dry run)
  python3 superlative_fix.py --apply FILE... # specific files, rewrite

The generators (generate_game_breakdown.py, generate_props_report.py) call
fix_superlatives() on every freshly generated report automatically.
"""
import glob
import re
import sys

TEAMS = 32

_ORD = r"(\d{1,2})(?:st|nd|rd|th)"
_ORD_RE = re.compile(_ORD, re.I)

# (kind, regex). Order matters only for readability; matches are collected
# from all patterns and de-duplicated by span.
_PATTERNS = [
    ("worst", re.compile(r"(?<![\w-])(?:league|NFL)-worst(?:-ranked)?", re.I), "league-worst"),
    ("worst", re.compile(r"(?<![\w-])the (?:league|NFL)(?:'|’)s worst", re.I), "the league's worst"),
    ("worst", re.compile(r"(?<![\w-])worst[- ]in[- ]the[- ](?:league|NFL)", re.I), "worst in the league"),
    ("worst", re.compile(r"(?<=\band )worst(?= [a-z])", re.I), "and worst"),
    ("best", re.compile(r"(?<![\w-])(?:league|NFL)-best(?:-ranked)?", re.I), "league-best"),
    ("best", re.compile(r"(?<![\w-])the (?:league|NFL)(?:'|’)s best", re.I), "the league's best"),
    ("best", re.compile(r"(?<![\w-])best[- ]in[- ]the[- ](?:league|NFL)", re.I), "best in the league"),
]

_HEDGE_BEFORE = re.compile(
    r"(one of|among|nearly|near|almost|close to|some of|part of)\s+(?:the\s+)?(?:\w+\s+){0,2}$", re.I)


def _ordinal(n):
    if 10 <= n % 100 <= 20:
        suf = "th"
    else:
        suf = {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return f"{n}{suf}"


def _find_rank(text, start, end):
    """The rank number this superlative is describing: an ordinal directly
    before it ("31st — worst in the NFL"), else the first ordinal after it in
    the same clause (stops at . ; newline or 130 chars). Ordinals that are
    themselves qualifiers ("3rd-worst", "2nd-fewest", "5th-best") don't count
    as the rank of the stat."""
    before = text[max(0, start - 18):start]
    m = re.search(_ORD + r"[\s,)—–\-:(]*(?:(?:nearly|almost|virtually|one of|among)\s+(?:the\s+)?)?$",
                  before, re.I)
    if m and not re.search(r"-\s*$", before[:m.start()]):
        return int(m.group(1))
    tail = text[end:end + 130]
    stop = re.search(r"[.;\n]\s|[.;\n]$", tail)
    if stop:
        tail = tail[:stop.start()]
    for m in _ORD_RE.finditer(tail):
        after = tail[m.end():m.end() + 8]
        if re.match(r"[- ](?:best|worst|fewest|most|ranked|lowest|highest)", after, re.I) \
                and not re.match(r"[- ]ranked", after, re.I):
            continue
        return int(m.group(1))
    return None


def scan(text):
    """Returns a list of dicts: kind, phrase, rank, status, span, context.
    status: OK | FIX | REVIEW | UNVERIFIED | SKIP"""
    found, taken = [], []
    for kind, rx, label in _PATTERNS:
        for m in rx.finditer(text):
            if any(not (m.end() <= a or m.start() >= b) for a, b in taken):
                continue
            taken.append((m.start(), m.end()))
            ctx = text[max(0, m.start() - 60):m.end() + 90].replace("\n", " ")
            hedged = bool(_HEDGE_BEFORE.search(text[max(0, m.start() - 30):m.start()]))
            window = text[max(0, m.start() - 40):m.end() + 50].lower()
            rank = _find_rank(text, m.start(), m.end())
            rec = dict(kind=kind, phrase=m.group(0), rank=rank, span=(m.start(), m.end()),
                       hedged=hedged, context=ctx, label=label)
            if "tied" in window or text[m.end():m.end() + 8].lower().startswith((" but one", "-tier")):
                rec["status"] = "SKIP"
            elif rank is None:
                rec["status"] = "UNVERIFIED"
            elif kind == "worst":
                if hedged:
                    rec["status"] = "OK" if rank >= 27 else "REVIEW"
                else:
                    rec["status"] = "OK" if rank >= TEAMS else ("FIX" if rank >= 17 else "REVIEW")
            else:
                if hedged:
                    rec["status"] = "OK" if rank <= 6 else "REVIEW"
                else:
                    rec["status"] = "OK" if rank <= 1 else ("FIX" if rank <= 16 else "REVIEW")
            found.append(rec)
    return sorted(found, key=lambda r: r["span"][0])


def _replacement(rec):
    r = rec["rank"]
    n = (TEAMS + 1 - r) if rec["kind"] == "worst" else r
    word = f"{_ordinal(n)}-{rec['kind']}"
    phrase = rec["phrase"]
    low = phrase.lower()
    if low.endswith("-ranked"):
        return word + "-ranked"
    if "'s" in low or "’s" in low:
        return re.sub(r"(worst|best)$", word, phrase, flags=re.I)
    if low.startswith(("worst", "best")):
        return re.sub(r"^(worst|best)", word, phrase, flags=re.I)
    return word  # league-worst / NFL-best


def fix_superlatives(text):
    """Returns (new_text, records). Only status FIX records are rewritten."""
    recs = scan(text)
    out, pos = [], 0
    for rec in recs:
        if rec["status"] != "FIX":
            continue
        a, b = rec["span"]
        rec["new"] = _replacement(rec)
        out.append(text[pos:a])
        out.append(rec["new"])
        pos = b
    out.append(text[pos:])
    return "".join(out), recs


def summarize(recs, label=""):
    fixes = [r for r in recs if r["status"] == "FIX"]
    review = [r for r in recs if r["status"] == "REVIEW"]
    unver = [r for r in recs if r["status"] == "UNVERIFIED"]
    lines = []
    for r in fixes:
        lines.append(f"  FIXED   {r['phrase']!r} -> {r['new']!r}  (cited rank {r['rank']}): ...{r['context'][40:150]}...")
    for r in review:
        lines.append(f"  REVIEW  {r['phrase']!r} with cited rank {r['rank']} (hedged={r['hedged']}) — check wording: ...{r['context'][40:150]}...")
    return fixes, review, unver, lines


def default_files():
    files = []
    for wk in sorted(glob.glob("game_breakdowns/wk*"))[-1:]:
        files += sorted(glob.glob(f"{wk}/*.md"))
    for wk in sorted(glob.glob("props_reports/wk*"))[-1:]:
        files += sorted(f for f in glob.glob(f"{wk}/props_parlay_report_*") if f.endswith((".md", ".json"))
                        and not f.endswith("_prompt.json"))
    return files


def main(argv):
    apply = "--apply" in argv
    files = [a for a in argv if not a.startswith("--")] or default_files()
    total_fix = total_review = total_unver = 0
    for f in files:
        try:
            text = open(f, encoding="utf-8").read()
        except OSError as e:
            print(f"skip {f}: {e}")
            continue
        new, recs = fix_superlatives(text)
        fixes, review, unver, lines = summarize(recs)
        total_fix += len(fixes); total_review += len(review); total_unver += len(unver)
        if lines:
            print(f"\n{f}")
            print("\n".join(lines))
        if apply and fixes:
            with open(f, "w", encoding="utf-8") as fh:
                fh.write(new)
    mode = "APPLIED" if apply else "DRY RUN (nothing written; add --apply)"
    print(f"\n{mode}: {total_fix} wrong superlative(s) rewritten, {total_review} need a human look, "
          f"{total_unver} absolute superlatives had no rank beside them to check "
          f"({len(files)} files)")


if __name__ == "__main__":
    main(sys.argv[1:])
