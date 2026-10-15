# GAME BREAKDOWN: Tennessee Titans @ Indianapolis Colts
### Week 6, 2026 Season | Sunday, October 18, 2026, 1:00 PM ET | Lucas Oil Stadium (Fieldturf)

**EVIDENCE METHODOLOGY NOTE:** Two player-level evidence fields that this Standard normally requires — home/road splits (`home_road_split`, `tier_home_road_split`) and clean 2025 season-final rates (`season_2025`) for players with fewer than three 2026 games — are not present anywhere in this week's evidence package, for either roster. This report therefore cites season-to-date averages and opponent-quality tier splits from each player's game log (which ARE present and are used extensively below) but cannot provide home/road-specific or 2025-carryover context for any player this week. This is a one-time disclosure rather than a per-player repetition. Separately, `cb_db_rankings`, `coverage_qb`/`coverage_wr`/`coverage_te`, `qb_run_vs_pass`, and `team_coverage_rate` are all empty or absent in this evidence package — no individual coverage-grade data and no team man/zone play-calling rate exist for this game, for either team. Where the Standard calls for that material, this report says so plainly rather than estimating it.

---

## 1. PREGAME BRIEFING

Tennessee arrives at 0-5 (LLL) as the league's lowest-scoring offense — 11.6 points per game, ranked 32nd of 32 — despite fielding a defense that has actually been respectable, allowing 21.8 points per game (12th). Indianapolis is 2-3 (WWL) with almost the inverse shape: a functional, top-third scoring offense (24.8 ppg, 11th) paired with a defense that has been genuinely leaky, allowing 27.6 points per game (27th) and 397.6 total yards per game (28th).

This is a division game (AFC South), but the two teams have not yet met this season, and the evidence package contains no prior-season opponent-specific game logs for any player on either roster — there is no real head-to-head history to draw on here beyond the familiarity two division rivals generally carry into a rematch. That absence is itself worth noting for a divisional matchup: neither roster has in-evidence experience against this specific opponent this year.

The broad shape this game profiles toward: Indianapolis's offense, which has already shown it can move the ball against a genuine top-tier defense (30 points against a Kansas City defense ranked 7th in points allowed in Week 2 — more below), should find a reasonable floor against a Tennessee defense that is better than its name suggests in the aggregate but carries a specific, exploitable weakness to wide receivers. Tennessee's offense, meanwhile, has not yet in 2026 faced what would reasonably be classified as a bad defense — its toughest-matchup and middle-tier splits both exist, but Indianapolis's defense would be new territory. Whether that absence of evidence predicts a Tennessee bounce-back or simply reflects a broken offense regardless of opponent is the real question this report works through below.

The single largest swing factor entering the week, however, isn't matchup-shaped at all — it's availability. Both teams' workhorse running backs, Tony Pollard (TEN) and Jonathan Taylor (IND), carry early-week "resting player" practice designations rather than hard injury labels (see Section 2). Both backs account for the clear majority of their team's rushing offense, and this report treats their status as the key swing variable in how this game is actually played, not a footnote.

---

## 2. INJURY & AVAILABILITY REPORT

**Source:** DraftKings-adjacent injury report (`injuries/wk06.json`, nflverse). Every entry below carries a `report_status` of **"Pending"** — meaning no final game designation (Questionable/Doubtful/Out) had been filed as of this evidence freeze (2026-10-15), roughly three days before kickoff. No `manual_updates` exist to override this data. Treat everything below as a mid-week snapshot, not a final word — confidence on all availability calls here is capped at LOW-to-MEDIUM given the "Pending" status.

**Tennessee:**
- **Tony Pollard (RB)** — Listed "Not injury related – resting player," Did Not Participate. This is significant: Pollard carries a 63.0% rush share and 54.5% red-zone touch share for Tennessee's offense. A real absence would hand the backfield to a committee of Tyjae Spears (also limited, see below), Julius Chestnut (0 touches in 3 games this season), Nicholas Singleton (2 games, 6.0 rush ypg), and Kalel Mullings (1 game).
- **Tyjae Spears (RB)** — Knee, Limited Participation. Already the clear passing-down piece behind Pollard (14 receptions on 16 targets, an 87.5% catch rate, but only 13.0 rush ypg on a 15.7% rush share). If Pollard sits, Spears is the most likely early-down/passing-down bridge, knee permitting.
- **John Franklin-Myers (DE)** — Resting, DNP. Depth-chart LDE1; a rest-day absence would lean more snaps to the interior rotation.
- **Amani Hooker (S)** — Concussion, Limited. Starting SS per depth chart.
- **Kevin Winston Jr. (S)** — Quadricep, DNP. Starting FS per depth chart; combined with Hooker's status, Tennessee's starting safety duo is in real question.
- **Marcus Harris (CB)** — Ankle, Limited. Starting nickel (NB) corner per depth chart — relevant given both Indianapolis slot targets (Josh Downs, Tyler Warren) draw heavy slot usage (see Section 4).
- **David Martin-Robinson (TE)** — Hamstring, Limited. Deep depth piece with zero 2026 game appearances (`roster_only`); minimal practical impact.

