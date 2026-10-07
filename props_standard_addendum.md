COEUS PROPS & PARLAY REPORT STANDARD — ADDENDUM v2.1 (2026-10-07)

This addendum is part of the Standard. Where it conflicts with Standard
v2.0 (or the Master Prompt) on any point below, THIS ADDENDUM GOVERNS.
Everything in v2.0 not contradicted here still applies in full — real
data only, the No Paragraphs Rule, the price format rule, the stat-and-
rank reasoning rule, the evidence_check rule, the line field rule.

============================================================
A1. 2026 DATA ONLY (NON-NEGOTIABLE)
============================================================

Every pick is grounded in 2026 regular-season data only.

- Do not cite any 2025 number, rank, trend, or game, in any pick's
  reason or anywhere else in the report. If a Game Breakdown or evidence
  block happens to mention 2025, ignore that figure; do not repeat it.
- The v2.0 RANK SHIFT RULE (2025-vs-2026 comparisons) and the
  `rank_shift` evidence_check type are RETIRED. Never write one.
- Every pick must state how many 2026 games its evidence rests on, both
  in the reason text ("through 4 games this season ...") and in the
  pick's `games_2026` field (integer). Small samples are fine to use but
  must be named as small: with 3 or fewer games behind a pick, say so in
  the reason and do not rank it among your top conviction plays.

============================================================
A2. YOUR OWN PROJECTION ON EVERY PICK (NON-NEGOTIABLE)
============================================================

Every pick in every JSON block carries a numeric `projection`: YOUR OWN
number for what you expect to happen, derived from the 2026 evidence,
not the posted line restated.

- Yardage and reception props: `projection` is your expected stat total
  for that player this game (e.g. 238 passing yards). An Over pick needs
  a projection ABOVE the line; an Under pick needs a projection BELOW it
  (for an alt/milestone "N or more" pick, the projection must reach N).
  A projection equal to the line is not a pick.
- Anytime TD: `projection` is your probability that the player scores,
  as a decimal between 0 and 1 (e.g. 0.58). It must exceed the price's
  implied probability (1 divided by the decimal price) or it is not a
  pick.
- Spreads: `projection` is your projected final margin for the team you
  are backing, in points (positive means that team wins by that many).
  It must clear the spread: projection + spread point must be greater
  than zero.
- The reason must show how the projection was built in one sentence
  (the 2026 per-game rate, adjusted for the opponent's 2026 rank and the
  game environment). The projection is graded against the real result
  after the game, so state your honest number, not a number chosen to
  agree with the side.
- A script rejects any pick whose projection contradicts its own side,
  or that is missing `projection` or `games_2026`.

============================================================
A3. GAME ENVIRONMENT CHECK FOR PASSING YARDS
============================================================

Passing-yardage picks (plain or alt) have been this report's weakest
market. Before writing one, read the game's real total and spread from
the FanDuel game lines provided, and state both in the reason.

- A QB passing Over needs an environment that supports passing volume
  (a total that is not low, a game that is not expected to be a lopsided
  run-out). If the total or spread points the other way, pick the Under
  or make no passing pick for that game.
- Do not default to passing-yardage Overs. In the weekly best 10, at
  most TWO picks may be QB passing-yardage Overs.
- Treat Overs and Unders with equal rigor across all markets; choose the
  pick types where the 2026 evidence is strongest, not the most
  recognizable names.

============================================================
A4. THE WEEKLY BEST 10 (REPLACES THE WHOLE-WEEK PARLAY SECTIONS)
============================================================

The whole-week run (after all game batches are done) now produces ONE
slate of exactly 10 plays, ranked 1 to 10 by conviction, drawn from the
whole week's slate. A play may be any real market on the board (a
yardage/reception Over or Under, an alt line, an Anytime TD, or a
mainline spread), and may reuse a pick from the batch reports or be a
better one found in the real data.

- Exactly 10 plays. No two with the same game, market, player and line.
- Every play carries the full pick JSON: player, market_key,
  canonical_event_id, price, side, line (or point/threshold as
  applicable), reason, evidence_check, projection, games_2026, plus
  `rank` (1 to 10).
- JSON block name: BEST_10, an object with a "picks" array, written
  exactly like the other blocks.

============================================================
A5. PARLAYS: 2, 3 AND 4 LEGS, BUILT ONLY FROM THE BEST 10
============================================================

Parlay Sections 6, 7 and 8 of v2.0 (the 3/4/5/6/7-team line parlays,
Anytime TD parlays and Spread parlays) are RETIRED. In their place:

- Exactly three parlays: a 2-leg, a 3-leg and a 4-leg.
- Every leg must be one of the 10 plays in BEST_10, exactly as written
  there (same player, market, side and line). No leg may come from
  outside the 10.
- Every leg of a parlay must come from a DIFFERENT game. No two legs
  from the same game, ever. Build each parlay from your highest-
  conviction plays that satisfy this.
- Markets may be mixed within a parlay (a TD or a spread may sit beside
  a yardage prop), since all legs come from the 10.
- JSON block names: PARLAY_2_TEAM, PARLAY_3_TEAM, PARLAY_4_TEAM, each an
  array of leg objects (same shape as the BEST_10 picks, including
  `projection` and `games_2026`).
- Per-game batch runs produce NO parlays at all.
