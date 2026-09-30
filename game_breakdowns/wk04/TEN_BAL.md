# GAME BREAKDOWN: Tennessee Titans @ Baltimore Ravens
### Week 4, 2026 Season | Scheduled 10/04/2026, 1:00 PM ET

**EVIDENCE PACKAGE NOTICE:** This evidence package is labeled as a bootstrap package (for an upcoming, unplayed game), but the underlying analytics are **not** prior-season data. Every team and player number below — records, per-game stats, game logs — reflects each team's actual first three games of the **current 2026 season** (TEN vs. NYJ, PHI, NYG; BAL vs. IND, NO, DAL). TEN and BAL have not yet met this season (`div_game: false`, and neither team's Week 1-3 log shows the other as an opponent), so there is no head-to-head evidence to draw on this year. Separately, this package's `rank_shifts` field — normally a real 2025-vs-2026 comparison — is not usable here: its "2025" figures are identical to this season's already-known 3-game numbers, and every "2026" field is null. No year-over-year comparison is cited anywhere in this report as a result; every claim below is built on the real, if thin, 3-game 2026 sample alone, consistent with this Standard's requirement that 2026 evidence stand on its own.

Given the sample size (3 games each), every number in this report should be read as **early-season, not fully stabilized** — confidence levels throughout reflect that reality rather than treating 3-game rates as settled form.

---

## 1. PREGAME BRIEFING

Tennessee is 0-3 to open the season and it shows up everywhere in the numbers: 30th in scoring (12.3 ppg), 31st in total offense (258.3 ypg), 30th in passing (168.0 pass ypg), and dead last in the league at generating rushing touchdowns (0 all season). Rookie quarterback Cam Ward is still finding his footing behind a low-volume, low-explosiveness passing offense (30th in pass yds/gm), though the defense has quietly kept Tennessee competitive — 8th against the pass (199.0 pass ypg allowed) and 10th in points allowed (19.7 ppg), even as the offense has produced almost nothing to work with.

Baltimore is 2-1 and looks like one of the more explosive offenses in the league early: 4th in scoring (30.7 ppg), 5th in total yards (415.7 ypg), and 3rd in rushing (167.3 rush ypg) behind a Derrick Henry who has been the engine of the offense (100.3 rush yds/gm, 6 rushing touchdowns already). Baltimore's defense has been more uneven — 19th against the pass, 21st in points allowed — but the offense has been productive enough to cover for it in two of three games.

No prior meeting exists between these two teams this season, and this isn't a division matchup, so there's no rivalry history or recent head-to-head form to lean on — every read here is built purely from each team's independent 3-game body of work.

The broad shape this profile suggests: Baltimore's offense, which already leans heavily on Henry and the run game in the red zone, is walking into a Tennessee defense that specifically surrenders more rushing volume than almost any team in the league once the ball crosses the 20 — a stylistic match that could push this game further in Baltimore's preferred direction than the box score gap alone suggests. Whether Tennessee's offense, which hasn't found real footing through three weeks, can generate enough points to make this competitive is the open question the rest of this report works through.

---

## 2. INJURY & AVAILABILITY REPORT

**No usable injury data exists in this evidence package.** The package's injury source note states plainly: *"injuries/wk04.json exists but reports zero teams league-wide — the real practice-week injury data for this week likely hadn't been published yet when this file was built. Genuinely unavailable, not confirmed-healthy."* No DraftKings status column or other designated source was present either. This report proceeds without any official availability information for either roster, and no web search fallback was able to be applied within the scope of this generation — treat every player below as presumptively available unless otherwise noted, with the explicit caveat that this has **not** been confirmed against any real source.

One log-based anomaly is worth flagging even though it carries no official designation: **Zay Flowers (BAL, WR)** has just 2 games logged this season, missing Baltimore's Week 2 home game against New Orleans entirely (no entry in his log for that week, and his `home_road_split` field is null — he has literally zero recorded snaps in a Baltimore home game this season). Nothing in this evidence package confirms a reason (injury, rest, healthy scratch), but the absence itself, and what it did to Baltimore's target distribution that week, is discussed further in Hidden Intelligence below. This is a genuine gap in Football Intel's own data, not a confirmed health concern — monitor independently before kickoff.

---

## 3. MATCHUP STATISTICS

### Tennessee Offense
- Scoring: 12.3 ppg (30th) | Total offense: 258.3 ypg (31st) | First downs: 13.0/gm (31st)
- Passing (Cam Ward, 100% snaps): 168.0 pass yds/gm (30th), 62.5% completion (19th), 2 total passing TDs (30th), 9.2 yds/completion (31st)
- Rushing (RB group): 80.3 rush yds/gm (21st), 18.3 carries/gm (28th), **0 rushing touchdowns all season (32nd, dead last)**
- Receiving (WR group): 121.0 rec yds/gm (25th), 17.3 targets/gm (21st), 2 TD (23rd), 10.7 yds/reception (30th)
- Receiving (TE group): 26.0 rec yds/gm (30th), 5.0 targets/gm (26th), 0 TD (31st), 7.1 yds/reception (31st)
- Down/Distance: 39.5% third-down conversion (17th) on 12.7 attempts/gm; 50.0% fourth-down conversion on an 8.7% go-for-it rate
- Red Zone Play Calling: 51.9% run rate in the red zone (13th), 48.1% pass rate (20th) — a near-even split, not a strong tendency either way
- Contextual Statistics: Tennessee's rushing production has scaled cleanly with opponent quality through three weeks — 68 rush yds in Week 1 (vs. a top-tier run front), 81 in Week 3 (mid-tier), and a season-high 122 in Week 2 (vs. a bottom-tier run defense). Passing output has been comparatively flat and low across the board (161.5 ypg average vs. its two toughest matchups, 181 in its one mid-tier game) — the passing game hasn't yet shown it can separate itself from a tough draw the way the ground game has started to.