**Indianapolis:**
- **Jonathan Taylor (RB)** — Listed "Not injury related – resting player," Limited Participation. This is the single most important injury-report line in this game. Taylor carries a 73.7% rush share and a 71.4% red-zone carry share — Indianapolis's run game is built almost entirely around him (5 of his 6 total touchdowns this season are red-zone rushing scores). The clear backup is Seth McGowan (12.4% rush share, 12.2 rush ypg), with DJ Giddens (`roster_only`, zero 2026 games) as a deeper option.
- **Josh Downs (WR)** — Resting, Limited. Indianapolis's leading target-share receiver (20.5%).
- **Keenan Allen (WR)** — Resting, DNP. Allen actually carries the highest target share on the team (21.2%) despite having already missed Week 4 for the same reason — this is a recurring veteran-maintenance pattern, not a new injury, which argues (LOW-MEDIUM confidence) toward him ultimately suiting up.
- **Charvarius Ward (CB)** — Resting, DNP. Indianapolis's starting RCB per depth chart (Sauce Gardner starts opposite him at LCB). A real absence would further stress a defense that is already allowing 159.6 WR receiving yards per game (19th) and 15.1 yards per reception to wide receivers (28th, among the most explosive-prone units in the league).
- **Ashton Dulin (WR)** — Hamstring, DNP. This is a genuine injury rather than a rest designation; Dulin is already a marginal depth piece (12.1% target share across just 2 games).
- **Jaylon Carlies (LB)** — Ribs, DNP. Starting WLB per depth chart.
- **Jalen Travis (T)** — Ankle, DNP. Starting RT per depth chart — a real line concern, though Indianapolis's pass protection (1.8 sacks/gm allowed, 8th-best) has been a team strength to date.
- **Matt Goncalves (G)** — Concussion evaluation, Limited. Starting RG per depth chart.
- **Jaylahn Tuimoloau (DE)** — Concussion evaluation, Limited. Starting LDE per depth chart.

**Net read:** Both lead backs are the swing factor. Everything in Sections 4–7 below that discusses Pollard and Taylor is written conditionally — what happens if each plays, and what happens if each doesn't — rather than assuming either workload is guaranteed.

---

## 3. MATCHUP STATISTICS

### Tennessee Offense
- **Team identity:** 11.6 ppg (32nd), 261.8 total yds/gm (32nd), 179.2 pass yds/gm (31st), 82.6 rush yds/gm (27th), 13.4 first downs/gm (31st).
- **QB group (Cam Ward):** 179.2 pass yds/gm (31st), 63.2% completion (21st), 31.0 attempts/gm (20th), 3 total passing TDs on the season (31st), 9.1 yards/completion (31st), 8.6 first downs/gm via pass (30th), 2.0 sacks taken/gm (13th-most), 0.6 interceptions/gm (17th).
- **RB group:** 70.6 rush yds/gm (25th), 18.6 carries/gm (28th), 18.4 rec yds/gm (28th), 1 total rushing TD all season (32nd — fewest in the NFL), 0 receiving TDs (32nd).
- **WR group:** 142.8 rec yds/gm (17th), 12.4 rec/gm (10th), 18.8 targets/gm (14th), 3 TDs (26th), 11.5 yards/reception (29th).
- **TE group:** 18.0 rec yds/gm (32nd — dead last), 2.8 rec/gm (32nd), 4.2 targets/gm (32nd), 0 TDs (31st), 6.4 yards/reception (32nd). This is the single worst positional group in this report's evidence by raw rank.
- **Down/Distance:** 35.6% third-down conversion rate (24th) on 11.8 attempts/gm; 4th-down go-for-it rate 15.8%, conversion 33.3%.
- **Red Zone Play Calling:** 62.2% run rate in the red zone (5th-most run-heavy), 37.8% pass rate (28th-least). This is a tendency stat, not a quality stat — see Section 4 for why it matters that this heavy run-calling has not translated into results.
- **Contextual Statistics (opponent-quality tiers, team level):** Tennessee has scored just 8.5 ppg against top-tier defenses faced so far (n=2: NYJ, NYG) and 13.7 ppg against mid-tier defenses (n=3: PHI, BAL, HOU). **Tennessee has not yet faced a bottom-tier scoring defense this season (n=0)** — Indianapolis's defense (27.6 ppg allowed, 27th) would be the first.

### Tennessee Defense
- **Team identity:** 21.8 ppg allowed (12th), 342.6 total yds/gm allowed (19th), 228.6 pass yds/gm allowed (14th), 114.0 rush yds/gm allowed (17th), 18.4 first downs/gm allowed (22nd).
- **vs. QB:** 228.6 pass yds/gm allowed (14th), but 74.0% completion rate allowed (31st — very high), 29.2 attempts/gm faced (7th-fewest), only 5 total passing TDs allowed (9th-fewest), 0.4 interceptions forced/gm (27th).
- **vs. RB:** 94.4 rush yds/gm allowed (18th), but 26.0 carries/gm faced (30th-most — teams run against this defense often), 25.6 rec yds/gm allowed to backs (10th-best).
- **vs. WR:** 173.6 rec yds/gm allowed (26th — a real weakness), 13.0 yards/reception allowed (16th).
- **vs. TE:** 29.4 rec yds/gm allowed (3rd-best in the NFL), 6.4 yards/reception allowed (2nd-best). A genuinely elite TE defense.
- **Down/Distance:** 38.5% third-down conversion allowed (15th), 61.5% stop rate; 4th-down stop rate 0.0% (small sample — only 9.5% go-for-it rate faced).
- **Red Zone Play Calling (allowed):** 64.3% run rate allowed (1st — opponents run on Tennessee in the red zone more than against any other defense), 35.7% pass rate allowed (32nd-lowest).
- **Contextual Statistics:** Not available in this week's evidence package (defensive opponent-quality splits are not provided; `team_context` covers offensive production only).

