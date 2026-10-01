"""
EVIDENCE_CHECK_VALIDATOR.PY
============================
Deterministic check for a rank/tier CLAIM made in a Coeus report,
against the real evidence Coeus was actually given. Same "Coeus
proposes, a script verifies" principle as parlay_validator.py (which
checks a parlay's arithmetic) and dfs_lineup_validator.py (which
checks a lineup's real cap usage) — here applied to a report's actual
factual reasoning, not just its numbers or math.

Shared between generate_props_report.py and generate_game_breakdown.py
(2026-09-21) rather than duplicated in each — both scripts ask Coeus
to cite real ranks, both need the identical real check against
identical real evidence shapes, and a fix made in one copy would
otherwise risk silently not applying to the other.

REAL, CONFIRMED FAILURE CASE THIS EXISTS TO CATCH (2026-09-21): a real
props report's pick reasoning stated Minnesota's real 2025 pass
defense ranked "32nd... the weakest in the league." The real evidence
Coeus was actually given for that exact claim — Jordan Love's own log
entry for that real Week 1 meeting — states plainly
`"tier": "top", "ranks": {"pass_yds": 2}`: Minnesota's real defense
ranked 2nd, not 32nd, the near-exact opposite of what was written. The
evidence itself was correct; the written claim directly contradicted
evidence Coeus had already been given. Frank independently caught a
second, similar case in a real Game Breakdown, which is why this
check now runs there too.

REWRITE (2026-09-30), per Frank's direct request and a real, confirmed
case (Week 4 GB_TB.md): of the 8 current_opponent "mismatches" that
run flagged, 6 were false alarms and the other 2 (Tucker Kraft, Emeka
Egbuka) turned out correct too, once Frank pointed out the real
methodology (Threats ranks only among players with 3+ games — see
build_matchup_stats.py's build_threats(), MIN_GAMES). Every one of
those 8 traced to the SAME root cause: this file was checking a claim
against evidence_bootstrap's own frozen, per-game COPY of a number,
never against Football Intel's actual live stats — and that frozen
copy doesn't always represent the same thing the live site does
(a team-WIDE position-group total and one INDIVIDUAL starter's own
total can legitimately share the exact same team+pos+stat "address"
in Coeus's claim schema, with no player-name field to tell them
apart). Frank's own direct words: "I think the evidence checker
should be checking the actual stats on Football Intel. All of the
available stats." So current_opponent claims now check DIRECTLY
against this project's own live, already-published data files —
matchup/wk{NN}.json, threats/wk{NN}.json, and teamstats/latest.json —
the same files the site itself is built from, rather than trusting
evidence_bootstrap's own internal copies. The frozen evidence package
is still consulted too, as a last-resort fallback only (see
_legacy_current_opponent_rank below) for any claim shape the live
files genuinely don't cover, so this rewrite can only ever catch MORE
real errors than before, never fewer.

log_opponent and rank_shift claims are untouched by this rewrite and
still check against the frozen evidence package — those are
legitimately about what Coeus was actually handed (a player's own
past-week log entry, a precomputed 2025-vs-2026 comparison), not
about today's live site, so pinning them to the frozen evidence is
correct, not a limitation.

Deliberately scoped to the real sources of rank data this project has
directly, repeatedly confirmed the real shape of — not a general
parser of arbitrary prose. Regex over free-form report text would be
unreliable both ways: missing real errors phrased slightly
differently, and false-flagging correct claims phrased in a way that
doesn't match a pattern. Instead, each Standard requires Coeus to
ALSO state any such claim in a small, structured, machine-checkable
list — never instead of the human-readable prose, alongside it — so
this function can confirm it against real, live data rather than
trusting the prose alone:

  - "log_opponent": a claim about a named player's own PAST game log
    entry's tagged opponent rank (the exact real source of the
    Love/MIN error) — checked against that player's own real evidence
    record for that exact real week.
  - "current_opponent": a claim about THIS WEEK'S real opponent's
    rank in a stat category — checked against this project's own
    live stat files (matchup/threats/teamstats), falling back to the
    frozen per-game evidence only if the live files can't cover it.
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# Reuse the exact, already-correct live-ranking helpers
# build_evidence_package_bootstrap.py itself uses to build Down/Distance
# and Red Zone Play Calling ranks from teamstats/latest.json, rather than
# writing a second, independent copy of the same sort-and-rank logic —
# a second copy is exactly the kind of quiet divergence this whole
# rewrite exists to stop happening again.
from build_evidence_package_bootstrap import rank_teams_by, RED_ZONE_KEY

POS_LIST = ("QB", "RB", "WR", "TE")

# (role, stat) -> which of the six precomputed rank dicts below to use.
# These six real stats never live in matchup/wkNN.json's team_off/team_def
# at all — only in teamstats/latest.json's raw Down/Distance and Red Zone
# Play Calling subgroups — confirmed directly against
# build_evidence_package_bootstrap.py's own down_distance_for_team() /
# red_zone_for_team() (see their real field lists).
TEAM_EXTRA_STAT_MAP = {
    ("off", "third_down_conversion_pct"): "dd_off",
    ("def", "third_down_pct_allowed"): "dd_def",
    ("off", "red_zone_run_pct"): "rz_off_run",
    ("off", "red_zone_pass_pct"): "rz_off_pass",
    ("def", "red_zone_run_pct_allowed"): "rz_def_run",
    ("def", "red_zone_pass_pct_allowed"): "rz_def_pass",
}

# REAL BUG FIX (2026-10-01), per Frank's direct catch (Week 4 batch
# covering LAR@PHI/GB@TB/MIA@MIN/KC@LV): every "off"-role RB rushing
# claim tagged `stat: "rush_ypg"` came back REAL MISMATCH (Kyren
# Williams, Bucky Irving, Aaron Jones, Ashton Jeanty, Kenneth Walker
# III, Saquon Barkley — six separate players, same exact shape), while
# every QB/WR claim in the identical run validated clean. Root cause:
# build_matchup_stats.py's THREAT_CATS (threats/wkNN.json, each
# starter's own individual per-game rank) stores this stat under the
# key "rush_yds" (RB) / "pass_yds" (QB) — NOT the "_ypg" spelling
# Coeus's own internal field-naming convention uses for a per-game
# rate (POS_METRICS, matchup/wkNN.json's GROUP-level fields, which
# really does have a separate, correctly-spelled "rush_ypg"/"pass_ypg"
# key). A claim tagged "rush_ypg" therefore never matched any
# individual starter's cats dict below — it silently fell through to
# ONLY the team-wide RB-group rank (matchup.json), which is a real,
# different number whenever a team splits carries across a committee
# backfield (exactly why this surfaced on RBs specifically and never
# on QBs, who are almost always a true one-starter position where the
# group rank and the individual's own rank coincide anyway, masking
# the identical gap). This maps a claim's "_ypg" spelling to the real
# THREAT_CATS key so the individual starter's own entry is actually
# found and checked, the same way group-level fields already are.
THREAT_STAT_ALIAS = {
    "rush_ypg": "rush_yds",
    "rec_ypg": "rec_yds",
    "pass_ypg": "pass_yds",
    "pass_td": "pass_tds",
}


def _load_json(path):
    if not os.path.exists(path):
        return None
    with open(path) as f:
        return json.load(f)


_live_week_cache = {}


def load_live_week(week):
    """This project's own live, already-published data files for a given
    week — matchup/wk{week}.json (team + position-group off/def, ranks
    already computed), threats/wk{week}.json (each team's starters,
    ranked among players with 3+ games — the Threat Engine's own real,
    documented methodology), and teamstats/latest.json (whole-team
    season totals, used to recompute Down/Distance and Red Zone ranks
    the identical way build_evidence_package_bootstrap.py does). Any
    file that doesn't exist on disk comes back None rather than
    raising — callers treat a None file as "this live source can't
    cover this claim" and fall back accordingly, they never crash on
    a missing file (e.g. an older archived week). Cached per week per
    process since a single validator run checks many claims against
    the same week's files."""
    if week in _live_week_cache:
        return _live_week_cache[week]
    wk = f"wk{week:02d}" if isinstance(week, int) else str(week)
    data = {
        "matchup": _load_json(f"matchup/{wk}.json"),
        "threats": _load_json(f"threats/{wk}.json"),
        "teamstats": _load_json("teamstats/latest.json"),
    }
    _live_week_cache[week] = data
    return data


