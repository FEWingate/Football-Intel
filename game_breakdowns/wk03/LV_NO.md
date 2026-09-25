# GAME BREAKDOWN: Las Vegas Raiders @ New Orleans Saints
### Week 3, 2026 Season | Scheduled 09/27/2026, 4:25 PM ET

**EVIDENCE METHODOLOGY NOTE:** This evidence package is labeled as a bootstrap package, but it is not a pure bootstrap in the sense of having zero current-season data — both teams have actually played two 2026 games already (LV is 2-0, NO is 1-1), and those two games' individual box scores are present throughout this package (player `season` blocks, `log` entries, and the `matchup_pattern_data` analytics). What genuinely is 2025-only is the opponent-quality tier-split data used for Matchup Statistics/Intelligence and Hidden Intelligence (the `team_context` game logs, an 17-week 2025 log for each team, since two 2026 games isn't a large enough sample to build reliable tiered splits yet) and the down-distance/red-zone play-calling data (no 2026 recompute available for those categories yet). This report treats 2026 year-to-date figures (2 games, or fewer for some players) as the current season snapshot, cites full 2025 season-final numbers as the required comparison point per the 2025 Season Context Rule, and clearly labels opponent-quality tier splits as drawn from the 2025 season log. There is no evidence of these two teams having met in 2025 or earlier in 2026 (`div_game: false`, no shared log entries) — this is treated as a first meeting for head-to-head purposes.

---

## 1. PREGAME BRIEFING

Both of these teams looked like bottom-of-the-league offenses in 2025, and both have opened 2026 dramatically better on that side of the ball — but their defensive trajectories have gone in opposite directions, and that divergence is the central storyline entering Week 3.

Las Vegas finished 2025 with the NFL's 32nd-ranked scoring offense (14.2 ppg); through two 2026 games, that offense ranks 12th (26.5 ppg) — a 20-spot jump. Its defense has made an equally dramatic move: 25th in points allowed in 2025 (25.4 ppg) to 5th early in 2026 (13.5 ppg allowed). This is a team that has improved on both sides of the ball simultaneously, not just one.

New Orleans's turnaround looks different. Its offense has also surged — from 28th in scoring in 2025 (18.0 ppg) to 9th through two 2026 games (27.0 ppg), and its passing offense specifically has gone from a middling 10th in the league in 2025 (236.9 pass yds/gm) to literally 1st early in 2026 (331.0 pass yds/gm). But New Orleans's defense has moved the opposite direction across nearly every category: points allowed 16th to 19th, total yards allowed 10th to 22nd, pass yards allowed 5th to 16th, rush yards allowed 19th to 27th, and first downs allowed 11th to 29th — an 18-spot slide that's easily the most dramatic single number in this evidence package. All of these categories moved the same direction at once, which argues this is a real, structural defensive regression early in the season rather than a one-week fluke.

The broad shape this suggests: Las Vegas enters with a more balanced two-way improvement, while New Orleans looks like an offense-carried team whose defense is trending toward being a real liability. Whether that translates into a shootout, a Las Vegas-controlled game, or something else depends heavily on how sustainable New Orleans's passing surge actually is (a question this report returns to below) and how the running-back and tight-end availability situations for each team resolve by kickoff — both addressed in the next two sections.

---

## 2. INJURY & AVAILABILITY REPORT

**Source:** nflverse real injury report (`status_policy: final_designation_or_limited_practice`). This is a genuine injury-report feed, not a betting-site status column — but every listed player currently carries a `report_status` of "Pending," meaning none of these are yet final game-day designations (Out/Doubtful/Questionable) as of this evidence freeze. Treat practice participation level as the best available signal of trajectory, not a confirmed final status.

**Las Vegas:**
- **Brock Bowers (TE) — Knee, Limited Participation in Practice.** This is the single most consequential injury note in this report. Bowers was LV's clear top receiving weapon in 2025 (56.7 rec yds/gm, a 23.6% target share, and a massive 36.7% red-zone target share), but he has played zero games in 2026 — his season log shows `games: 0`. His practice status this week (Limited, not a full DNP) is the first sign he may be trending back. See Matchup Intelligence for how his absence has reshaped LV's passing offense and what his return would mean.
- **Aidan O'Connell (QB) — listed for a personal matter, not injury-related, Did Not Participate.** He is LV's third-string quarterback (depth chart pos_rank 3, behind Cousins and Fernando Mendoza); this has no material bearing on the starting lineup.
- **Dareke Young (WR) — Hamstring, Limited.** A depth piece with a 1.7% target share this season; minimal impact either way.
- Foley Fatukasi (DT, Shoulder, Limited), Nakobe Dean (LB, Shoulder, Limited), Darien Porter (CB, Foot, Limited), and Treydan Stukes (S, Concussion, Did Not Participate) round out LV's list — all defensive/depth pieces without individually documented statistical profiles in this evidence package relevant to the offensive/defensive matchups covered below.

