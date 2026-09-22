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

Deliberately scoped to the two real sources of rank data this project
has directly, repeatedly confirmed the real shape of — not a general
parser of arbitrary prose. Regex over free-form report text would be
unreliable both ways: missing real errors phrased slightly
differently, and false-flagging correct claims phrased in a way that
doesn't match a pattern. Instead, each Standard requires Coeus to
ALSO state any such claim in a small, structured, machine-checkable
list — never instead of the human-readable prose, alongside it — so
this function can confirm it against the real evidence actually
provided rather than trusting the prose alone:

  - "log_opponent": a claim about a named player's own PAST game log
    entry's tagged opponent rank (the exact real source of the
    Love/MIN error) — checked against that player's own real evidence
    record for that exact real week.
  - "current_opponent": a claim about THIS WEEK'S real opponent's
    rank in a stat category — checked against the real matchup block
    in that game's own evidence.
"""


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


def verify_evidence_check(evidence_check, evidence_by_game):
    """evidence_check: a list of real, structured claim dicts (see the
    two real shapes described above). evidence_by_game: a dict keyed
    by (away, home) tuples -> that real game's own trimmed evidence
    package, exactly as it was actually sent this run — whichever
    caller built it (one game for generate_game_breakdown.py, several
    for generate_props_report.py's multi-game runs).

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
            real_rank = None
            for game_evidence in evidence_by_game.values():
                matchup = (game_evidence.get("matchup") or {}).get(team)
                if matchup is None:
                    continue
                cell = (matchup.get(role) or {}).get(pos, {}).get(stat)
                if isinstance(cell, dict) and cell.get("r") is not None:
                    real_rank = cell.get("r")
                    break
            if real_rank is None:
                mismatches.append(f"evidence_check cites {team}'s current {pos} {role} {stat} "
                                   f"rank, but no real matchup data for that exact combination "
                                   f"exists in any game's evidence actually provided.")
            elif real_rank != claimed_rank:
                mismatches.append(f"REAL MISMATCH: {team}'s real current {pos} {role} {stat} "
                                   f"rank is #{real_rank} — the report claimed #{claimed_rank}.")

        # REAL ADDITION (2026-09-22), per Frank's direct request: checks
        # a real 2025-vs-2026 rank-shift claim against evidence["rank_shifts"]
        # (see build_evidence_package_bootstrap.py's build_rank_shift_summary()
        # for how that real, pre-computed data is built). Genuinely
        # different lookup shape than current_opponent above — rank_shifts
        # is keyed by "away"/"home" per game, not by team code directly, so
        # each real game's own real game.away/game.home is used to resolve
        # which side the named team is actually on before reading its data.
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
