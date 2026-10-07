# GAME BREAKDOWN: Chicago Bears @ Green Bay Packers
### Week 5, 2026 Season | Scheduled 10/11/2026, 1:00 PM ET

**EVIDENCE PACKAGE NOTE:** This game has not been played. However, unlike a classic prior-season bootstrap, the team and player statistics below are genuine 2026 in-season data — both teams have played 4 real games this season (CHI 3-1, GB 2-2). The package is labeled "bootstrap" specifically because CHI and GB have not yet played each other in 2026, so the opponent-quality context embedded in the Threat Intelligence and matchup-pattern data (QB run-vs-pass, RB rush-vs-pass) had to be freshly recomputed for this exact pairing — those fields are explicitly flagged `opponent_context_recomputed_for_bootstrap: true` and are treated as current, legitimate evidence below. This is a real division game (`div_game: true`, NFC North) — the Division Game Rule is applied below, but no player in this evidence package has logged a 2026 meeting against this specific opponent (first meeting of the season), and no opponent-keyed multi-year history is available in the package. That absence is noted rather than skipped.

---

## 1. PREGAME BRIEFING

Chicago arrives at 3-1 having outscored opponents by better than 11 points a game, carrying the NFL's best rushing offense (196.2 rush yds/gm, 1st) and a defense that ranks top-5 in points allowed (16.2 ppg, 4th) and top-3 against the pass (194.0 pass yds/gm, 3rd). Green Bay is 2-2 with a profile that inverts the usual expectation for a modern offense: the Packers rank 8th in pass yards/gm (260.2) but dead last in rush yards/gm (58.0, 32nd) and 28th in total offense (318.2 ypg) — a passing-necessity offense rather than a passing-strength one, backed by a completion rate that ranks just 31st (56.5%). Green Bay's defense is a genuine split profile: 4th in pass yards allowed (200.5/gm) but 28th against the run (139.2/gm allowed).

On the broadest level, this looks like a collision between the league's most dominant rushing attack and one of its worst run defenses, while Green Bay's own offense — already thin on the ground — prepares to lean on the arm against a Chicago defense that's been one of the stingiest in the league through the air. That is the surface-level shape of this game; whether it plays out that cleanly depends on several swing factors worked through below, including a real complication at the Chicago quarterback position (see Section 2) and whether Green Bay's shutdown-caliber pass defense can keep the game from getting away from it early. Both teams' identities will be tested by the opposite number's one genuine strength — that tension, not a lopsided mismatch, is the real story to track.

No meeting between these two teams has occurred yet in 2026, and the evidence package contains no opponent-keyed prior-meeting data for any individual player against this specific opponent — despite this being a real division rivalry, there is no head-to-head sample to draw from this season.

---

## 2. INJURY & AVAILABILITY REPORT

**Source:** Real nflverse injury report (`status_policy: final_designation_or_limited_practice`). The evidence package confirms this report returned **zero** injury-relevant players for either CHI or GB for Week 5 — no player carries a report status, and no player shows a Limited or Did-Not-Participate practice designation. This is stated as a confirmed, clean result from the real injury file, not a data gap.

**However, a real and unresolved question exists at Chicago quarterback that the clean injury report does not explain.** Per the Current Starter Rule, Caleb Williams sits at pos_rank 1 on Chicago's depth chart (as of 2026-10-07, four days before kickoff) — but he has not appeared in a game since Week 2. Case Keenum started and played all offensive snaps in Week 3 (247 pass yds, 70.6% completion, 2 TD). Tyson Bagent then played a brief relief snap share in Week 2 (14%) before taking 100% of the Week 4 snaps himself (268 pass yds, 73.5% completion, 0 TD). The sequence — Williams, then Keenum, then Bagent, with no corresponding injury designation anywhere in the real injury file — is genuinely unusual, and no external, web-sourced confirmation was found or is available to this report beyond what the evidence package itself shows.

Given that, this report treats Caleb Williams as the more likely Week 5 starter **at LOW-MEDIUM confidence only**, consistent with the Standard's treatment of exactly this scenario: the depth chart is the more current signal, but the absence of any corroborating explanation (injury note, practice report) for why the healthy, pos_rank-1 quarterback hasn't played in two games is a real gap this report cannot resolve. All three Chicago quarterbacks are analyzed below (Section 4) so the breakdown holds regardless of who actually starts.

No Green Bay player carries any designation; Jordan Love has started and played every offensive snap in all 4 Green Bay games.

---

## 3. MATCHUP STATISTICS

