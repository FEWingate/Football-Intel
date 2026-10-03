# GAME BREAKDOWN: Detroit Lions @ Carolina Panthers
### Week 4, 2026 Season | Scheduled 10/04/2026, 8:20 PM ET

**EVIDENCE NOTICE:** This game has not been played (game.played: false), and these two teams have not met yet in 2026 — this will be their first meeting of the season, and it is not a division game. However, unlike a true "bootstrap" preview built on stale prior-season data, both teams carry real, current 2026 in-season evidence: Detroit is 2-1 and Carolina is 1-2, each with three real 2026 games logged. The evidence package flags that opponent-quality context for several fields (Threat Intelligence, QB/RB run-vs-pass splits) has already been specifically recomputed for this exact DET-CAR pairing ("opponent_context_recomputed_for_bootstrap": true) — those numbers are safe to use as written. By contrast, the blitz-rate fields explicitly warn that the opponent blitz-rate/rank figures are still tagged to each team's most recent real opponent, not Carolina or Detroit specifically, and the evidence package says plainly not to use those particular fields for this matchup — only the player's own, opponent-independent blitz-split numbers are reliable there, and that's all this report uses. Coverage man/zone splits, each defense's own coverage-rate tendency, CB/DB rankings, and 2025-vs-2026 rank shifts are all empty in this evidence package and are treated as unavailable throughout, not approximated.

---

## 1. PREGAME BRIEFING

Detroit arrives at 2-1 having split its first three weeks in wild fashion: a 31-30 home win over New Orleans, a 31-41 shootout loss at Buffalo, and a 31-24 home win over the Jets — three straight games of 31+ points scored, none of them particularly tight on the scoreboard either way. Carolina is 1-2, having lost a track meet to Chicago at home (37-59), blown out Atlanta on the road (34-3), and dropped a close one at Cleveland (18-21). Both offenses have been functional; both defenses have been a serious problem in specific, identifiable ways.

This is a case where the surface numbers for both teams tell a genuinely unusual story. Detroit's offense ranks 3rd in the NFL in scoring (31.0 points per game) and Carolina's ranks 5th (29.7 ppg) and 1st in passing yardage (313.0 per game) — both top-tier units. But both defenses are carrying real, specific, almost mirror-image weaknesses: Detroit's defense ranks 32nd — dead last — in points allowed, total yards allowed, and pass yards allowed, while its run defense is merely middling (22nd). Carolina's defense is the inverse: an genuinely elite pass defense (5th in yards allowed) paired with a run defense that ranks 32nd in the league, also dead last, allowing 144.7 rushing yards per game to running backs specifically.

The broad shape this suggests: two capable offenses each have an obvious, statistically extreme matchup advantage to attack — Carolina's passing game against Detroit's worst-in-the-league secondary, and Detroit's Jahmyr Gibbs against Carolina's worst-in-the-league run defense — while each defense's one real strength (Detroit's pass rush, Carolina's pass coverage) still has a path to disrupting the game. This profiles as a potential high-scoring affair built on two very different offensive approaches rather than a clean, balanced track meet; which specific mismatch gets exploited harder, and how each offense's own internal tendencies interact with the matchup, is the question the rest of this report works through.

---

## 2. INJURY & AVAILABILITY REPORT

No usable availability data exists for this game in the evidence package. The nflverse-sourced injury file for this week (injuries/wk04.json) came back reporting zero teams league-wide — per the evidence package's own note, this reflects a real publishing-timing gap (the practice-week injury report likely hadn't been published yet when this evidence was built), not a confirmation that every player on both rosters is healthy. The DraftKings-based fallback this report type sometimes relies on is also not present in this evidence package (dfs.available: false). No reliable outside confirmation could be established for this report, so every player discussed below should be read as presumed-active based on recent usage only — not as a confirmed-healthy designation.

A handful of roster notes are worth independent verification closer to kickoff given what the usage data alone suggests, without this report asserting any status for them: Carolina rookie running back Jonathon Brooks has played only 2 of 3 games with a reduced role (20.5% rush share); Darren Waller's snap share (43.3%) is notably below a full-time receiving tight end's workload for a player with his individual production; and Detroit's QB2 (Joshua Dobbs) and TE4 (Tyler Conklin) are both roster_only additions with zero 2026 game reps for their current teams. None of this should be read as a confirmed injury signal — just as context for why these specific names carry more week-to-week usage uncertainty than the rest of either roster.

---

## 3. MATCHUP STATISTICS

### Detroit Offense
Through three games, Detroit's offense ranks 3rd in the NFL in scoring (31.0 points per game), 9th in total yardage (388.0 ypg), 7th in passing (267.3 ypg), and 9th in rushing (120.7 ypg), with 22.7 first downs per game (3rd). Jared Goff's underlying passing indicators are excellent: 70.6% completion rate (4th), 25.7 completions per game (3rd), 8 touchdown passes through three games (3rd), and zero interceptions (1st) — a clean, mistake-free start. Sack rate is middling (2.33 per game, 18th).

At running back, Detroit's room as a whole is averaging 115.7 rushing yards per game (7th) and a remarkable 63.7 receiving yards per game (1st in the league) on 7.0 catches per game (also 1st) — almost entirely Jahmyr Gibbs, covered in depth below. At wide receiver, the group ranks 14th in receiving yardage (151.7 ypg) but 6th in target volume (20.7 per game) and 4th in touchdowns (5) — a unit that earns a lot of opportunities without always converting them into huge yardage totals. Tight end production is modest across the board (16th in yardage, 52.0 ypg; 20th in touchdowns with just 1).

**Down/Distance:** Detroit's offense converts 41.2% of third downs (13th) on 11.3 attempts per game, and converts 75.0% of fourth-down tries when it goes for it (18.2% go-for-it rate). The defense is a serious problem here: 56.1% of third downs are converted against it (31st), stopping just 43.9% — one of the league's worst third-down units, and it has not stopped a single fourth-down try all season (0.0%).

**Red Zone Play Calling:** Detroit's offense runs 45.5% of its red-zone plays (19th) and throws 54.5% (14th) — a fairly balanced, close-to-average mix. Its defense allows a near-identical split facing opponents (44.4% run allowed, 20th; 55.6% pass allowed, 12th) — this is a tendency reading, not a quality one; it describes what opponents have chosen to do against Detroit in the red zone, not how well Detroit has defended it.

