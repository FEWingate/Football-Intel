"""
GENERATE_PROPS_REPORT.PY
==========================
Generates the real, structured content behind three of Prop Center's
five sub-sections: Coeus Prop Breakdown (3 favorite props per game,
plus one favorite per skill position, each with a suggested line or
alt), Favorite Overs and Unders for the week, and the existing 3/4/5/
6/7-team parlays. (Game Lines/Totals/ML and Player Props are pure,
real, live data display, built and read directly from
fanduel_props/latest.json — no LLM involved, see prop_center.html.)

REAL DESIGN CHANGE (2026-09-12): the original version of this script
only gave Coeus the FINISHED Game Breakdown text for each game — never
the original evidence packages behind them (Contextual Stats,
Matchup Intelligence, Threat Intelligence). Per Frank's explicit
instruction, Coeus's prop picks must be grounded in the SAME evidence
used to build the Game Breakdowns, especially Contextual Stats — not
just a prose summary of it. Both are now included: the Game Breakdown
text (trusted, already-vetted analysis) AND the raw evidence package
(the real underlying data) for every game on the slate.

REAL DESIGN CHANGE (2026-09-12): build_fanduel_props.py now tracks
real per-family coverage (current / stale_last_known_good /
unavailable) after a real, confirmed upstream reliability problem with
parlay-api.com (see PARLAY_API_RELIABILITY_INVESTIGATION.md). This
script reads that coverage metadata and tells Coeus explicitly, in
plain language, which stat families are live, which are stale (and
how old), and which have nothing at all — so it can caveat picks
honestly instead of presenting stale numbers as current, silently
skipping a category, or guessing. A stat family with zero real
coverage (live or stale) gets no pick at all — Coeus is told plainly
not to produce one, matching the Standard's "an honest gap is better
than a filled-in placeholder" rule already established for Game
Breakdowns and Contextual Stats.

REQUIRES: pip install anthropic --break-system-packages
          export ANTHROPIC_API_KEY=...   (never commit)
          fanduel_props/latest.json must already exist — run
          build_fanduel_props.py first.

USAGE:
    python3 generate_props_report.py
    python3 generate_props_report.py --dry-run
"""

import argparse
import copy
import json
import os
import re
import sys
from datetime import datetime, timezone

from parlay_validator import validate_parlay, verify_legs_against_source, leg_key

PROMPTS_DIR = "prompts"
MASTER_PROMPT_PATH = f"{PROMPTS_DIR}/Coeus_Master_Prompt_v1.1.md"
PROPS_STANDARD_PATH = f"{PROMPTS_DIR}/Coeus_Props_Parlay_Report_Standard_v2.0.md"
FANDUEL_DATA_PATH = "fanduel_props/latest.json"

DEFAULT_MODEL = "claude-sonnet-5"
PARLAY_SIZES = [3, 4, 5, 6, 7]
SKILL_POSITIONS = ["QB", "RB", "WR", "TE"]
STAT_LABELS = {"passing_yards": "Passing Yards", "rushing_yards": "Rushing Yards",
               "receiving_yards": "Receiving Yards", "receptions": "Receptions",
               "anytime_td": "Anytime TD"}

TASK_INSTRUCTION = """\
Generate this week's Props report for the FULL slate below, following the \
Props & Parlay Report Standard exactly, in this order:

1. Coeus Prop Breakdown — 3 favorite props for EACH game on the slate, \
plus one favorite prop for each of QB/RB/WR/TE league-wide across the \
whole slate. For every pick, name the real line FanDuel has posted AND \
suggest a specific line or alt-line threshold from the real data — \
never an invented number.
2. Favorite Overs and Unders for the week — your best Over picks and \
best Under picks across the ENTIRE slate, ranked by conviction, not \
grouped by game.
3. Five separate parlays (3, 4, 5, 6, and 7 team).

Lists and short entries only, per the No Paragraphs Rule — never prose \
paragraphs. Every football claim must come from the Game Breakdowns \
and/or the real evidence packages below (Contextual Stats especially) \
— never from outside knowledge. Every market, line, and price must \
come from the real FanDuel data below — never invent one. The REAL \
DATA COVERAGE section below tells you which stat families are live, \
which are stale, and which have no real data at all right now — a \
stat family with no real data (live or stale) gets no pick; say so \
plainly rather than skipping it silently or guessing. Every JSON block \
specified in the Standard is required, not optional — a real program \
checks every one of them after you finish.

=== REAL DATA COVERAGE (what you can actually trust right now) ===
"""