### Chicago Offense
- **Team identity:** 28.0 ppg (9th), 440.2 total yds/gm (1st), 244.0 pass yds/gm (16th), 196.2 rush yds/gm (1st), 21.5 first downs/gm (4th).
- **QB group:** 244.0 pass yds/gm (16th), 68.2% completion (9th), 1.8 sacks/gm allowed (12th), 0.5 interceptions/gm (9th) — an efficient, low-mistake unit on raw numbers, complicated by the starter uncertainty above.
- **RB group:** 162.8 rush yds/gm (2nd), 33.2 carries/gm (1st — heaviest workload in the league), 6 total rushing touchdowns (3rd), plus 32.5 receiving yds/gm (13th) out of the backfield.
- **WR group:** 168.5 rec yds/gm (11th), 14.0 receptions/gm (6th) on real volume (18.5 targets/gm, 13th).
- **TE group:** 43.0 rec yds/gm (22nd) — a modest receiving role so far.
- **Down/Distance:** 47.4% third-down conversion rate (6th) on 14.2 attempts/gm.
- **Red Zone Play Calling (TENDENCY, not quality):** 57.5% run rate in the red zone (8th-highest in the league) vs. 42.5% pass (25th) — a clearly run-first identity once inside the 20.
- **Contextual Statistics:** Scoring output is dramatically opponent-dependent — just 3 points and 326 total yards in the only game against a true two-way elite defense (Week 2 at MIN), 59 points and 560 total yards against the weakest opponent faced (Week 1 CAR), and a 25.0-point, 437.5-yard average across the two mid-tier games in between. Rushing output, by contrast, stayed far more stable: 134 yards even in the MIN shutdown game (still logged as a "top"-tier run matchup) against a 217.0 yds/gm average in bottom-tier run-defense matchups (n=3).

### Chicago Defense
- **Team identity:** 16.2 ppg allowed (4th), 296.5 total yds/gm allowed (4th), 194.0 pass yds/gm allowed (3rd), 102.5 rush yds/gm allowed (13th), 13.0 first downs/gm allowed (2nd).
- **QB group faced:** 194.0 pass yds/gm allowed (3rd), opponents completing just 58.6% (4th), with a brutal 24.8 attempts/gm faced (1st-fewest) and 8.2 first downs/gm via pass allowed (2nd) — teams are not moving the ball through the air against this defense.
- **RB group faced:** 86.2 rush yds/gm allowed (12th) — a real, above-average run-stopping unit at the running back position specifically, tougher than the team-wide rush number (102.5, 13th) suggests on its own.
- **WR group faced:** 128.8 rec yds/gm allowed (9th).
- **TE group faced:** 34.8 rec yds/gm allowed (7th).
- **Down/Distance:** 23.7% third-down conversion allowed (2nd-best in the league) on 9.5 attempts faced/gm.
- **Red Zone Play Calling:** 52.2% run rate allowed (12th), 47.8% pass rate allowed (21st) — a modestly below-average rate of red-zone passing plays faced, not a glaring funnel either direction.

### Green Bay Offense
- **Team identity:** 18.2 ppg (28th), 318.2 total yds/gm (21st), 260.2 pass yds/gm (8th), 58.0 rush yds/gm (32nd — dead last in the league), 15.0 first downs/gm (27th).
- **QB group:** 260.2 pass yds/gm (8th) on real volume (38.5 attempts/gm, 6th) but just 56.5% completion (31st) and 8 total passing touchdowns (9th).
- **RB group:** 57.8 rush yds/gm (31st) on 16.2 carries/gm (32nd — fewest in the league).
- **WR group:** 174.0 rec yds/gm (10th) on massive volume (24.5 targets/gm, 2nd in the NFL).
- **TE group:** 65.5 rec yds/gm (10th).
- **Down/Distance:** 26.1% third-down conversion rate — **32nd, last in the league** — on 11.5 attempts/gm.
- **Red Zone Play Calling:** 43.2% run rate in the red zone (23rd) vs. 56.8% pass (10th-highest) — an offense that throws more than most teams even inside the 20, a direct consequence of having no real ground game.
- **Contextual Statistics:** Team-wide scoring splits show 22 points in the one true top-tier-opponent game (Week 1 at MIN) against a 17.0-point average across three mid-tier games (NYJ, ATL, TB). Rushing output stayed uniformly poor regardless of opponent quality — 56.3 yds/gm against top-tier run defenses (n=3) and 63.0 against the one bottom-tier run defense faced (n=1) — a sign this is a persistent personnel/scheme issue, not simply a tough-schedule artifact.

### Green Bay Defense
- **Team identity:** 26.2 ppg allowed (23rd), 339.8 total yds/gm allowed (14th), 200.5 pass yds/gm allowed (4th), 139.2 rush yds/gm allowed (28th), 18.0 first downs/gm allowed (20th).
- **QB group faced:** 200.5 pass yds/gm allowed (4th) — a legitimately elite pass defense on the surface.
- **RB group faced:** 113.8 rush yds/gm allowed — **29th**, a clear, specific weakness against running back production (distinct from, and worse than, the already-poor team-wide rush number of 139.2/gm, 28th).
- **WR group faced:** 139.0 rec yds/gm allowed (12th).
- **TE group faced:** 33.2 rec yds/gm allowed (6th) — Green Bay is genuinely tough on tight ends.
- **Down/Distance:** 48.2% third-down conversion allowed — **29th**, on 14.0 attempts faced/gm — a defense that gives up sustained drives at a near-bottom-of-the-league rate.
- **Red Zone Play Calling:** 63.6% run rate allowed (3rd-highest in the league — teams run against this defense in the red zone more than almost anyone else), 36.4% pass rate allowed (30th).

