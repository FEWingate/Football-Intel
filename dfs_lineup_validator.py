"""
DFS_LINEUP_VALIDATOR.PY
========================
Deterministic check for whether a proposed 9-player lineup is legal under
DraftKings NFL Classic Salary Cap rules. This is intentionally NOT trusted
to an LLM — Coeus proposes a lineup from reasoning, this function is the
actual arithmetic/rule check, matching the "Coeus proposes, optimizer
verifies" principle from early in this project. An LLM getting salary-cap
math wrong quietly is exactly the failure mode this exists to prevent.

Real DK NFL Classic rules, confirmed current as of Aug 2026:
  - Exactly 9 roster spots: QB, RB, RB, WR, WR, WR, TE, FLEX (RB/WR/TE), DST
  - Total salary must not exceed $50,000
  - Players from at least 2 different NFL teams
  - Players from at least 2 different games
  - Max 8 players from any one team
"""

from collections import Counter

SALARY_CAP = 50000
REQUIRED_POSITIONS = {"QB": 1, "RB": 2, "WR": 3, "TE": 1, "DST": 1}
FLEX_ELIGIBLE = {"RB", "WR", "TE"}
FLEX_POOL_TOTAL = 7  # 2 RB + 3 WR + 1 TE + 1 FLEX, all from {RB, WR, TE}


def validate_dk_lineup(lineup):
    """lineup: list of dicts, each with at least name/pos/team/salary, and
    ideally game_info (e.g. "NO@DET 09/13/2026 01:00PM ET") for the
    multi-game check. Returns (is_valid, errors, total_salary)."""
    errors = []

    if len(lineup) != 9:
        errors.append(f"Lineup has {len(lineup)} players, needs exactly 9.")

    total_salary = sum(p.get("salary", 0) for p in lineup)
    if total_salary > SALARY_CAP:
        errors.append(f"Total salary ${total_salary:,} exceeds the ${SALARY_CAP:,} cap "
                       f"by ${total_salary - SALARY_CAP:,}.")

    pos_counts = Counter(p.get("pos") for p in lineup)
    for pos in ("QB", "DST"):
        actual = pos_counts.get(pos, 0)
        if actual != REQUIRED_POSITIONS[pos]:
            errors.append(f"Needs exactly {REQUIRED_POSITIONS[pos]} {pos}, has {actual}.")

    rb, wr, te = pos_counts.get("RB", 0), pos_counts.get("WR", 0), pos_counts.get("TE", 0)
    if rb < REQUIRED_POSITIONS["RB"]:
        errors.append(f"Needs at least {REQUIRED_POSITIONS['RB']} RB, has {rb}.")
    if wr < REQUIRED_POSITIONS["WR"]:
        errors.append(f"Needs at least {REQUIRED_POSITIONS['WR']} WR, has {wr}.")
    if te < REQUIRED_POSITIONS["TE"]:
        errors.append(f"Needs at least {REQUIRED_POSITIONS['TE']} TE, has {te}.")
    flex_total = rb + wr + te
    if flex_total != FLEX_POOL_TOTAL:
        errors.append(f"RB+WR+TE total is {flex_total}, needs exactly {FLEX_POOL_TOTAL} "
                       f"(2 RB + 3 WR + 1 TE + 1 FLEX).")

    other_positions = set(pos_counts) - {"QB", "RB", "WR", "TE", "DST"}
    if other_positions:
        errors.append(f"Unexpected position(s) in lineup: {sorted(other_positions)}.")

    teams = set(p.get("team") for p in lineup)
    if len(teams) < 2:
        errors.append(f"Only {len(teams)} distinct team(s) — DK requires at least 2.")

    team_counts = Counter(p.get("team") for p in lineup)
    max_from_one_team = max(team_counts.values()) if team_counts else 0
    if max_from_one_team > 8:
        errors.append(f"{max_from_one_team} players from one team — DK max is 8.")

    games = set(p.get("game_info") for p in lineup if p.get("game_info"))
    if len(games) < 2:
        errors.append(f"Only {len(games)} distinct game(s) represented (based on available "
                       f"game_info data) — DK requires at least 2.")

    return (len(errors) == 0, errors, total_salary)