def load_text(path):
    if not os.path.exists(path):
        sys.exit(f"FATAL: {path} not found.")
    with open(path) as f:
        return f.read()


def load_json(path):
    if not os.path.exists(path):
        return None
    with open(path) as f:
        return json.load(f)


def discover_all_games():
    """Same lookup as generate_weekly_dfs_report.py's — every finished
    Game Breakdown, deduplicated across every game_breakdowns/*/manifest.json."""
    base = "game_breakdowns"
    if not os.path.isdir(base):
        return []
    seen = {}
    for folder in sorted(os.listdir(base)):
        manifest = load_json(os.path.join(base, folder, "manifest.json"))
        for key, g in (manifest.get("games") or {}).items() if manifest else []:
            if key not in seen:
                seen[key] = (folder, g["away"], g["home"])
    return list(seen.values())


def load_evidence_for_game(away, home):
    """Real evidence package for this game — bootstrap or regular,
    whichever actually exists, same lookup order the Game Breakdown
    generation itself uses. Returns (None, None) if neither exists,
    which is a real, reportable gap for this specific game, not
    something to silently paper over."""
    for path in (f"evidence_bootstrap/{away}_{home}.json", f"evidence/current/{away}_{home}.json"):
        data = load_json(path)
        if data:
            return data, path
    return None, None