def resolve_claim_week(game_evidence):
    """Which week's live files a game's current_opponent claims should be
    checked against: the bootstrap week for an upcoming-game evidence
    package (evidence["bootstrap_source"]["week"] — e.g. week 3 stats
    used as the foundation for a week 4 preview, exactly GB_TB.md's real
    case), or the evidence's own top-level "week" for an already-played
    game's evidence package (see build_evidence_package.py)."""
    bsrc = (game_evidence or {}).get("bootstrap_source") or {}
    if bsrc.get("week") is not None:
        return bsrc["week"]
    return (game_evidence or {}).get("week")


_team_extra_ranks_cache = {}


def _team_extra_ranks(teamstats_json):
    """Down/Distance and Red Zone Play Calling ranks the identical way
    build_evidence_package_bootstrap.py computes them (see its own
    dd_off_ranks/dd_def_ranks/rz_*_ranks) — reusing rank_teams_by()
    itself rather than re-deriving a third copy of this sort-and-rank
    logic. Cached by id(teamstats_json) since there's only ever one
    teamstats/latest.json loaded per process."""
    key = id(teamstats_json)
    if key in _team_extra_ranks_cache:
        return _team_extra_ranks_cache[key]
    if not teamstats_json:
        result = {}
    else:
        result = {
            "dd_off": rank_teams_by(teamstats_json, "offense", "d3_pct", ascending=False),
            "dd_def": rank_teams_by(teamstats_json, "defense", "d3_pct_allowed", ascending=True),
            "rz_off_run": rank_teams_by(teamstats_json, "offense", "rz_run_pct",
                                         subgroup=RED_ZONE_KEY, ascending=False),
            "rz_off_pass": rank_teams_by(teamstats_json, "offense", "rz_pass_pct",
                                          subgroup=RED_ZONE_KEY, ascending=False),
            "rz_def_run": rank_teams_by(teamstats_json, "defense", "rz_run_pct_faced",
                                         subgroup=RED_ZONE_KEY, ascending=False),
            "rz_def_pass": rank_teams_by(teamstats_json, "defense", "rz_pass_pct_faced",
                                          subgroup=RED_ZONE_KEY, ascending=False),
        }
    _team_extra_ranks_cache[key] = result
    return result