**Contextual Statistics:** Detroit's team-level passing production has followed the expected opponent-quality pattern through three weeks — 269 pass yards against its one top-tier pass defense faced (NYJ), 206 against its one mid-tier opponent (NO), and 327 against its one bottom-tier opponent (BUF). Team rushing output, by contrast, was actually lowest against the mid-tier opponent (66 yards) and highest against the bottom-tier one (165) — all single-game samples (n=1 in every bucket), so this should be read as a general direction rather than a settled pattern. Confidence: LOW given the sample size.

### Detroit Defense
This is a genuinely bad defense by nearly every team-wide measure: 31.7 points allowed per game (32nd, dead last), 443.7 total yards allowed (32nd), 326.3 pass yards allowed (32nd), and 25.3 first downs allowed per game (32nd). The one real exception is the pass rush: Detroit is generating 4.0 sacks per game, 2nd-best in the league — a defense that gets to the quarterback at an elite rate while still bleeding yardage and points at a historic rate. That combination (elite pressure, historically poor coverage) is the central defensive storyline of this matchup and is explored further below.

Position-by-position, the picture is almost uniformly bad in coverage: 189.3 receiving yards allowed per game to wide receivers (29th) and 14.0 catches allowed per game (29th); tight ends have been even worse — 117.0 receiving yards allowed per game (32nd, dead last), 9.7 catches per game (32nd), and 6 touchdowns allowed (32nd, also dead last) — this is, by every tracked category, the worst tight-end defense in the league. Run defense is the relative strong point, allowing 87.0 rushing yards per game to running backs (13th) — comfortably Detroit's best defensive position group, even if the team-wide rush number (117.3 ypg, 22nd) is pulled down some by scramble yardage against the group as a whole.

**Down/Distance:** Detroit's defense allows a 56.1% third-down conversion rate (31st) as already noted — this is the same figure cited under offense above, restated here for completeness within the defense's own profile.

**Red Zone Play Calling:** Already covered above under Offense (defense section of the same evidence field).

### Carolina Offense
Carolina's offense ranks 5th in scoring (29.7 ppg), 6th in total yardage (410.0 ypg), and is the single best passing offense in the league by yardage — 313.0 pass yards per game, 1st. The running game is a clear weak point by comparison, 21st at 97.0 yards per game. First downs sit at 20.0 per game (8th).

The passing profile underneath that #1 ranking is unusual: Bryce Young's completion percentage is just 59.0% (28th) — one of the least efficient completion rates in the league — yet the yardage and explosive-play numbers are elite: 13.3 completions of 10+ yards per game (1st in the NFL), 6.7 completions of 16+ yards (2nd), 4.3 completions of 20+ yards (1st), and 4.3 passing touchdowns per game average built on 7 total touchdowns through three games (6th). This is a true boom-or-bust, shot-taking passing attack rather than a high-floor, short-area offense — big chunks of yardage on a lower share of total attempts connecting.

At running back, the group's rushing output is modest (85.0 ypg, 18th) but the receiving role is real (39.3 receiving yards per game, 9th; 2 receiving touchdowns, 1st in the league at the position). At wide receiver, Carolina ranks 4th in yardage (193.7 ypg) on a 5th-ranked target share (21.7 per game) and a 5th-ranked 15.3 yards per reception — again, an explosive, vertical-oriented group. Tight end is a genuine weapon too: 80.0 receiving yards per game (5th), 10.0 targets per game (5th), and 5.0 first downs per game (1st in the league at the position).

**Down/Distance:** Carolina's offense converts 36.8% of third downs (21st) on 12.7 attempts per game — middling, consistent with an offense built more on explosive plays than sustained drives. Fourth-down aggression is notable (26.1% go-for-it rate) but conversion when going for it has been poor (16.7%). The defense allows a 45.2% third-down conversion rate (24th) while stopping 54.8%.

**Red Zone Play Calling:** Carolina is almost entirely pass-oriented once it reaches the red zone — 66.7% pass plays (3rd-highest rate in the league) against just 33.3% run plays (30th, among the lowest run rates in the league). This matches Young's downfield, pass-volume profile and helps explain why Chuba Hubbard has produced 2 red-zone receiving touchdowns against only 1 rushing touchdown this season — Carolina simply isn't handing the ball off much once it gets close. Defensively, Carolina faces the inverse of its own identity: 61.5% of red-zone plays faced are runs (3rd-highest rate allowed in the league), while only 38.5% are passes (30th) — a strong early signal that opponents are already recognizing Carolina's run-defense weakness and specifically exploiting it once the field compresses. This is a tendency reading, not a quality one, but the direction is unmistakable given what's covered under Defense below.

### Carolina Defense
Carolina's defense is a genuine tale of two units. Against the pass, it is elite: 186.0 yards allowed per game (5th), and specifically excellent against wide receivers — 111.7 receiving yards allowed per game (3rd) and 124.7 air yards allowed per game (1st, tightest coverage shell in the league by that measure). Tight end defense is solid in yardage (40.3 ypg allowed, 11th) but leaky in touchdowns allowed (3, ranked 28th) — containing yardage without fully closing off the end zone at that position.

Against the run, this defense is the worst in the league without qualification: 193.3 rushing yards allowed per game team-wide (32nd), and specifically 144.7 rushing yards allowed per game to running backs (32nd, dead last) on 24.7 carries faced per game (24th) — both the total surrendered and the rate of damage per carry point to a defense that simply cannot be trusted to contain a competent ground game. Scoring defense overall sits at 27.7 points allowed per game (26th) and 379.3 total yards allowed (26th) — middling marks that mask just how extreme the run/pass split in quality actually is.

**Down/Distance and Red Zone:** Already covered above under Offense (shared fields).

---

## 4. MATCHUP INTELLIGENCE

### Quarterbacks

**Jared Goff (DET).** Goff's season line (267.3 pass yds/gm, 70.6% completion, 8 TD, 0 INT) is tracking almost identically to his real 2025 level *(2025: 268.5 pass yds/gm, 68.0% completion)* — this is not a hot-start fluke, it's a continuation of an established, stable level of play. His three games this season show the expected opponent-quality pattern: 206 yards against a mid-tier pass defense (New Orleans, 17th), 327 against a bottom-tier one (Buffalo, 28th), and 269 against a top-tier one (the Jets, 4th) — directionally normal, though with only one game in each bucket (LOW confidence on the specific magnitude). Carolina's pass defense (5th in yards allowed, 3rd specifically against wide receivers) is a genuine top-tier test, arguably tougher than anything he's faced so far. Detroit is the road team this week; Goff's only road start to date was the Buffalo game (327 yards, 32.8 DK points), and he has no real sample yet of a road start against a defense this strong — that specific combination simply hasn't happened yet this season, so expect some regression off his season pace rather than a repeat of his road ceiling. Confidence: MEDIUM.