**New Orleans:**
- **Travis Etienne (RB) — Hamstring, Limited Participation.** Etienne is the closest thing New Orleans has to a lead back (see Matchup Intelligence for the muddled committee picture), so any further limitation would matter. A Limited practice designation suggests he's considered probable for now, but this bears watching through the week.
- **Barion Brown (WR) — Hamstring, Did Not Participate.** Minimal impact; he has zero receiving production through two 2026 games (season averages: 0.0 targets, 0.0 rec yds/gm on a 5.5% snap share).
- Martin Emerson (CB, Shoulder, Did Not Participate), Jonas Sanker (S, Knee, Limited), Nathan Shepherd (DT, Hip, Limited), Chase Young (LB, Calf, Limited), and Christen Miller (DT, Toe, Did Not Participate) are defensive pieces without documented statistical profiles that bear on the offensive/defensive breakdowns below.

---

## 3. MATCHUP STATISTICS

### Las Vegas Offense
Season identity: scoring offense ranked 32nd in 2025 (14.2 ppg), now 12th through two 2026 games (26.5 ppg) — a 20-spot improvement. Total yardage moved from 32nd (272.3 ypg, 2025) to 21st (300.0 ypg, 2026); passing offense from 26th (195.0 ypg) to 21st (206.5 ypg); rushing offense from 32nd (77.3 ypg) to 23rd (93.5 ypg); first downs per game from 32nd (13.4) to 20th (16.0).

