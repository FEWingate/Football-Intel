#!/usr/bin/env python3
"""
PATCH_CHEAT_SHEET_OPPONENT_STATS.PY
====================================
REAL ONE-OFF/REPEATABLE CLEANUP (2026-10-02), per Frank's direct request:
the Coeus Cheat Sheet (Standard v2.5, Section 8) is meant to let a reader
(Frank's son, specifically) get a game's key numbers in a few seconds
without reading the full breakdown — but the opponent defense's matching
rank+yardage-allowed number for each stat category only appeared once,
grouped under "Team Defense", not next to the individual player it
actually applies to. A reader has to cross-reference down to Team Defense
and remember which team is which to connect a QB's pass yds/gm to how
tough his opponent's pass defense actually is.

This script does NOT regenerate anything (no API cost, no re-reading the
evidence package) — it only re-reads data ALREADY PRESENT in each file's
own Team Defense bullets and appends the matching opponent figure onto
each individual player's own Passing/Rushing/Receiving line. Going
forward, the Standard itself has a separate fix (see the prompt edit
delivered alongside this script) so new breakdowns include this from the
start — this script is only for breakdowns already generated under the
OLD Standard wording.

SAFETY: defaults to a dry run (prints exactly what would change, touches
nothing). Pass --apply to actually write. Every file that IS written gets
a .bak backup first. Any line this script isn't confident it parsed
correctly is left untouched and reported, never guessed at.

Usage:
  python3 patch_cheat_sheet_opponent_stats.py wk04            # dry run
  python3 patch_cheat_sheet_opponent_stats.py wk04 --apply    # writes for real
"""
import os
import re
import sys
import glob

STAT_TAGS = {
    "pass": "pass",
    "rush": "rush",
    "rec_wr": "WR",
    "rec_te": "TE",
    "rec_rb": "RB",
}

# A rank in parentheses isn't always just "(23rd)" — real files have been
# seen with trailing qualifiers inside the same parens, e.g.
# "(26th, team-wide)". Capture the digits, tolerate anything else up to
# the closing paren.
RANK_RE = r'\(\s*(\d+)[a-z]{2}[^)]*\)'

# REAL FORMAT-DRIFT FIX (2026-10-02): Frank's actual generated files use at
# least three different punctuation styles for these same two sections,
# confirmed across real pasted examples — hyphen `-` bullets vs asterisk
# `*`, a literal "def:" word after the team code vs none, `|` vs `,` as
# the stat separator, "WR yds/gm allowed" (no "rec") vs "WR rec yds/gm
# allowed", and — newly confirmed — full team names ("Atlanta", "New
# Orleans") instead of abbreviations, and a "WR: 201.3 rec yds/gm allowed"
# label-before-number order instead of number-before-label. Coeus's own
# wording isn't byte-identical between generations, so all of these are
# tolerated below rather than assuming one canonical format.
TEAM_DEF_LINE_RE = re.compile(r'^[-*]\s*(?P<team>[A-Za-z][A-Za-z .]*?)(?:\s+def)?:\s*(?P<rest>.+)$')
PLAYER_LINE_RE = re.compile(
    # REAL BUG FIX (2026-10-02), caught in testing: a position tag with no
    # trailing digit ("LAR WR" rather than "LAR WR1" — a real, confirmed
    # case in Frank's actual pasted example, Konata Mumpfield) used to
    # require a digit inside the alternation, which made the ENTIRE line
    # fail to match (not just the tag), so that player was silently
    # skipped with no report line at all. The digit is now optional.
    # Also made the bullet character tolerant of both `-` and `*` (real
    # format drift confirmed in Frank's actual regenerated files), and the
    # separator before the position tag tolerant of a space OR a comma
    # (e.g. "(LAR WR1)" vs "(LAR, WR)").
    r'^[-*]\s*(?P<name>[^(]+?)\s*\((?P<team>[A-Z]{2,3})(?:[\s,]+(?P<postag>WR\d?|TE\d?|RB\d?))?\):\s*(?P<rest>.+)$'
)