**Bryce Young (CAR).** Young's 313.0 pass yards per game this season is a dramatic jump from his own real established level — *2025: 188.2 pass yds/gm* across a full 16-game season, and his career average (188.37 ypg) matches that 2025 level almost exactly. This is a real, large statistical swing worth taking seriously rather than dismissing as thin-sample noise, especially paired with his league-leading explosive-play rates (13.3 completions of 10+ yards/gm, 1st; 4.3 of 20+, 1st). His three opponents so far (Chicago, 13th; Atlanta, 27th; Cleveland, 20th) have ranged mid-to-bottom tier — he has not yet faced a genuinely elite pass defense this season. Detroit's defense, by contrast, ranks 32nd in pass yards allowed — the single worst pass defense in the league, by a wide margin even relative to Carolina's own weaker opponents so far. His one home start (Week 1 vs. Chicago, a mid-tier matchup) produced 361 yards; Carolina is home again this week, and the step down in opponent quality from mid-tier to bottom-tier argues his ceiling this week could exceed even that. Confidence: MEDIUM-HIGH given how extreme Detroit's pass defense ranking is, tempered by the thinness of Young's own 2026 sample.

### Running Backs

**Jahmyr Gibbs (DET).** The clear engine of Detroit's offense — 78.3% rush share, 90.0% of red-zone carries, and a dual-threat profile averaging 102.3 rushing yards per game and 52.0 receiving yards per game *(2025: 71.9 rush yds/gm, 36.2 rec yds/gm)* — both numbers represent a real step forward from his already-productive 2025 level. His rushing contact profile this season: 3.16 yards before contact per carry against 1.47 yards after contact, with 3.0 broken tackles per game — a back who is both benefiting from created space and forcing real missed tackles on top of it (broken-tackle rate is up sharply from *2025: 0.88 per game*, a notable individual improvement in contact balance). His own weekly matchups this season have scaled with opponent quality as expected — 156 yards against a bottom-tier run defense (New Orleans, 29th), 52 against a mid-tier one (Buffalo, 15th), and 99 against a top-tier one (the Jets, 10th). Carolina's run defense ranks 32nd against backs specifically — the single worst mark in this entire report, in either direction — comfortably Gibbs' best matchup of the season to date. He has no specific road-and-bottom-tier sample yet this season (his one road game, 52 yards, came against a mid-tier defense), so the exact number is uncertain, but the direction is unambiguous. Confidence: HIGH that this is a plus matchup; MEDIUM on the specific scale given the thin sample.