def trim_evidence_for_props(evidence):
    """REAL BUG FIX (2026-09-14): confirmed directly against real evidence
    files that a single game's full evidence package can run anywhere
    from ~23K to ~430K real characters — dominated almost entirely by
    each player's own "log" field: a full, real week-by-week game log
    (one detailed entry per week already played) sitting alongside that
    same player's already-aggregated "season" and "career" totals in the
    same record. For 5 real games this pushed the whole props prompt to
    ~375,000 tokens — a real, serious cost problem caught before it was
    ever run for real, not after.

    UPDATED (2026-09-15), per Frank's direct pushback: the original fix
    dropped "log" entirely. That went too far — a player's own recent
    games (who they actually played, what they actually did, and that
    opponent's real defensive tier/rank that week) is real, correctly-
    attributed evidence a season average can't give: whether they're
    actually hitting today's real posted line over their last 3/5/10
    games, against what caliber of defense. So "log" is now trimmed to
    the most recent 10 real entries per player, not removed — keeping
    that real recency and opponent-quality evidence while still
    avoiding the original cost problem (confirmed up to ~84% of one
    real game's entire evidence size in the worst case, from keeping
    all 17 weeks for every player on both rosters).

    This trim is props-specific — it does NOT touch the real evidence
    package on disk, and Game Breakdown generation (which can genuinely
    use the full week-by-week trend detail for its own deeper analysis)
    is completely unaffected.

    REAL CHANGE (2026-09-15), per Frank's direct request, for a
    different reason than cost — data correctness. A prop is a bet on
    one specific player producing one specific stat; it has nothing to
    do with which team wins or by how much. Several evidence blocks
    exist specifically to support real GAME-outcome narrative (Game
    Breakdown's whole purpose), not player-specific prop reasoning, and
    keeping them in the props prompt risks exactly what happened with
    the real, confirmed Mahomes Week 17 misattribution: team-level or
    schematic data getting reasoned into a specific player's stat line
    it was never actually about. Removed entirely for props:
      - team_context: both its per-game "log" and its "splits" are
        team-level, QB/RB/WR/TE POSITION-GROUP aggregates, never an
        individual player's own real production — the same real
        category of data that caused the Mahomes misattribution.
      - dfs: DraftKings salary/ownership data has zero real bearing on
        whether a FanDuel yardage or reception prop hits.
      - down_distance, red_zone_play_calling: real, but these describe
        team-level play-calling tendency and game script, not whether
        a specific named player reaches a specific number — the kind
        of evidence that supports a Game Breakdown's account of how a
        game is likely to unfold, not a prop pick's reasoning.
    Real, individual player evidence (threats, players.season/career/
    splits/ceiling, matchup's team_off/team_def category rankings —
    the actual opponent-side half of a real Threat-style convergence —
    and the player-specific slices of matchup_pattern_data) is
    untouched by this trim."""
    trimmed = copy.deepcopy(evidence)
    game_info = trimmed.get("game") or {}
    away_team, home_team = game_info.get("away"), game_info.get("home")
    players = trimmed.get("players")
    if isinstance(players, dict):
        for side_name, side in players.items():
            # REAL BUG FIX (2026-09-15), per Frank's direct request: a
            # division rival plays this same real opponent twice a real
            # season, and how a player has actually performed in those
            # specific past meetings is real, directly relevant
            # evidence — not just general recent form. A pure "last 10
            # games" trim could accidentally cut a real division
            # meeting that happened earlier in a season. This player's
            # real opponent TODAY (the other team in this game — away
            # players face home, home players face away) is checked
            # explicitly, and any of their real past log entries
            # against that same opponent are kept regardless of
            # whether they'd otherwise fall outside the most recent 10
            # — capped at the 3 most recent such meetings, since that's
            # the real, relevant window for head-to-head history, not
            # every meeting a multi-season log might ever contain.
            todays_opponent = home_team if side_name == "away" else away_team
            if isinstance(side, list):
                for p in side:
                    if isinstance(p, dict) and isinstance(p.get("log"), list):
                        sorted_log = sorted(p["log"], key=lambda e: e.get("week", 0))
                        recent10 = sorted_log[-10:]
                        vs_opponent = [e for e in sorted_log if e.get("opp") == todays_opponent][-3:]
                        merged = {id(e): e for e in recent10}
                        for e in vs_opponent:
                            merged.setdefault(id(e), e)
                        p["log"] = sorted(merged.values(), key=lambda e: e.get("week", 0))
    for key in ("team_context", "dfs", "down_distance", "red_zone_play_calling"):
        trimmed.pop(key, None)
    return trimmed


def coverage_summary_text(coverage):
    """Real, human-readable summary of which stat families Coeus can
    actually trust right now — built directly from build_fanduel_props.py's
    real coverage metadata (current / stale_last_known_good /
    unavailable), not re-derived or guessed at from the raw game data."""
    lines = []
    for stat, label in STAT_LABELS.items():
        meta = (coverage or {}).get(stat, {})
        status = meta.get("status", "unavailable")
        real_key = f"player_{stat}"
        if status == "current":
            lines.append(f"- {label} (real market_key: `{real_key}`): LIVE, current data "
                         f"({meta.get('current_event_count', 0)} real game(s)).")
        elif status == "stale_last_known_good":
            age_min = round((meta.get("source_age_seconds") or 0) / 60)
            lines.append(f"- {label} (real market_key: `{real_key}`): STALE — the live provider "
                         f"feed dropped out; showing the last real data from about {age_min} "
                         f"minute(s) ago, for {meta.get('carried_event_count', 0)} game(s). Say so "
                         f"plainly wherever this data is used — do not present it as live.")
        else:
            lines.append(f"- {label} (real market_key: `{real_key}`): UNAVAILABLE — no real data "
                         f"at all right now, live or stale. Do not produce a pick for this stat; "
                         f"say plainly that none is available.")
    # REAL BUG FIX (2026-09-14): confirmed directly that even with the
    # exact market_key instruction already in the Standard, Coeus
    # occasionally still wrote a shortened, plausible-sounding but real,
    # confirmed-wrong key ("player_pass_yards" instead of the real
    # "player_passing_yards") — a real hallucination the validator
    # correctly caught, failing every parlay that used it. This explicit,
    # short, copy-ready list — right where the prompt is read first, not
    # buried inside a large JSON blob — gives Coeus a real, unambiguous
    # reference for exactly these five strings, reducing reliance on
    # recalling them correctly from memory.
    lines.append("")
    lines.append("The five real, exact market_key strings this project ever uses (copy exactly, "
                 "never shorten or paraphrase): " +
                 ", ".join(f"`player_{stat}`" for stat in STAT_LABELS))
    return "\n".join(lines)