# Full team names seen in place of abbreviations in Team Defense lines
# (e.g. "Atlanta: ..." instead of "ATL def: ..."). City-only names like
# "Los Angeles" and "New York" are genuinely ambiguous (two NFL teams
# each) and are resolved using the two team codes implied by the file's
# own name (see resolve_team_token).
TEAM_FULL_NAMES = {
    "ARI": ["Arizona", "Cardinals", "Arizona Cardinals"],
    "ATL": ["Atlanta", "Falcons", "Atlanta Falcons"],
    "BAL": ["Baltimore", "Ravens", "Baltimore Ravens"],
    "BUF": ["Buffalo", "Bills", "Buffalo Bills"],
    "CAR": ["Carolina", "Panthers", "Carolina Panthers"],
    "CHI": ["Chicago", "Bears", "Chicago Bears"],
    "CIN": ["Cincinnati", "Bengals", "Cincinnati Bengals"],
    "CLE": ["Cleveland", "Browns", "Cleveland Browns"],
    "DAL": ["Dallas", "Cowboys", "Dallas Cowboys"],
    "DEN": ["Denver", "Broncos", "Denver Broncos"],
    "DET": ["Detroit", "Lions", "Detroit Lions"],
    "GB": ["Green Bay", "Packers", "Green Bay Packers"],
    "HOU": ["Houston", "Texans", "Houston Texans"],
    "IND": ["Indianapolis", "Colts", "Indianapolis Colts"],
    "JAX": ["Jacksonville", "Jaguars", "Jacksonville Jaguars"],
    "KC": ["Kansas City", "Chiefs", "Kansas City Chiefs"],
    "LAC": ["LA Chargers", "Los Angeles Chargers", "Chargers"],
    "LAR": ["LA Rams", "Los Angeles Rams", "Rams"],
    "LV": ["Las Vegas", "Raiders", "Las Vegas Raiders"],
    "MIA": ["Miami", "Dolphins", "Miami Dolphins"],
    "MIN": ["Minnesota", "Vikings", "Minnesota Vikings"],
    "NE": ["New England", "Patriots", "New England Patriots"],
    "NO": ["New Orleans", "Saints", "New Orleans Saints"],
    "NYG": ["NY Giants", "New York Giants", "Giants"],
    "NYJ": ["NY Jets", "New York Jets", "Jets"],
    "PHI": ["Philadelphia", "Eagles", "Philadelphia Eagles"],
    "PIT": ["Pittsburgh", "Steelers", "Pittsburgh Steelers"],
    "SEA": ["Seattle", "Seahawks", "Seattle Seahawks"],
    "SF": ["San Francisco", "49ers", "San Francisco 49ers"],
    "TB": ["Tampa Bay", "Buccaneers", "Tampa Bay Buccaneers"],
    "TEN": ["Tennessee", "Titans", "Tennessee Titans"],
    "WAS": ["Washington", "Commanders", "Washington Commanders"],
}
NAME_TO_ABBR = {}
for _abbr, _names in TEAM_FULL_NAMES.items():
    for _n in _names:
        NAME_TO_ABBR[_n.lower()] = _abbr


def resolve_team_token(token, expected_teams):
    """Normalize a Team Defense line's team identifier (abbreviation OR
    full name) to one of the two abbreviations implied by the filename.
    Returns None if it can't be confidently resolved — callers must skip
    rather than guess in that case."""
    token = token.strip()
    if token.upper() in expected_teams:
        return token.upper()
    key = token.lower()
    if key in NAME_TO_ABBR and NAME_TO_ABBR[key] in expected_teams:
        return NAME_TO_ABBR[key]
    # Ambiguous city-only names: disambiguate using the file's own two teams.
    if key == "los angeles":
        candidates = [t for t in expected_teams if t in ("LAC", "LAR")]
        if len(candidates) == 1:
            return candidates[0]
    if key == "new york":
        candidates = [t for t in expected_teams if t in ("NYG", "NYJ")]
        if len(candidates) == 1:
            return candidates[0]
    return None