### Tennessee Defense
- Scoring allowed: 19.7 ppg (10th) | Total yards allowed: 325.3 ypg (11th) | First downs allowed: 18.0/gm (18th)
- Pass defense: 199.0 pass yds/gm allowed (8th), but a concerning 71.1% completion rate allowed (30th) — stinginess on total yardage, not on letting throws connect
- Run defense: 126.3 rush yds/gm allowed (24th)
- Vs. WR: 157.3 rec yds/gm allowed (20th), 16.0 targets/gm faced (7th-most)
- Vs. TE: an elite **16.0 rec yds/gm allowed (1st in the NFL)**, 4.4 yds/reception allowed (1st), 11.7 air yds/gm allowed (1st) — tight ends have been almost entirely shut down
- Vs. RB (receiving): 25.7 rec yds/gm allowed (10th)
- Down/Distance: 39.5% third-down conversion allowed (15th) on 14.3 attempts/gm faced
- Red Zone Play Calling: opponents have run the ball on **72.0% of their red-zone snaps against Tennessee (1st in the NFL — the highest run rate allowed by any defense)**, passing on just 28.0% (32nd, the lowest pass rate allowed). This is a play-calling tendency stat, not a quality stat on its own — it describes what opponents are choosing to do, not necessarily how well Tennessee defends it — but it is a striking signal about how opponents are attacking this defense.
- Contextual Statistics: Tennessee's per-week opponents have been middling to tough on paper (a top-5 pass defense in Week 1, a top-10 pass defense in Week 2, a mid-tier defense in Week 3), and the unit has held up reasonably against the pass in all three; no data yet exists against a genuinely bottom-tier passing attack.

### Baltimore Offense
- Scoring: 30.7 ppg (4th) | Total offense: 415.7 ypg (5th) | First downs: 20.7/gm (5th)
- Passing (Lamar Jackson, 100% snaps): 248.3 pass yds/gm (12th), 69.7% completion (7th), 4 total passing TDs (18th), an explosive 14.1 yds/completion (1st in the NFL)
- Rushing (RB group, led by Henry): 119.3 rush yds/gm (5th), 26.3 carries/gm (5th), **6 rushing touchdowns (1st in the NFL)**
- Receiving (WR group): 169.7 rec yds/gm (8th), 13.7 targets/gm (28th-fewest) but an elite 18.9 yds/reception (1st) — fewer catches, far bigger plays
- Receiving (TE group): 58.7 rec yds/gm (12th), 8.0 targets/gm (11th), 1 TD (18th)
- Down/Distance: 37.0% third-down conversion (20th) on just 9.0 attempts/gm — the fewest third-down situations of either offense in this game, consistent with a ball-control approach
- Red Zone Play Calling: **69.4% run rate in the red zone (2nd in the NFL)**, just 30.6% pass rate (31st) — one of the most run-committed red-zone offenses in football, matching Henry's league-leading rushing-touchdown total directly
- Contextual Statistics: Baltimore's Week 1 blowout (41-23 over Indianapolis, the league's 29th-ranked run defense and 30th-ranked pass defense) is the outlier of the sample — both Jackson (324 pass yds) and the rush attack (202 team rush yds) peaked simultaneously against a genuinely overmatched opponent. In the two subsequent games, only one lever has fired at a time (see Hidden Intelligence).

### Baltimore Defense
- Scoring allowed: 26.0 ppg (21st) | Total yards allowed: 336.3 ypg (15th) | First downs allowed: 19.0/gm (24th)
- Pass defense: 231.3 pass yds/gm allowed (19th), 67.6% completion allowed (26th)
- Run defense: 105.0 rush yds/gm allowed (14th)
- Vs. RB (receiving): an elite 12.0 rec yds/gm allowed (3rd), 0 receiving TDs allowed to backs (2nd)
- Vs. WR: 173.3 rec yds/gm allowed (24th), but just 1 receiving TD allowed all season (3rd-best) — vulnerable to yardage, stingy on scores
- Vs. TE: 46.0 rec yds/gm allowed (14th)
- Down/Distance: 42.1% third-down conversion allowed (19th) on 12.7 attempts/gm faced
- Red Zone Play Calling: opponents have run 54.3% of red-zone snaps against Baltimore (10th), passed 45.7% (23rd) — a more balanced profile than what Tennessee's defense surrenders
- Contextual Statistics: Baltimore's defense has faced a lopsided schedule so far (Indianapolis and New Orleans, both bottom-10 offenses statistically, then a much tougher Dallas team) — the unit's raw numbers likely still carry some inflation from the two weaker opponents faced in Weeks 1-2.

---

## 4. MATCHUP INTELLIGENCE

### Quarterbacks

