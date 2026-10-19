"""
pff_context.py - builds the PRIVATE PFF context block for one game's Coeus breakdown.

Reads private/pff/slot_defense.json and private/pff/receivers.json (both written by pff_pull.py and
gitignored). Returns None when they are missing, so breakdowns generate exactly as before.
The block is merged into the model's input at generation time ONLY - it is never written into the
committed evidence/ files.
"""
import json
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
PRIV = os.path.join(ROOT, "private", "pff")


def _load(name):
    try:
        return json.load(open(os.path.join(PRIV, name)))
    except (OSError, ValueError):
        return None


def _slot_receivers(rows):
    """Receivers who line up in the slot a meaningful share of the time (>=25% slot, >=8 targets)."""
    out = [r for r in rows if (r.get("slot_rate") or 0) >= 25 and (r.get("targets") or 0) >= 8]
    return sorted(out, key=lambda r: -(r.get("slot_rate") or 0))


def _coverage_lean(pp, dz):
    """Offense's yards/target projected from THIS defense's man/zone mix, vs the offense's overall number.
    Needs >= 15 charted targets in each split; otherwise None (too thin to say anything)."""
    try:
        m, z = pp["man"], pp["zone"]
        if (m["targets"] or 0) < 15 or (z["targets"] or 0) < 15 or not dz or dz.get("man_pct") is None:
            return None
        base = (m["yards"] + z["yards"]) / (m["targets"] + z["targets"])
        exp = dz["man_pct"] / 100 * m["yards_per_target"] + dz["zone_pct"] / 100 * z["yards_per_target"]
        diff = exp - base
        return {"overall_yards_per_target": round(base, 2), "weighted_by_defense_mix": round(exp, 2),
                "difference": round(diff, 2),
                "reads_as": "about neutral" if abs(diff) < 0.15 else ("favors the offense" if diff > 0 else "favors the defense")}
    except (KeyError, TypeError, ZeroDivisionError):
        return None


def build(away, home):
    slot = _load("slot_defense.json")
    rec = _load("receivers.json")
    cov = _load("coverage_context.json")
    if not slot and not rec and not cov:
        return None
    block = {
        "source": "PFF (private). Slot = receiver lined up in the slot; rank 1 = toughest defense vs the slot, 32 = weakest.",
        "through_week": (slot or {}).get("through_week"),
        "slot_defense": {}, "receivers": {}, "slot_matchups": []}
    for team in (away, home):
        if slot:
            std = slot["season_to_date"].get(team)
            l3 = slot["last3"]["teams"].get(team)
            if std:
                block["slot_defense"][team] = {"season_to_date": std, "last3": l3, "last3_weeks": slot["last3"]["weeks"]}
        if rec and team in rec["teams"]:
            block["receivers"][team] = rec["teams"][team]
    if cov:
        def _trim(tv):
            if not tv:
                return tv
            tv = json.loads(json.dumps(tv))
            if "defenders" in tv.get("defense", {}):
                tv["defense"]["defenders"] = tv["defense"]["defenders"][:8]
            if "receivers" in tv.get("offense", {}):
                tv["offense"]["receivers"] = tv["offense"]["receivers"][:8]
            return tv
        block["coverage"] = {t: _trim((cov.get("teams") or {}).get(t)) for t in (away, home)}
        block["coverage_season"] = cov.get("season")
        block["man_zone_matchups"] = []
        for off, dfn in ((away, home), (home, away)):
            dz = ((cov.get("teams") or {}).get(dfn) or {}).get("defense", {}).get("man_zone")
            rcs = ((cov.get("teams") or {}).get(off) or {}).get("offense", {}).get("receivers") or []
            pp = ((cov.get("teams") or {}).get(off) or {}).get("offense", {}).get("passing_proxy")
            if dz or rcs or pp:
                entry = {"offense": off, "defense": dfn, "defense_man_zone": dz,
                         "offense_receivers_vs_man_zone": rcs[:6]}
                if pp:
                    entry["offense_team_passing_vs_man_zone"] = {k: v for k, v in pp.items() if k != "note"}
                    lean = _coverage_lean(pp, dz)
                    if lean:
                        entry["projected_vs_this_defense"] = lean
                block["man_zone_matchups"].append(entry)
    for off, dfn in ((away, home), (home, away)):
        d = block["slot_defense"].get(dfn, {}).get("season_to_date")
        slots = _slot_receivers(block["receivers"].get(off, []))
        if d and slots:
            block["slot_matchups"].append({
                "offense": off, "defense": dfn,
                "defense_slot_yards_pg_rank": d.get("rank_yards_pg"),
                "defense_slot_yards_per_target_rank": d.get("rank_yards_per_target"),
                "slot_receivers": [{"player": r["player"], "pos": r["pos"], "slot_rate": r["slot_rate"],
                                     "targets": r["targets"], "target_share": r["target_share"],
                                     "yprr": r["yprr"]} for r in slots[:3]]})
    return block


