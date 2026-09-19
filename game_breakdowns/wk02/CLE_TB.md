# GAME BREAKDOWN: Cleveland Browns @ Tampa Bay Buccaneers
### Week 2, 2026 Season | Scheduled 09/20/2026, 1:00 PM ET

---

## 1. PREGAME BRIEFING

**BOOTSTRAP EVIDENCE NOTICE:** This specific matchup has not been played (per the evidence package, `game.played: false`) — there is no box score, line, or result for CLE @ TB. However, this is not a fully hypothetical Week 1 preview: both teams have already played one real game in the 2026 season (their respective openers, not against each other), and that single-game 2026 sample is included in the evidence package alongside each team's complete, 2025 season-final statistical profile. Per the evidence package's own bootstrap source note, every team- and player-level season-long analytic (the `matchup`, `team_context`, `threats`, `players`, and `matchup_pattern_data` blocks) is built on 2025 season-final data for these two specific franchises — not a 2025 meeting between them, which the evidence explicitly notes likely never occurred as this exact pairing. Where this report says "this season" in a rate/rank context, it means the complete 2025 season used as the analytical foundation, unless explicitly marked as the current 1-game 2026 sample.

**Records.** Cleveland finished 2025 at 4-12; Tampa Bay finished 2025 at 7-9. Both are now 0-1 to open 2026 after their respective Week 1 losses (Cleveland at Jacksonville, Tampa Bay at home to Cincinnati). Neither the 2025 season-final logs nor the 2026 season-to-date logs in this evidence package show a meeting between these two specific teams — there is no real head-to-head data to draw on for this matchup.

**Broad shape of the game.** Both rosters enter this game as bottom-half-of-the-league offenses on paper: Cleveland's 2025 offense ranked in the bottom five of the NFL in scoring, total yardage, and passing yardage, while Tampa Bay's offense, while more middle-of-the-pack overall, still ranked in the bottom third in scoring and total yards. Both defenses, by contrast, carry real individual strengths — Cleveland's pass defense and Tampa Bay's run defense against backs both rank among the best units in this evidence package. On paper, this profiles as a lower-scoring, field-position-driven game between two rosters still working out their offensive identities early in the season, rather than a shootout. The deeper questions — who is actually playing quarterback for Cleveland, which unit's specific weaknesses get exploited, and what the actual expected script looks like — are addressed in the sections that follow.

---

## 2. INJURY & AVAILABILITY REPORT

Source: nflverse real injury report (`status_policy: final_designation_or_limited_practice`). All statuses below are listed as "Pending" in the raw feed, which per the source policy reflects a mid-week designation rather than a finalized game-status call — treat these as real, but not yet final, through the evidence freeze.

**Cleveland:**
- **Maliek Collins (DT)** — Quadricep, Limited Participation in Practice. A rotational interior lineman; limited impact on the specific matchups discussed below.
- **Elgton Jenkins (C)** — Back, Limited Participation in Practice.
- **Teven Jenkins (G)** — Back, Did Not Participate in Practice.
- **Tyson Campbell (CB)** — Ankle, Did Not Participate in Practice. A starting corner; his absence would be a real factor in coverage of Tampa Bay's outside receivers, though no individual CB/DB matchup data is available in this evidence package to quantify the effect (see Section 4).
- **Parker Brailsford (C)** — Thumb, Limited Participation in Practice.

Two real interior offensive line pieces (Elgton Jenkins and Teven Jenkins) carry meaningful practice-limiting back injuries, one of them a full non-participant. This is worth flagging directly against the backdrop of Cleveland's Week 1 pass protection, which allowed 5.0 sacks in that single game (see Section 4) — a line already dealing with real practice-participation questions at two starting interior spots.

**Tampa Bay:**
- **Miles Killebrew (S)** — Concussion, Limited Participation in Practice.
- **A'Shawn Robinson (DT)** — Listed as "Not injury related - resting player," Did Not Participate in Practice. A veteran load-management scratch, not an injury concern.
- **Jacob Parrish (CB)** — Back, Limited Participation in Practice.

