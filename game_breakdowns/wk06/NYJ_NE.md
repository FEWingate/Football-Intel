# GAME BREAKDOWN: New York Jets @ New England Patriots
### Week 6, 2026 Season | Sunday, October 18, 2026, 1:00 PM ET | Gillette Stadium (outdoors, fieldturf)

**Evidence notes before beginning:** This week's evidence package does not include several optional fields the Game Breakdown Standard calls for when available: `team_coverage_rate` (defensive man/zone play-calling rate), `home_road_split`/`tier_home_road_split` (player home-or-road production), `season_2025` (prior-season baseline for thin-sample players), `rank_shifts` (2025-vs-2026 team trend data), and `cb_db_rankings`/`coverage_qb`/`coverage_wr`/`coverage_te` (man/zone performance splits — all returned empty). DFS evidence is also explicitly marked unavailable (`dfs.available: false`). None of these gaps are treated as license to estimate — they are simply not cited below. Weather/forecast data is likewise absent from the evidence package; conditions are not discussed beyond noting this is an outdoor, fieldturf game in mid-October New England. Where a stat is genuinely unavailable, this report says so rather than filling the gap.

---

## 1. PREGAME BRIEFING

New York (2-3, LLW) visits New England (3-2, LWW) in an AFC East divisional meeting (`div_game: true`), the first time these two teams have played each other this season — neither team's weekly log (Weeks 1-5) shows a prior matchup, so there is no head-to-head recap to offer, and no individual player on either roster has a logged game against this specific opponent this season. That absence is itself notable for a division game: whatever happens here will be first-hand data for every player involved, not a repeat of a form line already established against each other.

Both teams arrive with genuinely unusual splits between their offensive and defensive performance. New York's offense ranks in the bottom third of the league in scoring (18.6 points per game, 28th) and total yardage (310.8 yards per game, 25th), but its defense is comfortably top-10 across the board — 6th in points allowed (19.2/game), 7th in total yards allowed (313.4/game), and 4th in pass yards allowed (195.4/game). New England's profile runs the opposite direction in degree if not in kind: an offense that is middle-of-the-pack in scoring (22.0 points per game, 20th) but genuinely productive in yardage (382.0 total yards per game, 8th), paired with a defense that is also top-10 across the board — 4th in points allowed (18.8/game), 6th in total yards allowed (313.4/game), 6th against the run (90.8 rush yards/game allowed).

The broad shape this points toward is a defense-forward, lower-scoring divisional game than either team's full-season averages might suggest in isolation — both units on both sides of the ball are better at preventing production than creating it, and (as detailed in Hidden Intelligence & Contextual Analysis below) both offenses have specific, data-backed histories of struggling against exactly the caliber of defense they're each facing this week. That is a thesis to test against the deeper matchup work below, not a final verdict — New England is also dealing with a genuinely leaky turnover profile at quarterback that could override any defensive stalemate on its own.

---

## 2. INJURY & AVAILABILITY REPORT

**Source:** DraftKings-style injury report (`injuries/wk06.json`, nflverse injury reports) — every player below carries a `report_status` of **"Pending,"** meaning no final game-status designation (Out/Doubtful/Questionable) had been filed as of this evidence freeze. `manual_updates` (which would override this feed if present and more current) is empty, so practice participation level is the best available signal of real availability.

**New York Jets:**
- **Breece Hall (RB) — DNP (Did Not Participate), Quadricep.** Significant. Hall is listed as New York's RB1 on the official depth chart (as of 2026-10-15), but has already missed Weeks 4-5 of this season and now returns to a full non-participation practice session with the same type of lower-body injury. See the Current Starter note in the Running Backs section below — this is a real, unresolved availability question, not a formality.
- **Adonai Mitchell (WR) — DNP, Finger.** Mitchell has emerged as a real secondary target (7.5 targets/game, 25.4% target share over his two games played) since arriving; a DNP is a real red flag for his snaps this week.
- **Kenyon Sadiq (TE) — Limited, Concussion.** Sadiq is New York's most-used slot tight end by PFF snap data (below) and leads the position room in targets; concussion protocol status bears watching through the week.
- **Omar Cooper Jr. (WR) — Limited, Ankle.** Minimal statistical role to date (1 game, 1 catch).
- **Joseph Ossai (DE) — DNP, Ankle.** A rotational pass rusher; his absence would be a modest subtraction from New York's already middling team sack rate context on the defensive side (not separately broken out in this evidence package).
- **Dylan Parham (G) — DNP, Knee.** Offensive line depth piece.
- **Dane Belton (S) — Limited, Knee.** Starting safety per the depth chart (`SS`, Base 4-3).

**New England Patriots:**
- **TreVeyon Henderson (RB) — Limited, Ankle.** Henderson is part of a genuine committee with Rhamondre Stevenson (see Running Backs section); a limited practice is worth tracking but not yet disqualifying.
- **A.J. Brown (WR) — Limited, Ankle.** Brown has appeared in only one game for New England this season (Week 1: 3 catches, 26 yards on 4 targets, 12.9% target share) — his specific role is still a thin sample even before factoring in the ankle issue.
- **Christian Gonzalez (CB) — Limited, Shoulder.** New England's RCB1 per the depth chart. If limited in coverage reps, this directly affects how New England can match up against Garrett Wilson (see Matchup Intelligence).
- **Carlton Davis III (CB) — DNP, Neck.** New England's LCB1 per the depth chart — a DNP for the starting boundary corner opposite Gonzalez is a meaningful secondary-health flag heading into a game against New York's most heavily targeted receiver.
- **Marcus Jones (CB) — Limited, Ankle.** New England's nickel/slot corner (NB) per the depth chart — relevant given New York's slot usage patterns (PFF section below).
- **Will Campbell (LT) — Limited, Knee** and **Morgan Moses (RT) — Limited, Foot.** Both starting tackles limited in practice; worth monitoring given Drake Maye's already-elevated sack rate exposure (see Quarterbacks).
- **Kevin Byard (S), Dre'Mont Jones (LB), Christian Elliss (LB), Craig Woodson (S), Marcus Bryant (T), Karon Prunty (CB), Channing Canada (CB)** — all limited or DNP; depth-level concerns without starter-level statistical profiles in this evidence package.