PROMPT_ADDENDUM = """

PFF COVERAGE DATA (private input - "pff.coverage" and "pff.man_zone_matchups"; 2026 season-to-date):
- pff.coverage[TEAM].defense.man_zone: the share of that defense's coverage snaps played in man vs zone \
(man_pct / zone_pct) and what it has allowed against each (yards per target, catch rate, TDs, INTs) with \
league ranks (rank 1 = best defense). These totals sum the qualifying defenders PFF lists, so describe them \
as "per PFF" figures.
- pff.coverage[TEAM].defense.defenders: that team's top coverage defenders (CB/S/LB) with PFF coverage grade, \
targets, catch rate allowed, yards per coverage snap, QB rating against, forced-incompletion rate, and each \
man-coverage and zone-coverage line. Use these for individual CB/DB matchups; name the defender and the number.
- pff.coverage[TEAM].offense.receivers and pff.man_zone_matchups: each receiver's production against man vs \
zone (targets, catches, yards, yards per route run, EPA, route grade). Pair a receiver's better split with the \
opposing defense's weaker split, and say which it is.
- These PFF numbers take precedence over hidden_intelligence.coverage_* (older, 2025 data) wherever both exist; \
cite the PFF figure and label it PFF. Small samples (under 10 targets in a split) must be called small.
- The man/zone lines cover only plays PFF charted as man or zone. A receiver's all_targets can be larger than \
his man + zone targets (uncharted_targets); the uncharted plays carry yards and TDs that are NOT in the man/zone \
lines, so a man+zone total can be lower than his season total. Never present man+zone totals as his season totals; \
use FI season stats for season totals.
- pff.man_zone_matchups[].offense_team_passing_vs_man_zone is that OFFENSE's team passing production against \
man and against zone (targets, completions, yards, yards per target, TDs, INTs, passer rating, man_share_pct), \
summed from its receivers' PFF charting. It is a team-level proxy for the quarterback, NOT the QB's own split: \
call it "the team's passing offense, per PFF receiver charting", never "Purdy's numbers against man". When \
multi_qb is true, name the quarterbacks and their share of attempts. projected_vs_this_defense (when present) \
weights that offense's man and zone yards per target by this defense's coverage mix: cite it as written.
- Never say the coverage data is missing or empty for a game: if a team has no row, leave coverage out silently.

MAN VS ZONE IS REQUIRED IN THIS BREAKDOWN (both sides of the ball, both directions):
- Section 4 (Matchup Intelligence) must contain a clearly labeled "Man vs Zone" part. For EACH of the two \
matchups (away offense vs home defense, then home offense vs away defense) state: (a) how often the defense \
plays man vs zone (man_pct / zone_pct with its rank) and what it allows to each (yards per target, with rank); \
(b) how the opposing offense has performed against man vs zone (team passing line, plus the one or two \
receivers or tight ends whose split matters most, with the target counts); (c) which coverage the offense \
prefers, which the defense leans on, and whether the two collide, using projected_vs_this_defense when present.
- Add one bullet per matchup to the Coeus Cheat Sheet summarizing the man/zone edge (for example "WAS offense: \
+0.4 yards/target vs SF's 56% man mix per PFF").
- ATTRIBUTION CHECK (applies to Section 4 AND the Cheat Sheet): every man/zone figure belongs to the team named \
in its pff.coverage key or its man_zone_matchups row ("defense" = the team playing that coverage; "offense" = the \
team whose receivers produced the split). Before writing each bullet, confirm the team name matches the entry the \
number came from; never swap the two teams' coverage mixes. Describe offense figures as "team passing offense, per \
PFF receiver charting" at least once per team.
- Cite every figure as per PFF, give the rank next to each raw stat, call a split under 10 targets small, and \
keep the season label (2026 to date) in the wording. If a particular number is absent, build the paragraph on \
the numbers that exist and do not comment on what is missing.
""" + """

PFF SLOT DATA (private input - the "pff" key in the evidence below):
- "pff.slot_defense" is how many yards, targets and yards per target each defense allows to receivers \
lined up in the slot, season-to-date and over the last 3 games. Rank 1 = toughest, 32 = weakest.
- "pff.receivers" gives each offense's top targets with slot_rate / wide_rate / inline_rate (share of \
their snaps lined up in each spot). "pff.slot_matchups" pairs each offense's real slot receivers with \
the opposing slot defense.
- Use it in Matchup Intelligence and the WR/TE positional analysis: say which receiver actually works \
the slot, and how the opposing defense has fared against the slot. Treat slot_rate >= 50 as a primary \
slot receiver; a split (e.g. 45/50) is a hybrid and must be described as one.
- Cite only numbers that appear in the pff block, label them as PFF slot figures, and never infer \
slot usage for a receiver who is not listed. Slot-defense numbers describe coverage allowed to the slot \
position, not any single defender's quality. If the pff key is absent, do not mention slot data at all.
"""