**Chuba Hubbard (CAR).** Carolina's lead back at a 61.2% rush share, averaging 61.3 rushing yards and 25.7 receiving yards per game *(2025: 34.1 rush yds/gm, 14.9 rec yds/gm)* — another real year-over-year jump. His contact profile (3.41 yards before contact, 1.23 after, 1.5 broken tackles per game) leans more on created space than individual tackle-breaking, a notable contrast with Gibbs' more balanced profile. His weekly numbers have tracked opponent quality cleanly: 49 yards against a mid-tier run defense (Chicago, 17th — also his only home game, matching this week's venue exactly), 53 against the league's best run defense (Atlanta, 1st), and 82 against a bottom-tier unit (Cleveland, 24th). Detroit's run defense ranks 22nd against backs — a true middle-of-the-road matchup, essentially identical in quality to the Chicago game that produced his home-and-mid-tier data point (49 yards, 23.7 DK points) — the single most directly comparable real data point available for projecting this week. Confidence: MEDIUM.

Backup notes: Jonathon Brooks (20.5% rush share, 2 games) and AJ Dillon (17.9% rush share, modest 1.88 yards-after-contact average) round out a committee that remains clearly secondary to Hubbard in current usage.

### Receivers and Tight Ends

**Amon-Ra St. Brown (DET).** The focal point of Detroit's passing game at a 32.4% target share, averaging 76.0 receiving yards per game on 11.67 targets *(2025: 82.4 rec yds/gm, 31.3% target share)* — essentially matching his established career level (76.24 ypg) and his 2025 target share almost exactly. His red-zone role is substantial (37.5% red-zone target share, 4 touchdowns on just 9 red-zone targets through three games). His own splits this season show real opponent-quality sensitivity: just 43.0 receiving yards per game combined against his two top-tier pass defenses faced (New Orleans, 2nd; the Jets, 5th), against 142.0 in his one game against a bottom-tier unit (Buffalo, 31st). Carolina's pass defense ranks 5th overall and 3rd specifically against wide receivers — among the tougher individual tests St. Brown has faced or will face this season, and directly in line with the suppressed end of his own career-established range. Confidence: MEDIUM-HIGH that this is a below-season-average expectation, given how consistently his top-tier splits have tracked.

**Jameson Williams (DET).** A lower-target-share complementary piece (15.7% target share, 5.67 targets/gm) but a legitimate big-play threat at 12.7 yards per reception, averaging 42.3 receiving yards per game — a real step down from *2025: 65.7 rec yds/gm* and zero touchdowns through three games compared to 7 across 17 games last season, worth flagging as a likely regression candidate given his volume hasn't fallen off a cliff. His weekly pattern is the inverse of what opponent-quality logic would predict: his two games against top-tier pass defenses (New Orleans, 2nd; the Jets, 5th) averaged 47.0 combined yards, while his one game against a bottom-tier defense (Buffalo, 31st) produced only 33 — the opposite direction from St. Brown's own clean, expected pattern over the same three weeks. This tension is explored further in Hidden Intelligence below.

**Sam LaPorta (DET).** A remarkably stable target, averaging 48.0 receiving yards per game on a 17.6% target share *(2025: 54.3 rec yds/gm, 18.6% target share)* — close to his established level. His own splits show almost no variance by opponent quality: 48.0 receiving yards per game against both his one bottom-tier matchup (New Orleans, 30th) and his combined top-tier matchups (Buffalo, 9th, and the Jets, 8th) — a matchup-proof floor target, similar in shape to a possession tight end whose role is schemed rather than matchup-dependent. Carolina's tight end defense (11th in yards allowed) is a tougher-than-average, if not truly elite, individual test — though his own available top-tier road figure (52.0 ypg, his lone road game, which happened to come against a comparably strong defense) suggests his floor should hold regardless. Confidence: MEDIUM-HIGH given how flat his production has been across tiers.

**Tetairoa McMillan (CAR).** Carolina's clear WR1 by target share (21.3%, 7.67 targets/gm) but still without a touchdown through three games (0 on 5 red-zone targets) despite averaging 64.3 receiving yards per game *(2025: 59.7 rec yds/gm, 7 TD across 17 games)* — a real touchdown-production gap relative to last year's established rate that argues for positive regression given the continued volume. His splits show real opponent-quality sensitivity: 46.0 receiving yards per game combined across his two mid-tier matchups (Chicago, 13th; Cleveland, 17th) against 101.0 in his one game against a bottom-tier defense (Atlanta, 32nd — the single weakest defense he's faced). Detroit's pass defense ranks 29th specifically against wide receivers — close to the extremity of that Atlanta game, and a genuinely favorable matchup by the raw numbers even though (as covered in Threat Intelligence below) his own production hasn't yet been loud enough to trigger the deterministic Threat system. Confidence: MEDIUM.

**Jalen Coker (CAR).** Carolina's WR2 at a 20.4% target share, averaging 74.0 receiving yards per game *(2025: 35.8 rec yds/gm, 14.9% target share)* — a real breakout relative to his rookie-year workload. His production has been volatile week to week: 138 yards in Week 1 (Chicago, mid-tier, also his only home game to date — his home average sits at exactly that 138.0 figure, a single data point well above his season average), 66 against Atlanta (bottom-tier), and just 18 against Cleveland (mid-tier) — the inverse of the expected pattern across his two mid-tier games, a small-sample quirk rather than a settled trend (LOW confidence on direction). Detroit's wide receiver defense (29th in yards allowed) sets up as another real opportunity regardless of which specific number materializes.

**Darren Waller (CAR).** Playing a reduced role by snap share (43.3%) relative to his name recognition, but efficient when targeted — 37.33 receiving yards per game on a 12.0% target share, with both of his touchdowns this season coming on just 2 red-zone targets (a perfect red-zone conversion rate through three games). Detroit's tight end defense ranks 32nd in the league in yards allowed, 32nd in catches allowed, and 32nd in touchdowns allowed — the single worst position-group matchup anywhere in this report for either team. Waller's own home split so far (28.0 ypg, Week 1 vs. Chicago, a mid-tier matchup) actually sits below his season average, and he has no real sample yet facing a defense this weak — the best available comparison is his one game against a bottom-tier unit (Cleveland, 24th), which produced his best game of the season (51 yards). His limited snap share is the real complicating factor capping how much of this matchup he can realistically absorb regardless of how weak Detroit's coverage is at the position. Confidence: MEDIUM.

**Tommy Tremble (CAR).** Carolina's primary tight end by snaps (53.3%) and by depth chart (listed TE1), but has been outproduced by Waller in yardage, red-zone touchdowns, and target share despite the larger role — 23.33 receiving yards per game and zero touchdowns through three games. Worth noting as a real role/production split: the player getting the plurality of snaps is not currently the player earning Carolina's best tight end opportunities.

### Pass Rush, Protection, and Coverage Notes

Detroit's defense presents a genuine split profile worth treating as two separate questions rather than one: its pass rush is legitimately elite (4.0 sacks per game, 2nd in the league) while its coverage is the worst in the league by nearly every measure. Carolina's own pass-block performance has been middling (Young is being sacked 2.33 times per game, 16th among qualifying quarterbacks), and Young's season-long trend shows real vulnerability specifically to pressure — a 48.6% completion rate and lower efficiency (5.26 yards/play) when the evidence package's blitz data shows him facing extra rushers, against 59.8% completion and 7.64 yards/play otherwise. Detroit's pass rush doesn't need to be exotic to matter here; a four-man rush that's already producing sacks at a top-2 rate league-wide is a real threat to Young regardless of Carolina's specific blitz-rate tendency this week (which the evidence package explicitly flags as not yet recomputed for this matchup and therefore not cited). On the other side, Goff's own splits show the opposite relationship — he performs considerably better when pressured in the pocket (72.5% completion, 0.48 EPA/play on pressure snaps) than when kept clean (63.2% completion, 0.161 EPA/play) — a pressure-resistant profile that argues Carolina's pass rush (2.3 sacks/gm, 11th, middling) is unlikely to be the deciding factor against Detroit's passing game.

No man/zone coverage splits, team-level coverage-rate tendencies, or individual CB/DB matchup data are available in this week's evidence package for either team — this is a genuine data gap, not an oversight, and should be treated as unavailable rather than inferred.

---

## 5. THREAT INTELLIGENCE

Football Intel's deterministic Threat Engine fires a designation when a player's own season-long rank in a specific statistical category AND the upcoming opponent's defensive rank in that same category both clear a fixed threshold — the convergence of genuinely elite individual production and a genuinely weak specific matchup, not either signal in isolation. The three tiers use exact, fixed thresholds (player rank is 1st-best; defense rank is 1st-toughest, so a high defense-rank number means a weak unit): **Nuclear** requires the player to rank top 3 in a category AND the opponent's defense to rank 30th or worse in that same category; **Elite** requires top 5 and a defense rank of 28th or worse; **Standard** requires top 10 and a defense rank of 23rd or worse. A "Double" designation means one category met both thresholds; "Triple" means a second category where the player's own rank alone clears the threshold even without the defense side converging; "Quadruple" means two or more categories fully converged on both sides.

**Bryce Young (CAR, QB) — Nuclear (pass_yds) + Elite (pass_tds), both Double.** Young's passing-yardage production and Detroit's pass defense both clear the Nuclear threshold in the same category: Detroit's pass defense ranks 32nd in the league in yards allowed (326.3 per game, the worst mark in this report), a weakness extreme enough to clear even the strictest threshold. His touchdown-pass rate separately clears the Elite threshold against the same defense (which also ranks 31st in passing touchdowns allowed, 9 through three games). This reflects season-long statistical stability on both sides, not a guarantee — and it's worth connecting honestly to the rest of this report: Detroit's pass rush is legitimately elite (2nd in sacks generated) even though its coverage is historically bad, and Young's own splits show he is notably less effective under pressure. The matchup-level case for a huge Young day is about as strong as this engine produces; the one real complicating factor is that Detroit can still disrupt individual dropbacks even while bleeding yardage overall. Confidence: HIGH on the yardage upside, MEDIUM on how clean that production will come.

**Jahmyr Gibbs (DET, RB) — Elite (Triple: rush_yds converged; rec_yds, rec extra).** Gibbs' rushing production and Carolina's run defense both clear the Elite threshold in the same category — Carolina ranks 32nd in rushing yards allowed to running backs (144.7 per game), the single worst specific number in this report in either direction. His own receiving volume (both yardage and catch rate) separately clears the threshold on his own side even though Carolina's pass defense against running backs isn't weak enough to converge there too — reflecting that Gibbs' receiving role alone is good enough to matter even against a defense that otherwise defends the position type reasonably in coverage. This is the cleanest, least qualified Threat designation in this game: no notable contradicting evidence elsewhere in this report argues against it. Confidence: HIGH.

**Jalen Coker (CAR, WR) — Standard (rec, Double).** Coker's reception total (not yardage, specifically catches) and Detroit's reception rate allowed to wide receivers both clear the Standard threshold — Detroit ranks 29th in catches allowed to wide receivers. This fired on the volume side of his profile rather than the explosive side; his own week-to-week yardage has been volatile (138 in Week 1, down to 18 in Week 3), so this designation should be read as supporting a real target/catch floor rather than guaranteeing a big yardage week specifically. Confidence: MEDIUM.

Two players carry real matchup advantages by the raw numbers without a designation firing, worth flagging honestly rather than treating the absence of a Threat as the absence of an edge: **Tetairoa McMillan** faces a Detroit wide-receiver defense that ranks 29th in yardage allowed — nearly as weak as Coker's qualifying matchup — but his own season-long production rank hasn't been loud enough yet to clear even the Standard threshold, likely held back by his zero-touchdown start. **Sam LaPorta** faces a Carolina tight-end defense that is genuinely tougher than average (11th in yardage allowed), so the absence of a designation there is consistent with the underlying matchup rather than a gap in the system. No designation fired for Amon-Ra St. Brown or Jared Goff this week, consistent with Carolina's defense being genuinely elite against the pass overall and specifically against wide receivers (3rd).

---

## 6. HIDDEN INTELLIGENCE & CONTEXTUAL ANALYSIS

**Finding 1: Carolina's offense behaves like a seesaw, not a stack — a big Bryce Young passing day and a good Chuba Hubbard rushing day have not historically happened together, which matters directly for how much this specific matchup actually helps the run game.** The evidence package's hit-rate splits show this cleanly from both directions: when Young's passing output is above his own average, Hubbard's rushing output hits its own average only 25.0% of the time (n=4); when Young is below his own average, Hubbard hits his own average 66.7% of the time (n=3). Read from the other side, it holds up again — when Hubbard is running well, Young hits his own passing average only 33.3% of the time (n=3); when Hubbard is running poorly, Young hits his own average 75.0% of the time (n=4). This season's own three-game log mostly reinforces the pattern: Week 2 (Atlanta) and Week 3 (Cleveland) both show Young hitting his average while Hubbard's rushing fell short, 2 of 3 available games. Why this isn't obvious: a reader would normally assume a competitive, functioning offense produces both a good passing day and a good rushing day together, the way Detroit's Jacobs/Love-style stack offenses often do elsewhere in the league — Carolina's own internal data argues the opposite is closer to true. Context Expansion: this lines up with Carolina's own red-zone identity (66.7% pass plays once inside the 20, 3rd-highest rate in the league, against just 33.3% run plays, 30th) — this is a offense built to lean fully into whichever is working, not to balance the two. What changes because of it for this specific game: even with Carolina's run defense being the single worst in the league against Hubbard's own position, Detroit's defensive weakness is concentrated even more heavily in the passing game (32nd overall, worst in the league) than the running game (22nd, merely middling) — if Young's early passing output is big, as the matchup argues it should be, this team's own pattern says Hubbard's workload and efficiency may not ride alongside it the way a cleaner run/pass funnel read would suggest. Confidence: MEDIUM given the small in-season sample size, but the direction is consistent across two independent measurements (QB-centric and RB-centric) and a larger historical sample behind both.

**Finding 2: Jameson Williams has produced more against tough pass defenses than weak ones this season — the exact opposite of the typical opponent-quality pattern, and the opposite of what Detroit's own team-wide numbers show.** His two games against top-tier pass defenses (New Orleans, 2nd; the Jets, 5th) averaged a combined 47.0 receiving yards, while his one game against a bottom-tier defense (Buffalo, 28th) produced only 33 yards — backwards from what opponent quality alone would predict. Why this isn't obvious: it runs directly against the grain of how receiver production normally scales, and it's also masked at the team level — Detroit's team-wide wide receiver production (driven primarily by St. Brown) follows the conventional pattern cleanly in the same three games (127 combined yards against the two top-tier defenses faced, 201 against the one bottom-tier defense), so a reader looking only at Detroit's team totals would never see Williams' individual inversion. Context Expansion: St. Brown's own individual splits over the same three weeks (43.0 ypg combined vs. top-tier defenses, 142.0 vs. the one bottom-tier defense) are the mirror opposite of Williams' — the team-level normal pattern is being generated entirely by St. Brown, while Williams is quietly bucking it. What changes because of it for this specific game: Carolina's pass defense is genuinely elite against wide receivers (3rd in yardage allowed), which argues for suppressed St. Brown production by his own established pattern — but if Williams' individual split is a real signal rather than small-sample noise, he may be the more live weekly piece specifically in a tough-coverage spot like this one, even though the team's overall receiving total should be expected to come in below its season average. Confidence: LOW given the extremely thin samples involved (two games in one bucket, one in the other) — this is a genuine, non-obvious cross-reference worth flagging rather than a settled conclusion.

---

## 7. COEUS FINAL READ

**Keys to the Game.**

If Detroit's pass rush (2nd in sacks generated) gets consistent pressure on Bryce Young, his own season-long splits say that's the one lever that can meaningfully cap an otherwise Nuclear-tier matchup — his completion rate and efficiency both collapse under pressure relative to a clean pocket, even though Carolina's pass-block unit has been only middling at preventing that pressure in the first place.

If Carolina's run defense performs to its season-long form (32nd in the league against running backs), Jahmyr Gibbs should see the clearest, least-qualified individual advantage in this entire report — but Finding 1 above argues that how much Gibbs' workload actually matters may depend less on Carolina's run defense and more on whether Jared Goff's own passing game (facing the single worst pass defense in the league) pulls Detroit's offense toward leaning on the air attack that's even more obviously open.

If Carolina's own seesaw tendency holds — Young hot, Hubbard colder, or vice versa — expect this game to be decided more by which specific unit gets rolling for Carolina on a given set of drives than by a clean, balanced offensive script.

**The Verdict.** Both offenses have a real, statistically extreme matchup to attack, but they are not symmetric opportunities: Detroit's overall pass defense is the single worst unit in this report by any measure (32nd across nearly every defensive passing category, including an unmatched 32nd-ranked tight end defense), while Carolina's weakness is real but narrower — its run defense is dead last specifically against backs, but its pass defense is genuinely elite. That asymmetry argues Carolina's passing attack, led by a quarterback already running well above his established career level, has the higher and more reliably attackable ceiling this week, with Darren Waller's matchup against Detroit's historically bad tight-end coverage standing out as the single most extreme individual mismatch in the entire game even before accounting for his limited snap share. Detroit's own best individual answer — Jahmyr Gibbs against the league's worst run defense — is a real, Threat-Engine-confirmed advantage, but Carolina's own internal tendencies suggest Detroit's offense may not lean on it as heavily as the raw matchup numbers alone would recommend, given how plainly broken Detroit's own pass defense is. Confidence: MEDIUM-HIGH that this is a high-scoring game built on each offense exploiting a real, specific weakness rather than a clean, low-event affair; MEDIUM on which side's advantage proves larger, given how thin every underlying 2026 sample still is three weeks into the season.

### Coeus Cheat Sheet

**Team**
- DET: 2-1 | 31.0 ppg (3rd) | 31.7 ppg allowed (32nd)
- CAR: 1-2 | 29.7 ppg (5th) | 27.7 ppg allowed (26th)

**Passing**
- Jared Goff (DET): 267.3 pass yds/gm (7th), 8 pass TD, 0 INT — opp D allows 186.0 pass yds/gm (5th)
- Bryce Young (CAR): 313.0 pass yds/gm (1st), 7 pass TD, 0.67 INT/gm — opp D allows 326.3 pass yds/gm (32nd)

**Rushing**
- Jahmyr Gibbs (DET): 102.3 rush yds/gm, 3.16 YBC/carry, 1.47 YAC/carry, 3.0 broken tackles/gm
- Chuba Hubbard (CAR): 61.3 rush yds/gm, 3.41 YBC/carry, 1.23 YAC/carry, 1.5 broken tackles/gm

**Receiving**
- Amon-Ra St. Brown (DET): 76.0 rec yds/gm, 32.4% target share
- Jameson Williams (DET): 42.3 rec yds/gm, 15.7% target share
- Sam LaPorta (DET, TE): 48.0 rec yds/gm, 17.6% target share
- Tetairoa McMillan (CAR): 64.3 rec yds/gm, 21.3% target share
- Jalen Coker (CAR): 74.0 rec yds/gm, 20.4% target share
- Darren Waller (CAR, TE): 37.3 rec yds/gm, 12.0% target share

**Team Defense**
- DET def: 326.3 pass yds/gm allowed (32nd) | 87.0 rush yds/gm allowed to RBs (13th) | 117.0 rec yds/gm allowed to TEs (32nd)
- CAR def: 186.0 pass yds/gm allowed (5th) | 144.7 rush yds/gm allowed to RBs (32nd) | 40.3 rec yds/gm allowed to TEs (11th)
- Team coverage rate (man%/zone%): not available in this week's evidence package for either team

**Down/Distance**
- DET offense: 41.2% third-down conv (13th) | DET defense: 56.1% allowed (31st)
- CAR offense: 36.8% third-down conv (21st) | CAR defense: 45.2% allowed (24th)

**Red Zone Play Calling**
- DET offense: 45.5% run / 54.5% pass (19th/14th) | DET defense allows: 44.4% run / 55.6% pass (20th/12th)
- CAR offense: 33.3% run / 66.7% pass (30th/3rd) | CAR defense allows: 61.5% run / 38.5% pass (3rd/30th)

**Head-to-head**
- No 2026 meeting between these two teams yet — this is their first matchup of the season, and not a division game.

---

EVIDENCE_CHECK
{"claims": [
{"type":"current_opponent","team":"DET","pos":"TEAM","stat":"ppg","role":"off","claimed_rank":3},
{"type":"current_opponent","team":"DET","pos":"TEAM","stat":"total_ypg","role":"off","claimed_rank":9},
{"type":"current_opponent","team":"DET","pos":"TEAM","stat":"pass_ypg","role":"off","claimed_rank":7},
{"type":"current_opponent","team":"DET","pos":"TEAM","stat":"rush_ypg","role":"off","claimed_rank":9},
{"type":"current_opponent","team":"DET","pos":"TEAM","stat":"fd_pg","role":"off","claimed_rank":3},
{"type":"current_opponent","team":"DET","pos":"TEAM","stat":"ppg","role":"def","claimed_rank":32},
{"type":"current_opponent","team":"DET","pos":"TEAM","stat":"total_ypg","role":"def","claimed_rank":32},
{"type":"current_opponent","team":"DET","pos":"TEAM","stat":"pass_ypg","role":"def","claimed_rank":32},
{"type":"current_opponent","team":"DET","pos":"TEAM","stat":"rush_ypg","role":"def","claimed_rank":22},
{"type":"current_opponent","team":"DET","pos":"TEAM","stat":"fd_pg","role":"def","claimed_rank":32},
{"type":"current_opponent","team":"CAR","pos":"TEAM","stat":"ppg","role":"off","claimed_rank":5},
{"type":"current_opponent","team":"CAR","pos":"TEAM","stat":"total_ypg","role":"off","claimed_rank":6},
{"type":"current_opponent","team":"CAR","pos":"TEAM","stat":"pass_ypg","role":"off","claimed_rank":1},
{"type":"current_opponent","team":"CAR","pos":"TEAM","stat":"rush_ypg","role":"off","claimed_rank":21},
{"type":"current_opponent","team":"CAR","pos":"TEAM","stat":"fd_pg","role":"off","claimed_rank":8},
{"type":"current_opponent","team":"CAR","pos":"TEAM","stat":"ppg","role":"def","claimed_rank":26},
{"type":"current_opponent","team":"CAR","pos":"TEAM","stat":"total_ypg","role":"def","claimed_rank":26},
{"type":"current_opponent","team":"CAR","pos":"TEAM","stat":"pass_ypg","role":"def","claimed_rank":5},
{"type":"current_opponent","team":"CAR","pos":"TEAM","stat":"rush_ypg","role":"def","claimed_rank":32},
{"type":"current_opponent","team":"CAR","pos":"TEAM","stat":"fd_pg","role":"def","claimed_rank":20},
{"type":"current_opponent","team":"DET","pos":"QB","stat":"comp_pg","role":"off","claimed_rank":3},
{"type":"current_opponent","team":"DET","pos":"QB","stat":"pass_td","role":"off","claimed_rank":3},
{"type":"current_opponent","team":"DET","pos":"QB","stat":"comp_pct","role":"off","claimed_rank":4},
{"type":"current_opponent","team":"DET","pos":"QB","stat":"int_pg","role":"off","claimed_rank":1},
{"type":"current_opponent","team":"DET","pos":"QB","stat":"sacks_pg","role":"off","claimed_rank":18},
{"type":"current_opponent","team":"DET","pos":"RB","stat":"rec_ypg","role":"off","claimed_rank":1},
{"type":"current_opponent","team":"DET","pos":"RB","stat":"rec_pg","role":"off","claimed_rank":1},
{"type":"current_opponent","team":"DET","pos":"RB","stat":"tgt_pg","role":"off","claimed_rank":3},
{"type":"current_opponent","team":"DET","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":7},
{"type":"current_opponent","team":"DET","pos":"RB","stat":"rush_td","role":"off","claimed_rank":3},
{"type":"current_opponent","team":"DET","pos":"RB","stat":"rec_td","role":"off","claimed_rank":2},
{"type":"current_opponent","team":"DET","pos":"WR","stat":"rec_ypg","role":"off","claimed_rank":14},
{"type":"current_opponent","team":"DET","pos":"WR","stat":"rec_pg","role":"off","claimed_rank":9},
{"type":"current_opponent","team":"DET","pos":"WR","stat":"tgt_pg","role":"off","claimed_rank":6},
{"type":"current_opponent","team":"DET","pos":"WR","stat":"td","role":"off","claimed_rank":4},
{"type":"current_opponent","team":"DET","pos":"TE","stat":"rec_ypg","role":"off","claimed_rank":16},
{"type":"current_opponent","team":"DET","pos":"TE","stat":"rec_pg","role":"off","claimed_rank":14},
{"type":"current_opponent","team":"DET","pos":"TE","stat":"tgt_pg","role":"off","claimed_rank":15},
{"type":"current_opponent","team":"DET","pos":"TE","stat":"td","role":"off","claimed_rank":20},
{"type":"current_opponent","team":"DET","pos":"QB","stat":"comp_pg","role":"def","claimed_rank":32},
{"type":"current_opponent","team":"DET","pos":"QB","stat":"pass_td","role":"def","claimed_rank":31},
{"type":"current_opponent","team":"DET","pos":"QB","stat":"comp_pct","role":"def","claimed_rank":28},
{"type":"current_opponent","team":"DET","pos":"QB","stat":"sacks_pg","role":"def","claimed_rank":2},
{"type":"current_opponent","team":"DET","pos":"QB","stat":"int_pg","role":"def","claimed_rank":15},
{"type":"current_opponent","team":"DET","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":13},
{"type":"current_opponent","team":"DET","pos":"RB","stat":"rec_ypg","role":"def","claimed_rank":7},
{"type":"current_opponent","team":"DET","pos":"RB","stat":"rush_td","role":"def","claimed_rank":20},
{"type":"current_opponent","team":"DET","pos":"WR","stat":"rec_ypg","role":"def","claimed_rank":29},
{"type":"current_opponent","team":"DET","pos":"WR","stat":"rec_pg","role":"def","claimed_rank":29},
{"type":"current_opponent","team":"DET","pos":"WR","stat":"td","role":"def","claimed_rank":18},
{"type":"current_opponent","team":"DET","pos":"TE","stat":"rec_ypg","role":"def","claimed_rank":32},
{"type":"current_opponent","team":"DET","pos":"TE","stat":"rec_pg","role":"def","claimed_rank":32},
{"type":"current_opponent","team":"DET","pos":"TE","stat":"td","role":"def","claimed_rank":32},
{"type":"current_opponent","team":"CAR","pos":"QB","stat":"comp_pg","role":"off","claimed_rank":7},
{"type":"current_opponent","team":"CAR","pos":"QB","stat":"att_pg","role":"off","claimed_rank":3},
{"type":"current_opponent","team":"CAR","pos":"QB","stat":"pass_td","role":"off","claimed_rank":6},
{"type":"current_opponent","team":"CAR","pos":"QB","stat":"comp_pct","role":"off","claimed_rank":28},
{"type":"current_opponent","team":"CAR","pos":"QB","stat":"p10_pg","role":"off","claimed_rank":1},
{"type":"current_opponent","team":"CAR","pos":"QB","stat":"p16_pg","role":"off","claimed_rank":2},
{"type":"current_opponent","team":"CAR","pos":"QB","stat":"p20_pg","role":"off","claimed_rank":1},
{"type":"current_opponent","team":"CAR","pos":"QB","stat":"sacks_pg","role":"off","claimed_rank":16},
{"type":"current_opponent","team":"CAR","pos":"QB","stat":"int_pg","role":"off","claimed_rank":15},
{"type":"current_opponent","team":"CAR","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":18},
{"type":"current_opponent","team":"CAR","pos":"RB","stat":"rec_ypg","role":"off","claimed_rank":9},
{"type":"current_opponent","team":"CAR","pos":"RB","stat":"rec_td","role":"off","claimed_rank":1},
{"type":"current_opponent","team":"CAR","pos":"RB","stat":"rush_td","role":"off","claimed_rank":16},
{"type":"current_opponent","team":"CAR","pos":"WR","stat":"rec_ypg","role":"off","claimed_rank":4},
{"type":"current_opponent","team":"CAR","pos":"WR","stat":"rec_pg","role":"off","claimed_rank":10},
{"type":"current_opponent","team":"CAR","pos":"WR","stat":"tgt_pg","role":"off","claimed_rank":5},
{"type":"current_opponent","team":"CAR","pos":"WR","stat":"td","role":"off","claimed_rank":11},
{"type":"current_opponent","team":"CAR","pos":"WR","stat":"ypr","role":"off","claimed_rank":5},
{"type":"current_opponent","team":"CAR","pos":"TE","stat":"rec_ypg","role":"off","claimed_rank":5},
{"type":"current_opponent","team":"CAR","pos":"TE","stat":"rec_pg","role":"off","claimed_rank":7},
{"type":"current_opponent","team":"CAR","pos":"TE","stat":"tgt_pg","role":"off","claimed_rank":5},
{"type":"current_opponent","team":"CAR","pos":"TE","stat":"td","role":"off","claimed_rank":8},
{"type":"current_opponent","team":"CAR","pos":"TE","stat":"fd_pg","role":"off","claimed_rank":1},
{"type":"current_opponent","team":"CAR","pos":"QB","stat":"comp_pg","role":"def","claimed_rank":6},
{"type":"current_opponent","team":"CAR","pos":"QB","stat":"pass_td","role":"def","claimed_rank":9},
{"type":"current_opponent","team":"CAR","pos":"QB","stat":"comp_pct","role":"def","claimed_rank":6},
{"type":"current_opponent","team":"CAR","pos":"QB","stat":"sacks_pg","role":"def","claimed_rank":11},
{"type":"current_opponent","team":"CAR","pos":"QB","stat":"int_pg","role":"def","claimed_rank":6},
{"type":"current_opponent","team":"CAR","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":32},
{"type":"current_opponent","team":"CAR","pos":"RB","stat":"rec_ypg","role":"def","claimed_rank":20},
{"type":"current_opponent","team":"CAR","pos":"RB","stat":"rush_td","role":"def","claimed_rank":29},
{"type":"current_opponent","team":"CAR","pos":"RB","stat":"rec_td","role":"def","claimed_rank":3},
{"type":"current_opponent","team":"CAR","pos":"WR","stat":"rec_ypg","role":"def","claimed_rank":3},
{"type":"current_opponent","team":"CAR","pos":"WR","stat":"rec_pg","role":"def","claimed_rank":7},
{"type":"current_opponent","team":"CAR","pos":"WR","stat":"td","role":"def","claimed_rank":4},
{"type":"current_opponent","team":"CAR","pos":"TE","stat":"rec_ypg","role":"def","claimed_rank":11},
{"type":"current_opponent","team":"CAR","pos":"TE","stat":"rec_pg","role":"def","claimed_rank":8},
{"type":"current_opponent","team":"CAR","pos":"TE","stat":"td","role":"def","claimed_rank":28},
{"type":"current_opponent","team":"DET","pos":"TEAM","stat":"third_down_conversion_pct","role":"off","claimed_rank":13},
{"type":"current_opponent","team":"DET","pos":"TEAM","stat":"third_down_pct_allowed","role":"def","claimed_rank":31},
{"type":"current_opponent","team":"CAR","pos":"TEAM","stat":"third_down_conversion_pct","role":"off","claimed_rank":21},
{"type":"current_opponent","team":"CAR","pos":"TEAM","stat":"third_down_pct_allowed","role":"def","claimed_rank":24},
{"type":"current_opponent","team":"DET","pos":"TEAM","stat":"red_zone_run_pct","role":"off","claimed_rank":19},
{"type":"current_opponent","team":"DET","pos":"TEAM","stat":"red_zone_pass_pct","role":"off","claimed_rank":14},
{"type":"current_opponent","team":"DET","pos":"TEAM","stat":"red_zone_run_pct_allowed","role":"def","claimed_rank":20},
{"type":"current_opponent","team":"DET","pos":"TEAM","stat":"red_zone_pass_pct_allowed","role":"def","claimed_rank":12},
{"type":"current_opponent","team":"CAR","pos":"TEAM","stat":"red_zone_run_pct","role":"off","claimed_rank":30},
{"type":"current_opponent","team":"CAR","pos":"TEAM","stat":"red_zone_pass_pct","role":"off","claimed_rank":3},
{"type":"current_opponent","team":"CAR","pos":"TEAM","stat":"red_zone_run_pct_allowed","role":"def","claimed_rank":3},
{"type":"current_opponent","team":"CAR","pos":"TEAM","stat":"red_zone_pass_pct_allowed","role":"def","claimed_rank":30},
{"type":"log_opponent","player":"Jared Goff","week":1,"stat":"pass_yds","claimed_rank":17},
{"type":"log_opponent","player":"Jared Goff","week":2,"stat":"pass_yds","claimed_rank":28},
{"type":"log_opponent","player":"Jared Goff","week":3,"stat":"pass_yds","claimed_rank":4},
{"type":"log_opponent","player":"Jahmyr Gibbs","week":1,"stat":"rush_yds","claimed_rank":29},
{"type":"log_opponent","player":"Jahmyr Gibbs","week":2,"stat":"rush_yds","claimed_rank":15},
{"type":"log_opponent","player":"Jahmyr Gibbs","week":3,"stat":"rush_yds","claimed_rank":10},
{"type":"log_opponent","player":"Amon-Ra St. Brown","week":1,"stat":"rec_yds","claimed_rank":2},
{"type":"log_opponent","player":"Amon-Ra St. Brown","week":2,"stat":"rec_yds","claimed_rank":31},
{"type":"log_opponent","player":"Amon-Ra St. Brown","week":3,"stat":"rec_yds","claimed_rank":5},
{"type":"log_opponent","player":"Jameson Williams","week":1,"stat":"rec_yds","claimed_rank":2},
{"type":"log_opponent","player":"Jameson Williams","week":2,"stat":"rec_yds","claimed_rank":31},
{"type":"log_opponent","player":"Jameson Williams","week":3,"stat":"rec_yds","claimed_rank":5},
{"type":"log_opponent","player":"Sam LaPorta","week":1,"stat":"rec_yds","claimed_rank":30},
{"type":"log_opponent","player":"Sam LaPorta","week":2,"stat":"rec_yds","claimed_rank":9},
{"type":"log_opponent","player":"Sam LaPorta","week":3,"stat":"rec_yds","claimed_rank":8},
{"type":"log_opponent","player":"Bryce Young","week":1,"stat":"pass_yds","claimed_rank":13},
{"type":"log_opponent","player":"Bryce Young","week":2,"stat":"pass_yds","claimed_rank":27},
{"type":"log_opponent","player":"Bryce Young","week":3,"stat":"pass_yds","claimed_rank":20},
{"type":"log_opponent","player":"Chuba Hubbard","week":1,"stat":"rush_yds","claimed_rank":17},
{"type":"log_opponent","player":"Chuba Hubbard","week":2,"stat":"rush_yds","claimed_rank":1},
{"type":"log_opponent","player":"Chuba Hubbard","week":3,"stat":"rush_yds","claimed_rank":24},
{"type":"log_opponent","player":"Tetairoa McMillan","week":1,"stat":"rec_yds","claimed_rank":13},
{"type":"log_opponent","player":"Tetairoa McMillan","week":2,"stat":"rec_yds","claimed_rank":32},
{"type":"log_opponent","player":"Tetairoa McMillan","week":3,"stat":"rec_yds","claimed_rank":17},
{"type":"log_opponent","player":"Jalen Coker","week":1,"stat":"rec_yds","claimed_rank":13},
{"type":"log_opponent","player":"Jalen Coker","week":2,"stat":"rec_yds","claimed_rank":32},
{"type":"log_opponent","player":"Jalen Coker","week":3,"stat":"rec_yds","claimed_rank":17},
{"type":"log_opponent","player":"Darren Waller","week":1,"stat":"rec_yds","claimed_rank":12},
{"type":"log_opponent","player":"Darren Waller","week":3,"stat":"rec_yds","claimed_rank":24}
]}