No weather or additional non-DraftKings-style injury source was available in the evidence package for this game.

---

## 3. MATCHUP STATISTICS

### New York Jets Offense
- **Team identity:** 18.6 points/game (28th), 310.8 total yards/game (25th), 15.4 first downs/game (25th).
- **Quarterback (Geno Smith):** 216.8 pass yards/game (20th), 69.4% completion rate (3rd in the NFL), 6 passing touchdowns on the season (24th), 3.2 sacks taken per game (29th — one of the league's most-pressured passers by raw sack rate), and remarkably just 0.0 interceptions per game (3rd-best protection of the football in the league).
- **Running back group:** 81.4 rush yards/game (21st), 26.0 receiving yards/game (18th), 3 rushing touchdowns (19th).
- **Wide receiver group:** 141.4 receiving yards/game (19th), 4 touchdowns (19th).
- **Tight end group:** 49.4 receiving yards/game (19th), 2 touchdowns (21st).
- **Third down:** 35.8% conversion rate (23rd) on 13.4 attempts/game. **Red zone play-calling:** 45.5% run (19th) / 54.5% pass (14th) on 6.6 red-zone plays/game — a roughly balanced red-zone identity.
- **Contextual Statistics (team_context, offensive tier splits):** New York's scoring output has varied significantly by opponent defensive quality this season — 12.0 points/game against top-tier defenses (n=1), 19.0 against mid-tier (n=3), 24.0 against bottom-tier (n=1). Passing yardage splits are noisier and partly garbage-time-driven (see Hidden Intelligence).

### New York Jets Defense
- **Team identity:** 19.2 points/game allowed (6th), 313.4 total yards/game allowed (7th), 16.2 first downs/game allowed (8th).
- **Vs. quarterback:** 195.4 pass yards/game allowed (4th), 62.5% completion rate allowed (10th), 3.4 sacks/game generated (5th) — but only 0.2 interceptions/game forced (31st of 32, nearly the worst takeaway rate at the position in the league).
- **Vs. running back:** 102.2 rush yards/game allowed (25th), 4 rushing touchdowns allowed (26th), 2 receiving touchdowns allowed to backs (29th) — a real soft spot specifically in touchdowns allowed to the position, despite otherwise strong team defense.
- **Vs. wide receiver:** 130.4 receiving yards/game allowed (9th), 4 touchdowns allowed (12th).
- **Vs. tight end:** 36.6 receiving yards/game allowed (7th), 0 touchdowns allowed (5th).
- **Third down:** 33.9% conversion rate allowed (8th), 66.1% stop rate, on 12.4 attempts faced/game. **Red zone play-calling allowed:** 53.7% run (10th) / 46.3% pass (24th) on 10.8 red-zone plays faced/game — New York's defense faces a rushing-leaning mix of red-zone plays relative to the league.
- **Contextual Statistics:** Not available in this week's evidence package (team_context carries offensive splits only).

### New England Patriots Offense
- **Team identity:** 22.0 points/game (20th), 382.0 total yards/game (8th), 18.6 first downs/game (12th).
- **Quarterback (Drake Maye, plus limited Tommy DeVito relief):** The position group combined for 251.6 pass yards/game (11th); Maye individually has thrown for 245.6 yards/game across his 5 starts, 65.4% completion (16th, team figure), 8 passing touchdowns (17th), 2.2 sacks/game (18th), and 1.4 interceptions/game — **32nd and worst in the league** at protecting the football.
- **Running back group:** 94.2 rush yards/game (13th), 32.4 receiving yards/game (15th), 3 rushing touchdowns (18th).
- **Wide receiver group:** 166.8 receiving yards/game (10th), 6 touchdowns (8th).
- **Tight end group:** 55.6 receiving yards/game (17th), 2 touchdowns (20th).
- **Third down:** 37.5% conversion rate (20th) on 12.8 attempts/game. **Red zone play-calling:** 32.5% run (31st — nearly the most pass-dependent red-zone offense in football) / 67.5% pass (2nd) on 8.0 red-zone plays/game — this is a real offensive identity, not noise.
- **Contextual Statistics:** New England's scoring has swung enormously by opponent quality — just **8.0 points/game against top-tier defenses (n=2: 10 vs. Seattle, 6 vs. Jacksonville)**, 20.0 against mid-tier (n=1), and **37.0 against bottom-tier (n=2: 29 vs. Buffalo, 45 vs. Las Vegas)**. Passing touchdown production shows the same shape: 0.0 TD/game against top-tier defenses (n=2) climbing to 3.5 TD/game against bottom-tier (n=2). (Full discussion and Context Expansion in Hidden Intelligence, Finding 1.)

### New England Patriots Defense
- **Team identity:** 18.8 points/game allowed (4th), 313.4 total yards/game allowed (6th), 15.4 first downs/game allowed (5th).
- **Vs. quarterback:** 222.6 pass yards/game allowed (10th), 66.0% completion rate allowed (24th), 2.2 sacks/game generated (16th), 0.6 interceptions/game forced (21st).
- **Vs. running back:** 79.8 rush yards/game allowed (9th — a genuinely strong run defense), but 40.0 receiving yards/game allowed to backs (27th) and 4 rushing touchdowns allowed (25th); 0 receiving touchdowns allowed to backs (13th).
- **Vs. wide receiver:** 137.6 receiving yards/game allowed (13th), 5 touchdowns allowed (23rd).
- **Vs. tight end:** 45.0 receiving yards/game allowed (11th), 1 touchdown allowed (11th).
- **Third down:** 38.3% conversion rate allowed (13th), 61.7% stop rate, on 12.0 attempts faced/game. **Red zone play-calling allowed:** 45.7% run (20th) / 54.3% pass (12th) on 9.2 red-zone plays faced/game.
- **Contextual Statistics:** Not available in this week's evidence package.

---

## 4. MATCHUP INTELLIGENCE

*Note on home/road and 2025-baseline citations: this week's evidence package does not include `home_road_split`/`tier_home_road_split` data for any player, nor `season_2025` baselines. Season averages and the tiered opponent-quality splits that ARE present are used below in their place; thin-sample players are flagged as such without a 2025 comparison point, per the evidence actually provided.*

### Quarterbacks

**Geno Smith (NYJ).** Smith's defining trait this season is accuracy without big-play explosiveness or risk: 69.4% completion (3rd in the league) and a perfect 0.0 interceptions/game (3rd), but only 216.8 pass yards/game (20th) and 6 total touchdowns (24th) across 5 starts. His week-to-week tier splits show real swings tied to opponent quality but not always in the expected direction — he threw for 247 yards against Green Bay's defense, which ranked 7th against the pass that week (a "top" tier matchup, and his best per-attempt week), but also piled up 321 yards against Detroit's 32nd-ranked pass defense in Week 3 (a blowout loss, 24-31, where volume likely inflated the total). He is taking a brutal amount of pressure (3.2 sacks/game, 29th), which matters directly against a Patriots pass rush that, while only middling by raw sack rate (2.2/game, 16th), blitzes at a notably high 38.4% rate (7th-most in the league) with modest success (55.9% success rate on blitzes, 18th). Confidence: MEDIUM — the accuracy profile is stable across 5 starts, but the touchdown/explosive-play ceiling looks genuinely capped.

**Drake Maye (NE), or Tommy DeVito if Maye is unavailable.** Maye is not listed on the injury report and projects as the starter; this is not a Questionable-status situation, but the distinction matters because DeVito's single relief appearance this season (Week 3 vs. Jacksonville, 30 yards on 5 attempts in mop-up duty of a 6-35 blowout) offers essentially no read on what a DeVito start would look like. Maye himself is a study in contrasts: 245.6 pass yards/game (team figure 251.6 including DeVit's relief snap, 11th), a respectable 65.4% completion rate (16th), 8 touchdowns (17th) — but a league-worst 1.4 interceptions/game (32nd of 32). His tiered splits are stark and directly relevant this week: against the two "top" pass-defense matchups he's faced this season (Seattle, 2nd-ranked pass defense that week; Jacksonville, which ironically ranked 30th that week but came with a 6-35 blowout script that cut his volume) he's averaged far less explosive production than against bottom-tier defenses, where he's thrown for an average of 280.7 yards/game (n=3) including a 374-yard, 4-touchdown outburst against Las Vegas in Week 5. New York's pass defense (4th in yards allowed, 10th in the yardage-allowed figure specific to Maye's position group) sits in exactly the range of competition that has previously suppressed him. Confidence: MEDIUM-HIGH on the directional read (multiple independent signals — team scoring splits, his own TD/yardage splits, and a historically bad interception rate — all point the same way), though sample sizes in the extreme tiers remain small (n=1-2 games).

### Running Backs

**New York Jets — a genuine starter question.** New York's official depth chart (as of 2026-10-15) lists **Breece Hall** at RB1, but Hall has played in only 3 of New York's 5 games this season (missing Weeks 4-5) and is now listed as a full non-participant in practice this week with a quadriceps injury — the same type of injury that likely cost him the two prior missed games. In his absence, **Braelon Allen** has taken over as the clear lead back: 100% rush share and 94% snap share in Week 4, and a season-high 24 carries for 116 yards in Week 5 (75% rush share, 86% snap share) — easily his best game of the year, against a Cleveland run defense that ranked 27th against backs that week. Per the Standard's Current Starter guidance, this is a genuine same-week tension: the depth chart's listed starter (Hall) has not practiced this week, while the player with the more current game-log usage (Allen) has been trending toward a true lead-back role. Treat Allen as the more likely lead if Hall is out, at LOW-to-MEDIUM confidence given this is an in-week read rather than a settled fact. If healthy, Hall remains the higher-ceiling receiving threat (60.0% rush share and a 3.33 targets/game receiving role across his 3 full games, albeit on a tiny sample) and was averaging 54.3 rush yards/game before his injury. New England's run defense ranks a strong 6th in rush yards allowed (90.8/game) — a difficult spot for either back regardless of who starts.

**New England Patriots — a true committee.** Rhamondre Stevenson is the depth-chart RB1 and has played all 5 games (45.4 rush yards/game, 37.7% rush share, plus a real receiving role at 22.2 rec yards/game and 12.8% target share), while TreVeyon Henderson — limited in practice this week with an ankle injury — has the higher per-touch burst when healthy (a 76-yard game against Pittsburgh in Week 2) but has seen his role shrink in recent weeks (just 16% rush share, 16 snaps in Week 5). Neither back carries meaningful rushing contact-efficiency detail beyond what's given — Stevenson's season-to-date rush_yac/rush_ybc averages (1.72 yards after contact, 2.26 before contact per carry) suggest a back who is more a product of his blocking than of broken tackles, which matters against a New York front that, while allowing a modest 102.2 rush yards/game (25th), has specifically allowed 4 rushing touchdowns to the position (26th) — a real red-zone/short-yardage soft spot. Henderson's own after-contact marks (1.60 YAC, 2.29 YBC per carry) are similar. Confidence on the committee split for this specific game: LOW, given Henderson's practice status.

### Wide Receivers / Tight Ends

**Garrett Wilson (NYJ).** The unquestioned focal point of New York's passing game — 30.2% target share (team-leading, not close), 74.8 receiving yards/game, 8.4 targets/game, and 3 touchdowns across 5 games. His tiered splits actually trend the "wrong" way on the surface (42.0 rec yards/game vs. mid-tier defenses, n=2, vs. 96.7 against bottom-tier, n=3) — worth treating cautiously given the bottom-tier average is inflated by a 107-yard, 13-target eruption against Detroit's 31st-ranked defense in a blowout loss. Per PFF slot data, Wilson is primarily an outside receiver (76.9% of his snaps wide, only 23.1% in the slot) — New England's CB room (Christian Gonzalez, Carlton Davis) is specifically what will see the most of him, and both corners carry real practice-participation flags this week (Gonzalez limited/shoulder, Davis DNP/neck). One additional, well-supported angle: Wilson's own splits against the blitz are dramatic — 85.7% completion, 11.71 yards per target, and a +0.836 EPA/target mark on 14 targets when blitzed this season, compared to a more pedestrian +0.271 EPA/target when not blitzed (29 targets). New England blitzes at a 38.4% rate (7th-highest in the league) with only middling success (55.9%, 18th) — a potential mismatch if New England brings extra rushers specifically at Wilson's side of the field. Confidence: MEDIUM (the blitz split is a real, sizable sample at 14 targets, but still a single season).

**Isaiah Williams and Adonai Mitchell (NYJ).** Williams is New York's primary slot receiver by PFF usage (51.3% slot rate on a 10.1% target share, 30.2 rec yards/game) but has been inefficient (1.01 yards per route run) and touchdown-shy (1 TD in 5 games). Mitchell (DNP this week, finger) has shown more per-target juice in his two games (61.5 rec yards/game, 25.4% target share) but is a genuine injury risk for Sunday. **Kenyon Sadiq (TE, limited this week, concussion)** is the more featured of New York's tight ends by target share (14.1%, 29.2 rec yards/game) and PFF route efficiency (1.85 yards per route run) relative to Jeremy Ruckert (5.9% target share, more inline-heavy usage) — his concussion status is a real swing factor for this passing attack if he's out.

**Romeo Doubs, Mack Hollins, DeMario Douglas (NE).** This is a genuinely flat, committee-style receiver room rather than a single alpha: Hollins actually leads in target share (16.9%, 52.25 rec yards/game across 4 games) ahead of Doubs (15.4% target share, 43.8 rec yards/game — including a zero-catch Week 1 on 3 targets against Seattle's defense), with Douglas (14.8% target share, 29.4 rec yards/game) rounding out the group as the clear primary slot receiver by PFF usage (86.2% slot rate, easily the highest of any player in this game). Doubs' red-zone role stands out specifically — 18.5% red-zone target share and 2 touchdowns on just 5 red-zone targets, both scores coming in the Week 4 game against Buffalo. **A.J. Brown (limited, ankle)** has appeared in just a single game for New England (3 catches, 26 yards, Week 1) — far too thin a sample to project a role from, and now carries injury risk on top of that. **Hunter Henry (TE)** is the clear lead tight end (12.8% target share, 35.4 rec yards/game, a 14.8% red-zone target share with 1 TD on 4 red-zone looks), with rookie-ish **Eli Raridon** (4 games, 25.25 rec yards/game, a real red-zone role at 14.3% target share) emerging as a legitimate second option.

**PFF slot matchup detail.** New York's defense ranks a middling 19th in slot yards/game allowed and 16th in yards-per-target allowed to the slot this season (improving slightly over the last 3 weeks to 11th in yards-per-target, though worsening to 25th in yards/game allowed over that same stretch) — New England's clear slot weapon, Douglas (86.2% slot rate), projects as a credible target volume play against a defense that has trended a bit soft there recently. New England's defense, conversely, ranks a stronger 15th in slot yards/game and 7th in yards-per-target allowed to the slot (though its last-3-week yards/game rank has slipped to 11th) — a tougher spot for New York's primary slot man, Isaiah Williams (51.3% slot rate), though Sadiq (29.1% slot rate, better per-route efficiency) may be the more dangerous slot look if his concussion clears.

### Red Zone Identity Clash

One structural note worth flagging explicitly: New England's red-zone offense is one of the most pass-dependent in the league (67.5% pass rate once inside the 20, 2nd-highest; just 32.5% run rate, 31st-lowest), while New York's red-zone defense has faced a rushing-leaning mix of plays relative to the rest of the league (53.7% run rate allowed, 10th-highest) — this is a genuine scheme question for New England's play-callers: lean into an identity that has worked overall, or adjust toward the run given what New York's defense has specifically been seeing. Framed correctly, this is a tendency observation, not a quality judgment on either unit by itself.

---

## 5. THREAT INTELLIGENCE

**How the system works:** Football Intel's deterministic Threat Engine flags a player when two conditions converge in the SAME statistical category: the player's own season rank in that category, and the upcoming opponent's defensive rank in that same category, both clear a tier's exact threshold. Three tiers, fixed thresholds (player rank is 1st-best; defense rank is 1st-toughest, so a high defense-rank number means a weak defense):
- **Nuclear** — player ranks top 3 in the category AND the opponent's defense ranks 30th or worse in that same category.
- **Elite** — player ranks top 5 AND opponent defense ranks 28th or worse.
- **Standard** — player ranks top 10 AND opponent defense ranks 23rd or worse.
"Double," "Triple," and "Quadruple" designations describe how many categories converge for a given player, not a different intensity of the same category.

**This week's result:** the Threat Engine evaluated every listed starter for both teams — Geno Smith, Braelon Allen, Garrett Wilson, Tim Patrick, and Mason Taylor for New York; Drake Maye, Rhamondre Stevenson, Romeo Doubs, Efton Chism III, and Hunter Henry for New England — and **no Threat designation fired for any player on either side of this game.** This is a direct, deterministic read of the data, not an oversight: neither team's offensive statistical profile this season has cleared the convergence thresholds against the other's specific defensive weaknesses in any tracked category. This should not be read as "nothing interesting is happening" — Sections 4 and 6 lay out real, evidence-backed angles (the blitz/Wilson mismatch, New England's top-tier-defense scoring collapse, New York's running back situation) that simply don't meet this particular system's convergence bar. Treat the analysis elsewhere in this report as the primary source of actionable insight for this matchup.

---

## 6. HIDDEN INTELLIGENCE & CONTEXTUAL ANALYSIS

**Finding 1: Both starting quarterbacks' offenses have already shown a near-identical collapse pattern against top-10 scoring defenses — and both are walking into exactly that kind of opponent this week.**

New England's offense has scored just 8.0 points per game against top-tier defenses this season (n=2: 10 points vs. Seattle, 6 points vs. Jacksonville) compared to 37.0 points per game against bottom-tier defenses (n=2: 29 vs. Buffalo, 45 vs. Las Vegas) — nearly a 5x scoring gap tied directly to opponent quality (Contextual Statistics, `team_context.home.splits.team.pts`). This isn't just a team-level artifact: Drake Maye's own individual splits move in lockstep — 0.0 passing touchdowns per game in those same two "top"-tier matchups (`off.QB.pass_td` splits, top tier, n=2) against 3.5 touchdowns per game against bottom-tier defenses (n=2), and his lone logged "top"-tier game by pass yardage (178 yards against Seattle's 2nd-ranked pass defense in Week 1) sits well below his season average of 245.6. New York's defense this week ranks 6th in points allowed and 4th in pass yards allowed — squarely in the range of competition that has already shut Maye and this offense down twice this season. Why this isn't obvious: New England's season-long passing average (251.6 yards/game, 11th) looks like a competent, middle-of-the-pack passing attack on its face; only the tier split reveals that average is being propped up almost entirely by two blowout wins over bad defenses, not genuine week-to-week consistency. What changes for this game: New England's offense should not be projected toward its season averages — its own history against this caliber of defense points toward a materially lower passing and scoring output than the raw numbers suggest. Confidence: MEDIUM — the direction is consistent across three independent signals (team scoring, individual TD rate, individual yardage), but every tier bucket involved is built on only 1-2 games.

**Finding 2: New York's tight end production is almost entirely a single-game mirage, and the player most responsible for it is banged up this week.**

New York's tight end group shows a respectable season average of 49.4 receiving yards per game (19th in the league) — but the Contextual Statistics tier split reveals that figure is almost entirely the product of one game: the "bottom-tier" opponent bucket shows an average of 164.0 receiving yards (n=1), which is the Week 3 game against Detroit (a 24-31 loss). Removing that single outlier, the position group's other four games combined for only 83 total receiving yards — an average of roughly 20.75 yards per game, less than half the season-long figure. This is independently confirmed at the individual level: in that same Week 3 game, Kenyon Sadiq (105 yards), Jeremy Ruckert (39 yards), and Jelani Woods (20 yards) combined for exactly the 164 yards and 13 catches the team-level entry shows — a blowout-script, high-target-volume outlier for the position group as a whole, not a sign of a genuinely productive tight end room. Why this isn't obvious: a reader citing only the season average (49.4 ypg, 19th) would reasonably conclude this is a usable, moderately productive tight end group; the split reveals the "true" baseline is closer to 20 yards per game. What changes for this game: expect tight end production in the 15-25 yard range rather than anywhere near the season average — and that already-modest projection carries extra downside risk given Sadiq, the room's most-targeted and most-efficient tight end (14.1% target share, 1.85 yards per route run), is in concussion protocol and only a limited practice participant this week. Confidence: MEDIUM-HIGH — the underlying math is exact (the individual logs sum perfectly to the team-level figure), though it rests on a single data point driving the outlier.

**Finding 3: New England's high blitz rate may be a live liability against Garrett Wilson specifically, not just a generic pressure tactic.**

New England blitzes at a 38.4% rate this season — the 7th-highest rate in the league — with only middling success when it does (55.9% success rate on blitz snaps, 18th). Garrett Wilson's own splits show he has turned blitzes into his most explosive opportunities of the season: 85.7% completion, 11.71 yards per target, and +0.836 EPA per target on 14 targets when blitzed, compared to a much more modest +0.271 EPA per target on 29 targets when not blitzed. Why this isn't obvious: a team blitzing at a top-10 rate with a credible pass rush (2.2 sacks/game, 16th) reads as an aggressive, disruptive approach on paper; Wilson's individual split suggests that against New York's specific top target, the tactic could backfire into exactly the kind of explosive completions a disruptive scheme is meant to prevent. What changes for this game: if New England dials up pressure on early or predictable passing downs the way its season-long rate suggests it will, Wilson's own history says that is where he is most dangerous, not most contained — a genuine tension worth weighing against New England's overall pass-rush approach. Confidence: LOW-MEDIUM — Wilson's blitz sample (14 targets) is real but still a single season, and this finding describes a tendency/opportunity, not a guarantee New England actually targets him with extra rushers.

---

## 7. COEUS FINAL READ

**Keys to the Game:**
- **If Drake Maye's interception trouble (league-worst 1.4/game) meets New York's aggressive pass rush (3.4 sacks/game, 5th) and New England's own limited/DNP tackle duo (Campbell, Moses) struggles to hold up,** this becomes the most likely single swing factor in the game — New York's defense doesn't need to force takeaways itself (it hasn't, at 0.2 interceptions/game, 31st) if New England's offense keeps giving the ball away on its own.
- **If New England leans into its extreme pass-heavy red-zone identity (67.5% pass rate, 2nd) against a New York defense that has specifically seen more rushing volume than most in the red zone (53.7% run rate allowed, 10th),** watch whether that identity persists even when the matchup data might argue for adjusting toward the run.
- **If Breece Hall is active,** New York's backfield outlook shifts meaningfully toward a higher receiving-game ceiling; if he's out, Braelon Allen's recent workload trend (100% rush share Week 4, 75% Week 5) suggests a real three-down role rather than a timeshare.
- **If New York's defense forces New England into the kind of low-scoring, low-touchdown game it has produced against every other top-10 defense this season** (0 points... 8.0 points per game, two-game sample), the game script likely favors New York regardless of which team's offense is otherwise viewed as more talented.