def live_current_opponent_ranks(live, team, pos, stat, role, opponent=None):
    """Returns the SET of real ranks `stat` could legitimately refer to
    for `team` (role="off"/"def", pos="TEAM" or a position code) —
    drawn from every live source that's actually relevant to that claim
    shape — or None if none of the live files needed to check it could
    be loaded at all (caller should fall back to the frozen evidence
    package in that case; an EMPTY set, by contrast, means the live
    files loaded fine but genuinely don't have this exact stat).

    THE REAL AMBIGUITY THIS RESOLVES (confirmed directly, GB_TB.md,
    2026-09-30): `off.WR.rec_yds` (a team's WHOLE WR corps combined)
    and one individual starter's own `rec_yds` are two real, different,
    correctly-computed numbers that just happen to share the same
    team+pos+stat "address" in Coeus's claim schema — there's no
    player-name field to tell them apart. Rather than guess which one
    a given claim meant, this checks it against BOTH the live
    position-group number (matchup/wkNN.json) and every starter's own
    live individual number at that position (threats/wkNN.json) and
    accepts a match against either. A real error still gets caught (it
    won't match ANY of them); a correct claim never gets falsely
    flagged just because it was individual rather than group-level.

    THE SECOND REAL AMBIGUITY THIS RESOLVES (also confirmed directly,
    GB_TB.md): a role="def" claim's `team` field sometimes names the
    OFFENSIVE player's own team, not the defense actually being
    described — e.g. "TB QB def pass_yds: 12" turned out to be GB's
    pass defense (the one Baker Mayfield, TB's QB, actually faces),
    mislabeled under TB. When `opponent` is given (the caller knows
    this game's other team), a role="def" pos-specific claim is also
    checked against the OPPONENT's own live defensive number at that
    position, not just the named team's."""
    matchup = live.get("matchup")
    threats = live.get("threats")
    found = set()

    if pos == "TEAM":
        if matchup:
            team_data = (matchup.get("teams") or {}).get(team) or {}
            group = team_data.get("team_off") if role == "off" \
                else team_data.get("team_def") if role == "def" else None
            cell = (group or {}).get(stat) if isinstance(group, dict) else None
            if isinstance(cell, dict) and cell.get("r") is not None:
                found.add(cell["r"])
        teamstats = live.get("teamstats")
        extra_key = TEAM_EXTRA_STAT_MAP.get((role, stat))
        if extra_key and teamstats is not None:
            extra = _team_extra_ranks(teamstats)
            cell = (extra.get(extra_key) or {}).get(team)
            if cell and cell.get("r") is not None:
                found.add(cell["r"])
        if matchup is None and teamstats is None:
            return None
        return found

    if matchup is None and threats is None:
        return None

    if matchup:
        team_data = (matchup.get("teams") or {}).get(team) or {}
        group = (team_data.get(role) or {}).get(pos)
        cell = (group or {}).get(stat) if isinstance(group, dict) else None
        if isinstance(cell, dict) and cell.get("r") is not None:
            found.add(cell["r"])
        if role == "def" and opponent:
            opp_data = (matchup.get("teams") or {}).get(opponent) or {}
            opp_group = (opp_data.get("def") or {}).get(pos)
            opp_cell = (opp_group or {}).get(stat) if isinstance(opp_group, dict) else None
            if isinstance(opp_cell, dict) and opp_cell.get("r") is not None:
                found.add(opp_cell["r"])

    if threats and role == "off":
        # threats.json only models each team's OWN starters' OFFENSIVE
        # production (see build_matchup_stats.py's build_threats(),
        # THREAT_CATS/LINEUP) — there's no "def" side in it at all, so a
        # role="def" claim is never checked against it.
        team_threat = (threats.get("teams") or {}).get(team) or {}
        threat_stat = THREAT_STAT_ALIAS.get(stat, stat)
        for starter in (team_threat.get("starters") or []):
            if starter.get("pos") != pos:
                continue
            cats = starter.get("cats") or {}
            cell = cats.get(stat)
            if not (isinstance(cell, dict) and cell.get("r") is not None) and threat_stat != stat:
                cell = cats.get(threat_stat)
            if isinstance(cell, dict) and cell.get("r") is not None:
                found.add(cell["r"])

    return found