def build_real_index(fanduel_data):
    """Real (canonical_event_id, market_key, player) -> real row index,
    built from the current games[]-based fanduel_props schema. Uses the
    exact same real market_key naming convention build_fanduel_props.py
    itself uses (e.g. "player_passing_yards",
    "player_passing_yards_milestones_250_or_more") so this matches
    leg_key()'s expected identity with no changes needed to
    parlay_validator.py."""
    index = {}
    for g in fanduel_data.get("games", []):
        eid = g["canonical_event_id"]
        for mkey in ("h2h", "spreads", "totals"):
            for o in g.get("game_lines", {}).get(mkey, []):
                index[(eid, mkey, o.get("name"))] = {
                    "canonical_event_id": eid, "market_key": mkey,
                    "player": o.get("name"), "price": o.get("price"), "point": o.get("point"),
                }
        for stat, by_player in (g.get("player_props") or {}).items():
            for name, p in by_player.items():
                if p.get("line"):
                    plain_key = f"player_{stat}"
                    index[(eid, plain_key, name)] = {
                        "canonical_event_id": eid, "market_key": plain_key,
                        "player": name, "price": p["line"]["over_price"],
                        "under_price": p["line"]["under_price"], "point": p["line"]["point"],
                    }
                for alt in (p.get("alts") or []):
                    alt_key = f"player_{stat}_milestones_{alt['threshold']}_or_more"
                    index[(eid, alt_key, name)] = {
                        "canonical_event_id": eid, "market_key": alt_key,
                        "player": name, "price": alt.get("over_price") or alt.get("under_price"),
                        "threshold": alt["threshold"],
                    }
        # REAL BUG FIX (2026-09-14): this was hardcoded to the OLD market
        # key from before build_fanduel_props.py switched to the /props
        # endpoint's real, confirmed key for this market. Confirmed
        # directly as the real cause of every parlay containing an
        # anytime-TD leg failing validation tonight — Coeus correctly
        # used "player_anytime_td" (the real key actually present in the
        # FanDuel data it was shown), but this index was still only
        # storing entries under the stale "player_anytime_touchdown_scorer"
        # key, so a completely real, accurate pick looked like a
        # hallucinated one. The pick was never wrong — this lookup table
        # was.
        for p in (g.get("anytime_td") or []):
            index[(eid, "player_anytime_td", p["player"])] = {
                "canonical_event_id": eid, "market_key": "player_anytime_td",
                "player": p["player"], "price": p["price"],
            }
    return index


def extract_json_block(report_text, tag):
    """Pulls one named JSON block (a JSON object, not a bare array —
    the parlay blocks use arrays, these use objects) out of the
    response. Returns None if the tag is missing or the JSON is
    unparseable — a real failure for that specific block, not something
    to silently paper over with an empty result."""
    match = re.search(rf"{tag}\s*\n(\{{.*?\n\}})", report_text, re.DOTALL)
    if not match:
        return None
    try:
        return json.loads(match.group(1))
    except json.JSONDecodeError:
        return None


