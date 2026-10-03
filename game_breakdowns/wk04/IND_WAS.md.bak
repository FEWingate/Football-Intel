# GAME BREAKDOWN: Indianapolis Colts @ Washington Commanders
### Week 4, 2026 Season | Scheduled 10/04/2026, 9:30 AM ET

**EVIDENCE NOTICE:** This game has not been played. There is no box score or line for this specific IND–WAS pairing. Despite the "bootstrap" tagging on this evidence package, the underlying team and player data is genuine **2026 in-season data** — both teams have played 3 real games this season (IND is 1-2, WAS is 1-2) — not prior-season data being used as a stand-in. The package's `rank_shifts` block (which would compare 2025-vs-2026 ranks) shows no 2026 values yet (too early in the season to compute), so no 2025-vs-2026 shift claims are made anywhere in this report. Certain fields (Threat category context, QB/RB run-vs-pass matchup data) have been explicitly recomputed against the real WAS-vs-IND pairing for this game; other fields (the blitz-rate tags inside the QB/WR blitz blocks) are explicitly flagged in the evidence as still referencing each team's actual *past* 2026 opponents rather than this matchup, and are **not** used below as opponent-specific context — only each player's own opponent-independent performance splits from those blocks are cited. No man/zone coverage rate data (`team_coverage_rate`) or individual CB/DB ranking data (`cb_db_rankings`) exists anywhere in this evidence package for either team — a genuine gap, not an omission, and it is treated that way throughout.

---

## 1. PREGAME BRIEFING

Both teams arrive at 1-2 having built nearly mirror-image identities through three weeks. Indianapolis owns a top-half scoring offense (24.0 points/game, ranked 15th) attached to one of the very worst defenses in football (30.3 points/game allowed, ranked 30th; 431.3 total yards/game allowed, ranked 31st). Washington is close to the same story: a slightly better offense by raw scoring (25.0 points/game, ranked 14th) paired with an even worse defense by one measure (30.7 points/game allowed, ranked 31st — the single worst mark in the league through three weeks).

There is no head-to-head history to draw on. This is not a division matchup, and Indianapolis and Washington have not played each other yet this season — Indianapolis's three games have come against Baltimore, Kansas City, and Houston, while Washington's have come against Philadelphia, Dallas, and Seattle. Every comparison in this report is therefore built from each team's own three-game body of work, not from any shared opponent or prior meeting.