def find_player_evidence(game_evidence, player_name):
    """Real players are stored under evidence["players"]["away"/"home"]
    in every evidence package this project produces (bootstrap or
    otherwise) — this is the one place that assumption lives, so a
    real schema change only ever needs updating here."""
    players = (game_evidence or {}).get("players") or {}
    for side in ("away", "home"):
        for p in (players.get(side) or []):
            if isinstance(p, dict) and p.get("name") == player_name:
                return p
    return None


def _legacy_current_opponent_rank(evidence_by_game, team, pos, stat, role):
    """LAST-RESORT fallback only, used when the live files (matchup/
    threats/teamstats) couldn't cover a claim at all — e.g. an older
    archived week whose live files have since been pruned. Checks the
    frozen per-game evidence package exactly as this file did before
    the 2026-09-30 live-data rewrite. Returns a rank or None — never
    called at all when live data already resolved the claim, so this
    can only ever add coverage, not take any away."""
    for game_evidence in evidence_by_game.values():
        game_info = game_evidence.get("game") or {}
        side = ("away" if game_info.get("away") == team
                 else "home" if game_info.get("home") == team else None)
        if side is None:
            continue
        side_data = (game_evidence.get("matchup") or {}).get(side)
        if not isinstance(side_data, dict):
            continue
        if pos == "TEAM":
            group = side_data.get("team_off") if role == "off" \
                else side_data.get("team_def") if role == "def" else None
            cell = (group or {}).get(stat) if isinstance(group, dict) else None
            side_group = "offense" if role == "off" else "defense" if role == "def" else None
            if not (isinstance(cell, dict) and cell.get("r") is not None) and side_group:
                for block_key in ("down_distance", "red_zone_play_calling"):
                    block = (game_evidence.get(block_key) or {}).get(side) or {}
                    group2 = block.get(side_group)
                    cell2 = (group2 or {}).get(stat) if isinstance(group2, dict) else None
                    if isinstance(cell2, dict) and cell2.get("r") is not None:
                        cell = cell2
                        break
        else:
            group = (side_data.get(role) or {}).get(pos)
            cell = (group or {}).get(stat) if isinstance(group, dict) else None
        if isinstance(cell, dict) and cell.get("r") is not None:
            return cell.get("r")
    return None