def extract_stat(rest, key):
    tag = STAT_TAGS[key]
    is_rec = key.startswith("rec_")
    candidates = []
    if is_rec:
        # "167.7 WR rec yds/gm allowed (23rd)" or "167.7 WR yds/gm allowed
        # (23rd)" — number before the tag, "rec" optional.
        candidates.append(r'([\d.]+)\s+' + tag + r'\s+(?:rec\s+)?yds/gm allowed\s*' + RANK_RE)
        # "WR: 201.3 rec yds/gm allowed (32nd)" — tag prefix before the
        # number (real format drift confirmed in ATL_NO.md).
        candidates.append(tag + r':\s*([\d.]+)\s+(?:rec\s+)?yds/gm allowed\s*' + RANK_RE)
    else:
        candidates.append(r'([\d.]+)\s+' + tag + r'\s+yds/gm allowed\s*' + RANK_RE)
    for pat in candidates:
        m = re.search(pat, rest)
        if m:
            return float(m.group(1)), int(m.group(2))
    return None


def ordinal(n):
    if 10 <= n % 100 <= 20:
        suf = "th"
    else:
        suf = {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return f"{n}{suf}"


def parse_team_defense(block_lines, expected_teams):
    """Returns {team: {'pass': (val, rank), 'rush': (...), 'rec_wr': (...), ...}}
    Team keys are always normalized to the abbreviation form, even when the
    source line used a full team name."""
    out = {}
    for line in block_lines:
        m = TEAM_DEF_LINE_RE.match(line.strip())
        if not m:
            continue
        team_token, rest = m.group("team"), m.group("rest")
        team = resolve_team_token(team_token, expected_teams)
        if team is None:
            continue
        stats = {}
        for key in STAT_TAGS:
            v = extract_stat(rest, key)
            if v:
                stats[key] = v
        out[team] = stats
    return out


def find_section(lines, header_pattern, next_header_patterns):
    """Find the line range of a bulleted subsection like **Passing** ... up
    to the next subsection header or a blank-then-header boundary."""
    start = None
    for i, line in enumerate(lines):
        if re.match(header_pattern, line.strip(), re.IGNORECASE):
            start = i + 1
            break
    if start is None:
        return None, None
    end = len(lines)
    for j in range(start, len(lines)):
        stripped = lines[j].strip()
        if any(re.match(p, stripped, re.IGNORECASE) for p in next_header_patterns):
            end = j
            break
    return start, end


HEADERS = {
    "team": r'^\*{0,2}Team\*{0,2}$',
    "passing": r'^\*{0,2}Passing\*{0,2}$',
    "rushing": r'^\*{0,2}Rushing\*{0,2}$',
    "receiving": r'^\*{0,2}Receiving\*{0,2}$',
    "team_defense": r'^\*{0,2}Team Defense\*{0,2}$',
    "down_distance": r'^\*{0,2}Down/Distance.*\*{0,2}$',
}
ALL_HEADER_PATTERNS = list(HEADERS.values())


def patch_file(path, apply_changes):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    lines = text.split("\n")

    # The filename itself ("ATL_NO.md" -> ["ATL", "NO"]) is the ground truth
    # for which two teams are in this game — used both to resolve full team
    # names in Team Defense lines and to disambiguate "Los Angeles"/"New York".
    expected_teams = [t.upper() for t in os.path.splitext(os.path.basename(path))[0].split("_")]

    td_start, td_end = find_section(lines, HEADERS["team_defense"], ALL_HEADER_PATTERNS)
    if td_start is None:
        return {"file": path, "status": "skipped", "reason": "no 'Team Defense' section found"}
    team_defense = parse_team_defense(lines[td_start:td_end], expected_teams)
    if len(team_defense) != 2:
        return {"file": path, "status": "skipped",
                "reason": f"expected 2 teams in Team Defense, found {len(team_defense)}: {list(team_defense)}"}
    teams = list(team_defense.keys())

    report_lines = []
    changed = False

    for section_key, stat_key_for_no_tag in [("passing", "pass"), ("rushing", "rush")]:
        s, e = find_section(lines, HEADERS[section_key], ALL_HEADER_PATTERNS)
        if s is None:
            continue
        for i in range(s, e):
            m = PLAYER_LINE_RE.match(lines[i].strip())
            if not m:
                continue
            team = m.group("team")
            if team not in team_defense:
                report_lines.append(f"  SKIP line (unrecognized team {team!r}): {lines[i].strip()[:70]}")
                continue
            opp = [t for t in teams if t != team]
            if len(opp) != 1:
                continue
            opp_stats = team_defense[opp[0]]
            if stat_key_for_no_tag not in opp_stats:
                report_lines.append(f"  SKIP (opponent {opp[0]} has no {stat_key_for_no_tag} allowed figure): "
                                     f"{lines[i].strip()[:70]}")
                continue
            if "opp D allows" in lines[i]:
                continue  # already patched — don't double-append on a re-run
            val, rank = opp_stats[stat_key_for_no_tag]
            label = f"{STAT_TAGS[stat_key_for_no_tag]} yds/gm"
            addition = f" — opp D allows {val} {label} ({ordinal(rank)})"
            lines[i] = lines[i] + addition
            changed = True

    s, e = find_section(lines, HEADERS["receiving"], ALL_HEADER_PATTERNS)
    if s is not None:
        for i in range(s, e):
            m = PLAYER_LINE_RE.match(lines[i].strip())
            if not m:
                continue
            team = m.group("team")
            postag = m.group("postag")  # e.g. WR1, TE1, RB2
            if team not in team_defense:
                report_lines.append(f"  SKIP line (unrecognized team {team!r}): {lines[i].strip()[:70]}")
                continue
            opp = [t for t in teams if t != team]
            if len(opp) != 1:
                continue
            opp_stats = team_defense[opp[0]]
            if not postag:
                report_lines.append(f"  SKIP (no WR/TE/RB tag to match against opponent defense): "
                                     f"{lines[i].strip()[:70]}")
                continue
            pos = postag[:2]  # 'WR', 'TE', or 'RB'
            rec_key = {"WR": "rec_wr", "TE": "rec_te", "RB": "rec_rb"}.get(pos)
            if rec_key not in opp_stats:
                report_lines.append(f"  SKIP (opponent {opp[0]} has no {pos}-specific rec yds/gm allowed figure "
                                     f"in this file — not available to cite): {lines[i].strip()[:70]}")
                continue
            if "opp D allows" in lines[i]:
                continue
            val, rank = opp_stats[rec_key]
            addition = f" — opp D allows {val} {pos} rec yds/gm ({ordinal(rank)})"
            lines[i] = lines[i] + addition
            changed = True

    result = {"file": path, "status": "changed" if changed else "unchanged", "notes": report_lines}
    if changed and apply_changes:
        backup_path = path + ".bak"
        if not os.path.exists(backup_path):
            with open(backup_path, "w", encoding="utf-8") as f:
                f.write(text)
        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        result["status"] = "written"
    return result


def main():
    if len(sys.argv) < 2:
        sys.exit(f"Usage: python3 {sys.argv[0]} <week_folder e.g. wk04> [--apply]")
    week_folder = sys.argv[1]
    apply_changes = "--apply" in sys.argv[2:]

    paths = sorted(glob.glob(f"game_breakdowns/{week_folder}/*.md"))
    if not paths:
        sys.exit(f"FATAL: no .md files found in game_breakdowns/{week_folder}/")

    print(f"{'APPLYING CHANGES' if apply_changes else 'DRY RUN (no files will be modified — pass --apply to write)'} "
          f"— {len(paths)} file(s) in game_breakdowns/{week_folder}/\n")

    changed_count = skipped_count = unchanged_count = 0
    for path in paths:
        result = patch_file(path, apply_changes)
        if result["status"] == "skipped":
            skipped_count += 1
            print(f"SKIPPED  {path}: {result['reason']}")
        elif result["status"] in ("changed", "written"):
            changed_count += 1
            verb = "would update" if result["status"] == "changed" else "updated"
            print(f"{verb.upper():10s} {path}")
            for note in result["notes"]:
                print(note)
        else:
            unchanged_count += 1
            if result["notes"]:
                print(f"UNCHANGED  {path} (nothing to add)")
                for note in result["notes"]:
                    print(note)

    print(f"\n{changed_count} file(s) {'updated' if apply_changes else 'would be updated'}, "
          f"{unchanged_count} already clean/nothing to add, {skipped_count} skipped (see reasons above).")
    if not apply_changes and changed_count:
        print(f"\nRe-run with --apply to actually write these changes "
              f"(a .bak backup is made of each file before it's touched).")


if __name__ == "__main__":
    main()