### Indianapolis Offense
- **Team identity:** 24.8 ppg (11th), 305.0 total yds/gm (26th), 204.2 pass yds/gm (23rd), 100.8 rush yds/gm (20th), 18.2 first downs/gm (15th).
- **QB group (Daniel Jones):** 204.2 pass yds/gm (23rd), 61.4% completion (25th), 35.2 attempts/gm (12th), only 3 total passing TDs on the season (30th), 9.5 yards/completion (30th), 1.8 sacks taken/gm (8th-fewest — good protection), 0.8 interceptions/gm (19th).
- **RB group:** 91.8 rush yds/gm (15th), 23.6 carries/gm (13th), 23.2 rec yds/gm (23rd), 6 rushing TDs (6th-best), 0 receiving TDs (24th).
- **WR group:** 131.6 rec yds/gm (23rd), 11.6 rec/gm (13th), 20.2 targets/gm (10th), just 1 TD all season (31st — very low), 11.3 yards/reception (31st).
- **TE group:** 49.4 rec yds/gm (18th), 6.8 rec/gm (8th), 8.4 targets/gm (10th), 2 TDs (16th), 7.3 yards/reception (31st — low per-catch average despite real volume).
- **Down/Distance:** 35.3% third-down conversion rate (25th) on 13.6 attempts/gm; 4th-down go-for-it rate 25.0%, conversion 72.7% — aggressive and successful when they choose to go.
- **Red Zone Play Calling:** 58.3% run rate (7th-most run-heavy), 41.7% pass rate (26th).
- **Contextual Statistics:** Indianapolis's scoring output by opponent tier is genuinely noisy — 30.0 ppg against its one top-tier defensive matchup (Kansas City, Week 2), 21.3 ppg against mid-tier opponents (n=3), and 30.0 ppg against its one bottom-tier matchup (Washington, Week 4). Unlike Tennessee's offense, Indianapolis has already shown it can score against a legitimately elite unit.

### Indianapolis Defense
- **Team identity:** 27.6 ppg allowed (27th), 397.6 total yds/gm allowed (28th), 268.0 pass yds/gm allowed (28th), 129.6 rush yds/gm allowed (27th), 18.4 first downs/gm allowed (21st).
- **vs. QB:** 268.0 pass yds/gm allowed (28th... team-level; position-group figure shows 29th), 62.9% completion rate allowed (12th-best — not bad), but 12.8 yards/completion allowed (30th — very explosive-prone), 0.2 interceptions forced/gm (29th — rarely wins the ball).
- **vs. RB:** 99.6 rush yds/gm allowed (20th), but 52.8 receiving yds/gm allowed to backs (32nd — worst in the NFL), 5 rushing TDs allowed (30th).
- **vs. WR:** 159.6 rec yds/gm allowed (19th), but 15.1 yards/reception allowed (28th — highly explosive-prone).
- **vs. TE:** 53.0 rec yds/gm allowed (18th), 4 TDs allowed (27th — a real weak spot in the end zone).
- **Down/Distance:** 30.5% third-down conversion allowed (4th-best in the NFL), 69.5% stop rate — a genuine strength despite the ugly yardage totals. 4th-down stop rate 50.0% on a 25.0% go-for-it rate faced.
- **Red Zone Play Calling (allowed):** 41.5% run rate allowed (26th), 58.5% pass rate allowed (7th-highest) — opponents choose to attack Indianapolis through the air once inside the 20, consistent with the team's weak WR and TE touchdown-prevention numbers above.
- **Contextual Statistics:** Not available in this week's evidence package.

---

## 4. MATCHUP INTELLIGENCE

### The Red Zone Paradox: Tennessee's Run-Heavy Identity Isn't Working

Tennessee calls running plays on 62.2% of its red-zone snaps (5th-most run-heavy offense in the league) — yet its running backs have combined for exactly **one** rushing touchdown all season (32nd, dead last). This is the clearest illustration of why Tennessee is averaging 11.6 points per game (32nd): the offense's red-zone tendency is run-heavy by design, but that tendency isn't converting into points. This is a tendency stat, not a quality stat, and the distinction matters here specifically — a reader should not read "run-heavy red zone offense" as inherently good or bad, but in this case the surrounding evidence (lowest team scoring in football, lowest RB rushing-TD rate in football) argues this specific identity is failing on execution, not matchup. Confidence: HIGH that the tendency exists as described; MEDIUM on attributing the failure purely to execution rather than opponent quality, since Tennessee hasn't yet faced a bottom-tier defense this season to test whether a softer matchup changes the picture — Indianapolis's defense (27.6 ppg allowed, 27th) would be exactly that test.

Indianapolis, by contrast, is also run-heavy in the red zone (58.3% run rate, 7th-most) — but it's working: Jonathan Taylor has scored 5 of his 6 total touchdowns on red-zone carries (71.4% red-zone carry share, 20 red-zone carries on the season), which is precisely why his real-or-rest status (Section 2) matters so much to this specific game plan. If Taylor sits, Indianapolis's proven red-zone scoring mechanism goes with him; Seth McGowan has yet to score in 2026.

### The Tennessee Defense's Funnel: Elite vs. Tight Ends, Leaky vs. Wide Receivers

Tennessee's pass defense looks solid in the aggregate — 228.6 pass yards per game allowed, ranked 14th — but that number hides a real split. Against tight ends specifically, Tennessee is elite: 29.4 receiving yards per game allowed, ranked 3rd in the NFL, with just 6.4 yards allowed per reception (2nd-best). Against wide receivers, the same defense is a real weakness: 173.6 receiving yards per game allowed, ranked 26th. The overall respectable number is being carried by the TE coverage; the WR coverage is genuinely below average.

This matters immediately for Indianapolis's game plan. Tyler Warren is Indianapolis's most heavily targeted receiver by share (21.7% target share, 36 targets through 5 games, an 83.3% catch rate) and draws real volume both from the slot (44.0% of his snaps) and inline (38.0%) — exactly the role that runs into Tennessee's best unit, not its worst. Indianapolis's own contextual game logs back this up directly: the team's TE production has already shown real sensitivity to defensive quality, dropping to just 13.0 receiving yards in its one game against a top-tier-caliber pass defense this season, compared to an 86.0-yard average against mid-tier units (n=2). Tennessee's TE defense (3rd in the league) sits squarely in that top-tier bracket, which argues Warren's real 42.6 rec yds/gm season average is a poor baseline expectation for this specific matchup — a materially tougher test than his volume alone suggests. Confidence: MEDIUM (the funnel split itself is HIGH-confidence evidence; the specific magnitude of Warren's expected suppression is an inference from a one-game top-tier sample).