The broad shape of this game, before digging into the specific matchup levers: two defenses that have both allowed 30-plus points per game through three weeks are facing two offenses that are middling-to-solid but hardly explosive. On paper, that points toward a track-meet — a game where whichever offense sustains drives and finishes them, rather than whichever defense forces stops, tends to come out ahead. But both defenses are not uniformly bad in the same way, and both offenses carry real questions of their own (including, on Washington's side, a genuine uncertainty about who takes the snaps at quarterback — covered next). The units that actually decide this game are not necessarily the ones the surface-level scoring numbers point to; the deeper matchup work in Sections 3-4 resolves that question, and Section 7 renders the actual verdict.

---

## 2. INJURY & AVAILABILITY REPORT

**No dedicated injury feed or DraftKings status-column data exists in this evidence package for this game.** The package explicitly notes that the Week 4 injury file (`injuries/wk04.json`) currently reports zero teams league-wide, meaning the real practice-week injury reports likely had not been published yet when this evidence was compiled — this is a genuine "not yet available" gap, not a "player group is confirmed healthy" signal. No live web search was performed for this report; readers should confirm final availability from a live source before kickoff. In the absence of that feed, two real, evidence-supported availability questions are worth flagging directly from game-log data:

- **Jayden Daniels (WAS, QB) — availability uncertain.** Daniels played 100% of Washington's offensive snaps in Week 1 (vs. PHI), then just 55% of snaps in Week 2 (vs. DAL), and does not appear anywhere in the Week 3 game log at all — Marcus Mariota played the entire Week 3 game (100% snap share) in his place. That in-game snap decline followed by a total absence the following week is consistent with an injury sustained during or after the Week 2 game. Washington's depth chart (as of 2026-09-29, the day before this evidence was compiled) still lists Daniels at pos_rank 1 (ahead of Mariota at pos_rank 2), which suggests he may be trending back toward availability, but his status for this specific Week 4 game cannot be confirmed from anything in this evidence package. Treat this as a real, open question — LOW-MEDIUM confidence on which quarterback actually starts — and read every Washington offensive projection below with that in mind. Marcus Mariota is the clear next man up if Daniels is out.
- **Chig Okonkwo (WAS, TE) — usage pattern worth flagging.** Okonkwo sits at pos_rank 1 on Washington's tight end depth chart, but has appeared in only 1 of Washington's 3 games this season (Week 1 vs. PHI, 56% snap share) — he is absent from both the Week 2 and Week 3 logs. No explicit reason is available in this evidence, but John Bates and Ben Sinnott have rotated into the earlier-down/receiving tight end role in the two games he's missed. Treat Okonkwo's Week 4 role as uncertain.

No other player on either roster carries any explicit availability flag in this evidence package.

---

## 3. MATCHUP STATISTICS

### Indianapolis Offense
Indianapolis ranks 15th in scoring (24.0 points/game) despite ranking just 26th in total yardage (307.0 yards/game) — an offense that is finding ways to score without piling up yardage, consistent with the red-zone-heavy rushing profile below. The passing game ranks 25th in yardage (203.7 pass yards/game) on a 66.3% completion rate (15th) but has produced only 3 total passing touchdowns through 3 games (25th) against 3 interceptions (1.0/game, 24th). The rushing attack is comfortably the more productive half of the offense: 103.3 rush yards/game (15th), fed almost entirely through one back (see Section 4).

**Down/Distance:** Indianapolis converts 40.5% of third downs (16th), on a heavy workload of 12.3 attempts/game. On fourth down, Indianapolis has gone for it on 21.7% of situations and converted 80.0% of those tries (a small sample, but a real one).

**Red Zone Play Calling (tendency, not quality):** Once inside the 20, Indianapolis leans run-heavy — 53.6% run plays (8th-highest run rate in the league) against 46.4% pass plays (25th-lowest pass rate). This is an identity marker, not a quality marker — it says Indianapolis calls more runs in the red zone than most teams, not that those runs are more effective than the league average. It becomes directly relevant to Jonathan Taylor's role in Section 4.

**Contextual splits:** Indianapolis's passing production has moved sharply with opponent quality through 3 games — 210 yards against a top-tier pass defense (Week 2, KC), 166 against a mid-tier defense (Week 1, BAL), and 235 against a bottom-tier defense (Week 3, HOU). Team rushing, by contrast, has stayed closer together across the same three games (104-yard average against top-tier run defenses on n=2, 102 against mid-tier on n=1) — early evidence, with all the sample-size caveats that come with three games, that the ground game is the more stable half of this offense regardless of who Indianapolis is facing.

### Washington Defense
Washington's defense is a genuine tale of two units. Against the run, it is one of the best fronts in football: 82.0 rush yards/game allowed (3rd), and specifically stingy against running backs — just 56.0 rush yards/game allowed to backs (3rd), on only 17.0 carries/game faced (3rd-fewest), with a league-best 1.7 first downs/game allowed via the run (1st). Zero rushing touchdowns have been credited against Washington's run defense from running backs, ranking a strong 7th.

Against the pass, this is one of the very worst units in the league. Washington ranks 31st in passing yards allowed (291.7/game) and has surrendered 11 total passing touchdowns already through 3 games — dead last in the NFL (32nd). The damage is concentrated at wide receiver: 191.0 receiving yards/game allowed to wideouts (30th), the most receptions allowed to wide receivers in the league (15.3/game, 32nd), and 6 wide receiver touchdowns allowed already (32nd, tied for worst). Tight ends have also done damage — 67.3 yards/game allowed (26th) and 5 touchdowns (31st, also from just 3 games). Washington's third-down defense reflects the same profile: 47.1% conversion rate allowed (26th), a unit that has real trouble getting off the field once a drive is sustained.

### Washington Offense
Washington's offense ranks 14th in scoring (25.0 points/game) on the back of an above-average ground game — 132.0 rush yards/game (8th) — carrying a below-average passing attack (184.7 pass yards/game, 28th, on a 60.2% completion rate, 25th). The offensive line has protected well regardless of the air-yardage total: just 1.0 sacks/game allowed (4th-best in the league), and ball security overall has been excellent — 0 interceptions thrown as a team through 3 games (4th).

**Down/Distance:** Washington converts 38.1% of third downs (18th) on a heavier workload than Indianapolis (14.0 attempts/game). Its fourth-down profile is a small, perfect sample so far — 12.5% go-for-it rate, 100% conversion rate.

**Red Zone Play Calling (tendency, not quality):** Washington is close to balanced once inside the 20 — 50.0% run (14th), 50.0% pass (19th) — a much more even split than Indianapolis's run-heavy approach.

**Contextual splits:** Washington's scoring has actually been highest against its one top-tier opponent so far (33 points, Week 3 vs. Seattle) versus 22 against a mid-tier defense (Week 1, Philadelphia) and 20 against a bottom-tier defense (Week 2, Dallas) — a genuinely small, three-game sample that runs counter to the usual expectation, and one worth treating with real caution rather than reading as a stable trend.

### Indianapolis Defense
Indianapolis's defense is bad nearly everywhere, but not uniformly so. It ranks 30th in points allowed (30.3/game), 31st in total yards allowed (431.3/game), 30th against the pass (291.0 yards/game) and 29th against the run (140.3 yards/game). The pass defense has been especially vulnerable to explosive plays — 16.8 yards allowed per completion (31st) and 66.7 yards/game of yards-after-catch allowed to wide receivers (29th) — and has generated zero interceptions through 3 games (30th). Against running backs specifically, Indianapolis has allowed 4 rushing touchdowns already (30th) despite a "merely" 27th-ranked rush-yards number — the touchdown vulnerability runs a level deeper than the yardage number alone suggests (more in Section 6).

The one real bright spot: Indianapolis's third-down defense is actually solid — 36.4% conversion rate allowed (10th) — a real disconnect from the overall unit grade that is worth remembering when thinking about how this defense actually loses games (broken coverages and touchdown-zone breakdowns more than sustained-drive failures).

---

## 4. MATCHUP INTELLIGENCE

### Quarterbacks

**Daniel Jones (IND).** Three starts, 203.7 pass yards/game (25th at his own position group level), on a 66.3% completion rate with 1.0 touchdown/game and 1.0 interception/game — turnover-prone through three weeks (24th in interception rate). He has already faced two pass defenses inside the top-10 this season — Kansas City in Week 2 (finishing that game 210 yards, ranked 3rd-toughest that game) and Houston in Week 3 (235 yards, though that opponent's pass defense actually graded bottom-tier that week per Indianapolis's own log) — a mixed, thin sample. On the road this season (his side for this game, matching Washington as the host), Jones's only road start came in that Week 2 Kansas City game: 210 pass yards, 71.0% completion, on 31 attempts — his single road data point, not enough to draw a real road tendency from (n=1). Washington's pass defense (291.7 yards/game allowed, ranked 31st) is a considerably weaker draw than either defense Jones has faced so far. Confidence: LOW-MEDIUM given the tiny 3-game sample, but the direction (a real step down in defensive quality from what he's seen) is clear.

**Jayden Daniels / Marcus Mariota (WAS).** Given the availability question flagged in Section 2, both quarterbacks require coverage. Daniels has started 2 games (130.0 pass yards/game, 56.9% completion, 3 total touchdowns, 0 interceptions) but has zero home appearances this season — every Daniels snap logged so far came on the road (Philadelphia, Dallas), so there is no home-specific split available for him at all heading into what would be his first home look of 2026 if he plays. Mariota has appeared in 2 games as well (147.0 pass yards/game, 63.8% completion, 4 total touchdowns, 0 interceptions), including Washington's lone home game so far — Week 3 vs. Seattle, in which he threw for 183 yards on 61.3% completion with 3 touchdowns, his best game of the season. Indianapolis's pass defense (291.0 yards/game allowed, ranked 30th) is barely behind Washington's own defense in overall badness — whichever quarterback plays is stepping into a genuinely favorable matchup on paper. Confidence: LOW on which quarterback plays, MEDIUM on the matchup being favorable to whichever one does.

**Pass rush and protection context:** Indianapolis's pass rush (2.3 sacks/game, 15th) is middling but real; it is facing a Washington offensive line that has been excellent in protection this season (1.0 sacks/game allowed, 4th-best in the league) — a tougher-than-average pass-rush matchup for Indianapolis. In the other direction, Washington's pass rush (1.7 sacks/game, 25th, below average) is facing a Daniel Jones who is already taking sacks at a moderate rate on his own (2.0/game, 14th-most) — Washington's front doesn't project as a unit that materially adds to that number.

### Running Backs

**Jonathan Taylor (IND).** The engine of this offense — 79.5% rush share, 80.0% share of red-zone carries, and already 4 rushing touchdowns through 3 games. His season average of 86.0 rush yards/game ranks 6th at his position. His road-specific average this season (his side for this game) is 92.0 rush yards/game, but that comes from a single game (Week 2 at Kansas City). Against opponents that rank top-10 against running back rushing specifically, Taylor has averaged 80.0 rush yards/game across 2 games this season (Kansas City, ranked 7th against the run in that matchup, and Houston, ranked 9th) — and the one game that combines both conditions (a road game against a top-10 run funnel) is that same Kansas City game: 92.0 rush yards on 24 carries (3.8 yards/carry), 2 touchdowns, plus 40.0 receiving yards. Washington's run defense (56.0 rush yards/game allowed to backs, ranked 3rd — tougher than either Kansas City or Houston graded when Taylor faced them) represents the stiffest run-funnel test he has seen in 2026. His underlying efficiency numbers this season are modest regardless of matchup — 2.19 yards before contact per carry and 2.23 yards after contact per carry, with 0.5 broken tackles/game — a between-the-tackles grinder rather than an explosive home-run threat, which matters against a defense built specifically to take away exactly that kind of back. Confidence: MEDIUM-LOW given the small samples on both sides, but every signal (opponent quality, his own contact-efficiency profile) points toward a tougher rushing day than his season average suggests.

**Seth McGowan (IND)** is a clear complementary/change-of-pace piece with almost no real workload (7.2% rush share, 4.7 rush yards/game) — not a factor in the game plan.

**Jacory Croskey-Merritt (WAS).** The clear early-down lead back — 49.0% rush share, and a heavy concentration of Washington's goal-line work (29.4% of red-zone carries, already 1 rushing touchdown). His season average of 47.3 rush yards/game comes with modest per-carry efficiency underneath it: 2.32 yards before contact and just 1.46 yards after contact per carry, with zero broken tackles logged this season — production built more on scheme and volume than on making defenders miss. His lone home game so far (Week 3 vs. Seattle, a genuinely tough run defense that week) was his worst outing of the season: 36 rush yards on 19 carries, just 1.9 yards/carry. Indianapolis's run defense (114.0 rush yards/game allowed to backs, ranked 27th) is a considerably more favorable matchup than what Croskey-Merritt's thin home sample reflects — his one logged home game came against a much tougher front than the one he's facing this week. Confidence: MEDIUM.

**Rachaad White (WAS)** is the clear passing-down complement — 22.9% rush share but a real receiving role (9.7% target share, 3.0 receptions/game, 17.0 receiving yards/game), including a touchdown catch in his lone home appearance this season (Week 3: 35 rush yards, 6 receiving yards, 1 receiving touchdown). **Kaytron Allen (WAS)** carries essentially no standalone role (14.1% rush share across 2 games).

### Wide Receivers / Tight Ends

**Josh Downs (IND).** Indianapolis's clear No. 1 target — a 25.5% target share and 80.0% snap share, averaging 62.0 receiving yards/game (his own rank of 19th at the position) on 4.67 catches/game. Washington's defense is about as favorable a draw as exists in this evidence package: 191.0 receiving yards/game allowed to wide receivers (30th) and the most catches allowed to wideouts in the league (15.3/game, 32nd). Downs's only road appearance and only game against a top-tier pass defense this season are the same data point (Week 2 at Kansas City): 7 catches, 9 targets, 72 receiving yards — his best game of the season, against a considerably tougher matchup than this one. Confidence: MEDIUM.

**Keenan Allen (IND).** The No. 2 target (21.3% target share, 33.3 receiving yards/game), but with a quiet season so far by his own standards (his own receiving-yards rank sits outside the top-50 among qualifying receivers) — a name more relevant for target volume than for per-target explosiveness against this matchup.

**Tyler Warren (IND).** A near-every-down piece at tight end — 92.0% snap share and a 23.4% target share, with an elite catch rate underneath modest per-catch yardage (18 catches on 22 targets, but just 4.94 yards per reception, 26.67 yards after the catch per game) — a checkdown/possession weapon more than a downfield threat. His own reception-count rank (3rd at the position) is real, but Washington's defense doesn't rank weak enough against tight end catch volume specifically (15th in that category) to create the kind of extreme mismatch his overall profile might suggest; Washington's real tight end vulnerability (67.3 yards/game allowed, ranked 26th) is more about yardage than catch volume. Confidence: MEDIUM.

**Darius Slayton (IND)** has not played a snap for Indianapolis yet this season (roster_only, zero games), but sits at WR pos_rank 3 on the depth chart — ahead of Laquon Treadwell, who has actually played all 3 games. With his prior team in 2025, Slayton logged a real role (14 games, 38.4 receiving yards/game, 15.2% target share, 81.3% snap share) — a name worth watching if he's active, given his depth-chart positioning outranks players who've already taken the field this year. Confidence: LOW, since his actual role with Indianapolis is unproven.

**Terry McLaurin (WAS).** Co-lead target with Diggs (23.7% target share, 7.33 targets/game), averaging 47.0 receiving yards/game. His only home appearance this season (Week 3 vs. Seattle, the toughest pass defense he's faced) produced his best game of the year — 77 receiving yards on 6 catches, 9 targets, 1 touchdown — against a defense ranked 1st against the pass that week. Indianapolis's own pass defense (179.3 receiving yards/game allowed to wide receivers, ranked 28th) is a considerably softer matchup than that one data point reflects, though the thin sample (n=1 home game, against an outlier-tough opponent) means his true home number is likely understated by that lone game rather than overstated. Confidence: MEDIUM.

**Stefon Diggs (WAS).** The other co-lead target (23.7% target share as well), averaging 45.0 receiving yards/game, but the standout number is his red-zone efficiency: 4 red-zone targets, 4 red-zone receptions, 3 red-zone touchdowns — essentially automatic once Washington gets him the ball inside the 20 this season. His lone home game (Week 3 vs. Seattle) was his quietest of the year (33 yards, 4 catches, 0 touchdowns), again against the league's best pass defense that week. Confidence: MEDIUM (small sample, but the red-zone conversion rate is a real, striking number).

**Antonio Williams (WAS)** is a real complementary piece (34.3 receiving yards/game, 11.8% target share) with a touchdown in Week 1, but has cooled since (24 and 15 yards in Weeks 2-3).

No man/zone coverage splits, individual CB/DB matchup data, or team-level man/zone coverage-rate data exist anywhere in this evidence package for this game — a genuine gap in this week's evidence, not an oversight in this report. The blitz-based splits that do exist (below) are the only scheme-level lens available.

### Blitz Notes (opponent-independent, player-level only — see notice above)

Josh Downs shows a real, large blitz split in his own career-spanning numbers: 75.0% completion rate, 9.75 yards per play, and a +1.153 EPA/target mark when blitzed (n=8), against a 50.0% completion rate and +0.242 EPA/target when not blitzed (n=16) — a receiver who has consistently produced more, not less, when the defense sends extra rushers. Daniel Jones shows a smaller but directionally similar pattern — a 45.2% success rate and -0.034 EPA/play when blitzed (n=31) against a 42.5% success rate and a notably worse -0.208 EPA/play when not blitzed (n=73). Neither of these splits can be tied to Washington's actual blitz tendency this season (that field is explicitly flagged as unavailable for this specific pairing), so they should be read as this offense's own tendency rather than a prediction about how Washington will play it. Jayden Daniels's own blitz splits (n=12 blitzed, n=41 not blitzed) and Terry McLaurin's (n=2 blitzed) are both too thin this season to draw a real conclusion from.

---

## 5. THREAT INTELLIGENCE

Football Intel's deterministic Threat Engine flags a player only when two conditions converge in the *same statistical category*: the player's own season rank in that category clears a threshold, **and** the upcoming opponent's defensive rank in that *same* category is weak enough to clear its own threshold. Both sides have to clear the bar together — elite individual production alone, or a terrible matchup alone, is not enough on its own. The three tiers use these exact thresholds (player rank is 1st-best; defense rank is 1st-toughest, so a high defense-rank number means a weak defense):

- **Nuclear** — player ranks top 3 in the category AND the opponent's defense ranks 30th or worse in that category
- **Elite** — player ranks top 5 AND opponent defense ranks 28th or worse
- **Standard** — player ranks top 10 AND opponent defense ranks 23rd or worse

**No Threat designation fired for any starter on either side of this matchup.** That is notable given how extreme some of the underlying matchups actually are, and worth explaining rather than just reporting as a blank:

- **Josh Downs (IND, WR)** is the closest miss on the board. His own receiving-yards rank (19th) and reception rank (19th) both sit outside the Standard tier's top-10 threshold — even though Washington's defense clears the *Nuclear*-tier defensive threshold in both categories (30th in receiving yards allowed to wide receivers, 32nd in catches allowed). The matchup is as good as this evidence package shows anywhere in this game; the engine simply requires Downs's own season line to climb into the top 10 at his position before it would fire, which a still-developing, three-game 2026 sample hasn't yet produced.
- **Jonathan Taylor (IND, RB)** clears the player-side threshold comfortably (6th in rush yards, well inside Standard/Elite range), but Washington's run defense grades far too well to qualify as a weak opponent (3rd against running back rushing, 18th against running back receiving) — the opposite of what the engine looks for. No designation fires here for the correct reason: this is a genuinely difficult individual matchup, not a near-miss.
- **Tyler Warren (IND, TE)** narrowly misses in two different ways — his reception rank (3rd, well inside the threshold) pairs with a Washington tight end-catches defensive rank (15th) that isn't weak enough to qualify, while his receiving-yards rank (19th) pairs with a defensive rank (26th) that *would* qualify if his own side cleared the bar. Two categories, two different reasons for the same non-designation.
- On Washington's side, none of Jacory Croskey-Merritt, Terry McLaurin, or Stefon Diggs currently rank inside the top-25 to top-55 range (by category) needed to even approach the player-side threshold, despite Indianapolis's defense being genuinely bad across nearly every category. Jayden Daniels and Chig Okonkwo carry no ranked categories at all in this evidence (insufficient qualifying sample, consistent with their limited/uncertain availability this season, per Section 2).

The absence of a Threat designation here is a Week 4, small-sample effect — it reflects that neither team's skill players have yet accumulated enough of a season-long track record to separate into the top tiers the engine requires, not an absence of real matchup advantage. Section 4 above and Section 6 below carry the real edges in this game.

---

## 6. HIDDEN INTELLIGENCE & CONTEXTUAL ANALYSIS

**Finding 1: Washington's glaring pass-defense weaknesses may not fully convert into passing scores for Indianapolis, because Indianapolis's own red-zone identity is run-first — a tension the surface-level matchup data alone would miss.** Washington's defense has allowed 6 wide receiver touchdowns already this season (32nd, tied for worst in the league) and 5 tight end touchdowns (31st) — an extraordinary short-yardage/red-zone vulnerability through the air. The instinctive read is that Indianapolis's passing weapons (Josh Downs, Tyler Warren) are obvious touchdown-upside plays this week. But Indianapolis's own red-zone play-calling profile runs the other way: once inside the 20, Indianapolis calls run plays 53.6% of the time — the 8th-highest run rate in the league — against just 46.4% pass plays (25th-lowest). And that run-heavy approach is itself concentrated overwhelmingly on one player: Jonathan Taylor has carried 80.0% of Indianapolis's red-zone rushing attempts this season, already producing 3 rushing touchdowns. The two pieces of evidence, read together, suggest the touchdown upside from Washington's leaky red-zone pass defense is real but may be smaller than it looks for Indianapolis's receivers specifically — Indianapolis simply doesn't throw as much as most teams once it gets close, and when it does, one running back is already claiming most of the goal-line work. Confidence: MEDIUM.

**Finding 2: Washington's defense is split into an elite run-stopping unit and a historically bad pass unit — but Daniel Jones's own career-long pattern says his best passing days come *with* a working run game, not as a substitute for one, which complicates the obvious "just throw on Washington" read.** Across a broader sample of his career starts, Jones's own splits show a real connection between his passing performance and Indianapolis's rushing success in the same game: when Indianapolis's run game has been hot, Jones has turned in an above-average passing game 62.5% of the time (n=8); when the run game has been cold, that rate drops to 28.6% (n=7). The relationship runs both ways — when Jones himself is hot, Indianapolis's run game has hit 71.4% of the time (n=7), against just 37.5% when he's cold (n=8). Washington represents the most extreme version of a split-personality defense Indianapolis has faced all season (3rd against the run, 31st against the pass) — meaningfully tougher against the run than either Kansas City (7th) or Houston (9th), the two run funnels Indianapolis has already seen in 2026. If Washington's run defense does what its season-long profile suggests and takes Jonathan Taylor out of the game the way it has taken away every other running back it has faced, Jones's own history argues that is more likely to correlate with a *quieter* passing day for him too — not the volume-driven big day that Washington's raw pass-defense ranking alone would suggest. This directly complicates Finding 1 and the broader instinct to treat Washington's pass defense as an easy target in isolation. Confidence: LOW-MEDIUM (the underlying splits carry decent but not large samples, and Washington is a genuinely new type of matchup for this specific offense this season).

**Finding 3: Indianapolis's run defense is a bigger red-zone/touchdown liability than its overall rushing-yardage rank suggests — a distinction that matters directly for Jacory Croskey-Merritt's role.** Indianapolis ranks 27th in rush yards allowed to running backs (114.0/game) — bad, but not catastrophic on its face. Its rushing-touchdown defense, however, ranks a full three spots worse at 30th, having already allowed 4 rushing touchdowns to running backs through just 3 games. That gap between the yardage rank (27th) and the touchdown rank (30th) is the kind of detail a reader skimming the yardage number alone would miss entirely, and it lines up specifically with Croskey-Merritt's actual role: he already carries 29.4% of Washington's red-zone rushing share and has scored on the ground once this season despite modest per-carry efficiency underneath it (2.32 yards before contact, just 1.46 after). Indianapolis's defense is specifically softer in the exact area — goal-line/short-yardage rushing — where Croskey-Merritt already does most of his damage. Confidence: MEDIUM.

---

## 7. COEUS FINAL READ

**Keys to the Game:**

- **If Washington's run defense does to Jonathan Taylor what it has done to every running back it has faced this season** (56.0 rush yards/game allowed, 3rd in the league, with a league-best 1.7 first downs/game allowed via the run), Indianapolis's offense is forced away from its most stable, most opponent-proof unit — and per Finding 2, Daniel Jones's own history suggests that is more likely to drag his passing performance down with it than to force a compensating big air-yardage day.
- **If Indianapolis's passing attack does get going against Washington's pass defense**, the touchdown-zone version of that story (Finding 1) is more likely to run through Jonathan Taylor's continued red-zone workload than through Josh Downs or Tyler Warren, given Indianapolis's run-heavy red-zone identity — watch Indianapolis's red-zone play mix specifically, not just its overall passing volume.
- **If Jayden Daniels is unavailable or limited**, Washington's passing operation shifts to Marcus Mariota, whose only home look this season (Week 3 vs. Seattle) was his best game of the year — a modest positive signal, though built on a single data point against a very different caliber of pass defense than Indianapolis's.
- **If Indianapolis's defense allows this to become a sustained-drive, high-play-count game**, its actual third-down defense (36.4% allowed, 10th-best in the league) is a real strength that runs counter to its overall grade — Washington moving the ball in bulk doesn't automatically mean Washington converts on third down at the rate its overall passing volume might suggest.

**The Verdict:** The Pregame Briefing's broad thesis — two bad defenses, two capable-enough offenses, shootout potential — holds up only partially once the specific levers are examined. The clearest, best-supported edge in this game belongs to Washington's run defense against Jonathan Taylor, which is a real, elite-caliber unit (3rd in the league against backs) facing an Indianapolis offense whose passing success has historically moved together with its rushing success, not against it. That argues for a more competitive, lower-scoring version of this game than the raw defensive rankings alone would suggest — not because Washington's overall defense is good (it isn't, particularly through the air), but because the one unit standing squarely in Indianapolis's best path to offense is genuinely strong. On the other side of the ball, Indianapolis's defense is bad broadly enough, and specifically vulnerable enough in the running-back touchdown zone, that Washington's ground game — Jacory Croskey-Merritt in particular — projects as a real source of production and scoring even without an efficient per-carry profile behind it. The game most likely turns on which team's offense is willing and able to lean on the pass when its preferred path (the run, for Indianapolis; a balanced red-zone approach, for Washington) gets contested — and the deepest uncertainty in that equation, Jayden Daniels's availability, remains genuinely unresolved from this evidence alone.

---

### COEUS CHEAT SHEET

**Team**
- IND: 1-2, 24.0 ppg (15th) / 30.3 ppg allowed (30th)
- WAS: 1-2, 25.0 ppg (14th) / 30.7 ppg allowed (31st)

**Passing**
- Daniel Jones (IND): 203.7 pass yds/gm (own rank 25th team-level), 66.3% comp, 1.0 TD/gm, 1.0 INT/gm
- Jayden Daniels (WAS): 130.0 pass yds/gm (2 games), 56.9% comp, 1.5 TD/gm, 0 INT/gm — availability uncertain
- Marcus Mariota (WAS): 147.0 pass yds/gm (2 games), 63.8% comp, 2.0 TD/gm, 0 INT/gm

**Rushing**
- Jonathan Taylor (IND): 86.0 rush yds/gm (own rank 6th), 79.5% rush share, 4 rush TD
- Jacory Croskey-Merritt (WAS): 47.3 rush yds/gm, 49.0% rush share, 1 rush TD
- QB rushing: not tracked in this evidence package for either quarterback

**Receiving**
- Josh Downs (IND, WR1): 62.0 rec yds/gm, 25.5% target share
- Keenan Allen (IND, WR2): 33.3 rec yds/gm, 21.3% target share
- Tyler Warren (IND, TE1): 29.7 rec yds/gm, 23.4% target share, 92% snap share
- Terry McLaurin (WAS, WR1): 47.0 rec yds/gm, 23.7% target share
- Stefon Diggs (WAS, WR2): 45.0 rec yds/gm, 23.7% target share, 3 red-zone TD on 4 red-zone targets
- Chig Okonkwo (WAS, TE1): 16.0 rec yds in his only game played (Week 1); availability uncertain

**Team Defense**
- IND def: 291.0 pass yds/gm allowed (30th), 140.3 rush yds/gm allowed (29th), no team-level WR/TE receiving-yards-allowed rank cited beyond position splits above
- WAS def: 291.7 pass yds/gm allowed (31st), 82.0 rush yds/gm allowed (3rd)
- IND def vs. WR: 179.3 rec yds/gm allowed (28th) | vs. RB rush: 114.0 yds/gm allowed (27th), 4 rush TD allowed (30th)
- WAS def vs. WR: 191.0 rec yds/gm allowed (30th), 6 WR TD allowed (32nd) | vs. RB rush: 56.0 yds/gm allowed (3rd)
- Man/zone coverage rate: not available in this evidence package for either team

**Down/Distance**
- IND offense: 40.5% third-down conversion (16th) | IND defense: 36.4% allowed (10th)
- WAS offense: 38.1% third-down conversion (18th) | WAS defense: 47.1% allowed (26th)

**Red Zone Play Calling**
- IND offense: 53.6% run (8th) / 46.4% pass (25th)
- WAS offense: 50.0% run (14th) / 50.0% pass (19th)
- IND defense allowed: 45.5% run (19th) / 54.5% pass (14th)
- WAS defense allowed: 39.3% run (25th) / 60.7% pass (9th)

**Head-to-head**
- No meeting between these two teams this season; not a division matchup.

---

EVIDENCE_CHECK
{"claims": [
  {"type": "current_opponent", "team": "IND", "pos": "TEAM", "stat": "ppg", "role": "off", "claimed_rank": 15},
  {"type": "current_opponent", "team": "IND", "pos": "TEAM", "stat": "ppg", "role": "def", "claimed_rank": 30},
  {"type": "current_opponent", "team": "IND", "pos": "TEAM", "stat": "total_ypg", "role": "off", "claimed_rank": 26},
  {"type": "current_opponent", "team": "IND", "pos": "TEAM", "stat": "total_ypg", "role": "def", "claimed_rank": 31},
  {"type": "current_opponent", "team": "IND", "pos": "QB", "stat": "pass_ypg", "role": "off", "claimed_rank": 25},
  {"type": "current_opponent", "team": "IND", "pos": "QB", "stat": "comp_pct", "role": "off", "claimed_rank": 15},
  {"type": "current_opponent", "team": "IND", "pos": "QB", "stat": "pass_td", "role": "off", "claimed_rank": 25},
  {"type": "current_opponent", "team": "IND", "pos": "QB", "stat": "int_pg", "role": "off", "claimed_rank": 24},
  {"type": "current_opponent", "team": "IND", "pos": "RB", "stat": "rush_ypg", "role": "off", "claimed_rank": 15},
  {"type": "current_opponent", "team": "IND", "pos": "TEAM", "stat": "red_zone_run_pct", "role": "off", "claimed_rank": 8},
  {"type": "current_opponent", "team": "IND", "pos": "TEAM", "stat": "red_zone_pass_pct", "role": "off", "claimed_rank": 25},
  {"type": "current_opponent", "team": "IND", "pos": "TEAM", "stat": "third_down_conversion_pct", "role": "off", "claimed_rank": 16},
  {"type": "current_opponent", "team": "WAS", "pos": "TEAM", "stat": "rush_ypg", "role": "def", "claimed_rank": 3},
  {"type": "current_opponent", "team": "WAS", "pos": "RB", "stat": "rush_ypg", "role": "def", "claimed_rank": 3},
  {"type": "current_opponent", "team": "WAS", "pos": "RB", "stat": "fd_pg", "role": "def", "claimed_rank": 1},
  {"type": "current_opponent", "team": "WAS", "pos": "RB", "stat": "rush_td", "role": "def", "claimed_rank": 7},
  {"type": "current_opponent", "team": "WAS", "pos": "TEAM", "stat": "pass_ypg", "role": "def", "claimed_rank": 31},
  {"type": "current_opponent", "team": "WAS", "pos": "QB", "stat": "pass_td", "role": "def", "claimed_rank": 32},
  {"type": "current_opponent", "team": "WAS", "pos": "WR", "stat": "rec_ypg", "role": "def", "claimed_rank": 30},
  {"type": "current_opponent", "team": "WAS", "pos": "WR", "stat": "rec", "role": "def", "claimed_rank": 32},
  {"type": "current_opponent", "team": "WAS", "pos": "WR", "stat": "td", "role": "def", "claimed_rank": 32},
  {"type": "current_opponent", "team": "WAS", "pos": "TE", "stat": "rec_ypg", "role": "def", "claimed_rank": 26},
  {"type": "current_opponent", "team": "WAS", "pos": "TE", "stat": "td", "role": "def", "claimed_rank": 31},
  {"type": "current_opponent", "team": "WAS", "pos": "TE", "stat": "rec", "role": "def", "claimed_rank": 15},
  {"type": "current_opponent", "team": "WAS", "pos": "TEAM", "stat": "third_down_pct_allowed", "role": "def", "claimed_rank": 26},
  {"type": "current_opponent", "team": "WAS", "pos": "TEAM", "stat": "ppg", "role": "off", "claimed_rank": 14},
  {"type": "current_opponent", "team": "WAS", "pos": "RB", "stat": "rush_ypg", "role": "off", "claimed_rank": 8},
  {"type": "current_opponent", "team": "WAS", "pos": "QB", "stat": "pass_ypg", "role": "off", "claimed_rank": 28},
  {"type": "current_opponent", "team": "WAS", "pos": "QB", "stat": "comp_pct", "role": "off", "claimed_rank": 25},
  {"type": "current_opponent", "team": "WAS", "pos": "QB", "stat": "sacks_pg", "role": "off", "claimed_rank": 4},
  {"type": "current_opponent", "team": "WAS", "pos": "QB", "stat": "int_pg", "role": "off", "claimed_rank": 4},
  {"type": "current_opponent", "team": "WAS", "pos": "TEAM", "stat": "third_down_conversion_pct", "role": "off", "claimed_rank": 18},
  {"type": "current_opponent", "team": "WAS", "pos": "TEAM", "stat": "red_zone_run_pct", "role": "off", "claimed_rank": 14},
  {"type": "current_opponent", "team": "WAS", "pos": "TEAM", "stat": "red_zone_pass_pct", "role": "off", "claimed_rank": 19},
  {"type": "current_opponent", "team": "WAS", "pos": "TEAM", "stat": "red_zone_pass_pct_allowed", "role": "def", "claimed_rank": 9},
  {"type": "current_opponent", "team": "WAS", "pos": "TEAM", "stat": "red_zone_run_pct_allowed", "role": "def", "claimed_rank": 25},
  {"type": "current_opponent", "team": "IND", "pos": "TEAM", "stat": "pass_ypg", "role": "def", "claimed_rank": 30},
  {"type": "current_opponent", "team": "IND", "pos": "TEAM", "stat": "rush_ypg", "role": "def", "claimed_rank": 29},
  {"type": "current_opponent", "team": "IND", "pos": "WR", "stat": "ypr", "role": "def", "claimed_rank": 31},
  {"type": "current_opponent", "team": "IND", "pos": "WR", "stat": "yac_pg", "role": "def", "claimed_rank": 29},
  {"type": "current_opponent", "team": "IND", "pos": "QB", "stat": "int_pg", "role": "def", "claimed_rank": 30},
  {"type": "current_opponent", "team": "IND", "pos": "RB", "stat": "rush_td", "role": "def", "claimed_rank": 30},
  {"type": "current_opponent", "team": "IND", "pos": "RB", "stat": "rush_ypg", "role": "def", "claimed_rank": 27},
  {"type": "current_opponent", "team": "IND", "pos": "TEAM", "stat": "third_down_pct_allowed", "role": "def", "claimed_rank": 10},
  {"type": "current_opponent", "team": "IND", "pos": "QB", "stat": "sacks_pg", "role": "def", "claimed_rank": 15},
  {"type": "current_opponent", "team": "WAS", "pos": "QB", "stat": "sacks_pg", "role": "def", "claimed_rank": 25},
  {"type": "current_opponent", "team": "IND", "pos": "WR", "stat": "rec_ypg", "role": "def", "claimed_rank": 28},
  {"type": "log_opponent", "player": "Jonathan Taylor", "week": 2, "stat": "rush_yds", "claimed_rank": 7},
  {"type": "log_opponent", "player": "Jonathan Taylor", "week": 3, "stat": "rush_yds", "claimed_rank": 9},
  {"type": "log_opponent", "player": "Daniel Jones", "week": 2, "stat": "pass_yds", "claimed_rank": 3},
  {"type": "log_opponent", "player": "Terry McLaurin", "week": 3, "stat": "rec_yds", "claimed_rank": 1},
  {"type": "log_opponent", "player": "Stefon Diggs", "week": 3, "stat": "rec_yds", "claimed_rank": 1},
  {"type": "log_opponent", "player": "Josh Downs", "week": 2, "stat": "rec_yds", "claimed_rank": 4}
]}