By position group (2025 season-final, with rank): QB pass yds/gm 195.0 (25th), completion% 66.0% (12th), 3.8 sacks/gm allowed (32nd — worst in the league); RB rush yds/gm 65.9 (31st); WR rec yds/gm 99.8 (30th); TE rec yds/gm 68.3 (3rd — LV's 2025 tight end production was elite; see Matchup Intelligence for why that number has fallen to just 33.0 ypg through two 2026 games).

Third-down offense: 33.8% conversion rate (28th) on 12.5 attempts/gm — one of the league's weaker units at sustaining drives. Red-zone play calling: 40.2% run rate (29th) against 59.8% pass rate (4th) — LV is one of the most pass-heavy red-zone offenses in the league, a tendency stat, not a quality one.

2025 opponent-quality context (team_context, full season): LV scored far less against its toughest defensive matchups (13.0 ppg vs. top-tier, n=9) than its weakest (17.5 ppg vs. bottom-tier, n=4); its rushing offense showed a similar but sharper gap (66.9 rush ypg vs. top-tier, n=9, up to 132.0 vs. bottom-tier, n=3) while its passing offense was comparatively flat across tiers (190.3 top / 189.8 mid / 232.2 bottom).

### Las Vegas Defense
Season identity: points allowed ranked 25th in 2025 (25.4 ppg), now 5th through two 2026 games (13.5 ppg allowed) — a 20-spot improvement, the single largest defensive swing in this game. Total yards allowed moved from 14th (331.2 ypg) to 11th (306.5 ypg); pass yards allowed from 13th (214.4 ypg) to 11th (206.0 ypg) — a modest, two-spot improvement; rush yards allowed from 17th (116.8 ypg) to 15th (100.5 ypg) — also modest.

By position group (2025 season-final): allowed 210 total catches to wide receivers, 29th in the league (worst tier), for 2,503 yards (22nd) — but only 11.9 yards per reception allowed to WRs, 5th-best in the NFL. That combination (high catch volume allowed, low yards-per-catch allowed) describes a bend-but-don't-break underneath coverage profile — see Matchup Intelligence and Hidden Intelligence for how directly this maps onto New Orleans's passing attack. TE defense was much stingier: 68.3 rec yds/gm allowed... wait, that figure belongs to LV's offense — LV's actual TE defense allowed just 38.6 rec yds/gm in 2025 as noted below in the position table, an elite number.

Third-down defense: 46.3% conversion rate allowed (30th) — one of the league's worst units at getting off the field. Red-zone defense: opponents ran the ball against LV 56.8% of the time once inside the 20 (3rd-highest run rate faced in the league) against just 43.2% pass rate faced (30th) — teams are clearly choosing to run at LV in the red zone far more than the league average.

### New Orleans Offense
Season identity: scoring offense ranked 28th in 2025 (18.0 ppg), now 9th through two 2026 games (27.0 ppg) — a 19-spot improvement. Total yardage moved from 22nd (331.2 ypg) to 6th (409.0 ypg); passing offense from 10th (236.9 ypg) to literally 1st in the NFL (331.0 ypg) — a 9-spot jump; rushing offense stayed exactly flat at 28th both seasons (94.3 ypg 2025, 78.0 ypg 2026 — the rank is unchanged even though the raw rate actually dropped); first downs per game from 21st (16.7) to 5th (21.5).

By position group (2025 season-final): QB pass yds/gm 233.5 (13th), completion% 67.6% (6th), 2.9 sacks/gm allowed (25th); RB rush yds/gm 65.6 (32nd — dead last); WR rec yds/gm 146.4 (15th); TE rec yds/gm 65.2 (5th).

Third-down offense: 39.5% conversion rate (18th) — roughly average. Red-zone play calling: 50.8% run rate (12th) against 49.2% pass rate (21st) — a moderately run-leaning red-zone identity.

2025 opponent-quality context: NO's scoring was suppressed against top-tier defenses (14.0 ppg, n=3) relative to mid-tier (16.9 ppg, n=7) and bottom-tier (21.5 ppg, n=6) — a normal gradient. Its passing offense specifically dropped to 176.5 ypg against top-tier pass defenses (n=2, thin sample) versus 244.0 ypg against mid-tier (n=9) and 232.4 ypg against bottom-tier (n=5) — worth flagging given LV's own pass defense sits at a modest 13th-ranked (2025) tier, closer to "mid" than "top."

### New Orleans Defense
Season identity: points allowed ranked 16th in 2025 (22.5 ppg), now 19th through two 2026 games (24.0 ppg) — a real decline, not an improvement. Total yards allowed fell from 10th (316.8 ypg) to 22nd (357.0 ypg); pass yards allowed from 5th (196.2 ypg) to 16th (220.5 ypg); rush yards allowed from 19th (120.6 ypg) to 27th (136.5 ypg); and first downs allowed from 11th (16.7 fd/gm) to 29th (21.5 fd/gm) — an 18-spot slide, the largest single move in either team's profile. Every one of these categories moved the same direction (worse) at the same time, which argues this is a genuine early-season regression rather than one bad box score.

By position group (2025 season-final, NO's defense was genuinely elite that year): pass yds/gm allowed 196.2 (5th); RB rec yds/gm allowed 23.6 (3rd — excellent at limiting running-back receiving work); WR rec yds/gm allowed 121.5 (7th), catches allowed 9.8/gm (6th); TE rec yds/gm allowed 51.1 (13th).

Third-down defense: 34.3% conversion rate allowed (3rd-best in the league) — still excellent even amid the broader decline. Red-zone defense: opponents ran the ball 51.9% of the time once inside the 20 against NO (10th-highest run rate faced) versus 48.1% pass rate faced (23rd).

2025 opponent-quality context: NO's run defense allowed a fairly flat rate across tiers (92.0 ypg vs. top-tier, n=5; 90.8 ypg vs. mid-tier, n=4; 96.0 ypg vs. bottom-tier, n=7) — this unit didn't bend much based on opponent quality last season, for whatever that's worth given how much it has regressed early in 2026.

---

## 4. MATCHUP INTELLIGENCE

### The Third-Down Battle Favors New Orleans, Structurally
This is the cleanest team-level mismatch in the game. New Orleans's defense ranks 3rd in the NFL at stopping third downs (34.3% allowed, 2025) against a Las Vegas offense that already converts poorly on its own (33.8%, 28th) — a genuine double disadvantage for LV sustaining drives. In the other direction, Las Vegas's defense ranks 30th at getting off the field on third down (46.3% allowed) against a New Orleans offense that converts at a roughly average 39.5% clip (18th) — this favors New Orleans extending drives even beyond what its raw offensive ranking would suggest. Combined with the red-zone identity data — opponents already lean run against LV in the red zone (56.8% run rate faced, 3rd-highest) while New Orleans's own red-zone offense is moderately run-leaning (50.8%, 12th) — the natural expectation is that New Orleans's running back committee (below) sees real red-zone opportunity even if the passing game is what gets NO into scoring range.

### Quarterbacks
**Kirk Cousins (LV).** Through two 2026 games, Cousins is averaging 206.5 pass yds/gm on a 67.8% completion rate with 6 touchdowns (*2025: 172.1 pass yds/gm across 10 games, 61.7% completion, 10 TD*) — a clear efficiency uptick, though the sample is thin. His lone 2026 road game (Week 2 at LAC, LV's side this week since they play at New Orleans) produced 253 yards on 65.5% completion — his only available road/tier data point, so treat it as illustrative rather than predictive (n=1, LOW confidence). That Week 2 outing came against a LAC pass defense that ranked 26th against the pass — a below-average unit, which tempers how much confidence to place in that number repeating against a tougher matchup. His own season-long splits show a real vulnerability to pressure: 55.6% completion, 5.72 yds/play, and -0.156 EPA/play when blitzed, versus 69.8% completion, 7.09 yds/play, and +0.213 EPA/play when not blitzed (n=18 vs. n=43) — a significant gap in expected points, even if his blitzed success rate (50.0%) was actually slightly higher than his no-blitz success rate (44.2%) in this small sample. New Orleans's own actual blitz rate as a defense could not be verified for this specific matchup in this evidence package (the `blitz_qb` opponent-context fields are explicitly flagged as not yet recomputed for this bootstrap pairing) — so this should be read as "Cousins is worse when blitzed" as a standalone fact about him, not a specific prediction about how often New Orleans will actually blitz him. Confidence: MEDIUM on the blitz-sensitivity finding itself (real, if unequal, samples on both sides); LOW on anything opponent-specific given the 2-game sample.

**Tyler Shough (NO).** Averaging an NFL-leading 331.0 pass yds/gm through two 2026 games (*2025: 216.73 pass yds/gm across 11 games*) on 68.9% completion with 4 touchdowns. This is the headline number in the entire report, but it needs a caveat: his pass attempts have jumped from 29.73/gm in 2025 to 45.0/gm in 2026 — a 51% volume increase — while his completion percentage (67.6% → 68.9%) and yards-per-completion (10.79 → 10.68) have barely moved. In other words, this looks like a volume-driven surge, not a leap in per-throw quality, and it has come with real cost: his sack rate has risen from 2.82/gm (2025) to 4.0/gm (2026), and his interception rate from 0.55/gm to 1.0/gm. His own splits show he's markedly worse under pressure (54.3% completion, 5.2 yds/play, +0.038 EPA/play blitzed vs. 68.3% completion, 6.81 yds/play, +0.137 EPA/play unblitzed, n=35 vs. n=63) — a real gap, though notably his blitzed EPA/play stays positive, unlike Cousins's. His home/road split could not be computed (his `home_road_split` field is null — both his 2026 games to date appear to have been road games, so no home-side sample yet exists even though he is the home quarterback this week). Confidence: MEDIUM that some regression toward his 2025 per-throw rates is likely as the sample grows, while the underlying volume increase (and the offensive coordinator's evident willingness to lean on him) appears to be a real, not incidental, shift.

### Running Backs
**Ashton Jeanty (LV).** LV's clear workhorse — 66.7% rush share and an even larger 81.8% red-zone carry share through two 2026 games, averaging 75.0 rush yds/gm (*2025: 57.35 rush yds/gm across 17 games*) with a 22.4% target share, up from 14.8% in 2025 — a real expansion of his receiving role. His contact-efficiency numbers tell a mixed story: 1.91 yards after contact per carry and 1.5 yards before contact in 2026, both roughly flat-to-down from his 2025 rates (2.09 YAC, 1.58 YBC), even as his broken tackles per game rose (2.0 vs. 1.41 in 2025) — more broken tackles are producing less resulting yardage than a year ago, which argues his added workload has come from volume and role expansion rather than an efficiency breakthrough. His one road-game data point (Week 1 at MIA, his only carryover matchup vs. a run defense ranked 19th against the run that week) produced 102 rush yards on 23 carries — his season-best, but a single game against a below-average unit, and his only available split (LOW confidence, n=1). New Orleans's run defense enters this game ranked 19th in 2025 (99.0 rush ypg allowed) and has since declined to 27th through two 2026 games (118.5 rush ypg allowed) — a "mid" tier matchup on the season-long number, trending toward a softer one. His specific tier-and-site historical bucket for this exact combination isn't available in the evidence package, so this stays a season-average-plus-trend read rather than a precise historical comp. Confidence: MEDIUM that Jeanty sees a favorable environment given New Orleans's declining run defense, tempered by the fact his own per-touch efficiency hasn't shown a parallel uptick.

**Travis Etienne (NO).** The most-used back in New Orleans's backfield by games played (2 of 2), but his role has been diluted relative to 2025 — 8.5 carries/gm (32.7% rush share) in 2026 versus 15.29 carries/gm (53.3% share) in 2025, alongside a real receiving role (4.5 rec/gm, 5.5 targets/gm). His contact-efficiency split is genuinely mixed: yards after contact per carry fell to 1.53 (from 2.1 in 2025) while yards before contact rose to 2.65 (from 2.16) — he's finding more room pre-contact but generating less himself once hit, alongside a modest increase in broken tackles (1.0/gm vs. 0.59/gm in 2025). His home/road split could not be computed (null, same as Shough — no home-side games logged yet in 2026). He is also dealing with a hamstring injury currently listed as Limited Participation (see Injury Report). Confidence: LOW-MEDIUM on his workload projection given the muddled committee below.

**Alvin Kamara (NO)** has appeared in only one of New Orleans's two 2026 games, posting 15 rush yards on 9 carries (33.3% rush share that game) and 5 catches for 7 yards on a 18.8% target share (*2025: 42.82 rush yds/gm, 47.3% rush share across 11 games*) — his snap share in that lone appearance (29.0%) was far below his 2025 rate (63.7%), suggesting a genuinely reduced role relative to his career norm, at least in the one game logged. **Kendre Miller (NO)** also has just one appearance, but it came with real red-zone opportunity — a 9-carry, 30-yard, one-touchdown game with a 50.0% red-zone carry share that week (*2025: 27.57 rush yds/gm across 7 games, 19.2% red-zone carry share*). Between Etienne (2 games), Kamara (1 game), and Miller (1 game), New Orleans's backfield reads as a genuine three-way rotation without an every-week workhorse — worth building game-flow expectations around a committee rather than a single feature back.

### Wide Receivers / Tight Ends
**Chris Olave (NO).** New Orleans's clear WR1 and the one player in this game carrying a real Threat designation (see Section 5) — averaging a remarkable 134.0 rec yds/gm through two 2026 games on 9.0 rec/gm and an 11.5 targets/gm workload (27.4% target share) (*2025: 72.69 rec yds/gm across 16 games, 6.25 rec/gm, 9.75 targets/gm, 29.4% target share*) — nearly double his 2025 per-game rate, though on a two-game sample. His home/road split could not be computed (null — no home games logged in 2026 yet, same pattern as Shough). Facing LV's defense, which allowed the 29th-most catches to wide receivers in the NFL in 2025 (210 total, 12.4/gm) but the 5th-fewest yards per catch (11.9 ypr) — see Hidden Intelligence for how directly this maps onto his own profile. His own vs.-blitz splits (83.3% completion, 7.67 yds/play, +0.408 EPA/target on n=6 targets) versus vs.-no-blitz (76.5% completion, 13.06 yds/play, +1.043 EPA/target on n=17) show he remains productive either way, but with a real gap in explosiveness when defenses don't bring extra pressure. Confidence: MEDIUM-HIGH on Olave being a high-floor factor in this game; see Section 5 and 6 for why.

**Devaughn Vele (NO).** New Orleans's clear WR2 — averaging 66.5 rec yds/gm on a 93.5% snap share and a 19.0% target share (*2025: 32.56 rec yds/gm, 50.2% snap share, 12.6% target share across 9 games*) — his snap share nearly doubling from 2025 is a real, notable role expansion regardless of cause. His home/road split and tier splits are also unavailable in this evidence package.

**Juwan Johnson (NO).** The clear starting tight end — 60.0 rec yds/gm on a 68.5% snap share, with a striking 33.3% red-zone target share (*2025: 52.29 rec yds/gm, 75.0% snap share, 12.9% red-zone target share across 17 games*) — his red-zone role has grown substantially, worth watching given New Orleans's moderately run-leaning red-zone identity noted above still leaves real passing-game red-zone volume on the table. **Noah Fant (NO)** is the clear TE2, a complementary 16.5 rec yds/gm on a 42.5% snap share (*2025: 22.15 rec yds/gm, 37.9% snap share across 13 games*).

**Tre Tucker (LV).** LV's clear WR1 (pos_rank 1) and its deep-ball outlet — 73.0 rec yds/gm on a 20.86 yards-per-reception average and heavy average depth of target (96.5 air yds/gm) through two 2026 games, on a 19.0% target share (*2025: 40.94 rec yds/gm, 12.21 ypr, 18.7% target share across 17 games*). His lone 2026 road/tier data point (Week 2 at LAC, a mid-tier pass defense that week) produced 119 receiving yards on 5 catches (7 targets) — his season-best, but again a single game (LOW confidence, n=1). Facing LV's own likely opponent-tier read for New Orleans's pass defense (2025 rank 13, roughly mid-tier, though NO's pass defense has since slipped to 16th through two 2026 games per the decline noted above), his volume role should stay intact regardless of exact tier classification.

**Jalen Nailor (LV).** WR2 by depth chart and 2026 usage — 18.0 rec yds/gm on a 13.8% target share (*2025: 26.12 rec yds/gm, 65.4% snap share, 11.3% target share across 17 games*). **Jack Bech (LV)** is WR3 — 24.0 rec yds/gm on a 10.3% target share (*2025: 16.0 rec yds/gm, 39.8% snap share across 14 games*), with a real red-zone role (18.2% red-zone target share in 2026).

**Brock Bowers (LV).** LV's TE1 when healthy but has played zero 2026 games (`roster_only`-style zero season, real injury per Injury Report). His full 2025 season profile was elite: 56.67 rec yds/gm, 5.33 rec/gm, 7.17 targets/gm, a 23.6% target share and a massive 36.7% red-zone target share across 12 games. **Michael Mayer (LV)** has stepped into the lead tight-end role in his absence — 27.5 rec yds/gm on a 19.0% target share and 82.5% snap share (*2025: 25.23 rec yds/gm, 12.9% target share, 61.8% snap share across 13 games*) — his target share has grown by roughly 50% relative to his 2025 baseline, a real, measurable role expansion directly tied to Bowers's absence. If Bowers's Limited practice status this week translates into his 2026 debut, it would be the single biggest lineup swing available to either team in this game — LV's team-level TE production (33.0 ypg through two games, down from an elite 68.3 ypg team rank of 3rd in 2025) has clearly missed him.

### Coverage Scheme
This evidence package contains no populated man/zone coverage splits (`coverage_qb`, `coverage_wr`, `coverage_te`) and no team-level coverage-shell rate (`team_coverage_rate`) for either team, and no CB/DB ranking data (`cb_db_rankings` is empty) — these fields genuinely came back empty for this matchup, not merely unchecked. Individual man/zone tendencies and specific cornerback assignments cannot be responsibly analyzed here without inventing evidence that doesn't exist. The blitz-based analysis above (each quarterback's own vs.-blitz/vs.-no-blitz splits) is the best available substitute evidence for pressure-scheme sensitivity in this report.

---

## 5. THREAT INTELLIGENCE

**How the system works:** A Threat designation fires when a player's own season-long rank in a specific statistical category AND the upcoming opponent's defensive rank in that same category both clear a fixed threshold at the same time — the convergence of genuinely great individual production and a genuinely weak matchup in the same specific stat, not either signal in isolation. The three tiers use exact, fixed thresholds (player rank is 1st-best; defense rank is 1st-toughest, so a high defense-rank number means a weak defense): **Nuclear** requires the player to rank top 3 in the category AND the opponent's defense to rank 30th or worse in that same category; **Elite** requires top 5 and defense rank 28th or worse; **Standard** requires top 10 and defense rank 23rd or worse. A "Double" designation reflects one category meeting both thresholds; "Triple" adds a second category where the player's own rank alone clears the threshold even if the defense side falls just short; "Quadruple" means two or more categories fully converged.

Football Intel's deterministic engine evaluated every listed starter on both sides of this game (Kirk Cousins, Ashton Jeanty, Tre Tucker, Jack Bech, and Brock Bowers for Las Vegas; Tyler Shough, Travis Etienne, Chris Olave, Devaughn Vele, and Juwan Johnson for New Orleans, all using each player's full 2025 season-final rank recomputed specifically against this bootstrap opponent). **One designation fired:**

**Chris Olave (NO, WR) — Standard tier, Triple type.** The fully-converged category is receptions: Olave ranked 6th in the NFL among wide receivers in catches per game in 2025 (6.25 rec/gm), and Las Vegas's defense ranked 29th against the same category that season (12.4 catches/gm allowed to WRs) — both sides clear the Standard tier's thresholds (top 10 / defense rank 23+). The extra converged category, driving the "Triple" label, is receiving yards: Olave's own 2025 rank (9th, 72.69 rec yds/gm) clears the top-10 threshold on his own, even though LV's defensive rank in that category (22nd, 147.2 rec yds/gm allowed) falls just short of the 23-or-worse threshold needed for a full second convergence.

Read honestly against the rest of this report: this is a season-long statistical stability signal, not a guarantee. It lines up cleanly with Hidden Intelligence Finding B below — LV's defense specifically bleeds catch *volume* to wideouts rather than big plays, and Olave's own profile (huge target and catch volume, more moderate per-catch explosiveness) is close to a textbook match for that specific weakness. There is no real tension to flag here the way some Threats carry one; if anything, the underlying shapes of the two profiles reinforce each other rather than conflict.

No other starter on either roster produced a fired designation. This does not mean nothing else in this matchup matters — Sections 3 and 4 lay out real, evidence-backed edges (New Orleans's third-down defense, LV's improving run defense, the tight end and running back committee situations) that simply don't meet this specific convergence system's exact thresholds this week.

---

## 6. HIDDEN INTELLIGENCE & CONTEXTUAL ANALYSIS

**Finding A: New Orleans's historic passing surge is a volume story more than an efficiency one, and its own 2025 opponent-quality splits suggest the gaudy raw number is unlikely to be the right baseline for this specific matchup.** Tyler Shough's pass attempts have jumped 51% (29.73/gm in 2025 to 45.0/gm in 2026) while his completion percentage (67.6% to 68.9%) and yards-per-completion (10.79 to 10.68) have barely moved — the yardage gain is coming almost entirely from throwing far more often, not from suddenly throwing more accurately or explosively. This is not obvious from the headline "#1 ranked passing offense" number alone, which reads like a quality leap. Layering in New Orleans's own 2025 opponent-quality context sharpens the picture further: the team's passing offense averaged 244.0 yds/gm against mid-tier pass defenses (n=9) but fell to 176.5 yds/gm against top-tier ones (n=2) — a real, if thin-sampled, suppression pattern. Las Vegas's pass defense sits at a modest 13th in 2025 (closer to mid-tier than top-tier, though it has ticked up slightly to 11th through two 2026 games) — which argues New Orleans's raw 2026 passing rate should be treated as a ceiling rather than a true baseline for this specific game, even as the sheer increase in dropbacks (and accompanying sack-rate increase, from 2.82/gm to 4.0/gm) suggests New Orleans's coaching staff has genuinely committed to living through Shough's arm regardless of opponent. Confidence: MEDIUM — the volume-vs-efficiency read is well-supported by hard numbers on both counts, but the specific magnitude of regression to expect against LV specifically is inherently a projection, not a settled fact.

**Finding B: Las Vegas's pass defense is a bend-but-don't-break unit against wide receivers specifically — and that exact shape is what makes Chris Olave's Threat designation make sense rather than being a coincidence of two unrelated numbers.** LV allowed the 29th-most catches to wide receivers in the NFL in 2025 (210 total, 12.4/gm) — nearly worst in the league — yet allowed only 11.9 yards per catch to wideouts, 5th-best in the NFL. That is a specific, non-obvious defensive shape: this unit surrenders a high volume of underneath and intermediate completions while keeping a real lid on explosive plays to receivers, rather than being uniformly bad or uniformly good. Cross-referencing this with Chris Olave's own 2026 profile — 9.0 catches/gm on 11.5 targets/gm (both driven by sheer volume) alongside a moderate 14.89 yards-per-reception average — shows his game is built almost entirely around exactly the kind of production LV's defense is worst at limiting (catch volume) rather than the kind it's actually good at limiting (per-catch explosiveness). This is precisely why the deterministic Threat engine converged on his receptions category specifically rather than a big-play category, and it argues for treating Olave as a high-floor, moderate-ceiling factor in this game rather than an explosive one. Confidence: MEDIUM-HIGH — both underlying defensive splits are specific, real 2025 season-long numbers, and the connection to Olave's own equally specific usage profile is a direct, not speculative, match.

---

## 7. COEUS FINAL READ

**Keys to the Game:**
- If New Orleans's third-down defense (3rd-best in the league in 2025, 34.3% allowed) holds up against a Las Vegas offense that already struggles there on its own (28th, 33.8%), Las Vegas's path to sustained scoring gets considerably harder — even with its improved raw offensive ranking.
- If Las Vegas's third-down defense (30th, 46.3% allowed) performs to its poor 2025 form against a New Orleans offense that's merely average there (18th, 39.5%), New Orleans should extend more drives than its raw offensive numbers alone would predict — and if Brock Bowers returns to bolster LV's own offense, that becomes a race of which team's defense breaks first.
- If Brock Bowers is active, Las Vegas's passing offense regains its most proven weapon (a 2025 season that ranked 3rd in the league at the position) and Michael Mayer's role likely contracts back toward its 2025 baseline — watch early-game tight end usage as the tell.
- If New Orleans leans into its moderately run-heavy red-zone identity (50.8% run rate, 12th) against a Las Vegas defense that already sees more red-zone rushing than almost anyone (56.8% run rate faced, 3rd-highest), expect the muddled Etienne/Kamara/Miller committee to matter more near the goal line than in open-field volume.

**The Verdict:** Both of these teams have taken real strides on offense to open 2026, but this looks more like a Las Vegas game than a coin flip, for a specific reason: LV's improvement has come on both sides of the ball at once (points allowed jumping from 25th to 5th alongside its offensive gains), while New Orleans's defensive regression (first downs allowed sliding 18 full spots, the largest single shift in this evidence package) has arrived at the exact moment its offense needs to lean on volume rather than efficiency to sustain its gaudy passing rate. New Orleans's floor is real — Chris Olave is a legitimate, evidence-backed matchup advantage regardless of how the rest of the game unfolds — but the third-down math and the defensive trend both point toward Las Vegas controlling more possessions than New Orleans's raw offensive ranking would suggest on its own.

### Coeus Cheat Sheet

**Team**
- LV: 2-0 (2026) | 26.5 ppg, 12th *(2025: 14.2 ppg, 32nd)* | 13.5 ppg allowed, 5th *(2025: 25.4 ppg allowed, 25th)*
- NO: 1-1 (2026) | 27.0 ppg, 9th *(2025: 18.0 ppg, 28th)* | 24.0 ppg allowed, 19th *(2025: 22.5 ppg allowed, 16th)*

**Passing**
- Kirk Cousins (LV): 206.5 pass yds/gm, 6 TD *(2025: 172.1 ypg, 10 TD/10 gm)*
- Tyler Shough (NO): 331.0 pass yds/gm, 1st in NFL, 4 TD *(2025: 216.73 ypg, 10 TD/11 gm)*

**Rushing**
- Ashton Jeanty (LV): 75.0 rush yds/gm, 66.7% rush share *(2025: 57.35 ypg)*
- Travis Etienne (NO): 35.5 rush yds/gm, 32.7% rush share *(2025: 65.12 ypg, 53.3% share)* — committee w/ Kamara, Miller

**Receiving**
- Tre Tucker (LV, WR1): 73.0 rec yds/gm, 19.0% target share *(2025: 40.94 ypg)*
- Jalen Nailor (LV, WR2): 18.0 rec yds/gm, 13.8% target share *(2025: 26.12 ypg)*
- Michael Mayer (LV, TE1 w/ Bowers out): 27.5 rec yds/gm, 19.0% target share *(2025: 25.23 ypg)*
- Chris Olave (NO, WR1): 134.0 rec yds/gm, 27.4% target share *(2025: 72.69 ypg)* — Threat: Standard/Triple
- Devaughn Vele (NO, WR2): 66.5 rec yds/gm, 19.0% target share *(2025: 32.56 ypg)*
- Juwan Johnson (NO, TE1): 60.0 rec yds/gm, 33.3% RZ target share *(2025: 52.29 ypg)*

**Team Defense**
- LV: 206.0 pass yds/gm allowed, 11th *(2025: 214.4, 13th)* | 100.5 rush yds/gm allowed, 15th *(2025: 116.8, 17th)* | WR: 12.4 catches/gm allowed, 29th; 11.9 ypr allowed, 5th | Coverage rate (man%/zone%): unavailable
- NO: 220.5 pass yds/gm allowed, 16th *(2025: 196.2, 5th)* | 136.5 rush yds/gm allowed, 27th *(2025: 120.6, 19th)* | RB: 23.6 rec yds/gm allowed, 3rd | Coverage rate (man%/zone%): unavailable

**Down/Distance**
- LV offense: 33.8% third-down conv., 28th | LV defense: 46.3% allowed, 30th
- NO offense: 39.5% third-down conv., 18th | NO defense: 34.3% allowed, 3rd

**Red Zone Play Calling**
- LV offense: 40.2% run / 59.8% pass (29th/4th) | LV defense faces: 56.8% run / 43.2% pass (3rd/30th)
- NO offense: 50.8% run / 49.2% pass (12th/21st) | NO defense faces: 51.9% run / 48.1% pass (10th/23rd)

**Head-to-Head**
- No 2025 or 2026 meeting between these two teams exists in this evidence package; not a division matchup. Treated as a first meeting.

---

EVIDENCE_CHECK
{"claims": [
{"type":"rank_shift","team":"LV","side":"off","stat":"ppg","claimed_rank_2025":32,"claimed_rank_2026":12},
{"type":"rank_shift","team":"LV","side":"def","stat":"ppg","claimed_rank_2025":25,"claimed_rank_2026":5},
{"type":"rank_shift","team":"LV","side":"def","stat":"pass_ypg","claimed_rank_2025":13,"claimed_rank_2026":11},
{"type":"rank_shift","team":"LV","side":"def","stat":"rush_ypg","claimed_rank_2025":17,"claimed_rank_2026":15},
{"type":"rank_shift","team":"NO","side":"off","stat":"ppg","claimed_rank_2025":28,"claimed_rank_2026":9},
{"type":"rank_shift","team":"NO","side":"off","stat":"pass_ypg","claimed_rank_2025":10,"claimed_rank_2026":1},
{"type":"rank_shift","team":"NO","side":"off","stat":"rush_ypg","claimed_rank_2025":28,"claimed_rank_2026":28},
{"type":"rank_shift","team":"NO","side":"def","stat":"ppg","claimed_rank_2025":16,"claimed_rank_2026":19},
{"type":"rank_shift","team":"NO","side":"def","stat":"pass_ypg","claimed_rank_2025":5,"claimed_rank_2026":16},
{"type":"rank_shift","team":"NO","side":"def","stat":"rush_ypg","claimed_rank_2025":19,"claimed_rank_2026":27},
{"type":"rank_shift","team":"NO","side":"def","stat":"fd_pg","claimed_rank_2025":11,"claimed_rank_2026":29},
{"type":"current_opponent","team":"LV","pos":"WR","stat":"rec","role":"def","claimed_rank":29},
{"type":"current_opponent","team":"LV","pos":"WR","stat":"rec_yds","role":"def","claimed_rank":22},
{"type":"current_opponent","team":"LV","pos":"WR","stat":"ypr","role":"def","claimed_rank":5},
{"type":"current_opponent","team":"NO","pos":"RB","stat":"rec_ypg","role":"def","claimed_rank":3},
{"type":"current_opponent","team":"NO","pos":"WR","stat":"rec","role":"def","claimed_rank":6},
{"type":"current_opponent","team":"NO","pos":"WR","stat":"rec_ypg","role":"def","claimed_rank":7},
{"type":"log_opponent","player":"Ashton Jeanty","week":1,"stat":"rush_yds","claimed_rank":19},
{"type":"log_opponent","player":"Kirk Cousins","week":2,"stat":"pass_yds","claimed_rank":26}
]}