**Quarterback availability note — genuine evidence tension.** No quarterback appears anywhere in either team's injury report. Yet the evidence package's own Threat Intelligence starters list (see Section 5) identifies **Shedeur Sanders**, not Deshaun Watson, as Cleveland's projected starter for this game — despite Watson being the quarterback who actually played, and posted the real Week 1 2026 numbers (205 pass yards, 1 TD, 1 INT, 5.0 sacks/game), in Cleveland's opener. This is a real conflict between two evidence sources: the injury report shows no quarterback change, but the deterministic starters list used for Threat Intelligence has already shifted to Sanders. This report treats that as a genuine, unresolved tension rather than picking one source over the other — the quarterback analysis in Section 4 covers both passers rather than assuming either is confirmed. Confidence on who actually starts: **LOW.**

---

## 3. MATCHUP STATISTICS

### Cleveland Offense (2025 season-final, with 2026 Week 1 value noted as v26)
- Scoring: 16.4 ppg (31st)
- Total offense: 282.4 yds/gm (31st); Week 1 2026: 292.0
- Passing: 185.4 pass yds/gm (31st); Week 1 2026: 205.0
- Rushing: 97.0 rush yds/gm (27th); Week 1 2026: 87.0
- First downs: 13.8/gm (31st)
- QB unit: 58.0% completion (32nd), 9.8 yards/completion (29th), 16 pass TD on the season (30th), 1.1 INT/gm (29th), 3.0 sacks/gm allowed (26th)
- RB unit: 70.8 rush yds/gm (30th) but 36.5 rec yds/gm (8th), 5.6 rec/gm (4th), 7.1 targets/gm (5th) — a passing-game-heavy backfield despite the weak ground numbers
- WR unit: 86.3 rec yds/gm (32nd — last in the league), 6.9 rec/gm (32nd), 4 total TD (32nd)
- TE unit: 62.6 rec yds/gm (8th), 6.5 rec/gm (3rd), 9.9 targets/gm (2nd), 10 TD (6th) — clearly the more trusted position group in the passing game relative to the WR corps

**Contextual Statistics (2025 opponent-quality splits, team level):** Cleveland's points scored scaled with opponent quality as expected — 15.0 ppg against top-tier defenses (n=2) up to 19.8 ppg against bottom-tier defenses (n=5). Passing yardage showed the same pattern more sharply: 161.2 pass yds/gm vs. top-tier defenses (n=4) rising to 220.4 vs. bottom-tier (n=7). Rushing production, by contrast, stayed essentially flat across all three tiers (103.0 / 89.3 / 104.2) — the ground game did not meaningfully expand or contract based on opponent quality.

**Down/Distance:** 33.6% third-down conversion rate (29th) on 13.8 attempts/gm; 18.5% fourth-down go-for-it rate, 41.4% conversion when going for it.

**Red Zone Play Calling:** 47.3% run rate in the red zone (18th), 52.7% pass rate (15th), on 7.6 red-zone plays/gm. This is a tendency stat, not a quality stat — it describes Cleveland's red-zone play mix, not how well it executes there.

### Cleveland Defense
- Scoring allowed: 22.3 ppg (14th)
- Total defense: 305.8 yds/gm (6th); Week 1 2026: 368.0
- Pass defense: 189.4 pass yds/gm (3rd); Week 1 2026: 245.0
- Rush defense: 116.4 rush yds/gm (16th); Week 1 2026: 123.0
- QB allowed: 63.3% completion allowed (11th), 3.1 sacks/gm generated (3rd), 0.6 INT/gm generated (17th), 24 pass TD allowed on the season (12th)
- RB allowed: 97.9 rush yds/gm (18th), 28.4 rec yds/gm allowed (12th)
- WR allowed: 109.5 rec yds/gm (1st in the NFL — the single best pass defense against wide receivers in this evidence package)
- TE allowed: 51.5 rec yds/gm (14th)

**Down/Distance:** 36.3% third-down conversion allowed (7th-best in the league), 63.7% stop rate, on 13.3 attempts faced/gm.

**Red Zone Play Calling (allowed):** 49.7% run rate allowed (16th), 50.3% pass rate allowed (18th) — roughly middle-of-the-pack in terms of what opponents choose to call against this defense inside the 20.