---

## 4. MATCHUP INTELLIGENCE

### The Central Tension: CHI's Run Game vs. GB's Run Defense

The single clearest positional mismatch in this game is Chicago's rushing attack (196.2 yds/gm, 1st in the NFL) against a Green Bay run defense that ranks 28th overall (139.2 yds/gm allowed) and, more precisely, 29th specifically against running back production (113.8 yds/gm allowed to RBs). Green Bay's defense is not uniformly bad — its pass defense (200.5 yds/gm allowed, 4th) is one of the better units in football — but the run-defense gap is real, specific, and lines up directly against the one thing Chicago does better than anyone in the league. Compounding this, Chicago's own offense already shows a run-heavy red-zone identity (57.5% run rate inside the 20, 8th-highest), and teams already run against Green Bay in the red zone at the 3rd-highest rate in the league (63.6% allowed) — two tendencies that point the same direction.

### Quarterbacks

**Jordan Love (GB).** Entrenched starter, 4 games, 100% snap share every week. Season averages: 260.2 pass yds/gm (8th in the league), 56.5% completion (31st), 8 total passing touchdowns. His own opponent-quality splits show real variance: 243.0 pass yds/gm across his three games against top-tier pass defenses (n=3) against a 312.0-yard outlier in his one game against a bottom-tier pass defense (Week 3 at ATL, which ranked 29th against the pass that week — *log_opponent claim*). Chicago's pass defense (194.0 yds/gm allowed, 3rd) sits at the tougher end of what Love has seen, closer to his suppressed range than his ceiling. His own splits against pressure are a real concern: 50.0% completion and -0.222 EPA/play against the blitz, compared to 56.2% completion and +0.2 EPA/play when unblitzed (season blitz rate faced: 40.7%) — a meaningful gap, though Chicago's actual blitz rate specifically against Green Bay this week is not available in the evidence package (the opponent-blitz fields are explicitly flagged as not yet recomputed for this pairing), so this is cited as a standing vulnerability rather than a confirmed plan. Confidence: MEDIUM.

**Caleb Williams (CHI).** Only 2 games played this season (<3 games — 2025 Season Context Rule applies): 203.5 pass yds/gm, 65.45% completion, 2 total touchdowns, 0.5 sacks/gm faced, 0.5 interceptions/gm *(2025: 231.88 pass ypg, 58.1% completion, 1.59 pass TD/gm, 1.41 sacks/gm, 0.41 int/gm)*. His one 2026 road game (Week 1 at CAR, a mid-tier pass defense that game, ranked 20th — *log_opponent claim*) produced 269 yards on 72.4% completion. In his one game against a genuinely tough pass defense this season (Week 2 vs. MIN, ranked 10th that week — *log_opponent claim*), he was held to 138 yards on 57.7% completion. Green Bay's pass defense (4th) profiles as a tougher test than either sample fully captures. Confidence: LOW given the 2-game sample and the starter uncertainty itself.

**Case Keenum (CHI).** 1 start (Week 3 vs. PHI, mid-tier matchup): 247 yards, 70.6% completion, 2 TD — a clean spot start. No 2025 season recorded in the evidence package (under 3 games and no `season_2025` value) — stated plainly rather than substituting career numbers. His extensive career track record (77 games through 2025, 200.29 pass ypg, 62.46% career completion) reflects a journeyman who can manage an offense competently in a spot start.

**Tyson Bagent (CHI).** 2 appearances (<3 games): one brief relief snap share in Week 2 (14%, 54 yards) and a full Week 4 start (100% snaps, 268 yards, 73.5% completion, 0 touchdowns) *(2025: 23.5 pass ypg across 2 games, 75.0% completion — a tiny, low-leverage 2025 sample)*. Whoever starts, Chicago's passing operation behind this trio carries real week-to-week uncertainty that the clean injury report does not resolve.

### Running Backs

**D'Andre Swift (CHI).** Clear early-season lead back by role: 57.2% season snap share, 43.4% rush share, 77.75 rush yds/gm, plus a real receiving role (21.0 rec yds/gm, 9.1% target share). **Carries a Threat designation — see Section 5.** Contact efficiency: 2.09 yards after contact per carry, 2.42 yards before contact per carry, 1.0 broken tackle/gm (season). His one 2026 road game (Week 1 vs. CAR, a bottom-tier run defense) produced 124 rush yards on an outsized day (18 carries, 3 TD) — and that bottom-tier/road combination is the exact matchup type Green Bay represents this week (29th against RBs specifically), making that 124-yard sample directly relevant despite its small size (n=1). Confidence: MEDIUM.