**Cam Ward (TEN).** A rookie still building consistency: 168.0 pass yds/gm (30th), 62.5% completion (19th), and just 2 total passing touchdowns through 3 games. *(2026 rookie season — no 2025 comparison exists; his `career` totals are identical to his `season` totals.)* His week-to-week sample is entirely against tougher competition so far: his two games against top-10 pass defenses (Week 1 vs. NYJ, ranked 4th; Week 2 vs. PHI, ranked 7th) produced a suppressed 161.5 pass yds/gm average, while his one mid-tier matchup (Week 3 vs. NYG, ranked 16th) produced 181 yards — actually above his season average. Baltimore's pass defense ranks 19th, squarely mid-tier — Ward's own thin track record points toward something close to his mid-tier number (181) rather than the suppressed top-tier one, which is a modestly encouraging signal for a struggling rookie. His road-specific number (181 pass yds, his only road game this season, Week 3) happens to be the exact same data point as his mid-tier number — a single overlapping sample, so treat this as informative but not conclusive. Notably, Ward has actually performed *better* against the blitz (63.6% completion, +0.049 EPA/play, n=22) than against standard rushes (57.7% completion, -0.211 EPA/play, n=71) — and Baltimore blitzes at a 37.5% rate, 7th-most in the league. Confidence: LOW-MEDIUM given the tiny samples on both sides, but the blitz-rate mismatch is worth watching (see Hidden Intelligence).

**Lamar Jackson (BAL).** 248.3 pass yds/gm (12th), 69.7% completion (7th), and an explosive 14.1 yards per completion (1st in the NFL) — an efficient, big-play passing operation through 3 games. His one true "tough matchup" sample this season came in Week 3 against Dallas, ranked 9th against the pass — a near-identical defensive profile to what Tennessee brings this week (ranked 8th). In that game, Jackson's passing dipped to a season-low 186 yards, while Derrick Henry carried the ball 26 times for 89 yards and 2 touchdowns as Baltimore leaned into the run to win 34-31. Given Tennessee's pass defense (8th) is essentially as tough as Dallas's was, and Tennessee's run defense (24th) is even a shade more generous than Dallas's (31st) was that week, the direct precedent points toward a similar plan: modest, efficient Jackson passing numbers, heavy Henry volume. Baltimore's only true home game this season (Week 2 vs. New Orleans, a mid-tier pass defense) produced 235 pass yards — no home-and-elite-defense sample exists yet to compare directly against this week's actual matchup type. Confidence: MEDIUM-HIGH on the Henry-lean projection given how directly the Dallas game maps onto this one; LOW-MEDIUM on Jackson's specific passing total given the shallow sample.

*(Backups: Tennessee's Mitchell Trubisky has zero 2026 games played with TEN — his most recent action came with a previous team in 2025, 4 games, 78.25 pass yds/gm. Baltimore's Tyler Huntley similarly has zero 2026 snaps, with a 2025 line of 5 games, 85.2 pass yds/gm, also with a previous roster. Neither carries meaningful expected involvement barring an availability change that this evidence package cannot confirm.)*

### Running Backs