### Tampa Bay Offense
- Scoring: 22.4 ppg (18th)
- Total offense: 335.4 yds/gm (21st); Week 1 2026: 305.0
- Passing: 220.9 pass yds/gm (19th); Week 1 2026: 216.0
- Rushing: 114.5 rush yds/gm (21st); Week 1 2026: 89.0
- First downs: 17.0/gm (19th)
- QB unit: 62.9% completion (21st), 26 pass TD (15th), 0.6 INT/gm (17th), 2.2 sacks/gm allowed (18th)
- RB unit: 88.1 rush yds/gm (22nd), 31.1 rec yds/gm (15th)
- WR unit: 155.0 rec yds/gm (9th), 21.4 targets/gm (5th), 19 TD (7th) — a genuinely productive receiver corps
- TE unit: 34.6 rec yds/gm (32nd — dead last), 3.6 rec/gm (32nd), 2 TD (32nd) — the single worst-used position group in this evidence package on either side

**Contextual Statistics:** Tampa Bay's team scoring splits were non-monotonic and worth flagging as noisy — 22.6 ppg vs. top-tier defenses (n=5), 24.1 vs. mid-tier (n=8), but only 19.3 vs. bottom-tier (n=3, a small sample). Passing yardage followed a similarly flat, non-monotonic pattern (204.0 / 234.8 / 225.0 across tiers, with the bottom-tier figure resting on just n=2 games). The WR unit's production was the most stable of any group in this report — 157.0 rec yds/gm vs. top-tier defenses (n=8) against 163.7 vs. mid-tier (n=7), essentially flat regardless of matchup quality. The TE unit, while dead last overall, still showed some matchup sensitivity (14.8 rec yds/gm vs. top-tier, n=6, climbing to 46.2 vs. bottom-tier, n=4).

**Down/Distance:** 41.2% third-down conversion rate (11th) on 13.4 attempts/gm; 21.5% fourth-down go-for-it rate, 44.8% conversion.

**Red Zone Play Calling:** 44.3% run rate (24th), 55.7% pass rate (9th-highest pass rate in the red zone in the league) — a team that leans toward the pass once inside the 20 more than most.

### Tampa Bay Defense
- Scoring allowed: 24.2 ppg (20th)
- Total defense: 355.9 yds/gm (20th); Week 1 2026: 360.0
- Pass defense: 254.8 pass yds/gm (27th); Week 1 2026: 254.0
- Rush defense: 101.1 rush yds/gm (5th); Week 1 2026: 106.0
- QB allowed: 66.7% completion allowed (26th), 30 pass TD allowed (26th), 2.2 sacks/gm generated (18th), 0.8 INT/gm generated (13th)
- RB allowed: 78.8 rush yds/gm (6th — very good) but 50.6 rec yds/gm allowed (32nd — worst in the NFL)
- WR allowed: 147.6 rec yds/gm (23rd)
- TE allowed: 57.0 rec yds/gm (21st)

**Down/Distance:** 39.5% third-down conversion allowed (15th), 60.5% stop rate, on 11.8 attempts faced/gm.

**Red Zone Play Calling (allowed):** 43.4% run rate allowed (26th), 56.6% pass rate allowed (7th-highest pass rate faced in the red zone) — opponents throw against this defense inside the 20 more than against almost anyone else in the league. Again, a tendency, not a quality read on its own.