**Kyle Monangai (CHI).** The clear complementary piece earlier in the season (37.7% rush share, 81.0 rush yds/gm) — but the committee balance shifted hard in Week 4: Monangai outcarried Swift 30-to-15 and out-rushed him 146-to-58 yards, with superior contact numbers on the season to match (2.55 yards after contact, 2.85 before contact, 0.5 broken tackles/gm). His one road game (Week 1 vs. CAR, bottom tier) produced 100 yards on just 10 carries (10.0 ypc). Whether Week 4's shift toward Monangai holds or reverts is a real, recent-usage question worth monitoring — both backs get real red-zone work (Swift 45.2% red-zone carry share season, Monangai 33.3%).

**Green Bay's backfield has no clear lead back.** MarShawn Lloyd (depth chart RB1) carries a 41.1% rush share but modest output (20.25 rush yds/gm, 1.2 yards after contact, 1.5 before contact — both poor churn numbers) alongside a real receiving role (12.25 rec yds/gm). Kaleb Johnson (27.4% rush share, 20.0 rush yds/gm) and Chris Brooks (20.5% rush share, 17.5 rush yds/gm, more of a receiving specialist historically) round out a genuine three-man committee with no standout. Against Chicago's run defense — which, while only 13th team-wide, ranks a real 12th specifically against running back production (86.2 yds/gm allowed) — an already-struggling committee faces a defense built to make things harder, not easier.

### Wide Receivers / Tight Ends

**Rome Odunze (CHI, depth chart WR1).** 58.25 rec yds/gm, 16.5% target share, but a big-play rather than high-volume profile (16.64 yards per reception, only 3.5 rec/gm on 5.0 targets/gm). His best game of the season came against the toughest individual matchup he's faced — 94 yards in Week 4 against NYJ, logged as a "top"-tier matchup that week (8th-ranked WR defense — *log_opponent claim*) — a genuine counter-indicator worth flagging (LOW confidence given the single data point) against the general expectation that tough coverage suppresses him.

**Luther Burden III (CHI, depth chart WR2).** Despite ranking below Odunze on the depth chart, Burden is Chicago's actual **volume leader** — 24.0% target share (team-high), 7.25 targets/gm, 54.75 rec yds/gm. This is a real target-share/depth-chart-rank mismatch worth knowing: Burden, not Odunze, is the receiver seeing the ball most often.

**Kalif Raymond (CHI, depth chart WR3).** 55.0 rec yds/gm, 19.0% target share — a sizable Week 1 outlier (84 yards on 9 targets against CAR) pulls his season average up; he's been quieter since.

Both face a Green Bay secondary allowing 139.0 rec yds/gm to wide receivers (12th) — a moderately tough, upper-middle matchup, not a soft one.

**Christian Watson (GB, depth chart WR1).** The clear top weapon — 82.75 rec yds/gm, 21.3% target share, 4 touchdowns, and a big-play profile (16.55 yards per reception). Heavy red-zone usage (28.0% red-zone target share, 3 TDs on just 7 red-zone targets). His one 2026 home game (Week 3 vs. ATL, a bottom-tier matchup that week, 29th — *log_opponent claim*) produced his best output, 96 yards on 7 catches; his one top-tier matchup game (Week 4 vs. TB, ranked 2nd — *log_opponent claim*) limited him to 47 yards. Chicago's defense (128.8 rec yds/gm allowed to WRs, 9th) sits closer to that suppressed end. No tier-matched home sample exists against a top-tier pass defense specifically — stated plainly rather than estimated. Confidence: MEDIUM.

**Matthew Golden (GB, depth chart WR2, rookie).** Actually leads Green Bay in target share at 24.7% (9.25 targets/gm, highest raw volume on the team) with 68.5 rec yds/gm. His one home sample (Week 3 vs. ATL, bottom tier — *log_opponent claim*, 100 yards) is his best game; his one top-tier matchup (Week 4 vs. TB, rank 2 — *log_opponent claim*) limited him to 21 yards. Golden's own splits show a specific, significant blitz vulnerability — see Section 6.