**Derrick Henry (BAL).** The clear focal point of Baltimore's offense — 68.0% rush share, 100.3 rush yds/gm (5th in the league), and an outsized **80.0% share of Baltimore's red-zone carries**, which explains his league-leading 6 rushing touchdowns. *(2026 pace of 100.3 rush ypg through 3 games vs. 2025: 93.82 rush ypg over a full 17-game season — a modest step up, though see the caveat below on who he's faced.)* Every one of Henry's three 2026 games has come against a bottom-10 run defense by opponent rank (Indianapolis 27th, New Orleans 29th, Dallas 28th) — his excellent per-game average has not yet been tested against a stiffer front, and Tennessee's run defense (24th) continues that favorable trend, if not quite as extreme as his first three opponents. His contact-efficiency profile is notable: 3.22 yards after contact per carry against just 2.08 yards before contact, with 2.0 broken tackles per game — Henry is generating the bulk of his own yardage himself right now rather than leaning on his blocking, a change from 2025 (2.25 YAC, 2.94 YBC) that's worth watching as either an improving individual season or an early sign of a shakier offensive line. His lone home game this season (Week 2 vs. New Orleans, also his lone bottom-tier-run-defense-at-home data point) was actually his quietest by yardage (68 yards on 16 carries, though still with a rushing touchdown) — his two biggest games came on the road. Confidence: MEDIUM-HIGH on continued heavy volume and red-zone usage; LOW on translating his gaudy season average directly, given the uniformly soft schedule so far.

**Tony Pollard (TEN).** Tennessee's clear early-down back in a genuine committee — 59.4% rush share, but averaging just 69.0 rush yds/gm across his two full "starts" (his cumulative 3-game average of 57.67 rush ypg includes a lighter Week 1 committee snap share of 53%). *(No 2025 comparison relevant here — his career numbers with Tennessee are new this season.)* His one road game this season (Week 3, 74 rush yards on 17 carries, mid-tier opponent) is his only available road/tier data point; Baltimore's run defense ranks 12th, tougher than either opponent he's faced in a "hit" game so far. His broken-tackle rate (1.0/gm) and after-contact average (2.0 YAC/carry vs. 2.71 YBC/carry) suggest a back who is currently more schemed-open than one creating extra yardage himself, a different profile than Henry's. Tyjae Spears (20.3% rush share, a real receiving role at 13.67 rec yds/gm) remains the clear complementary/passing-down piece behind him. Confidence: MEDIUM.

### Wide Receivers / Tight Ends

**Carnell Tate (TEN).** Tennessee's clear rookie WR1 — 25.0% target share, 6.67 targets/gm, 41.0 rec yds/gm. *(3 career games, all in 2026 — no prior-season data exists.)* His Week 1 game came against New York Jets' pass defense, ranked 5th in the league — a tough draw — and he still produced a representative 38 yards on 4 catches (6 targets), suggesting stability regardless of matchup so far. His one road game this season (Week 3, 58 yards, 6 catches, 9 targets, his best game of the season) came against a mid-tier pass defense; no data exists yet against a bottom-10 unit, which is exactly the tier Baltimore's pass defense (24th vs. WR) falls into this week — a favorable, untested-tier matchup. Notably, on a tiny sample (n=3 targets), Tate has been dramatically more productive against the blitz (100% catch rate, +0.455 EPA/target) than against standard coverage (58.8% catch rate, -0.173 EPA/target) — paired with Baltimore's heavy blitz rate, this is worth watching even at low confidence. Confidence: LOW-MEDIUM given the rookie sample size, but directionally favorable given the matchup tier and volume share.

**Wan'Dale Robinson (TEN).** Tennessee's WR2 — 22.5% target share, 6.0 targets/gm, 34.67 rec yds/gm, with a season-best game already on record (Week 3: 57 yards, 7 catches, 11 targets, 1 TD, a 31.4% target share that game). *(2025 with a prior roster: 1,014 rec yds over 16 games, 63.38 ypg, 29.7% target share — a legitimately larger role last year, worth noting as an established baseline his 2026 role hasn't yet matched.)* His only road/mid-tier data point this season is that same Week 3 line; no bottom-tier-defense sample exists yet, which is the tier Baltimore's pass defense (24th vs. WR) falls into. Confidence: MEDIUM.

**Gunnar Helm (TEN).** The clear starting tight end — 81.7% snap share, 3.67 targets/gm, 18.33 rec yds/gm, with real red-zone usage (23.1% red-zone target share on a small sample). His one road/mid-tier game this season (Week 3, 14 rec yds) lines up almost exactly with this week's actual matchup: Baltimore's tight end defense ranks 14th, squarely mid-tier — a rare instance where the available split matches the matchup type precisely. Confidence: MEDIUM.

**Zay Flowers (BAL).** Statistically the most explosive receiver in this evidence package — 27.3% target share, 6.0 targets/gm, and a gaudy 117.0 rec yds/gm across his two games played (150 yards in Week 1 against a bottom-10 pass defense, 84 yards in Week 3 against a top-10 unit) — production that has held up regardless of opponent tier so far. But his role carries real question marks: his snap share in those two games was just 29% and 33%, remarkably low for a WR1-caliber target earner, and he has zero recorded snaps in Baltimore's only true home game this season (missing Week 2 entirely — see Injury & Availability and Hidden Intelligence). No home or home-tier split exists for him as a result. Confidence: MEDIUM on continued high per-target efficiency if he plays a full complement of snaps; LOW on his exact role/volume this week given the unexplained Week 2 absence and unusually light snap counts even when active.

**Rashod Bateman (BAL).** Baltimore's clear WR2 by usage — 17.8% target share, 4.33 targets/gm, 41.67 rec yds/gm — but with a genuinely inverted opponent-quality pattern so far: his best game (88 yards, 7 catches, 9 targets, 1 TD) came in Week 2 against New Orleans' defense, ranked 2nd in the league against the pass, while his quietest game (0 catches on 1 target) came in Week 1 against Indianapolis, ranked 28th — a defense he'd be expected to feast on. His lone home game this season is that same Week 2 outburst (top-tier-defense-at-home, n=1) — no mid-tier home sample exists yet, which is the tier Tennessee's pass defense (20th vs. WR) actually represents this week. The likely explanation for the inversion, discussed further below, is tied to Flowers' absence that same week. Confidence: LOW-MEDIUM given the counterintuitive pattern and thin sample.

**Mark Andrews (BAL).** Baltimore's clear starting tight end — 24.7% target share, a robust 6.0 targets/gm, 40.67 rec yds/gm, though without a touchdown yet this season. His lone home game (Week 2 vs. New Orleans, also his lone bottom-tier matchup) produced 49 rec yards on 6 catches — his best game of the season by yardage. This week presents Andrews with, by a wide margin, the toughest individual matchup in this entire report: Tennessee's tight end defense ranks **1st in the NFL** (16.0 rec yds/gm allowed, 4.4 yds/reception allowed, both league-best), and Andrews has no top-tier-matchup sample on record yet to gauge how he responds to a defense this stingy specifically against his position. Confidence: MEDIUM on a real role reduction risk this week — this isn't a marginal mismatch, it's the single most extreme unit-vs-position matchup in the evidence package.

*(Depth notes: Tennessee's Elic Ayomanor (11.2% target share) carries a real red-zone role (38.5% red-zone target share on low volume) despite modest overall production; Calvin Ridley has played just 2 games with Tennessee this season (target share under 6%). Baltimore's Devontez Walker (2 games, one 47-yard connection) and Chris Moore (8.2% target share, 1 receiving TD) round out a shallow complementary corps behind Flowers and Bateman.)*

### Coverage and Scheme

No man/zone coverage splits, defensive coverage-rate data, or CB/DB ranking data were present anywhere in this evidence package for either team (`coverage_qb`, `coverage_wr`, `coverage_te`, and `team_coverage_rate` are all empty, and `cb_db_rankings` is an empty list). Per the Coverage Scheme Rule, this analysis is omitted rather than assumed or estimated — no individual coverage-shell or man/zone tendency claims are made anywhere in this report as a result. The blitz-rate and blitz-success data discussed above under the Quarterbacks section is the only pressure/scheme-adjacent evidence available this week.

---

## 5. THREAT INTELLIGENCE

Football Intel's Threat Engine is deterministic: a Threat designation fires only when a player's own **season rank** in a specific statistical category, and the upcoming opponent's defensive rank in that **same exact category**, both clear a fixed tier threshold at the same time — not either signal in isolation. The three tiers use these exact thresholds (player rank is 1st-best; defense rank is 1st-toughest, so a high defense-rank number means a weak defense):

- **Nuclear** — player ranks top 3 in the category AND the opponent's defense ranks 30th or worse in that same category
- **Elite** — player ranks top 5 AND opponent defense ranks 28th or worse
- **Standard** — player ranks top 10 AND opponent defense ranks 23rd or worse

"Double," "Triple," and "Quadruple" describe how many categories converged for that player, not the strength of any single one.

**Derrick Henry (BAL, RB) — Standard tier, Double type.** The category that converged: **rush_yds**. Henry's own season rank in rushing yards is 5th in the league (100.3 rush yds/gm) — comfortably clearing even the Elite tier's player-side threshold (top 5). But Tennessee's run defense, in the specific category the Threat Engine used for this matchup, ranks 25th — enough to clear the Standard tier's 23rd-or-worse threshold, but not the Elite tier's tougher 28th-or-worse bar. That's why this fired as Standard rather than Elite: the individual side of the equation is elite-caliber, but the matchup side isn't quite bad enough to unlock the higher tier.

Read this honestly alongside the rest of this report: Henry's Threat reflects real, current statistical stability, but as noted in Matchup Intelligence, every one of his three 2026 games has come against a bottom-10 run defense — this Threat is confirming a matchup type Henry has already proven he exploits, not introducing new information beyond what the season-long profile already shows. It does not, by itself, guarantee he replicates his 100+ yard pace against a Tennessee front that, while generous, is a shade less extreme than his first three opponents.

**No other Threat designation fired for any evaluated starter on either side** — Cam Ward, Tony Pollard, Carnell Tate, Wan'Dale Robinson, and Gunnar Helm for Tennessee; Lamar Jackson, Rashod Bateman, Chris Moore, and Mark Andrews for Baltimore all came back with empty `threat_classification` arrays. This does not mean nothing else is actionable in this matchup — Section 4 above and Section 6 below both identify real, evidence-backed edges (particularly Baltimore's red-zone rushing identity against Tennessee's red-zone run funnel) that simply don't happen to meet this specific convergence system's fixed thresholds.

---

## 6. HIDDEN INTELLIGENCE & CONTEXTUAL ANALYSIS

**Finding 1: Baltimore's offense has fired on only one lever at a time in every competitive game so far — and this week's opponent profile points to which lever fires next.** Across Baltimore's 3 games, Lamar Jackson and Derrick Henry have never *both* exceeded their own season averages except in Week 1's 41-23 blowout of Indianapolis (ranked 29th against the run, 30th against the pass — the league's two weakest units, faced simultaneously). In every other game, exactly one hit while the other didn't, and which one hit tracked the specific weakness of that week's opponent: in Week 2 against New Orleans (17th against the pass, 27th against the run), Jackson topped his average (235 yards) while Henry's rushing did not (68 yards); in Week 3 against Dallas (9th against the pass, 31st against the run), Henry's volume and scoring carried the game (26 carries, 89 yards, 2 TDs) while Jackson's passing dipped to a season-low 186. Tennessee this week presents almost the same defensive shape Dallas did (8th against the pass vs. Dallas's 9th; 24th against the run vs. Dallas's 31st) — directly pointing toward a Henry-driven approach again. Context Expansion: this is already Baltimore's stated offensive identity, not just matchup-driven — the offense runs on 69.4% of its red-zone snaps (2nd in the NFL) and has Baltimore facing the fewest third-down situations per game (9.0) of either offense in this matchup, both signs of a team built to lean on the ground game rather than needing to throw its way into contention. Confidence: MEDIUM — three games is a real pattern, not proof, but every data point lines up the same direction.

**Finding 2: Tennessee's "8th-ranked" pass defense is not a pressure-based unit, and its own red-zone tendencies show teams are already choosing to attack it on the ground — which converges directly with Finding 1.** Tennessee blitzes on just 22.5% of pass snaps (26th-most in the league, i.e. one of the least frequent blitz teams) and, when it does blitz, succeeds only 35.0% of the time (31st, nearly the least effective in football). Yet the raw pass defense number (199.0 yds/gm, 8th) still looks strong — a sign the stat is more about limiting big plays and facing fewer attempts (Tennessee has faced the 6th-fewest pass attempts per game in the league) than genuine coverage or pass-rush dominance. Context Expansion: this lines up precisely with Tennessee's own red-zone play-calling data — opponents have run the ball on 72.0% of their red-zone snaps against Tennessee this season, the highest rate allowed by any defense in the league, while passing just 28.0% of the time (the lowest allowed). Teams are already recognizing and exploiting exactly the profile Tennessee presents. This converges directly with Finding 1: Baltimore, a team that already wants to hand the ball to Henry in the red zone more than almost any offense in football, is walking into the exact defense that most invites that approach league-wide. Confidence: MEDIUM-HIGH — both halves of this finding (Tennessee's blitz inefficiency and its red-zone run rate allowed) are drawn from clean, unambiguous ranked fields, and they reinforce rather than merely echo each other.

**Finding 3: A rookie-QB blitz vulnerability may be walking into one of the league's most blitz-heavy defenses — a tactical tension worth flagging even at low confidence.** Both Cam Ward (+0.049 EPA/play vs. blitz, n=22, vs. -0.211 EPA/play vs. standard rushes, n=71) and his top rookie target Carnell Tate (+0.455 EPA/target vs. blitz, n=3, vs. -0.173 EPA/target vs. no blitz, n=17) show the same directional pattern early this season: both perform notably better against pressure looks than against standard coverage. Baltimore blitzes at a 37.5% rate, 7th-highest in the league. Context Expansion: this sits in real tension with Tennessee's own down/distance profile (a middling 39.5% third-down conversion offense, 17th) — if Baltimore's blitz-heavy approach inadvertently plays into Ward's and Tate's early strengths, it could help sustain the kind of third-down drives Tennessee's offense hasn't shown it can generate on its own volume. Confidence: LOW — the samples here (n=22, n=3) are small enough that this could easily be noise, but it's a genuine, non-obvious cross-reference between two separate evidence categories (blitz splits for a QB and his top receiver) that a surface read of either team's season stats would not surface.

**Finding 4: Zay Flowers' unexplained Week 2 absence appears to have directly inflated Rashod Bateman's role that same week — worth watching if Flowers is fully active this week.** Bateman's single best game this season (88 yards, 9 targets, a 31.0% target share — nearly double his season rate of 17.8%) came in the exact week Flowers is missing from Baltimore's target log entirely. In the two weeks Flowers has played, Bateman's target share was 4.2% (Week 1) and 15.0% (Week 3) — both far below his Week 2 spike. Context Expansion: this matters directly for target-distribution expectations this week — if Flowers is active and sees anything close to a normal complement of snaps (his own snap shares even when active, 29% and 33%, have been unusually light for a lead receiver, so even his "active" games may understate a fuller role), Bateman's target beneficiary window from Week 2 may not repeat, since that spike appears tied specifically to Flowers' absence rather than a standing role change. Confidence: LOW-MEDIUM — this is inferred from a single data point (n=1 week of overlap) rather than a repeated pattern, but the magnitude of the shift (17.8% season rate vs. a 31.0% single-week spike, precisely coinciding with Flowers' only missed game) is large enough to flag rather than dismiss as noise.

---

## 7. COEUS FINAL READ

**Keys to the Game:**

- **If Baltimore leans on Derrick Henry the way its Week 3 game against a similarly-shaped Dallas defense suggests it will,** expect a run-heavy approach with real red-zone touchdown equity — both Henry's Threat designation and the red-zone funnel Tennessee's defense presents (Finding 2) point the same direction.
- **If Tennessee's offense cannot generate more than its season-long 12.3 points per game,** even a modest, disciplined Baltimore offensive performance should be enough — Tennessee's own third-down conversion rate (39.5%, 17th) and complete absence of rushing touchdowns this season give it little margin for error if it falls behind.
- **If Baltimore blitzes at anything close to its season rate (37.5%, 7th-most),** watch whether Ward and Tate's small-sample blitz-efficiency edge (Finding 3) shows up as a real complication for Baltimore's defensive plan, however unlikely that seems on paper.
- **If Mark Andrews sees a real workload reduction against Tennessee's league-best tight end defense,** Baltimore's passing offense may lean even more heavily on Flowers and Bateman than its already WR-forward target distribution suggests.

**The Verdict:** Every structural signal in this evidence package points the same direction — Baltimore's offense, defense, and red-zone identity all line up more favorably than Tennessee's o-line-deprived, touchdown-starved offense can currently counter. But the more interesting, evidence-backed story here isn't just "Baltimore is better" — it's that Baltimore's specific offensive identity (Henry-centric, red-zone-run-heavy) and Tennessee's specific defensive vulnerability (a run funnel disguised by a respectable yardage number) are a near-perfect stylistic match, pointing toward a heavier, more Henry-driven version of Baltimore's Week 3 win over Dallas rather than a shootout. Tennessee's counter-punch, if there is one, likely has to come from its defense forcing a very different game script than its offense has shown it can sustain on its own through three weeks.

### Coeus Cheat Sheet

**Team**
- TEN: 0-3 | 12.3 ppg (30th) scored / 19.7 ppg (10th) allowed
- BAL: 2-1 | 30.7 ppg (4th) scored / 26.0 ppg (21st) allowed

**Passing**
- Cam Ward (TEN): 168.0 pass yds/gm (30th), 2 pass TD, 62.5% comp (19th)
- Lamar Jackson (BAL): 248.3 pass yds/gm (12th), 4 pass TD, 69.7% comp (7th), 14.1 yds/comp (1st)

**Rushing**
- Tony Pollard (TEN): 57.67 rush yds/gm (season cum.), 59.4% rush share, 0 rush TD
- Derrick Henry (BAL): 100.3 rush yds/gm (5th), 68.0% rush share, 6 rush TD (1st)
- Lamar Jackson's individual rush total is not broken out in this evidence package (team rush total exceeds the RB group's own total by ~48 yds/gm, implying a real scramble/design-run contribution, but no specific per-game figure is available to cite)

**Receiving**
- TEN: Carnell Tate — 41.0 rec ypg (25.0% tgt share) | Wan'Dale Robinson — 34.67 rec ypg (22.5% tgt share) | Gunnar Helm (TE) — 18.33 rec ypg (81.7% snap share)
- BAL: Zay Flowers — 117.0 rec ypg (27.3% tgt share, 2 games) | Rashod Bateman — 41.67 rec ypg (17.8% tgt share) | Mark Andrews (TE) — 40.67 rec ypg (24.7% tgt share)

**Team Defense**
- TEN def: 199.0 pass ypg allowed (8th) | 126.3 rush ypg allowed (24th) | 16.0 TE rec ypg allowed (1st) | team coverage rate: not available in evidence package
- BAL def: 231.3 pass ypg allowed (19th) | 105.0 rush ypg allowed (14th) | 12.0 RB rec ypg allowed (3rd) | team coverage rate: not available in evidence package

**Down/Distance**
- TEN off: 39.5% third-down conv. (17th) | TEN def: 39.5% allowed (15th)
- BAL off: 37.0% third-down conv. (20th) | BAL def: 42.1% allowed (19th)

**Red Zone Play Calling**
- TEN off: 51.9% run (13th) / 48.1% pass (20th) | TEN def: 72.0% run allowed (1st) / 28.0% pass allowed (32nd)
- BAL off: 69.4% run (2nd) / 30.6% pass (31st) | BAL def: 54.3% run allowed (10th) / 45.7% pass allowed (23rd)

**Head-to-Head**
- No meeting between these two teams this season; not a division matchup. No prior-form basis to cite.

---

EVIDENCE_CHECK
{"claims": [
{"type": "current_opponent", "team": "TEN", "pos": "TEAM", "stat": "ppg", "role": "off", "claimed_rank": 30},
{"type": "current_opponent", "team": "TEN", "pos": "TEAM", "stat": "total_ypg", "role": "off", "claimed_rank": 31},
{"type": "current_opponent", "team": "TEN", "pos": "TEAM", "stat": "pass_ypg", "role": "off", "claimed_rank": 30},
{"type": "current_opponent", "team": "TEN", "pos": "TEAM", "stat": "rush_ypg", "role": "off", "claimed_rank": 28},
{"type": "current_opponent", "team": "TEN", "pos": "TEAM", "stat": "fd_pg", "role": "off", "claimed_rank": 31},
{"type": "current_opponent", "team": "TEN", "pos": "TEAM", "stat": "ppg", "role": "def", "claimed_rank": 10},
{"type": "current_opponent", "team": "TEN", "pos": "TEAM", "stat": "pass_ypg", "role": "def", "claimed_rank": 8},
{"type": "current_opponent", "team": "TEN", "pos": "TEAM", "stat": "rush_ypg", "role": "def", "claimed_rank": 24},
{"type": "current_opponent", "team": "TEN", "pos": "RB", "stat": "rush_yds", "role": "off", "claimed_rank": 21},
{"type": "current_opponent", "team": "TEN", "pos": "RB", "stat": "rush_td", "role": "off", "claimed_rank": 32},
{"type": "current_opponent", "team": "TEN", "pos": "WR", "stat": "rec_yds", "role": "off", "claimed_rank": 25},
{"type": "current_opponent", "team": "TEN", "pos": "TE", "stat": "rec_yds", "role": "off", "claimed_rank": 30},
{"type": "current_opponent", "team": "TEN", "pos": "RB", "stat": "rec_yds", "role": "def", "claimed_rank": 10},
{"type": "current_opponent", "team": "TEN", "pos": "WR", "stat": "rec_yds", "role": "def", "claimed_rank": 20},
{"type": "current_opponent", "team": "TEN", "pos": "TE", "stat": "rec_yds", "role": "def", "claimed_rank": 1},
{"type": "current_opponent", "team": "TEN", "pos": "QB", "stat": "comp_pct", "role": "def", "claimed_rank": 30},
{"type": "current_opponent", "team": "BAL", "pos": "TEAM", "stat": "ppg", "role": "off", "claimed_rank": 4},
{"type": "current_opponent", "team": "BAL", "pos": "TEAM", "stat": "total_ypg", "role": "off", "claimed_rank": 5},
{"type": "current_opponent", "team": "BAL", "pos": "TEAM", "stat": "rush_ypg", "role": "off", "claimed_rank": 3},
{"type": "current_opponent", "team": "BAL", "pos": "TEAM", "stat": "pass_ypg", "role": "off", "claimed_rank": 12},
{"type": "current_opponent", "team": "BAL", "pos": "TEAM", "stat": "fd_pg", "role": "off", "claimed_rank": 5},
{"type": "current_opponent", "team": "BAL", "pos": "TEAM", "stat": "ppg", "role": "def", "claimed_rank": 21},
{"type": "current_opponent", "team": "BAL", "pos": "TEAM", "stat": "pass_ypg", "role": "def", "claimed_rank": 19},
{"type": "current_opponent", "team": "BAL", "pos": "TEAM", "stat": "rush_ypg", "role": "def", "claimed_rank": 14},
{"type": "current_opponent", "team": "BAL", "pos": "RB", "stat": "rush_yds", "role": "off", "claimed_rank": 5},
{"type": "current_opponent", "team": "BAL", "pos": "RB", "stat": "rush_td", "role": "off", "claimed_rank": 1},
{"type": "current_opponent", "team": "BAL", "pos": "WR", "stat": "rec_yds", "role": "off", "claimed_rank": 8},
{"type": "current_opponent", "team": "BAL", "pos": "WR", "stat": "ypr", "role": "off", "claimed_rank": 1},
{"type": "current_opponent", "team": "BAL", "pos": "QB", "stat": "ypc", "role": "off", "claimed_rank": 1},
{"type": "current_opponent", "team": "BAL", "pos": "TE", "stat": "rec_yds", "role": "off", "claimed_rank": 12},
{"type": "current_opponent", "team": "BAL", "pos": "RB", "stat": "rush_yds", "role": "def", "claimed_rank": 12},
{"type": "current_opponent", "team": "BAL", "pos": "RB", "stat": "rec_yds", "role": "def", "claimed_rank": 3},
{"type": "current_opponent", "team": "BAL", "pos": "WR", "stat": "rec_yds", "role": "def", "claimed_rank": 24},
{"type": "current_opponent", "team": "BAL", "pos": "WR", "stat": "td", "role": "def", "claimed_rank": 3},
{"type": "current_opponent", "team": "BAL", "pos": "TE", "stat": "rec_yds", "role": "def", "claimed_rank": 14},
{"type": "current_opponent", "team": "TEN", "pos": "TEAM", "stat": "third_down_conversion_pct", "role": "off", "claimed_rank": 17},
{"type": "current_opponent", "team": "TEN", "pos": "TEAM", "stat": "third_down_pct_allowed", "role": "def", "claimed_rank": 15},
{"type": "current_opponent", "team": "BAL", "pos": "TEAM", "stat": "third_down_conversion_pct", "role": "off", "claimed_rank": 20},
{"type": "current_opponent", "team": "BAL", "pos": "TEAM", "stat": "third_down_pct_allowed", "role": "def", "claimed_rank": 19},
{"type": "current_opponent", "team": "TEN", "pos": "TEAM", "stat": "red_zone_run_pct", "role": "off", "claimed_rank": 13},
{"type": "current_opponent", "team": "TEN", "pos": "TEAM", "stat": "red_zone_pass_pct", "role": "off", "claimed_rank": 20},
{"type": "current_opponent", "team": "TEN", "pos": "TEAM", "stat": "red_zone_run_pct_allowed", "role": "def", "claimed_rank": 1},
{"type": "current_opponent", "team": "TEN", "pos": "TEAM", "stat": "red_zone_pass_pct_allowed", "role": "def", "claimed_rank": 32},
{"type": "current_opponent", "team": "BAL", "pos": "TEAM", "stat": "red_zone_run_pct", "role": "off", "claimed_rank": 2},
{"type": "current_opponent", "team": "BAL", "pos": "TEAM", "stat": "red_zone_pass_pct", "role": "off", "claimed_rank": 31},
{"type": "current_opponent", "team": "BAL", "pos": "TEAM", "stat": "red_zone_run_pct_allowed", "role": "def", "claimed_rank": 10},
{"type": "current_opponent", "team": "BAL", "pos": "TEAM", "stat": "red_zone_pass_pct_allowed", "role": "def", "claimed_rank": 23},
{"type": "current_opponent", "team": "BAL", "pos": "TEAM", "stat": "opp_blitz_rank", "role": "def", "claimed_rank": 7},
{"type": "current_opponent", "team": "BAL", "pos": "TEAM", "stat": "opp_blitz_success_rank", "role": "def", "claimed_rank": 18},
{"type": "current_opponent", "team": "TEN", "pos": "TEAM", "stat": "opp_blitz_rank", "role": "def", "claimed_rank": 26},
{"type": "current_opponent", "team": "TEN", "pos": "TEAM", "stat": "opp_blitz_success_rank", "role": "def", "claimed_rank": 31},
{"type": "log_opponent", "player": "Cam Ward", "week": 1, "stat": "pass_yds", "claimed_rank": 4},
{"type": "log_opponent", "player": "Lamar Jackson", "week": 1, "stat": "pass_yds", "claimed_rank": 31},
{"type": "log_opponent", "player": "Lamar Jackson", "week": 3, "stat": "pass_yds", "claimed_rank": 9},
{"type": "log_opponent", "player": "Derrick Henry", "week": 1, "stat": "rush_yds", "claimed_rank": 27},
{"type": "log_opponent", "player": "Derrick Henry", "week": 2, "stat": "rush_yds", "claimed_rank": 29},
{"type": "log_opponent", "player": "Derrick Henry", "week": 3, "stat": "rush_yds", "claimed_rank": 28},
{"type": "log_opponent", "player": "Rashod Bateman", "week": 1, "stat": "rec_yds", "claimed_rank": 28},
{"type": "log_opponent", "player": "Rashod Bateman", "week": 2, "stat": "rec_yds", "claimed_rank": 2},
{"type": "log_opponent", "player": "Carnell Tate", "week": 1, "stat": "rec_yds", "claimed_rank": 5},
{"type": "log_opponent", "player": "Zay Flowers", "week": 1, "stat": "rec_yds", "claimed_rank": 28},
{"type": "log_opponent", "player": "Zay Flowers", "week": 3, "stat": "rec_yds", "claimed_rank": 10}
]}