**Evidence gap, stated plainly:** `team_coverage_rate` (each defense's own man%/zone% play-calling identity) returned empty for both teams in this evidence package, as did the `blitz_qb`, `blitz_wr`, `coverage_qb`, `coverage_wr`, `coverage_te`, `rb_rush_vs_pass`, and `cb_db_rankings` fields. These categories are not available for this matchup and are not fabricated below — the Matchup Intelligence section notes this explicitly where relevant rather than guessing.

---

## 4. MATCHUP INTELLIGENCE

### Quarterbacks

**Cleveland — Deshaun Watson vs. Shedeur Sanders (starter uncertain — see Section 2).** Watson actually played Cleveland's Week 1 2026 opener at Jacksonville: 205 pass yards, 16-of-22 (72.7%), 1 TD, 1 INT, and — the number that stands out — 5.0 sacks in that single game, a brutal protection number in any context. He has no 2025 season to compare against (`season_2025` is null) — he missed the entire 2025 season. His career averages (74 games through 2025: 244.7 pass ypg, 66.3% completion, 11.7 yards/completion) sit meaningfully above his Week 1 2026 output, though a single game is too thin a sample to draw a firm conclusion from either direction. Confidence: LOW, given both the tiny sample and the uncertainty over whether he even plays.

Shedeur Sanders, meanwhile, is the quarterback the evidence package's own Threat Intelligence starters list projects for this game, despite having zero 2026 games logged. His most relevant number is his 2025 season line as a rookie: 8 games, 175.0 pass ypg, 56.6% completion, 7 pass TD, 1.25 INT/gm, and 2.88 sacks/gm — a rough, high-turnover, high-sack rookie sample. *(2025: 175.0 pass ypg, 56.6% comp, 7 pass TD, 1.25 INT/gm, 2.88 sacks/gm across 8 games.)*

Whichever passer plays, the opponent-quality context is the same and doesn't depend on which name is under center: Tampa Bay's pass defense ranks 27th in the NFL (254.8 pass yds/gm allowed) — a genuinely soft matchup — while Tampa Bay's run defense ranks 6th (78.8 rush yds/gm allowed) — a much tougher one. The evidence package's own QB Run-vs-Pass data (built on Watson's Week 1 sample, `opponent_context_recomputed_for_bootstrap`) classifies this specific opponent split as a "bottom"-tier pass matchup for Cleveland (favorable) against a "top"-tier run matchup (unfavorable) — consistent with the raw defensive ranks above. Confidence in this specific opponent read: MEDIUM, since it's built from team-level 2025 season-final ranks rather than a single-QB sample.

**Tampa Bay — Baker Mayfield.** His Week 1 2026 line was efficient but unremarkable in scoring terms: 23-of-28 (82.1% completion — well above his career norm), 216 pass yards, 0 TD, 0 INT, but 4.0 sacks allowed. *(2025: 217.2 pass ypg, 63.2% comp, 26 pass TD, 0.65 INT/gm, 2.12 sacks/gm across 17 games.)* The completion rate spike (82.1% vs. a 63.2% 2025 season rate) alongside zero touchdowns suggests a short, high-percentage, low-explosive game plan in the opener — worth watching whether that becomes a pattern (see Section 6). He now faces Cleveland's pass defense, which ranks 3rd in the NFL (189.4 pass ypg allowed) — the toughest individual defensive matchup either quarterback in this game will see. The evidence package's own opponent-quality classification confirms this: a "top"-tier pass matchup (unfavorable) against a "mid"-tier run matchup (Cleveland's run defense ranks 16th, 97.9 rush ypg allowed). Confidence: MEDIUM-HIGH that Mayfield's efficient-but-modest profile continues against this specific pass defense.

### Running Backs

**Cleveland — Quinshon Judkins.** The clear lead back: 54.5% rush share in the Week 1 opener (12 carries, 33 rush yards, 2 catches for 17 yards), and a dominant 66.1% rush share and 64.7% red-zone carry share across his full 2025 season (14 games, 59.07 rush ypg, 7 rush TD). *(2025: 59.07 rush ypg, 16.43 car/gm, 66.1% rush share, 64.7% red-zone carry share.)* His rushing-contact profile flipped between samples: in 2025 he averaged 2.20 yards after contact per carry against just 1.40 yards before contact — a runner who created much of his own yardage — with 0.79 broken tackles/gm. His Week 1 2026 sample (0.83 yards after contact, 1.92 before contact, 0 broken tackles) inverted that pattern, though on just 12 carries against Jacksonville, not this week's opponent. He now faces a Tampa Bay run defense ranked 6th in the league (78.8 rush ypg allowed) — a legitimately tough individual matchup on the ground. Where he profiles as more interesting is as a receiver: his RB unit ranks top-10 in the NFL in receiving usage (see Section 3), and Tampa Bay's defense is specifically the worst in the league against receiving backs (50.6 rec yds/gm allowed, 32nd) — see Section 6 for the full cross-reference. Confidence: MEDIUM on the rushing matchup being tough, MEDIUM on the receiving role being a live outlet.

Behind him, **Dylan Sampson** logged zero touches in the Week 1 opener despite a real 17.4% rush share across 15 games in 2025 — worth monitoring as a real change in role, though nothing in the injury report explains it. **Raheim Sanders** saw a complementary 4.5% rush share and 13.6% target share in Week 1 (1 rush yard, 3 catches for 25 yards) — a modest but real receiving role.

**Tampa Bay — Bucky Irving.** The clear lead back, and his Week 1 usage jumped notably in the passing game: 40.0% rush share (8 carries, 45 yards, 1 rush TD) alongside a 25.9% target share (7 targets, 7 catches, 48 yards) — well above his 2025 season target share of 11.3%. *(2025: 58.8 rush ypg, 27.7 rec ypg, 59.2% rush share, 11.3% target share, 34.4% red-zone touch share across 10 games.)* His contact-efficiency numbers were consistent across samples — 2.62 yards after contact / 3.00 before contact in Week 1 versus 1.64 after / 1.76 before across his 2025 season, with 1.0 broken tackle/gm in both samples — a back who creates real value after first contact regardless of sample size. He now faces a Cleveland run defense ranked 16th (97.9 rush ypg allowed) — a middle-of-the-road matchup, neither a funnel nor a shutdown unit. **Kenny Gainwell** (25.0% rush share, 15 yards on 5 carries in Week 1) is the clear complementary piece, and **Sean Tucker** — a real, established 2025 short-yardage/red-zone specialist (7 rush TD, 31.8% red-zone carry share across 17 games in 2025) — logged zero 2026 games despite no injury designation, worth flagging as a real absence from the offense's usage pattern so far.

### Wide Receivers / Tight Ends

**Cleveland — Jerry Jeudy.** The established WR1: 18.2% target share in Week 1 (4 targets, 2 catches, 26 yards), broadly consistent with his full 2025 role (106 targets, 6.24 targets/gm, 35.41 rec ypg, 20.3% target share, 84.5% snap share across 17 games). *(2025: 35.41 rec ypg, 20.3% target share, 84.5% snap share.)* He now faces the single toughest individual matchup in this entire evidence package: Cleveland's own passing attack aside, Tampa Bay's defense is not the concern here — Jeudy is on offense. The relevant opposing unit is Tampa Bay's pass defense (27th, 254.8 pass ypg allowed) — a genuinely favorable matchup on paper for Cleveland's passing attack broadly, even though Jeudy's own WR unit has been the least productive position group on either roster in this report (32nd in the league).

**Denzel Boston** had arguably the standout individual performance of Week 1 for either team: 59 receiving yards on 2 catches (4 targets), including a touchdown, an 18.2% target share, and a 92% snap share — but he has no 2025 season to compare against (a rookie; `season_2025` is null). Treat this as a genuine but extremely thin sample. **KC Concepcion** also debuted productively (43 yards, 4 catches on 5 targets, 22.7% target share) with no 2025 season available either. Confidence on either rookie sustaining Week 1 usage: LOW, single-game samples only.

**Harold Fannin Jr. (TE)** is Cleveland's most trusted target beyond Jeudy: 82% snap share and a 13.6% target share in Week 1 (3 targets, 2 catches, 21 yards), building on a real, established 2025 season (16 games, 45.69 rec ypg, 21.4% target share, 16.7% red-zone target share). *(2025: 45.69 rec ypg, 21.4% target share, 16.7% red-zone target share.)* Cleveland's TE unit ranks top-10 in the NFL in receiving production (see Section 3), and Fannin is the reason why.

**Tampa Bay — Chris Godwin Jr.** Week 1: 40 yards on 4 catches (4 targets), 14.8% target share, 86% snap share. *(2025: 40.0 rec ypg, 18.3% target share, across 9 games — a season limited by injury.)* **Emeka Egbuka** is the clear WR1 by target share: 22.2% target share in Week 1 (6 targets, 5 catches, 63 yards), consistent with a real 2025 rookie season (17 games, 55.18 rec ypg, 23.5% target share, 14.89 yards/reception). *(2025: 55.18 rec ypg, 23.5% target share, 14.89 ypr.)* He now faces the single best pass defense against wide receivers in this entire evidence package — Cleveland ranks 1st in the NFL, allowing just 109.5 WR receiving yards per game. This is the toughest individual assignment in this report, and it deserves real weight against his otherwise strong role. Confidence: MEDIUM that this specific matchup suppresses his raw output below his season norm, tempered by the fact that Tampa Bay's WR unit as a whole showed almost no sensitivity to opponent quality in 2025 (157.0 rec ypg vs. top-tier defenses, 163.7 vs. mid-tier — essentially flat; see Section 3). **Jalen McMillan**, a real complementary piece from the same 2025 roster (4 games, 44.5 rec ypg, 12.2% target share before injury), logged zero 2026 games with no injury listed — a real, established option currently out of the rotation for reasons the evidence doesn't clarify.

**Cade Otton (TE)** posted a real red-zone role in Week 1 that stands in sharp contrast to his unit's full-season 2025 profile: 5 targets (18.5% target share), including 2 of Tampa Bay's red-zone targets (a 50.0% red-zone target share for one game), on a 98% snap share. *(2025: 38.13 rec ypg, 16.9% target share, 10.0% red-zone target share across 15 games.)* Tampa Bay's TE unit ranked dead last in the NFL across every meaningful category in 2025 (see Section 3) — Otton's early 2026 role is a real deviation worth tracking, developed further in Section 6.

**Coverage and scheme detail — evidence gap, stated plainly.** This report cannot provide man/zone coverage tendencies, blitz rate effects, or individual CB/DB matchup detail for this game. The `team_coverage_rate`, `blitz_qb`, `blitz_wr`, `coverage_qb`, `coverage_wr`, `coverage_te`, and `cb_db_rankings` evidence fields are all empty in this bootstrap package for both teams. This is a genuine data gap, not an oversight — no scheme-level claims are made in place of it.

---

## 5. THREAT INTELLIGENCE

**How the system works.** A Threat designation fires when a player's own season rank in a specific statistical category and the upcoming opponent's defensive rank in that same category both clear a tier's exact threshold at the same time — the convergence of genuinely elite individual production and a genuinely weak matchup in the same specific stat, not either signal on its own. The three tiers use these exact thresholds (player rank is 1st-best; defense rank is 1st-toughest, so a high defense-rank number means a weak defense):

- **Nuclear** — player ranks top 3 in the category AND the opponent's defense ranks 30th or worse in that same category
- **Elite** — player ranks top 5 AND opponent defense ranks 28th or worse
- **Standard** — player ranks top 10 AND opponent defense ranks 23rd or worse

Double/Triple/Quadruple labels reflect how many categories converged for that player at once.

**Result for this matchup: no Threat designation fired for any evaluated player on either side.** The evidence package's Threat Engine evaluated Shedeur Sanders, Quinshon Judkins, Jerry Jeudy, Isaiah Bond, and Harold Fannin for Cleveland, and Baker Mayfield, Kenneth Gainwell, Chris Godwin, Emeka Egbuka, and Cade Otton for Tampa Bay. None of the underlying category convergences met even the Standard tier's thresholds.

This absence is itself informative in one specific case: Emeka Egbuka's own receiving profile is genuinely strong, but the opposing defense in that category — Cleveland's WR pass defense — ranks 1st in the NFL (the opposite of a weak defense), which is precisely why no Threat could fire there regardless of his own numbers; the convergence mechanism requires weakness on both sides, not strength on one. The absence of a Threat designation elsewhere in this game should be read as "this specific convergence system's thresholds weren't met" — not as evidence that no real matchup edges exist. Sections 3, 4, and 6 identify genuine matchup advantages (Cleveland's RB receiving game against Tampa Bay's league-worst RB pass defense, in particular) that fall outside this system's specific dual-threshold design.

---

## 6. HIDDEN INTELLIGENCE & CONTEXTUAL ANALYSIS

**Finding 1: Tampa Bay's single worst individual defensive weakness in this entire evidence package lines up almost perfectly with a stable, opponent-quality-resistant part of Cleveland's offensive identity.** Tampa Bay's defense allows 50.6 receiving yards per game to running backs — the worst mark in the NFL (32nd). Cleveland's running back corps, meanwhile, ranks top-10 in the league in exactly that usage: 36.5 rec yds/gm (8th), 5.6 rec/gm (4th), and 7.1 targets/gm (5th) to its backs. The reason this is more than a simple "strength vs. weakness" pairing is the context: Cleveland's RB receiving production barely moved across opponent quality in 2025 (37.0 rec yds/gm vs. top-tier defenses, n=6; 40.2 vs. mid-tier, n=6; 31.5 vs. bottom-tier, n=4) — Cleveland uses its backs as receivers as a matter of scheme identity, not as a response to a soft matchup. That combination — a stable tendency meeting the single worst defense in the league at defending it — is a stronger, more repeatable signal than either fact alone. This applies most directly to Quinshon Judkins as the clear early-down/passing-down lead back, with Raheim Sanders as a real complementary outlet. Confidence: MEDIUM (built on full-season 2025 rank extremes on both sides, but Tampa Bay's specific defensive number reflects only a partial 2025 sample against Cleveland's exact personnel).

**Finding 2: Tampa Bay's tight end usage was the single worst position-group profile on either roster in 2025 — dead last in the NFL in every major category — yet the Week 1 2026 opener already shows a real break from that pattern.** Cade Otton drew 5 targets (an 18.5% target share) and, notably, 2 of Tampa Bay's red-zone targets that game — a 50.0% red-zone target share for a single game — against a full 2025 season in which the position averaged only a 16.9% target share and 10.0% red-zone target share. This matters specifically because Tampa Bay already throws more than most teams once it reaches the red zone (55.7% red-zone pass rate, 9th-highest in the league) — in 2025, that red-zone passing volume mostly bypassed the tight end position; the Week 1 sample suggests it may not this year. One game is a thin foundation to build a firm conclusion on, but the direction and magnitude of the shift (18.5% vs. 16.9% target share, and a dramatic red-zone jump) is large enough to flag as a real, if unconfirmed, change worth tracking against a Cleveland defense that is otherwise a middling matchup for tight ends (51.5 rec ypg allowed, 14th). Confidence: LOW-MEDIUM, given the single-game sample.

**Finding 3: Cleveland's own pass defense generates pressure without generating takeaways, which — cross-referenced with both teams' third-down profiles — points toward a longer, lower-variance kind of game than the raw scoring numbers alone would suggest.** Cleveland's defense ranks 3rd in the NFL in sacks generated (3.1/gm) but only 17th in interceptions forced (0.6/gm) and allows a middling 24 pass touchdowns on the season (12th) — a defense that wins on negative plays rather than takeaways. Layer in the down-and-distance picture: Tampa Bay's offense converts third downs at a real 41.2% clip (11th), while Cleveland's defense allows just 36.3% on third down (7th-best in the league) — two above-average units set against each other rather than a clear mismatch. The early evidence from Baker Mayfield's own Week 1 debut supports this shape directly: 82.1% completion but zero touchdowns, a profile built on short, high-percentage completions rather than explosive plays. None of this guarantees a low-scoring outcome, but it argues against a shootout script specifically — sustained drives, real third-down battles, and negative plays (sacks) rather than turnovers or explosive completions deciding field position. Confidence: MEDIUM — each individual data point is real and specific, but the combined "grinding, low-explosive" read is an inference rather than a directly labeled outcome.

---

## 7. COEUS FINAL READ

**Keys to the Game:**

- **If Cleveland's interior offensive line (Elgton Jenkins and Teven Jenkins, both dealing with real practice-limiting back injuries) cannot hold up,** the Week 1 sack rate (5.0 sacks allowed in that single game) is likely to repeat or worsen — a real risk regardless of which quarterback plays, and a factor that could turn an already-favorable Cleveland pass-yardage matchup into a low-value one if the quarterback never gets time to access it.
- **If Cleveland leans on its backs and tight ends in the passing game rather than forcing the ball to its league-worst wide receiver corps,** that plays directly into Tampa Bay's specific defensive weakness at RB pass defense (Finding 1) — watch early-down target distribution as a signal of whether the offense is playing to that funnel.
- **If Cade Otton's Week 1 red-zone role (2 of Tampa Bay's red-zone targets) repeats rather than reverting to the team's 2025 season-long tight-end profile (dead last in the league),** that changes where Tampa Bay's most likely scoring plays come from in a game that otherwise projects as low-scoring.
- **If both third-down units perform to their real 2025 form** (Tampa Bay converting near 41%, Cleveland allowing under 37%), expect a genuine field-position battle rather than a game decided by one unit's collapse.

**The Verdict.** This opens as a game between two rosters still finding their offensive footing, and the deeper evidence supports that broad framing rather than complicating it: Cleveland's offense is bottom-five across nearly every meaningful category, Tampa Bay's is middling, and both defenses carry one real individual strength (Cleveland's pass defense, Tampa Bay's run defense against backs) without an obviously dominant complete unit on either side. The specific mechanism worth watching is not which team's stars take over, but which team's structural weaknesses get exposed first — Cleveland's protection questions against its own uncertain quarterback situation, or Tampa Bay's league-worst tight end usage and worst-in-the-NFL RB pass defense getting attacked directly by Cleveland's stable backfield passing-game usage. Confidence in the overall shape (a longer, lower-scoring, field-position-driven game rather than a shootout): MEDIUM. Confidence in any single specific outcome inside that shape: LOW, given the number of open questions (starting quarterback, offensive line health, and the very early, thin 2026 samples) still unresolved heading into kickoff.

---

### COEUS CHEAT SHEET

**Team**
- CLE: 2025 record 4-12; 2026 record 0-1
- TB: 2025 record 7-9; 2026 record 0-1
- CLE 2025 scoring: 16.4 ppg (31st) | TB 2025 scoring: 22.4 ppg (18th)
- CLE 2025 points allowed: 22.3 ppg (14th) | TB 2025 points allowed: 24.2 ppg (20th)

**Passing**
- Deshaun Watson (CLE, Week 1 2026 starter): 205 pass yds, 1 TD, 1 INT, 5.0 sacks taken *(no 2025 season — missed the year)*
- Shedeur Sanders (CLE, projected Threat-list starter): 0 2026 games *(2025: 175.0 pass ypg, 56.6% comp, 7 TD, 1.25 INT/gm)*
- Baker Mayfield (TB): 216 pass yds, 0 TD, 0 INT, 82.1% comp *(2025: 217.2 pass ypg, 63.2% comp, 26 TD)*

**Rushing**
- Quinshon Judkins (CLE): 33 rush yds/12 car, 1 TD *(2025: 59.07 rush ypg, 66.1% rush share, 7 rush TD)*
- Bucky Irving (TB): 45 rush yds/8 car, 1 TD *(2025: 58.8 rush ypg, 59.2% rush share)*

**Receiving**
- Jerry Jeudy (CLE): 26 yds/2 rec/4 tgt *(2025: 35.41 rec ypg, 20.3% target share)*
- Harold Fannin Jr. (CLE, TE): 21 yds/2 rec/3 tgt *(2025: 45.69 rec ypg, 21.4% target share)*
- Emeka Egbuka (TB): 63 yds/5 rec/6 tgt *(2025: 55.18 rec ypg, 23.5% target share)*
- Cade Otton (TB, TE): 26 yds/3 rec/5 tgt, 50% RZ target share *(2025: 38.13 rec ypg, 16.9% target share)*

**Team Defense**
- CLE pass D: 189.4 ypg allowed (3rd) | CLE rush D: 116.4 ypg allowed (16th)
- CLE vs. WR: 109.5 ypg allowed (1st) | CLE vs. TE: 51.5 ypg allowed (14th)
- TB pass D: 254.8 ypg allowed (27th) | TB rush D: 101.1 ypg allowed (5th)
- TB vs. RB (receiving): 50.6 ypg allowed (32nd — worst in NFL) | TB vs. WR: 147.6 ypg allowed (23rd)
- Team coverage rate (man%/zone%): not available in this evidence package for either team

**Down/Distance**
- CLE offense: 33.6% third-down conv. (29th) | CLE defense: 36.3% allowed (7th)
- TB offense: 41.2% third-down conv. (11th) | TB defense: 39.5% allowed (15th)

**Red Zone Play Calling**
- CLE offense: 47.3% run / 52.7% pass (18th/15th) | CLE defense allowed: 49.7% run / 50.3% pass (16th/18th)
- TB offense: 44.3% run / 55.7% pass (24th/9th) | TB defense allowed: 43.4% run / 56.6% pass (26th/7th)

**Head-to-head**
- No meeting between these two teams exists in the available 2025 or 2026 evidence.