**Colston Loveland (CHI, rookie TE, depth chart TE1).** Already ahead of established veteran Cole Kmet in role (86.0% snap share vs. Kmet's 64.8%) despite modest box-score output so far (22.75 rec yds/gm, 14.9% target share, 19.4% red-zone target share). Faces a Green Bay unit that is genuinely tough on tight ends — 33.2 rec yds/gm allowed, 6th-best in the league.

**Tucker Kraft (GB, depth chart TE1).** 37.0 rec yds/gm, 16.0% target share, 83.0% snap share — a real red-zone weapon (16.0% red-zone target share). Faces a Chicago defense that is similarly stingy to tight ends (34.8 rec yds/gm allowed, 7th).

---

## 5. THREAT INTELLIGENCE

Football Intel's deterministic Threat Engine flags a designation only when a player's own **season** rank in a specific statistical category and the upcoming opponent's defensive rank in that **same** category both clear a tier's exact threshold — the convergence of individually elite production and a specifically weak matchup, not either signal alone. The three tiers use these exact thresholds (player rank is 1st-best; defense rank is 1st-toughest, so a high defense-rank number means a weak unit):

- **Nuclear** — player ranks top 3 in the category AND the opponent's defense ranks 30th or worse in that category
- **Elite** — player ranks top 5 AND opponent defense ranks 28th or worse
- **Standard** — player ranks top 10 AND opponent defense ranks 23rd or worse

"Double," "Triple," and "Quadruple" describe how many categories converged — Double is one category meeting both thresholds; higher tiers stack additional categories where at least the player's own rank clears, even if the defense side doesn't fully converge.

The Engine evaluated five starters on each side for this matchup: Caleb Williams, D'Andre Swift, Rome Odunze, Kalif Raymond, and Colston Loveland for Chicago; Jordan Love, Chris Brooks, Matthew Golden, Christian Watson, and Tucker Kraft for Green Bay. (Notably, Luther Burden III — Chicago's actual target-share leader — was not among the evaluated starters despite his role; this report notes that factually rather than speculating on the Engine's roster selection.)

**One designation fired: D'Andre Swift (CHI RB) — Standard tier, Double type, category converged: rush_yds.**

Swift's own season rush-yardage rank sits at 8th in the league (77.8 yds/gm) — inside the top-10 Standard threshold. Green Bay's defense ranks 29th specifically against running back rushing production (113.8 yds/gm allowed) — well past the 23rd-or-worse threshold required. Both conditions converge on the same category, producing the Standard/Double designation.

This lines up directly with the broader matchup read in Section 4: Chicago's run game is its most stable, least opponent-sensitive unit (134 yards even in its one true shutdown game against MIN), and Green Bay's run defense is its one clear statistical soft spot. The real tension worth naming honestly: Swift has not been a clean workhorse this season — Kyle Monangai outproduced him significantly in the most recent game (146 to 58 rush yards, Week 4), and the touches could again be shared rather than concentrated on Swift alone. A Threat designation reflects Swift's own season-long statistical profile converging with Green Bay's season-long weakness — it does not guarantee he, rather than Monangai, is the one who cashes in on a given week. Confidence on the underlying matchup edge: MEDIUM-HIGH; confidence on it specifically manifesting through Swift's own box score rather than a split touch distribution: MEDIUM.

No other Threat fired for either team. This should be read plainly: it does not mean no other real edges exist in this matchup (Section 4 documents several, including Green Bay's own run-game and third-down deficiencies) — only that no other player/category combination cleared this specific convergence system's thresholds this week.

---

## 6. HIDDEN INTELLIGENCE & CONTEXTUAL ANALYSIS

**Finding 1: The one defense that actually slowed Chicago down this season did it with a two-way shutdown, not a one-dimensional strength — and Green Bay's defense is built the opposite way.** Chicago's offense has shown extreme opponent-quality sensitivity in scoring: 3 points and 326 total yards in its only game against a genuinely elite, well-rounded defense (Week 2 at MIN, a unit that ranked top-tier against both the pass and the run that week), against a 25.0-point, 437.5-yard average in its two mid-tier games and a 59-point outburst against the league's weakest opponent faced. The detail that makes this non-obvious: even in that MIN shutdown, Chicago's *rushing* output barely moved (134 yards, still logged as a "top"-tier run matchup that week) — it was specifically the passing game that collapsed (138 yards, well below Chicago's own average). Green Bay's defense is not built like MIN's. It is legitimately elite against the pass (200.5 yds/gm allowed, 4th) but one of the league's worst against the run, specifically against running backs (113.8 yds/gm allowed, 29th). In other words, Green Bay presents Chicago with exactly the one dimension (the run) that has never actually been taken away from it this season, while the dimension Green Bay *can* take away (the pass) is the one Chicago is least dependent on given its run-first offensive identity (196.2 rush yds/gm, 1st; 57.5% red-zone run rate, 8th-highest). Confidence: MEDIUM.

**Finding 2: Jordan Love's passing efficiency appears to move together with Green Bay's rushing success, not inversely to it — a real risk given how bad that rushing has been.** Love's own hit-rate data shows he exceeds his own passing baseline in 66.7% of games where Green Bay's run game also exceeds its own baseline, versus only 40.0% of games when the run game is cold — a "connected offense" pattern (a good rushing day correlates with a good Love day) rather than the more intuitive "he has to carry the offense when the run game fails" pattern. This matters directly here because Green Bay's run game has been uniformly poor regardless of opponent quality this season — 56.3 yds/gm against top-tier run defenses and 63.0 against the one bottom-tier run defense faced (team-level splits, n=3 and n=1 respectively) — a sign this is a standing unit problem, not a schedule artifact. If that persists against Chicago (a 13th-ranked, 12th-ranked-vs.-RBs run defense — a middling-to-tough matchup, not a soft one), Love's own data suggests his passing numbers are more likely to track toward the suppressed end of his range than to compensate for the run game's absence. Confidence: MEDIUM-LOW given sample size, but directionally consistent with the independently poor rushing splits above.

**Finding 3: Green Bay's most heavily used passing weapon has a specific, well-documented blitz problem that compounds Jordan Love's own blitz struggles — a real, if conditional, risk.** Love's own season splits show meaningfully worse play when blitzed (-0.222 EPA/play, 37.9% success rate, 50.0% completion) than when he isn't (+0.2 EPA/play, 42.7% success, 56.2% completion). Layered on top of that: Matthew Golden — who leads Green Bay in target share at 24.7% and sees the most raw volume on the team (9.25 targets/gm) — shows an even more dramatic swing specifically on blitz snaps (-0.826 EPA/target, 23.1% success rate, 38.5% completion) versus non-blitz snaps (+0.657 EPA/target, 54.2% success, 54.2% completion). This is not a complementary piece being affected; it is the team's single most-targeted receiver. The caveat that keeps this conditional rather than certain: Chicago's actual blitz rate specifically against Green Bay this week is not available in the evidence package — the opponent-blitz fields here are explicitly flagged as not yet recomputed for this specific pairing, so this finding describes a real vulnerability that would be exploitable *if* Chicago brings extra pressure, not a confirmed plan. Confidence: MEDIUM, conditional on blitz usage that cannot be confirmed from this evidence package.

A note on scope: no individual CB/DB coverage-ranking data and no man/zone coverage splits (player-level or team-level play-calling rate) are available in the evidence package for this specific matchup — those fields returned empty. This analysis is built entirely from the statistical, role, and situational evidence above, without individual coverage-assignment detail this week.

---

## 7. COEUS FINAL READ

**Keys to the Game:**

*If Chicago's run game gets the volume its profile suggests it should against Green Bay's run defense* (29th specifically against running backs), expect Chicago to control time of possession and set up manageable third downs — a real advantage given Chicago already converts at a 47.4% clip (6th) against a Green Bay defense that allows conversions at a near-bottom-of-the-league 48.2% rate (29th).

*If Green Bay's run game stays as unproductive as it's been all season* (58.0 yds/gm, 32nd, with no tier of opponent producing real relief), Jordan Love's own correlation data says his passing is more likely to track down than to compensate — a genuine risk for an offense that already ranks 32nd on third down (26.1%).

*If Chicago's quarterback situation resolves cleanly* (Williams returns and performs at his career baseline rather than his thin 2026 sample), Chicago's offense adds a dimension beyond the run that Green Bay's genuinely good pass defense (4th) would have to account for. If it doesn't resolve cleanly, Chicago likely leans on the run even more than its already run-first identity suggests — not obviously a bad outcome given Green Bay's specific weakness there.

**The Verdict:** This matchup resolves around one real, well-supported mismatch — Chicago's No. 1 rushing offense against a Green Bay run defense that is specifically poor against running backs (29th) — layered on top of a Green Bay offense that has shown no real path to balance all season (32nd rushing, 32nd on third down) and would need its passing attack to both stay efficient and overcome a legitimately difficult Chicago pass defense (3rd) to keep pace. Chicago's own passing situation carries real uncertainty given the quarterback question, but its floor — a dominant, matchup-proof run game against the league's 29th-ranked unit at that specific point of attack — gives it the sturdier foundation in a game where either team's passing game could underperform its raw season numbers. Confidence: MEDIUM, reflecting both the real strength of the central run-game mismatch and the genuine, unresolved uncertainty at Chicago quarterback and in how Green Bay's committee backfield distributes touches on the other side.

---

### COEUS CHEAT SHEET

**Team**
- CHI: 3-1 | 28.0 ppg (9th) / 16.2 ppg allowed (4th)
- GB: 2-2 | 18.2 ppg (28th) / 26.2 ppg allowed (23rd)

**Passing**
- Caleb Williams (CHI, starter uncertain — LOW-MEDIUM confidence): 203.5 pass ypg *(2025: 231.88 ypg)* — vs. GB pass D: 200.5 ypg allowed (4th)
- Jordan Love (GB): 260.2 pass ypg (8th) — vs. CHI pass D: 194.0 ypg allowed (3rd)

**Rushing**
- D'Andre Swift (CHI, RB1): 77.75 rush ypg (Threat: Standard/Double, rush_yds) — vs. GB run D (RB-specific): 113.8 ypg allowed (29th)
- MarShawn Lloyd (GB, RB1): 20.25 rush ypg — vs. CHI run D (RB-specific): 86.2 ypg allowed (12th)

**Receiving**
- Rome Odunze (CHI, WR1): 58.25 rec ypg — vs. GB WR D: 139.0 ypg allowed (12th)
- Luther Burden III (CHI, WR2/volume leader, 24.0% tgt share): 54.75 rec ypg — vs. GB WR D: 139.0 ypg allowed (12th)
- Colston Loveland (CHI, TE1): 22.75 rec ypg — vs. GB TE D: 33.2 ypg allowed (6th)
- Christian Watson (GB, WR1): 82.75 rec ypg — vs. CHI WR D: 128.8 ypg allowed (9th)
- Matthew Golden (GB, WR2/volume leader, 24.7% tgt share): 68.5 rec ypg — vs. CHI WR D: 128.8 ypg allowed (9th)
- Tucker Kraft (GB, TE1): 37.0 rec ypg — vs. CHI TE D: 34.8 ypg allowed (7th)

**Team Defense**
- CHI: pass 194.0 ypg allowed (3rd) | rush 102.5 ypg allowed (13th) | WR rec 128.8 ypg allowed (9th) | TE rec 34.8 ypg allowed (7th) | coverage rate (man%/zone%): not available this week
- GB: pass 200.5 ypg allowed (4th) | rush 139.2 ypg allowed (28th) | WR rec 139.0 ypg allowed (12th) | TE rec 33.2 ypg allowed (6th) | coverage rate (man%/zone%): not available this week

**Down/Distance**
- CHI: 47.4% third-down conversion (6th, off) / 23.7% allowed (2nd, def)
- GB: 26.1% third-down conversion (32nd, off) / 48.2% allowed (29th, def)

**Red Zone Play Calling**
- CHI: 57.5% run / 42.5% pass (off, run rank 8th) | 52.2% run / 47.8% pass allowed (def)
- GB: 43.2% run / 56.8% pass (off, pass rank 10th) | 63.6% run / 36.4% pass allowed (def, run-allowed rank 3rd)

**Head-to-Head**
- No meeting yet in 2026 — first matchup of the season between these division rivals; no prior-meeting data available.

---

EVIDENCE_CHECK
{"claims": [
{"type":"current_opponent","team":"CHI","pos":"TEAM","stat":"ppg","role":"off","claimed_rank":9},
{"type":"current_opponent","team":"CHI","pos":"TEAM","stat":"total_ypg","role":"off","claimed_rank":1},
{"type":"current_opponent","team":"CHI","pos":"TEAM","stat":"pass_ypg","role":"off","claimed_rank":16},
{"type":"current_opponent","team":"CHI","pos":"TEAM","stat":"rush_ypg","role":"off","claimed_rank":1},
{"type":"current_opponent","team":"CHI","pos":"TEAM","stat":"fd_pg","role":"off","claimed_rank":4},
{"type":"current_opponent","team":"CHI","pos":"TEAM","stat":"ppg","role":"def","claimed_rank":4},
{"type":"current_opponent","team":"CHI","pos":"TEAM","stat":"total_ypg","role":"def","claimed_rank":4},
{"type":"current_opponent","team":"CHI","pos":"TEAM","stat":"pass_ypg","role":"def","claimed_rank":3},
{"type":"current_opponent","team":"CHI","pos":"TEAM","stat":"rush_ypg","role":"def","claimed_rank":13},
{"type":"current_opponent","team":"CHI","pos":"TEAM","stat":"fd_pg","role":"def","claimed_rank":2},
{"type":"current_opponent","team":"GB","pos":"TEAM","stat":"ppg","role":"off","claimed_rank":28},
{"type":"current_opponent","team":"GB","pos":"TEAM","stat":"total_ypg","role":"off","claimed_rank":21},
{"type":"current_opponent","team":"GB","pos":"TEAM","stat":"pass_ypg","role":"off","claimed_rank":8},
{"type":"current_opponent","team":"GB","pos":"TEAM","stat":"rush_ypg","role":"off","claimed_rank":32},
{"type":"current_opponent","team":"GB","pos":"TEAM","stat":"fd_pg","role":"off","claimed_rank":27},
{"type":"current_opponent","team":"GB","pos":"TEAM","stat":"ppg","role":"def","claimed_rank":23},
{"type":"current_opponent","team":"GB","pos":"TEAM","stat":"total_ypg","role":"def","claimed_rank":14},
{"type":"current_opponent","team":"GB","pos":"TEAM","stat":"pass_ypg","role":"def","claimed_rank":4},
{"type":"current_opponent","team":"GB","pos":"TEAM","stat":"rush_ypg","role":"def","claimed_rank":28},
{"type":"current_opponent","team":"GB","pos":"TEAM","stat":"fd_pg","role":"def","claimed_rank":20},
{"type":"current_opponent","team":"CHI","pos":"QB","stat":"comp_pct","role":"off","claimed_rank":9},
{"type":"current_opponent","team":"CHI","pos":"QB","stat":"sacks_pg","role":"off","claimed_rank":12},
{"type":"current_opponent","team":"CHI","pos":"QB","stat":"int_pg","role":"off","claimed_rank":9},
{"type":"current_opponent","team":"CHI","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":2},
{"type":"current_opponent","team":"CHI","pos":"RB","stat":"car_pg","role":"off","claimed_rank":1},
{"type":"current_opponent","team":"CHI","pos":"RB","stat":"rush_td","role":"off","claimed_rank":3},
{"type":"current_opponent","team":"CHI","pos":"RB","stat":"rec_ypg","role":"off","claimed_rank":13},
{"type":"current_opponent","team":"CHI","pos":"WR","stat":"rec_ypg","role":"off","claimed_rank":11},
{"type":"current_opponent","team":"CHI","pos":"WR","stat":"rec_pg","role":"off","claimed_rank":6},
{"type":"current_opponent","team":"CHI","pos":"TE","stat":"rec_ypg","role":"off","claimed_rank":22},
{"type":"current_opponent","team":"CHI","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":12},
{"type":"current_opponent","team":"CHI","pos":"WR","stat":"rec_ypg","role":"def","claimed_rank":9},
{"type":"current_opponent","team":"CHI","pos":"TE","stat":"rec_ypg","role":"def","claimed_rank":7},
{"type":"current_opponent","team":"GB","pos":"QB","stat":"comp_pct","role":"off","claimed_rank":31},
{"type":"current_opponent","team":"GB","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":31},
{"type":"current_opponent","team":"GB","pos":"RB","stat":"car_pg","role":"off","claimed_rank":32},
{"type":"current_opponent","team":"GB","pos":"WR","stat":"rec_ypg","role":"off","claimed_rank":10},
{"type":"current_opponent","team":"GB","pos":"WR","stat":"tgt_pg","role":"off","claimed_rank":2},
{"type":"current_opponent","team":"GB","pos":"TE","stat":"rec_ypg","role":"off","claimed_rank":10},
{"type":"current_opponent","team":"GB","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":29},
{"type":"current_opponent","team":"GB","pos":"WR","stat":"rec_ypg","role":"def","claimed_rank":12},
{"type":"current_opponent","team":"GB","pos":"TE","stat":"rec_ypg","role":"def","claimed_rank":6},
{"type":"current_opponent","team":"CHI","pos":"TEAM","stat":"third_down_conversion_pct","role":"off","claimed_rank":6},
{"type":"current_opponent","team":"CHI","pos":"TEAM","stat":"third_down_pct_allowed","role":"def","claimed_rank":2},
{"type":"current_opponent","team":"GB","pos":"TEAM","stat":"third_down_conversion_pct","role":"off","claimed_rank":32},
{"type":"current_opponent","team":"GB","pos":"TEAM","stat":"third_down_pct_allowed","role":"def","claimed_rank":29},
{"type":"current_opponent","team":"CHI","pos":"TEAM","stat":"red_zone_run_pct","role":"off","claimed_rank":8},
{"type":"current_opponent","team":"CHI","pos":"TEAM","stat":"red_zone_pass_pct","role":"off","claimed_rank":25},
{"type":"current_opponent","team":"CHI","pos":"TEAM","stat":"red_zone_run_pct_allowed","role":"def","claimed_rank":12},
{"type":"current_opponent","team":"CHI","pos":"TEAM","stat":"red_zone_pass_pct_allowed","role":"def","claimed_rank":21},
{"type":"current_opponent","team":"GB","pos":"TEAM","stat":"red_zone_run_pct","role":"off","claimed_rank":23},
{"type":"current_opponent","team":"GB","pos":"TEAM","stat":"red_zone_pass_pct","role":"off","claimed_rank":10},
{"type":"current_opponent","team":"GB","pos":"TEAM","stat":"red_zone_run_pct_allowed","role":"def","claimed_rank":3},
{"type":"current_opponent","team":"GB","pos":"TEAM","stat":"red_zone_pass_pct_allowed","role":"def","claimed_rank":30},
{"type":"log_opponent","player":"Jordan Love","week":1,"stat":"pass_yds","claimed_rank":10},
{"type":"log_opponent","player":"Jordan Love","week":3,"stat":"pass_yds","claimed_rank":29},
{"type":"log_opponent","player":"Christian Watson","week":3,"stat":"rec_yds","claimed_rank":29},
{"type":"log_opponent","player":"Christian Watson","week":4,"stat":"rec_yds","claimed_rank":2},
{"type":"log_opponent","player":"Matthew Golden","week":4,"stat":"rec_yds","claimed_rank":2},
{"type":"log_opponent","player":"Rome Odunze","week":4,"stat":"rec_yds","claimed_rank":8},
{"type":"log_opponent","player":"D'Andre Swift","week":2,"stat":"rush_yds","claimed_rank":8},
{"type":"log_opponent","player":"Caleb Williams","week":2,"stat":"pass_yds","claimed_rank":10}
]}