def extract_parlay_blocks(report_text):
    """Pulls all five PARLAY_N_TEAM JSON blocks out of the response.
    Returns {size: legs_list_or_None} — a missing or unparseable block
    for a given size is a real failure to report for THAT size, not
    something to silently skip past; the other sizes are unaffected."""
    result = {}
    for size in PARLAY_SIZES:
        tag = f"PARLAY_{size}_TEAM"
        match = re.search(rf"{tag}\s*\n(\[.*?\])", report_text, re.DOTALL)
        if not match:
            result[size] = None
            continue
        try:
            result[size] = json.loads(match.group(1))
        except json.JSONDecodeError:
            result[size] = None
    return result


def verify_pick(pick, real_by_key):
    """Cross-checks one proposed pick (player/market_key/canonical_event_id)
    against the real source data — same principle as
    verify_legs_against_source() for parlay legs. Returns (verified_pick,
    is_real) — verified_pick has its price overwritten with the REAL
    price wherever a match is found, in case of a transcription slip;
    is_real is False when the pick doesn't exist in the real data at
    all, which is a real problem (Coeus referenced something not
    actually on the board), not a rounding difference to shrug off."""
    key = leg_key(pick)
    real = real_by_key.get(key)
    if real is None:
        return pick, False
    merged = dict(pick)
    merged["price"] = real.get("price")
    return merged, True


def verify_pick_list(picks, real_by_key):
    verified, mismatches = [], []
    for p in picks:
        vp, is_real = verify_pick(p, real_by_key)
        verified.append(vp)
        if not is_real:
            mismatches.append(p)
    return verified, mismatches


def verify_prop_breakdown(raw, real_by_key):
    if not raw:
        return None, ["Could not parse the PROP_BREAKDOWN JSON block."]
    errors = []
    per_game = []
    for game in (raw.get("per_game") or []):
        picks, mismatches = verify_pick_list(game.get("picks") or [], real_by_key)
        if mismatches:
            errors.append(f"{game.get('away')}@{game.get('home')}: {len(mismatches)} pick(s) "
                           f"don't exist in the real FanDuel data.")
        per_game.append({"away": game.get("away"), "home": game.get("home"), "picks": picks,
                          "mismatch_count": len(mismatches)})
    per_position = {}
    for pos in SKILL_POSITIONS:
        pick = (raw.get("per_position") or {}).get(pos)
        if not pick:
            continue
        vp, is_real = verify_pick(pick, real_by_key)
        if not is_real:
            errors.append(f"{pos} favorite pick doesn't exist in the real FanDuel data.")
        per_position[pos] = vp
    return {"per_game": per_game, "per_position": per_position}, errors


def verify_favorite_ou(raw, real_by_key):
    if not raw:
        return None, ["Could not parse the FAVORITE_OU JSON block."]
    errors = []
    overs, over_mismatches = verify_pick_list(raw.get("overs") or [], real_by_key)
    unders, under_mismatches = verify_pick_list(raw.get("unders") or [], real_by_key)
    if over_mismatches:
        errors.append(f"{len(over_mismatches)} favorite Over(s) don't exist in the real FanDuel data.")
    if under_mismatches:
        errors.append(f"{len(under_mismatches)} favorite Under(s) don't exist in the real FanDuel data.")
    return {"overs": overs, "unders": unders}, errors


