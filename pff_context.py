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


def build(away, home):
    slot = _load("slot_defense.json")
    rec = _load("receivers.json")
    if not slot and not rec:
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