Meanwhile, Josh Downs (69.9% slot rate) and Laquon Treadwell (87.1% snap rate outside, 13.5 average depth of target — a vertical, low-volume deep threat) face the unit Tennessee actually struggles to defend. Downs in particular is worth flagging separately below for a specific wrinkle tied to blitz rate.

### Tennessee's Own Wide Receiver Corps Faces the Inverse Setup

The same funnel cuts in Tennessee's favor on the other side of the ball. Indianapolis's defense is a genuine weakness against wide receivers in a different way than Tennessee's — not in total yardage allowed (159.6/gm, 19th, middling) but in explosiveness: 15.1 yards allowed per reception, ranked 28th, among the most big-play-prone units in the league. Tennessee's own receiving corps has shown real sensitivity to exactly this kind of matchup: its contextual game logs show WR production jumping to 163.7 receiving yards per game against bottom-tier defenses faced so far (n=3), compared to just 94.0 yards against its one top-tier matchup and 129.0 against its one mid-tier matchup. Carnell Tate, Tennessee's clear WR1 (25.9% target share, 142.8-yards-per-game team swarm around him), lines up outside on 72.6% of his snaps with a 12.7 average depth of target — a profile built for exactly the explosive-play vulnerability Indianapolis's secondary has shown. This doesn't resolve Tennessee's larger scoring problem (which, per the red-zone discussion above, looks more like a finishing issue than a yardage issue), but it is a specific, real subplot: Tate and Elic Ayomanor (8.6% target share but a team-leading 35.3% red-zone target share and Tennessee's only receiving touchdown producer among the wideouts) both plausibly see a yardage bump against this specific defense even while the broader offense struggles to turn drives into points. Confidence: MEDIUM.

### Running Backs — Entirely Conditional on Availability

**Tennessee:** If Tony Pollard plays, he is the clear bell cow (63.0% rush share, 54.6 rush yds/gm, 52.5% red-zone touch share). His per-carry profile leans more on blocking than individual creation — 2.46 yards before contact per carry against 1.56 yards after contact, with 0.6 broken tackles/gm — meaning his output is more dependent on Tennessee's offensive line creating room than on him creating yardage independently. He faces an Indianapolis run defense that ranks 27th in team rush yards allowed (129.6/gm), a favorable matchup on paper if he's full-go. If Pollard sits, Tyjae Spears (himself limited with a knee issue) is the direct backup but profiles very differently — a 15.7% rush share paired with real receiving usage (14 catches on 16 targets, 87.5%). That receiving profile would run directly into Indianapolis's single worst defensive statistic in this report: 52.8 receiving yards per game allowed to running backs, ranked dead last (32nd) in the NFL. A diminished Tennessee run game could, perversely, open up one of the most favorable individual matchups on this slate for whichever Tennessee back catches passes out of the backfield. Confidence: LOW on which scenario plays out, MEDIUM on the matchup read within either scenario.

**Indianapolis:** If Jonathan Taylor plays, he remains Indianapolis's offense in miniature — a 73.7% rush share, 79.6 rush yds/gm, and the red-zone scoring engine detailed above. He faces a Tennessee run defense ranked a middling 17th in rush yards allowed (94.4/gm) but one that faces a heavy workload (26.0 carries/gm faced, 30th-most) — teams run on Tennessee often, consistent with its WR-funnel weakness pushing some offenses toward the ground instead. If Taylor sits, Seth McGowan becomes the early-down option; his per-carry marks (2.12 yards after contact vs. 1.47 before contact, 0.75 broken tackles/gm) actually suggest more individual juice than Taylor shows, but on a tiny sample (17 carries total) that shouldn't be read as a like-for-like replacement for a 20-carry, 71.4%-red-zone-share workhorse. Confidence: LOW-MEDIUM.

### Blitz Tendencies: Both Teams Rarely Blitz, and Neither Does It Well

Indianapolis blitzes Cam Ward at a 20.5% rate (30th-lowest in the league) with a 44.4% blitz success rate when it does (29th). Ward's own splits don't show real fear of the blitz regardless — he's actually been modestly more efficient against it this season (5.67 yards/play, -0.039 EPA/play on 33 blitzed dropbacks) than against a standard rush (4.77 yards/play, -0.244 EPA/play on 133 dropbacks), though both marks reflect a broadly struggling passing offense. Tennessee's own blitz tendency against Daniel Jones is even more lopsided: a 22.4% blitz rate (29th-lowest) that succeeds just 34.3% of the time — the least successful blitz rate in the NFL. Neither team projects to lean on exotic pressure as a gameplan, and if Tennessee does deviate from its low-blitz identity, the individual risk is concentrated on Josh Downs specifically: Downs has a 70.0% hit rate and a +0.931 EPA/target mark against the blitz this season (10 targets) compared to a 37.5% hit rate and +0.099 EPA/target with no blitz (24 targets) — a real, wide split that argues against Tennessee abandoning restraint against him. Confidence: MEDIUM.

### Coverage Scheme — Not Available This Week

This Standard calls for man/zone coverage context (team coverage rate, individual player man/zone splits, CB/DB coverage grades) in this section. None of that data exists in this week's evidence package: `team_coverage_rate`, `coverage_qb`, `coverage_wr`, `coverage_te`, and `cb_db_rankings` are all empty or absent for both teams. This report cannot make any man-vs-zone claims for this matchup and does not attempt to infer them.

### PFF Slot Matchups

Per PFF slot-coverage data: **Indianapolis's slot defense is the single worst exploitable matchup identified anywhere in this report** — 88.2 slot yards allowed per game (32nd, dead last) and 9.0 yards allowed per slot target (30th) season-to-date, though the most recent 3 games show some improvement (61.0 slot yds/gm, rank 20th; 5.9 yards/target, rank 13th). Tennessee's primary slot weapon, Wan'Dale Robinson, runs 78.1% of his routes from the slot and carries a 21.0% target share — the clearest beneficiary of this specific weakness, even accounting for the recent uptick in Indianapolis's slot performance. Tennessee's own slot defense, by contrast, grades out as a top-third unit (10th in slot yards/gm allowed season-to-date, 13th in yards per slot target; last three games: 13th and 10th respectively) — Indianapolis's primary slot receiver, Josh Downs (69.9% slot rate), and hybrid slot/inline piece Tyler Warren (44.0% slot rate) face a materially tougher individual matchup in that specific alignment than Robinson does on the other side. Confidence: MEDIUM-HIGH given the extremity and consistency of Indianapolis's season-long slot numbers.

---

## 5. THREAT INTELLIGENCE

Football Intel's deterministic Threat Engine evaluates every listed starter by checking whether a player's own season rank in a stat category AND the upcoming opponent's defensive rank in that same category both clear a fixed threshold — the convergence of great individual production and a genuinely weak specific matchup, not either signal in isolation. The three tiers use these exact thresholds (player rank is 1st-best; defense rank is 1st-toughest, so a high defense-rank number means a weak defense): **Nuclear** requires a player ranked top 3 AND an opponent defense ranked 30th-or-worse in that category; **Elite** requires top 5 AND opponent ranked 28th-or-worse; **Standard** requires top 10 AND opponent ranked 23rd-or-worse. A "Double" designation reflects one category meeting both thresholds; "Triple"/"Quadruple" reflect additional categories where at least the player's own side clears the bar.

Football Intel evaluated all ten listed starters for this matchup — Cam Ward, Tony Pollard, Carnell Tate, Wan'Dale Robinson, and Gunnar Helm for Tennessee; Daniel Jones, Jonathan Taylor, Laquon Treadwell, Josh Downs, and Tyler Warren for Indianapolis — against each team's upcoming opponent, and **no Threat designation fired for any player on either side of this game.**

This should be read plainly: it does not mean this matchup lacks real individual edges. Section 4 above documents multiple genuine, evidence-backed advantages (Tennessee's WR corps against Indianapolis's explosive-play-prone secondary, Wan'Dale Robinson against Indianapolis's league-worst slot defense, either team's backup pass-catching back against Indianapolis's RB-receiving funnel). It means none of those specific advantages happened to converge at the exact individual-season-rank-plus-opponent-rank thresholds this deterministic system screens for — most notably because neither Tate nor Robinson individually ranks inside the league's top 10 in receiving production by raw season totals, even though their matchup-specific profile is favorable. Treat Section 4's analysis as the primary source of actionable matchup insight here rather than looking for a Threat-driven angle that the data doesn't support.

---

## 6. HIDDEN INTELLIGENCE & CONTEXTUAL ANALYSIS

**Finding 1: Tennessee's passing and rushing games appear to work as alternatives to each other, not complements — the inverse of the typical "good offense, good in every phase" pattern.** Cross-referencing Cam Ward's game-by-game passing output against Tony Pollard's rushing output shows a counterintuitive relationship: Pollard exceeds his own season rushing average in 40.0% of games where Ward is passing below his own average (n=10), but in only 33.3% of games where Ward is passing above his average (n=9). The same pattern holds from the other direction — Ward's own "hit rate" (exceeding his passing average) is 50.0% in games where Pollard is rushing below his average (n=12), versus just 42.9% when Pollard is rushing above his average (n=7). In other words, Tennessee's two units have not been clicking together this season; when one struggles, the other has modestly more often picked up, rather than both rising or falling together as the Weeks logs show for more cohesive offenses. Context Expansion: this tracks with Tennessee's own team-level contextual splits, which show passing output swinging far more by opponent tier (160.5 pass yds/gm against top-tier defenses vs. 222.0 against its one mid-tier matchup) than rushing output does (57.0 rush yds/gm against its one top-tier matchup vs. 91.7 against mid-tier, n=3) — the passing game is the more volatile, opponent-quality-sensitive unit, and on weeks it's suppressed, the more stable rushing operation appears to pick up relative share, not disappear alongside it. For this specific game, that argues against assuming a poor Cam Ward passing performance against Indianapolis (plausible, given Section 4's funnel discussion doesn't actually favor Tennessee's WRs enough to guarantee volume) would drag Tennessee's run game down with it — if Pollard is available, his workload may hold up even in a stalled-passing script. Confidence: LOW (the underlying samples are 7–12 games each, genuinely thin), but this is a real, non-obvious contradiction of the more intuitive "bad passing game means bad overall offense" assumption, not a restatement of either stat alone.