def main():
    ap = argparse.ArgumentParser(description="Generate the Props & Parlay Report.")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--max-tokens", type=int, default=48000)
    ap.add_argument("--stake", type=float, default=100,
                     help="Hypothetical per-parlay stake used to compute a real "
                          "payout figure in the validator output. Default $100.")
    ap.add_argument("--dry-run", action="store_true",
                     help="Build and save the exact prompt without calling the API.")
    args = ap.parse_args()

    games = discover_all_games()
    if not games:
        sys.exit("FATAL: no finished Game Breakdowns found — nothing to build "
                 "a props report from yet.")

    fanduel_data = load_json(FANDUEL_DATA_PATH)
    if fanduel_data is None:
        sys.exit(f"FATAL: {FANDUEL_DATA_PATH} not found. Run build_fanduel_props.py first.")
    coverage = fanduel_data.get("coverage") or {}
    if not any((coverage.get(s) or {}).get("status") != "unavailable" for s in STAT_LABELS):
        sys.exit("FATAL: every real stat family is unavailable (no live or stale data at all) — "
                 "nothing real to build picks from. Re-run build_fanduel_props.py once the "
                 "provider's coverage recovers.")

    # REAL BUG FIX (2026-09-12): fanduel_props/latest.json covers the
    # WHOLE week's slate (14+ games), but this run only has finished
    # Game Breakdowns for a handful of them. Sending every other game's
    # full prop data (every player, every real alt-line rung) for no
    # reason was confirmed directly to balloon a 4-game run to ~308,000
    # input tokens — real, billed cost for data Coeus was never even
    # asked about. Filtered down to only the games actually relevant to
    # this run, before it's built into the prompt OR the verification
    # index — Coeus can't reference a game it was never shown, so
    # restricting both consistently loses nothing real.
    relevant_codes = {(away, home) for _, away, home in games}
    fanduel_data = dict(fanduel_data)
    fanduel_data["games"] = [
        g for g in fanduel_data.get("games", [])
        if (g.get("away_code"), g.get("home_code")) in relevant_codes
    ]
    if len(fanduel_data["games"]) < len(games):
        missing_fd = relevant_codes - {(g.get("away_code"), g.get("home_code")) for g in fanduel_data["games"]}
        print(f"  NOTE: {len(missing_fd)} game(s) with a finished breakdown have no real FanDuel "
              f"data at all right now: {missing_fd}.")

    # REAL BUG FIX (2026-09-14): confirmed directly that most of a real
    # 5-game run's cost was evidence/breakdown text for games with ZERO
    # real FanDuel data — games already played, with no live line left
    # to bet on. Coeus cannot produce a real prop pick for a game with no
    # real prop data, no matter how much evidence it's given for that
    # game — so sending full evidence and breakdown text for those games
    # was pure cost with no possible benefit. Narrowing `games` itself
    # here (not just fanduel_data, which was already filtered above)
    # means this reduction cascades naturally into the evidence loop,
    # the breakdown-text loop, and games_included below, instead of
    # needing a separate fix in each place.
    live_codes = {(g.get("away_code"), g.get("home_code")) for g in fanduel_data["games"]}
    games_with_no_real_props = [(folder, away, home) for folder, away, home in games
                                  if (away, home) not in live_codes]
    games = [(folder, away, home) for folder, away, home in games if (away, home) in live_codes]
    if games_with_no_real_props:
        print(f"  Excluding {len(games_with_no_real_props)} game(s) from evidence/breakdown "
              f"text entirely — no real prop data exists for them right now, so there's "
              f"nothing a pick could be grounded in regardless of how much evidence is sent.")
    if not games:
        sys.exit("FATAL: none of the finished Game Breakdowns have any real, live FanDuel "
                 "prop data right now — nothing real to build picks from.")

    real_by_key = build_real_index(fanduel_data)

    gb_texts, evidence_texts, folders_used, missing_evidence = [], [], set(), []
    for folder, away, home in games:
        gb_path = os.path.join("game_breakdowns", folder, f"{away}_{home}.md")
        gb_texts.append(f"--- {away} @ {home} ---\n{load_text(gb_path)}")
        folders_used.add(folder)
        evidence, ev_path = load_evidence_for_game(away, home)
        if evidence:
            trimmed_evidence = trim_evidence_for_props(evidence)
            evidence_texts.append(f"--- {away} @ {home} (from {ev_path}, per-player week-by-week "
                                    f"logs trimmed — real season/career/splits/ceiling totals kept) ---\n" +
                                    json.dumps(trimmed_evidence, separators=(",", ":")))
        else:
            missing_evidence.append(f"{away}_{home}")
    combined_breakdowns = "\n\n".join(gb_texts)
    combined_evidence = "\n\n".join(evidence_texts)
    if missing_evidence:
        print(f"  NOTE: no evidence package found for {len(missing_evidence)} game(s) — "
              f"{', '.join(missing_evidence)} — Coeus will rely on their Game Breakdown text alone.")

    master_prompt = load_text(MASTER_PROMPT_PATH)
    props_standard = load_text(PROPS_STANDARD_PATH)
    system = [
        {"type": "text", "text": master_prompt, "cache_control": {"type": "ephemeral"}},
        {"type": "text", "text": props_standard, "cache_control": {"type": "ephemeral"}},
    ]

    fanduel_json = json.dumps(fanduel_data, separators=(",", ":"))
    user_content = (
        TASK_INSTRUCTION + coverage_summary_text(coverage) +
        "\n\n=== GAME BREAKDOWNS (every finished game on this slate) ===\n" + combined_breakdowns +
        "\n\n=== REAL EVIDENCE PACKAGES (Contextual Stats, Matchup Intelligence, Threat "
        "Intelligence — the same underlying data the Game Breakdowns above were built from) ===\n" +
        combined_evidence +
        "\n\n=== REAL FANDUEL GAME LINES + PROPS DATA (this slate only) ===\n" + fanduel_json
    )

    out_dir = f"props_reports/{list(folders_used)[0]}" if len(folders_used) == 1 else "props_reports/mixed"
    os.makedirs(out_dir, exist_ok=True)
    out_stem = f"{out_dir}/props_parlay_report"

    prompt_record = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "model": args.model, "max_tokens": args.max_tokens,
        "games_included": [f"{a}_{h}" for _, a, h in games],
        "fanduel_data_source": FANDUEL_DATA_PATH,
        "evidence_missing_for": missing_evidence,
        "system_char_count": len(master_prompt) + len(props_standard),
        "user_char_count": len(user_content),
    }
    with open(f"{out_stem}_prompt.json", "w") as f:
        json.dump(prompt_record, f, indent=2)

    approx_input_tokens = (len(master_prompt) + len(props_standard) + len(user_content)) // 4
    print(f"Games included: {len(games)}")
    print(f"Evidence packages found: {len(evidence_texts)} of {len(games)}")
    print(f"Rough input size: ~{approx_input_tokens:,} tokens (estimate only)")

    if args.dry_run:
        with open(f"{out_stem}_prompt_full.txt", "w") as f:
            f.write("=== SYSTEM (Master Prompt) ===\n\n" + master_prompt +
                     "\n\n=== SYSTEM (Props & Parlay Standard) ===\n\n" + props_standard +
                     "\n\n=== USER MESSAGE ===\n\n" + user_content)
        print(f"\nDRY RUN — no API call made. Prompt written to {out_stem}_prompt_full.txt")
        return

    try:
        import anthropic
    except ImportError:
        sys.exit("FATAL: pip install anthropic --break-system-packages")
    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("FATAL: ANTHROPIC_API_KEY not set.")

    client = anthropic.Anthropic()
    print(f"\nCalling {args.model} (streaming)...\n")
    with client.messages.stream(
        model=args.model, max_tokens=args.max_tokens, system=system,
        messages=[{"role": "user", "content": user_content}],
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)
        response = stream.get_final_message()
    print()

    report_text = "".join(block.text for block in response.content if block.type == "text")
    print(f"stop_reason: {response.stop_reason}")
    if response.stop_reason == "max_tokens":
        print("WARNING: hit the max_tokens ceiling before finishing — INCOMPLETE.")
    if not report_text.strip():
        sys.exit("FATAL: empty response, nothing written.")

    with open(f"{out_stem}.md", "w") as f:
        f.write(report_text)
    usage = response.usage
    prompt_record["usage"] = {"input_tokens": usage.input_tokens, "output_tokens": usage.output_tokens}
    with open(f"{out_stem}_prompt.json", "w") as f:
        json.dump(prompt_record, f, indent=2)
    print(f"\nWrote {out_stem}.md — {usage.input_tokens:,} input / {usage.output_tokens:,} output tokens")

    print("\n" + "=" * 60)

    prop_breakdown_raw = extract_json_block(report_text, "PROP_BREAKDOWN")
    prop_breakdown, pb_errors = verify_prop_breakdown(prop_breakdown_raw, real_by_key)
    print("\nPROP BREAKDOWN VALIDATION:")
    if pb_errors:
        for e in pb_errors:
            print(f"  ISSUE: {e}")
    else:
        print("  PASSED — every pick verified against real FanDuel data.")

    favorite_ou_raw = extract_json_block(report_text, "FAVORITE_OU")
    favorite_ou, fou_errors = verify_favorite_ou(favorite_ou_raw, real_by_key)
    print("\nFAVORITE OVERS/UNDERS VALIDATION:")
    if fou_errors:
        for e in fou_errors:
            print(f"  ISSUE: {e}")
    else:
        print("  PASSED — every pick verified against real FanDuel data.")

    parlays = extract_parlay_blocks(report_text)
    parlay_results = {}
    for size in PARLAY_SIZES:
        legs = parlays[size]
        print(f"\n{size}-TEAM PARLAY VALIDATION:")
        if legs is None:
            print(f"  FAILED — could not find or parse a PARLAY_{size}_TEAM JSON "
                  f"block. This parlay has NOT been checked. Do not trust it.")
            parlay_results[size] = {"valid": False, "errors": ["Could not parse this parlay's JSON block."],
                                     "warnings": [], "result": None, "legs": None, "mismatches": []}
            continue
        verified_legs, mismatches = verify_legs_against_source(legs, real_by_key)
        if mismatches:
            print(f"  {len(mismatches)} leg(s) do NOT exist in the real FanDuel data "
                  f"provided — Coeus referenced something not actually on the board:")
            for m in mismatches:
                print(f"    - {m}")
        is_valid, errors, warnings, result = validate_parlay(
            verified_legs, expected_size=size, stake=args.stake)
        passed = is_valid and not mismatches
        if passed:
            print(f"  PASSED — {result['legs']} real legs, combined odds "
                  f"{result['combined_decimal']} (American {result['combined_american']:+d}), "
                  f"${args.stake:.0f} stake -> ${result['payout']:.2f} payout.")
        else:
            print(f"  FAILED:")
            for e in errors:
                print(f"    - {e}")
        for w in warnings:
            print(f"  NOTE: {w}")
        parlay_results[size] = {
            "valid": passed, "errors": errors, "warnings": warnings,
            "result": result, "legs": verified_legs,
            "mismatches": [m for m in mismatches],
        }
    print("=" * 60)

    report_json = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "games_included": [f"{a}_{h}" for _, a, h in games],
        "coverage": coverage,
        "stake_used_for_payout_examples": args.stake,
        "markdown": report_text,
        "prop_breakdown": prop_breakdown, "prop_breakdown_errors": pb_errors,
        "favorite_ou": favorite_ou, "favorite_ou_errors": fou_errors,
        "parlays": {str(size): parlay_results[size] for size in PARLAY_SIZES},
    }
    with open(f"{out_stem}.json", "w") as f:
        json.dump(report_json, f)
    print(f"Wrote {out_stem}.json (structured, for the Prop Center page)")

    os.makedirs("props_reports", exist_ok=True)
    with open("props_reports/latest.json", "w") as f:
        json.dump({
            "generated_at": report_json["generated_at"],
            "report_path": f"{out_stem}.json",
        }, f)
    print(f"Wrote props_reports/latest.json — points to {out_stem}.json")


if __name__ == "__main__":
    main()