**The Verdict:** This profiles as a tighter, lower-scoring divisional game than New England's season-long offensive numbers suggest, because New York's defense is specifically the caliber of unit that has already shut this Patriots offense down twice this season — and New England's own turnover-prone quarterback situation adds a second way for this game to tip toward New York beyond pure matchup quality. The swing variables are Breece Hall's availability (clarifying New York's backfield ceiling), the health of New England's starting corners and tackles (both groups carry real practice-participation flags), and whether New England's pass-rush-inviting red-zone identity holds up against a defense that funnels a bit more work to the ground than average. Absent clarity on those fronts, this is a game to watch unfold on availability news through the week rather than one with an obviously lopsided read in either direction.

---

### COEUS CHEAT SHEET

**Team**
- NYJ: 2-3 | 18.6 PPG (28th) | 19.2 PPG allowed (6th)
- NE: 3-2 | 22.0 PPG (20th) | 18.8 PPG allowed (4th)

**Passing**
- Geno Smith (NYJ): 216.8 pass yds/gm (20th), 6 TD, 0.0 INT/gm — vs. NE pass defense: 222.6 yds/gm allowed (10th)
- Drake Maye (NE): 245.6 pass yds/gm individually (team: 251.6, 11th), 8 TD, 1.4 INT/gm (32nd, worst in NFL) — vs. NYJ pass defense: 195.4 yds/gm allowed (4th)

**Rushing**
- Braelon Allen (NYJ, lead back if Hall is out): 47.2 rush yds/gm (season) — vs. NE run defense: 79.8 yds/gm allowed (9th)
- Breece Hall (NYJ, DC-listed RB1, DNP this week): 54.3 rush yds/gm — vs. NE run defense: 79.8 yds/gm allowed (9th)
- Rhamondre Stevenson (NE): 45.4 rush yds/gm — vs. NYJ run defense: 102.2 yds/gm allowed (25th)
- TreVeyon Henderson (NE, Limited practice): 40.75 rush yds/gm — vs. NYJ run defense: 102.2 yds/gm allowed (25th)

**Receiving**
- Garrett Wilson (NYJ, WR): 74.8 rec yds/gm, 30.2% target share — vs. NE WR defense: 137.6 yds/gm allowed (13th)
- Isaiah Williams (NYJ, WR): 30.2 rec yds/gm, 10.1% target share — vs. NE WR defense: 137.6 yds/gm allowed (13th)
- Kenyon Sadiq (NYJ, TE, Limited/concussion): 29.2 rec yds/gm, 15.1% target share — vs. NE TE defense: 45.0 yds/gm allowed (11th)
- Romeo Doubs (NE, WR): 43.8 rec yds/gm, 15.4% target share — vs. NYJ WR defense: 130.4 yds/gm allowed (9th)
- Mack Hollins (NE, WR): 52.25 rec yds/gm, 16.9% target share — vs. NYJ WR defense: 130.4 yds/gm allowed (9th)
- Hunter Henry (NE, TE): 35.4 rec yds/gm, 12.8% target share — vs. NYJ TE defense: 36.6 yds/gm allowed (7th)

**Team Defense**
- NYJ: 195.4 pass yds/gm allowed (4th) | 118.0 rush yds/gm allowed (19th) | 130.4 WR rec yds/gm allowed (9th) | 36.6 TE rec yds/gm allowed (7th)
- NE: 222.6 pass yds/gm allowed (10th) | 90.8 rush yds/gm allowed (6th) | 137.6 WR rec yds/gm allowed (13th) | 45.0 TE rec yds/gm allowed (11th)
- Team coverage rate (man%/zone%): Not available in this week's evidence package for either team.

**Down/Distance**
- NYJ offense: 35.8% third-down conversion (23rd) | NYJ defense: 33.9% allowed (8th)
- NE offense: 37.5% third-down conversion (20th) | NE defense: 38.3% allowed (13th)

**Red Zone Play Calling**
- NYJ offense: 45.5% run / 54.5% pass (19th/14th) | NYJ defense allowed: 53.7% run / 46.3% pass (10th/24th)
- NE offense: 32.5% run / 67.5% pass (31st/2nd) | NE defense allowed: 45.7% run / 54.3% pass (20th/12th)

**Head-to-head**
- No meeting between these two teams yet this season (first matchup, Week 6).

---

```
EVIDENCE_CHECK
{"claims": [
{"type":"current_opponent","team":"NYJ","pos":"TEAM","stat":"ppg","role":"off","claimed_rank":28},
{"type":"current_opponent","team":"NYJ","pos":"TEAM","stat":"ppg","role":"def","claimed_rank":6},
{"type":"current_opponent","team":"NYJ","pos":"TEAM","stat":"total_ypg","role":"off","claimed_rank":25},
{"type":"current_opponent","team":"NYJ","pos":"TEAM","stat":"total_ypg","role":"def","claimed_rank":7},
{"type":"current_opponent","team":"NYJ","pos":"TEAM","stat":"fd_pg","role":"off","claimed_rank":25},
{"type":"current_opponent","team":"NYJ","pos":"TEAM","stat":"fd_pg","role":"def","claimed_rank":8},
{"type":"current_opponent","team":"NE","pos":"TEAM","stat":"ppg","role":"off","claimed_rank":20},
{"type":"current_opponent","team":"NE","pos":"TEAM","stat":"ppg","role":"def","claimed_rank":4},
{"type":"current_opponent","team":"NE","pos":"TEAM","stat":"total_ypg","role":"off","claimed_rank":8},
{"type":"current_opponent","team":"NE","pos":"TEAM","stat":"total_ypg","role":"def","claimed_rank":6},
{"type":"current_opponent","team":"NE","pos":"TEAM","stat":"fd_pg","role":"off","claimed_rank":12},
{"type":"current_opponent","team":"NE","pos":"TEAM","stat":"fd_pg","role":"def","claimed_rank":5},
{"type":"current_opponent","team":"NYJ","pos":"QB","stat":"pass_ypg","role":"off","claimed_rank":20},
{"type":"current_opponent","team":"NYJ","pos":"QB","stat":"comp_pct","role":"off","claimed_rank":3},
{"type":"current_opponent","team":"NYJ","pos":"QB","stat":"pass_td","role":"off","claimed_rank":24},
{"type":"current_opponent","team":"NYJ","pos":"QB","stat":"sacks_pg","role":"off","claimed_rank":29},
{"type":"current_opponent","team":"NYJ","pos":"QB","stat":"int_pg","role":"off","claimed_rank":3},
{"type":"current_opponent","team":"NYJ","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":4},
{"type":"current_opponent","team":"NYJ","pos":"QB","stat":"comp_pct","role":"def","claimed_rank":10},
{"type":"current_opponent","team":"NYJ","pos":"QB","stat":"sacks_pg","role":"def","claimed_rank":5},
{"type":"current_opponent","team":"NYJ","pos":"QB","stat":"int_pg","role":"def","claimed_rank":31},
{"type":"current_opponent","team":"NYJ","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":21},
{"type":"current_opponent","team":"NYJ","pos":"RB","stat":"rec_ypg","role":"off","claimed_rank":18},
{"type":"current_opponent","team":"NYJ","pos":"RB","stat":"rush_td","role":"off","claimed_rank":19},
{"type":"current_opponent","team":"NYJ","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":25},
{"type":"current_opponent","team":"NYJ","pos":"RB","stat":"rush_td","role":"def","claimed_rank":26},
{"type":"current_opponent","team":"NYJ","pos":"RB","stat":"rec_td","role":"def","claimed_rank":29},
{"type":"current_opponent","team":"NYJ","pos":"WR","stat":"rec_ypg","role":"off","claimed_rank":19},
{"type":"current_opponent","team":"NYJ","pos":"WR","stat":"td","role":"off","claimed_rank":19},
{"type":"current_opponent","team":"NYJ","pos":"WR","stat":"rec_ypg","role":"def","claimed_rank":9},
{"type":"current_opponent","team":"NYJ","pos":"WR","stat":"td","role":"def","claimed_rank":12},
{"type":"current_opponent","team":"NYJ","pos":"TE","stat":"rec_ypg","role":"off","claimed_rank":19},
{"type":"current_opponent","team":"NYJ","pos":"TE","stat":"td","role":"off","claimed_rank":21},
{"type":"current_opponent","team":"NYJ","pos":"TE","stat":"rec_ypg","role":"def","claimed_rank":7},
{"type":"current_opponent","team":"NYJ","pos":"TE","stat":"td","role":"def","claimed_rank":5},
{"type":"current_opponent","team":"NE","pos":"QB","stat":"pass_ypg","role":"off","claimed_rank":11},
{"type":"current_opponent","team":"NE","pos":"QB","stat":"comp_pct","role":"off","claimed_rank":16},
{"type":"current_opponent","team":"NE","pos":"QB","stat":"pass_td","role":"off","claimed_rank":17},
{"type":"current_opponent","team":"NE","pos":"QB","stat":"sacks_pg","role":"off","claimed_rank":18},
{"type":"current_opponent","team":"NE","pos":"QB","stat":"int_pg","role":"off","claimed_rank":32},
{"type":"current_opponent","team":"NE","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":10},
{"type":"current_opponent","team":"NE","pos":"QB","stat":"comp_pct","role":"def","claimed_rank":24},
{"type":"current_opponent","team":"NE","pos":"QB","stat":"sacks_pg","role":"def","claimed_rank":16},
{"type":"current_opponent","team":"NE","pos":"QB","stat":"int_pg","role":"def","claimed_rank":21},
{"type":"current_opponent","team":"NE","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":13},
{"type":"current_opponent","team":"NE","pos":"RB","stat":"rec_ypg","role":"off","claimed_rank":15},
{"type":"current_opponent","team":"NE","pos":"RB","stat":"rush_td","role":"off","claimed_rank":18},
{"type":"current_opponent","team":"NE","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":9},
{"type":"current_opponent","team":"NE","pos":"RB","stat":"rec_ypg","role":"def","claimed_rank":27},
{"type":"current_opponent","team":"NE","pos":"RB","stat":"rush_td","role":"def","claimed_rank":25},
{"type":"current_opponent","team":"NE","pos":"RB","stat":"rec_td","role":"def","claimed_rank":13},
{"type":"current_opponent","team":"NE","pos":"WR","stat":"rec_ypg","role":"off","claimed_rank":10},
{"type":"current_opponent","team":"NE","pos":"WR","stat":"td","role":"off","claimed_rank":8},
{"type":"current_opponent","team":"NE","pos":"WR","stat":"rec_ypg","role":"def","claimed_rank":13},
{"type":"current_opponent","team":"NE","pos":"WR","stat":"td","role":"def","claimed_rank":23},
{"type":"current_opponent","team":"NE","pos":"TE","stat":"rec_ypg","role":"off","claimed_rank":17},
{"type":"current_opponent","team":"NE","pos":"TE","stat":"td","role":"off","claimed_rank":20},
{"type":"current_opponent","team":"NE","pos":"TE","stat":"rec_ypg","role":"def","claimed_rank":11},
{"type":"current_opponent","team":"NE","pos":"TE","stat":"td","role":"def","claimed_rank":11},
{"type":"current_opponent","team":"NYJ","pos":"TEAM","stat":"third_down_conversion_pct","role":"off","claimed_rank":23},
{"type":"current_opponent","team":"NYJ","pos":"TEAM","stat":"third_down_pct_allowed","role":"def","claimed_rank":8},
{"type":"current_opponent","team":"NE","pos":"TEAM","stat":"third_down_conversion_pct","role":"off","claimed_rank":20},
{"type":"current_opponent","team":"NE","pos":"TEAM","stat":"third_down_pct_allowed","role":"def","claimed_rank":13},
{"type":"current_opponent","team":"NYJ","pos":"TEAM","stat":"red_zone_run_pct","role":"off","claimed_rank":19},
{"type":"current_opponent","team":"NYJ","pos":"TEAM","stat":"red_zone_pass_pct","role":"off","claimed_rank":14},
{"type":"current_opponent","team":"NYJ","pos":"TEAM","stat":"red_zone_run_pct_allowed","role":"def","claimed_rank":10},
{"type":"current_opponent","team":"NYJ","pos":"TEAM","stat":"red_zone_pass_pct_allowed","role":"def","claimed_rank":24},
{"type":"current_opponent","team":"NE","pos":"TEAM","stat":"red_zone_run_pct","role":"off","claimed_rank":31},
{"type":"current_opponent","team":"NE","pos":"TEAM","stat":"red_zone_pass_pct","role":"off","claimed_rank":2},
{"type":"current_opponent","team":"NE","pos":"TEAM","stat":"red_zone_run_pct_allowed","role":"def","claimed_rank":20},
{"type":"current_opponent","team":"NE","pos":"TEAM","stat":"red_zone_pass_pct_allowed","role":"def","claimed_rank":12},
{"type":"current_opponent","team":"NE","pos":"TEAM","stat":"blitz_rate","role":"def","claimed_rank":7},
{"type":"current_opponent","team":"NE","pos":"TEAM","stat":"blitz_success_rate","role":"def","claimed_rank":18},
{"type":"current_opponent","team":"NYJ","pos":"TEAM","stat":"blitz_rate","role":"def","claimed_rank":11},
{"type":"current_opponent","team":"NYJ","pos":"TEAM","stat":"blitz_success_rate","role":"def","claimed_rank":5},
{"type":"current_opponent","team":"NYJ","pos":"TEAM","stat":"slot_yards_pg","role":"def","claimed_rank":19},
{"type":"current_opponent","team":"NYJ","pos":"TEAM","stat":"slot_yards_per_target","role":"def","claimed_rank":16},
{"type":"current_opponent","team":"NE","pos":"TEAM","stat":"slot_yards_pg","role":"def","claimed_rank":15},
{"type":"current_opponent","team":"NE","pos":"TEAM","stat":"slot_yards_per_target","role":"def","claimed_rank":7},
{"type":"log_opponent","player":"Geno Smith","week":2,"stat":"pass_yds","claimed_rank":7},
{"type":"log_opponent","player":"Geno Smith","week":3,"stat":"pass_yds","claimed_rank":32},
{"type":"log_opponent","player":"Drake Maye","week":1,"stat":"pass_yds","claimed_rank":2},
{"type":"log_opponent","player":"Drake Maye","week":3,"stat":"pass_yds","claimed_rank":30},
{"type":"log_opponent","player":"Braelon Allen","week":5,"stat":"rush_yds","claimed_rank":27}
]}
```