**Finding 2: Indianapolis's defense is quietly one of the best third-down units in football, which sits in direct tension with its otherwise poor overall numbers — and this tension specifically works against Tennessee's own already-weak third-down offense.** Indianapolis's defense ranks 28th in total yards allowed and 27th in points allowed, numbers that read as a bad defense across the board. But its third-down conversion rate allowed is just 30.5%, ranked 4th-best in the NFL (69.5% stop rate) — a defense that bends for long gains between downs but has been unusually good at ending drives on third down specifically. Tennessee's offense, meanwhile, converts just 35.6% of its own third downs (24th) — already below average independent of opponent. Layering these together: Tennessee's offense, which already struggles on third down in general, is walking into one of the single hardest third-down environments in the league this week, a tougher specific test than its overall ranking against Indianapolis's defense (28th in yardage, suggesting an easy week) would otherwise imply. Context Expansion: Tennessee's own contextual splits don't carry a third-down-specific breakdown by opponent tier, but the team's broader point-scoring splits reinforce the same read — Tennessee's offense has already shown its efficiency metrics (not just raw yardage) degrade against stronger underlying units even when the raw yardage allowed by that unit doesn't look imposing on paper, exactly the gap Indianapolis's defense represents here. Confidence: MEDIUM.

**Finding 3: Indianapolis's own defensive red-zone tendency (opponents pass against it far more often than they run) is a mismatch against the one Tennessee unit built to counteract it.** Indianapolis allows opponents to pass on 58.5% of red-zone plays against it (7th-highest in the league) rather than run — consistent with the defense's weak WR/TE touchdown prevention (TE touchdowns allowed ranked 27th). Yet Tennessee's own offense is specifically red-zone pass-averse, calling pass plays on just 37.8% of its red-zone snaps (28th-least) — the one offensive unit in this game least inclined to exploit the exact red-zone vulnerability Indianapolis's defense is showing. This is a real mismatch of identity rather than ability: Tennessee's red-zone approach (run-heavy, and per Finding 1 above, already non-productive) is not shaped to attack the part of Indianapolis's defense that is actually struggling. Confidence: MEDIUM-LOW (this is an inference from two tendency stats rather than a directly measured outcome, and Tennessee's red-zone play-calling could reasonably shift given the opponent).

---

## 7. COEUS FINAL READ

**Keys to the Game:**

- **If Tony Pollard and Jonathan Taylor both play**, this becomes a more conventional matchup of competent-if-unspectacular run games against defenses that are each vulnerable in different specific ways — Taylor into a middling Tennessee run defense that nonetheless faces heavy rushing volume, Pollard into a bottom-tier (27th) Indianapolis run defense. **If either sits**, the backup profile (Spears's receiving role against Indianapolis's league-worst RB-receiving defense; McGowan's higher per-touch efficiency on a tiny sample) changes the expected shape of that team's offense more than a simple downgrade would suggest.
- **If Tennessee's passing game struggles against Indianapolis's elite third-down defense** (Finding 2) **the way its own third-down profile already suggests it might**, expect a low-possession, field-position-driven game that favors whichever defense wins more individual explosive-play battles — which, given Indianapolis's leaky WR/TE touchdown defense, could still produce scoring for Indianapolis even in a game Tennessee's defense otherwise controls on paper.
- **If Tyler Warren sees his normal 20%-plus target share** against the one Tennessee unit built to stop him (3rd-ranked TE defense), that volume may not translate to his season-average production — watch whether Indianapolis adjusts by funneling more early targets to Josh Downs and Laquon Treadwell, who face Tennessee's real weakness instead.

**The Verdict:** The structural case for Indianapolis is real but incomplete — a top-third scoring offense against a defense that, while statistically respectable overall, has a genuine, two-sided hole against wide receivers that both teams can plausibly exploit, not just Indianapolis. Tennessee's season-long offensive floor (worst scoring offense in football, a red-zone approach that isn't converting, and a passing game that has shown real sensitivity to defensive quality) argues this remains an uphill climb regardless of matchup, but this is also the first genuinely bottom-tier defense Tennessee's offense has faced all season — the first real data point on whether its struggles are purely self-inflicted or partly opponent-driven. The swing variable that could reshape either team's approach more than any scheme note above is the Pollard/Taylor availability picture, which remained unresolved as of this evidence freeze. Confidence in a Indianapolis advantage on paper: MEDIUM. Confidence in exactly how competitive the game is: LOW, given how much hinges on information not yet finalized.

### COEUS CHEAT SHEET

**Team**
- TEN: 0-5 (LLL) | 11.6 ppg (32nd) / 21.8 ppg allowed (12th)
- IND: 2-3 (WWL) | 24.8 ppg (11th) / 27.6 ppg allowed (27th)

**Passing**
- Cam Ward (TEN): 179.2 pass yds/gm (31st), 3 pass TD (31st), 0.6 INT/gm (17th) — vs. IND pass D: 268.0 yds/gm allowed (28th)
- Daniel Jones (IND): 204.2 pass yds/gm (23rd), 3 pass TD (30th), 0.8 INT/gm (19th) — vs. TEN pass D: 228.6 yds/gm allowed (14th)

**Rushing**
- Tony Pollard (TEN, resting/DNP – availability uncertain): 54.6 rush yds/gm, 63.0% rush share, 1 rush TD (team total ranks 32nd) — vs. IND rush D: 129.6 yds/gm allowed (27th)
- Jonathan Taylor (IND, resting/Limited – availability uncertain): 79.6 rush yds/gm, 73.7% rush share, 6 rush TD (team total ranks 6th) — vs. TEN rush D: 114.0 yds/gm allowed (17th)
- Cam Ward rushing: 59 yds / 11.8 ypg over 5 games (secondary role)
- Daniel Jones rushing: 25 yds / 5.0 ypg over 5 games (secondary role)

**Receiving**
- Carnell Tate (TEN, WR): 54.8 rec yds/gm, 25.9% target share — vs. IND WR D: 159.6 yds/gm allowed (19th)
- Wan'Dale Robinson (TEN, WR): 35.2 rec yds/gm, 21.0% target share — vs. IND WR D: 159.6 yds/gm allowed (19th)
- Gunnar Helm (TEN, TE): 12.0 rec yds/gm, 9.1% target share — vs. IND TE D: 53.0 yds/gm allowed (18th)
- Josh Downs (IND, WR): 49.8 rec yds/gm, 20.5% target share — vs. TEN WR D: 173.6 yds/gm allowed (26th)
- Keenan Allen (IND, WR, resting/DNP): 36.25 rec yds/gm, 21.2% target share — vs. TEN WR D: 173.6 yds/gm allowed (26th)
- Tyler Warren (IND, TE): 42.6 rec yds/gm, 21.7% target share — vs. TEN TE D: 29.4 yds/gm allowed (3rd)

**Team Defense**
- TEN D: Pass 228.6 yds/gm allowed (14th) | Rush 114.0 yds/gm allowed (17th) | WR rec 173.6 yds/gm allowed (26th) | TE rec 29.4 yds/gm allowed (3rd) | Coverage rate (man%/zone%): not available in evidence
- IND D: Pass 268.0 yds/gm allowed (28th) | Rush 129.6 yds/gm allowed (27th) | WR rec 159.6 yds/gm allowed (19th) | TE rec 53.0 yds/gm allowed (18th) | Coverage rate (man%/zone%): not available in evidence

**Down/Distance**
- TEN offense: 35.6% third-down conv. (24th) | TEN defense: 38.5% third-down allowed (15th)
- IND offense: 35.3% third-down conv. (25th) | IND defense: 30.5% third-down allowed (4th)

**Red Zone Play Calling**
- TEN offense: 62.2% run / 37.8% pass (run rank 5th) | TEN defense allowed: 64.3% run / 35.7% pass (run-allowed rank 1st)
- IND offense: 58.3% run / 41.7% pass (run rank 7th) | IND defense allowed: 41.5% run / 58.5% pass (pass-allowed rank 7th)

**Head-to-head**
- No meeting between these two teams yet in 2026; no prior-season opponent-specific player data available in evidence. First matchup of the season.

---

EVIDENCE_CHECK
{"claims": [
{"type":"current_opponent","team":"TEN","pos":"team_off","stat":"ppg","role":"off","claimed_rank":32},
{"type":"current_opponent","team":"TEN","pos":"team_def","stat":"ppg","role":"def","claimed_rank":12},
{"type":"current_opponent","team":"IND","pos":"team_off","stat":"ppg","role":"off","claimed_rank":11},
{"type":"current_opponent","team":"IND","pos":"team_def","stat":"ppg","role":"def","claimed_rank":27},
{"type":"current_opponent","team":"IND","pos":"team_def","stat":"total_ypg","role":"def","claimed_rank":28},
{"type":"current_opponent","team":"TEN","pos":"QB","stat":"pass_ypg","role":"off","claimed_rank":31},
{"type":"current_opponent","team":"TEN","pos":"QB","stat":"comp_pct","role":"off","claimed_rank":21},
{"type":"current_opponent","team":"TEN","pos":"QB","stat":"att_pg","role":"off","claimed_rank":20},
{"type":"current_opponent","team":"TEN","pos":"QB","stat":"pass_td","role":"off","claimed_rank":31},
{"type":"current_opponent","team":"TEN","pos":"QB","stat":"ypc","role":"off","claimed_rank":31},
{"type":"current_opponent","team":"TEN","pos":"QB","stat":"fd_pg","role":"off","claimed_rank":30},
{"type":"current_opponent","team":"TEN","pos":"QB","stat":"sacks_pg","role":"off","claimed_rank":13},
{"type":"current_opponent","team":"TEN","pos":"QB","stat":"int_pg","role":"off","claimed_rank":17},
{"type":"current_opponent","team":"TEN","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":25},
{"type":"current_opponent","team":"TEN","pos":"RB","stat":"car_pg","role":"off","claimed_rank":28},
{"type":"current_opponent","team":"TEN","pos":"RB","stat":"rec_ypg","role":"off","claimed_rank":28},
{"type":"current_opponent","team":"TEN","pos":"RB","stat":"rush_td","role":"off","claimed_rank":32},
{"type":"current_opponent","team":"TEN","pos":"RB","stat":"rec_td","role":"off","claimed_rank":32},
{"type":"current_opponent","team":"TEN","pos":"WR","stat":"rec_ypg","role":"off","claimed_rank":17},
{"type":"current_opponent","team":"TEN","pos":"WR","stat":"rec_pg","role":"off","claimed_rank":10},
{"type":"current_opponent","team":"TEN","pos":"WR","stat":"tgt_pg","role":"off","claimed_rank":14},
{"type":"current_opponent","team":"TEN","pos":"WR","stat":"td","role":"off","claimed_rank":26},
{"type":"current_opponent","team":"TEN","pos":"WR","stat":"ypr","role":"off","claimed_rank":29},
{"type":"current_opponent","team":"TEN","pos":"TE","stat":"rec_ypg","role":"off","claimed_rank":32},
{"type":"current_opponent","team":"TEN","pos":"TE","stat":"rec_pg","role":"off","claimed_rank":32},
{"type":"current_opponent","team":"TEN","pos":"TE","stat":"tgt_pg","role":"off","claimed_rank":32},
{"type":"current_opponent","team":"TEN","pos":"TE","stat":"td","role":"off","claimed_rank":31},
{"type":"current_opponent","team":"TEN","pos":"TE","stat":"ypr","role":"off","claimed_rank":32},
{"type":"current_opponent","team":"TEN","pos":"off","stat":"third_down_pct","role":"off","claimed_rank":24},
{"type":"current_opponent","team":"TEN","pos":"off","stat":"red_zone_run_pct","role":"off","claimed_rank":5},
{"type":"current_opponent","team":"TEN","pos":"off","stat":"red_zone_pass_pct","role":"off","claimed_rank":28},
{"type":"current_opponent","team":"TEN","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":14},
{"type":"current_opponent","team":"TEN","pos":"QB","stat":"comp_pct","role":"def","claimed_rank":31},
{"type":"current_opponent","team":"TEN","pos":"QB","stat":"att_pg","role":"def","claimed_rank":7},
{"type":"current_opponent","team":"TEN","pos":"QB","stat":"pass_td","role":"def","claimed_rank":9},
{"type":"current_opponent","team":"TEN","pos":"QB","stat":"int_pg","role":"def","claimed_rank":27},
{"type":"current_opponent","team":"TEN","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":18},
{"type":"current_opponent","team":"TEN","pos":"RB","stat":"car_pg","role":"def","claimed_rank":30},
{"type":"current_opponent","team":"TEN","pos":"RB","stat":"rec_ypg","role":"def","claimed_rank":10},
{"type":"current_opponent","team":"TEN","pos":"WR","stat":"rec_ypg","role":"def","claimed_rank":26},
{"type":"current_opponent","team":"TEN","pos":"WR","stat":"ypr","role":"def","claimed_rank":16},
{"type":"current_opponent","team":"TEN","pos":"TE","stat":"rec_ypg","role":"def","claimed_rank":3},
{"type":"current_opponent","team":"TEN","pos":"TE","stat":"ypr","role":"def","claimed_rank":2},
{"type":"current_opponent","team":"TEN","pos":"def","stat":"third_down_pct_allowed","role":"def","claimed_rank":15},
{"type":"current_opponent","team":"TEN","pos":"def","stat":"red_zone_run_pct_allowed","role":"def","claimed_rank":1},
{"type":"current_opponent","team":"TEN","pos":"def","stat":"red_zone_pass_pct_allowed","role":"def","claimed_rank":32},
{"type":"current_opponent","team":"IND","pos":"QB","stat":"pass_ypg","role":"off","claimed_rank":23},
{"type":"current_opponent","team":"IND","pos":"QB","stat":"comp_pct","role":"off","claimed_rank":25},
{"type":"current_opponent","team":"IND","pos":"QB","stat":"att_pg","role":"off","claimed_rank":12},
{"type":"current_opponent","team":"IND","pos":"QB","stat":"pass_td","role":"off","claimed_rank":30},
{"type":"current_opponent","team":"IND","pos":"QB","stat":"ypc","role":"off","claimed_rank":30},
{"type":"current_opponent","team":"IND","pos":"QB","stat":"sacks_pg","role":"off","claimed_rank":8},
{"type":"current_opponent","team":"IND","pos":"QB","stat":"int_pg","role":"off","claimed_rank":19},
{"type":"current_opponent","team":"IND","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":15},
{"type":"current_opponent","team":"IND","pos":"RB","stat":"car_pg","role":"off","claimed_rank":13},
{"type":"current_opponent","team":"IND","pos":"RB","stat":"rec_ypg","role":"off","claimed_rank":23},
{"type":"current_opponent","team":"IND","pos":"RB","stat":"rush_td","role":"off","claimed_rank":6},
{"type":"current_opponent","team":"IND","pos":"WR","stat":"rec_ypg","role":"off","claimed_rank":23},
{"type":"current_opponent","team":"IND","pos":"WR","stat":"tgt_pg","role":"off","claimed_rank":10},
{"type":"current_opponent","team":"IND","pos":"WR","stat":"td","role":"off","claimed_rank":31},
{"type":"current_opponent","team":"IND","pos":"WR","stat":"ypr","role":"off","claimed_rank":31},
{"type":"current_opponent","team":"IND","pos":"TE","stat":"rec_ypg","role":"off","claimed_rank":18},
{"type":"current_opponent","team":"IND","pos":"TE","stat":"rec_pg","role":"off","claimed_rank":8},
{"type":"current_opponent","team":"IND","pos":"TE","stat":"tgt_pg","role":"off","claimed_rank":10},
{"type":"current_opponent","team":"IND","pos":"TE","stat":"ypr","role":"off","claimed_rank":31},
{"type":"current_opponent","team":"IND","pos":"off","stat":"third_down_pct","role":"off","claimed_rank":25},
{"type":"current_opponent","team":"IND","pos":"off","stat":"red_zone_run_pct","role":"off","claimed_rank":7},
{"type":"current_opponent","team":"IND","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":28},
{"type":"current_opponent","team":"IND","pos":"QB","stat":"comp_pct","role":"def","claimed_rank":12},
{"type":"current_opponent","team":"IND","pos":"QB","stat":"ypc","role":"def","claimed_rank":30},
{"type":"current_opponent","team":"IND","pos":"QB","stat":"int_pg","role":"def","claimed_rank":29},
{"type":"current_opponent","team":"IND","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":27},
{"type":"current_opponent","team":"IND","pos":"RB","stat":"rec_ypg","role":"def","claimed_rank":32},
{"type":"current_opponent","team":"IND","pos":"RB","stat":"rush_td","role":"def","claimed_rank":30},
{"type":"current_opponent","team":"IND","pos":"WR","stat":"rec_ypg","role":"def","claimed_rank":19},
{"type":"current_opponent","team":"IND","pos":"WR","stat":"ypr","role":"def","claimed_rank":28},
{"type":"current_opponent","team":"IND","pos":"TE","stat":"rec_ypg","role":"def","claimed_rank":18},
{"type":"current_opponent","team":"IND","pos":"TE","stat":"td","role":"def","claimed_rank":27},
{"type":"current_opponent","team":"IND","pos":"def","stat":"third_down_pct_allowed","role":"def","claimed_rank":4},
{"type":"current_opponent","team":"IND","pos":"def","stat":"red_zone_run_pct_allowed","role":"def","claimed_rank":26},
{"type":"current_opponent","team":"IND","pos":"def","stat":"red_zone_pass_pct_allowed","role":"def","claimed_rank":7},
{"type":"current_opponent","team":"TEN","pos":"WR","stat":"slot_yards_pg","role":"def","claimed_rank":10},
{"type":"current_opponent","team":"TEN","pos":"WR","stat":"slot_yards_per_target","role":"def","claimed_rank":13},
{"type":"current_opponent","team":"IND","pos":"WR","stat":"slot_yards_pg","role":"def","claimed_rank":32},
{"type":"current_opponent","team":"IND","pos":"WR","stat":"slot_yards_per_target","role":"def","claimed_rank":30},
{"type":"current_opponent","team":"TEN","pos":"QB","stat":"blitz_success_rate","role":"def","claimed_rank":29},
{"type":"current_opponent","team":"IND","pos":"QB","stat":"blitz_success_rate","role":"def","claimed_rank":32}
]}