def verify_evidence_check(evidence_check, evidence_by_game):
    """evidence_check: a list of real, structured claim dicts (see the
    shapes described above). evidence_by_game: a dict keyed by (away,
    home) tuples -> that real game's own trimmed evidence package,
    exactly as it was actually sent this run — whichever caller built
    it (one game for generate_game_breakdown.py, several for
    generate_props_report.py's multi-game runs).

    Returns a list of real, human-readable mismatch descriptions —
    empty when every real claim checks out. Searches across ALL real,
    retained games' evidence (not just one specific away/home) since a
    claim isn't always tied to a single game's own context — a
    favorite pick or parlay leg in generate_props_report.py can name
    any player from any game in the run; a player's name
    (log_opponent) or a team code (current_opponent) is looked up
    wherever it's actually found in the real evidence that was sent."""
    if not evidence_check:
        return []
    mismatches = []
    for claim in evidence_check:
        ctype = claim.get("type")
        claimed_rank = claim.get("claimed_rank")

        if ctype == "log_opponent":
            player_name, week, stat = claim.get("player"), claim.get("week"), claim.get("stat")
            p = None
            for game_evidence in evidence_by_game.values():
                p = find_player_evidence(game_evidence, player_name)
                if p is not None:
                    break
            if p is None:
                mismatches.append(f"evidence_check cites {player_name}'s week {week} log, but "
                                   f"no real evidence record for {player_name} was found in "
                                   f"any game's real evidence sent this run.")
                continue
            log_entry = next((e for e in (p.get("log") or []) if e.get("week") == week), None)
            if log_entry is None:
                mismatches.append(f"evidence_check cites {player_name}'s week {week} log entry, "
                                   f"but no real log entry for that week exists in the evidence "
                                   f"actually provided (it may have been trimmed) — this claim "
                                   f"can't be verified against what Coeus was actually given.")
                continue
            real_rank = (log_entry.get("ranks") or {}).get(stat)
            if real_rank is None:
                mismatches.append(f"evidence_check cites {player_name}'s week {week} {stat} rank, "
                                   f"but the real log entry has no ranks.{stat} field at all.")
            elif real_rank != claimed_rank:
                mismatches.append(f"REAL MISMATCH: {player_name}'s real week {week} log entry "
                                   f"shows their opponent ranked #{real_rank} in {stat} — the "
                                   f"report claimed #{claimed_rank}.")

        elif ctype == "current_opponent":
            team, pos, stat, role = claim.get("team"), claim.get("pos"), claim.get("stat"), claim.get("role")

            # Find which game (and this claim's week + opponent) this
            # team belongs to, so live files can be loaded and, for a
            # "def" claim, the opponent's own defense can be checked too.
            week, opponent = None, None
            for game_evidence in evidence_by_game.values():
                game_info = game_evidence.get("game") or {}
                if game_info.get("away") == team:
                    week, opponent = resolve_claim_week(game_evidence), game_info.get("home")
                    break
                if game_info.get("home") == team:
                    week, opponent = resolve_claim_week(game_evidence), game_info.get("away")
                    break

            found_ranks = None
            if week is not None:
                live = load_live_week(week)
                found_ranks = live_current_opponent_ranks(live, team, pos, stat, role, opponent)

            if found_ranks is not None and claimed_rank in found_ranks:
                continue  # verified live — matches the actual, current stat on Football Intel

            # Live files didn't confirm it outright — fall back to the
            # frozen evidence package too (covers both "live files truly
            # unavailable" and "live files loaded but this exact stat
            # wasn't in them") before calling it a real mismatch.
            legacy_rank = _legacy_current_opponent_rank(evidence_by_game, team, pos, stat, role)
            if legacy_rank is not None:
                if found_ranks is None:
                    found_ranks = set()
                found_ranks.add(legacy_rank)

            if claimed_rank in (found_ranks or set()):
                continue
            if not found_ranks:
                mismatches.append(f"evidence_check cites {team}'s current {pos} {role} {stat} "
                                   f"rank, but no real data for that exact combination could be "
                                   f"found on Football Intel (live stats or evidence actually "
                                   f"provided).")
            else:
                real_desc = " or ".join(f"#{r}" for r in sorted(found_ranks))
                mismatches.append(f"REAL MISMATCH: {team}'s real current {pos} {role} {stat} "
                                   f"rank is {real_desc} — the report claimed #{claimed_rank}.")

        # REAL ADDITION (2026-09-22), per Frank's direct request: checks
        # a real 2025-vs-2026 rank-shift claim against evidence["rank_shifts"]
        # (see build_evidence_package_bootstrap.py's build_rank_shift_summary()
        # for how that real, pre-computed data is built). Genuinely
        # different lookup shape than current_opponent above — rank_shifts
        # is keyed by "away"/"home" per game, not by team code directly, so
        # each real game's own real game.away/game.home is used to resolve
        # which side the named team is actually on before reading its data.
        # Unaffected by the 2026-09-30 live-data rewrite above — a 2025-
        # vs-2026 SHIFT comparison is inherently about what Coeus was
        # actually given, not today's live stats.
        elif ctype == "rank_shift":
            team, side, stat = claim.get("team"), claim.get("side"), claim.get("stat")
            side_label = "offense" if side == "off" else "defense" if side == "def" else side
            claimed_2025, claimed_2026 = claim.get("claimed_rank_2025"), claim.get("claimed_rank_2026")
            entry = None
            for game_evidence in evidence_by_game.values():
                game_info = game_evidence.get("game") or {}
                game_side = "away" if game_info.get("away") == team else "home" if game_info.get("home") == team else None
                if game_side is None:
                    continue
                shifts = ((game_evidence.get("rank_shifts") or {}).get(game_side) or {}).get(side_label) or {}
                if stat in shifts:
                    entry = shifts[stat]
                    break
            if entry is None:
                mismatches.append(f"evidence_check cites {team}'s {side_label} {stat} rank shift, "
                                   f"but no real rank_shifts data for that exact combination "
                                   f"exists in any game's evidence actually provided.")
                continue
            real_2025, real_2026 = entry.get("rank_2025"), entry.get("rank_2026")
            if claimed_2025 is not None and real_2025 != claimed_2025:
                mismatches.append(f"REAL MISMATCH: {team}'s real 2025 {side_label} {stat} rank "
                                   f"is #{real_2025} — the report claimed #{claimed_2025}.")
            if claimed_2026 is not None and real_2026 != claimed_2026:
                mismatches.append(f"REAL MISMATCH: {team}'s real 2026 {side_label} {stat} rank "
                                   f"is #{real_2026 if real_2026 is not None else 'not yet available'} "
                                   f"— the report claimed #{claimed_2026}.")
        else:
            mismatches.append(f"evidence_check entry has an unrecognized type: {ctype!r}.")

    return mismatches
