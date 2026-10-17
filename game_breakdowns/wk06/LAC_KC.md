# GAME BREAKDOWN: Los Angeles Chargers @ Kansas City Chiefs
### Week 6, 2026 Season | Sunday, 2026-10-18, 4:25 PM ET | GEHA Field at Arrowhead Stadium (outdoors, grass)

**EVIDENCE NOTE:** This is a real, scheduled Week 6 matchup, not a bootstrap package — every statistic below is drawn from actual 2026 season-to-date data (LAC 5 games played, KC 4 games played). No weather/temperature data is present in this week's evidence package, so none is cited. Two evidence categories that are normally part of this report's scheme analysis — man/zone coverage performance splits (`coverage_qb`, `coverage_wr`, `coverage_te`) and individual CB/DB performance rankings (`cb_db_rankings`) — came back completely empty for this game and are not available to cite. Team-level man/zone play-calling rate (`team_coverage_rate`) is also absent from this week's package. Similarly, no `home_road_split`, `tier_home_road_split`, or `season_2025` fields exist anywhere in this evidence package for any player on either roster — the Home/Road Split and 2025 Season Context requirements cannot be fulfilled this week for any player, and that gap is noted here once rather than repeated after each name.

---

## 1. PREGAME BRIEFING

Los Angeles arrives at 0-5 (form: LLL), Kansas City at 4-0 (form: WWW) — the widest gap between these two rosters' season results of any game on the schedule context available here. This is a genuine AFC West division game (`div_game: true`), but the evidence package shows no meeting between these two teams anywhere in either team's 2026 game log yet (LAC's five logged opponents are ARI, LV, BUF, SEA, DEN; KC's four are DEN, IND, MIA, LV) — this will be the first meeting of the season, so there is no actual head-to-head result, and no specific per-player history against this exact opponent, to draw on this week. That absence is itself worth noting for a division matchup, where familiarity normally plays a role.

Rest is uneven: Kansas City enters on 14 days' rest (coming off a bye), Los Angeles on a standard 7-day turnaround — extra preparation time for the team that already owns the larger talent and record edge.

On paper, nearly every team-level category favors Kansas City, and by wide margins in several — KC's offense ranks top-5 in points per game and top-3 in total yards, while LAC's offense ranks in the bottom third of the league in scoring and passing production. But the picture is not simply "good team vs. bad team" underneath the surface: Los Angeles's defense is a genuinely competitive, top-10 unit in total yards and pass yards allowed, and the turnover margin implied by the season box score (LAC 7 giveaways, KC 2) suggests the Chargers' record owes as much to self-inflicted damage as to being outclassed snap-for-snap. Kansas City also walks in banged up at a skill spot of its own (Rashee Rice did not practice this week), and Los Angeles's injury report is considerably longer and touches the secondary, both lines, and most of the receiving corps at once. The broad shape this profiles toward: a game where Kansas City's structural advantages are real and significant, but where Los Angeles's own margin for error — turnovers, protection, and health in its defensive backfield — is the swing factor in how lopsided it actually plays out. The deeper matchup work below, and the final verdict in Section 7, work through exactly which of those levers matters most.

---

## 2. INJURY & AVAILABILITY REPORT

**Source:** Football Intel's nflverse weekly injury report (`injuries/wk06.json`), not the DraftKings slate Status column — this is a more detailed source, carrying body part and practice participation. All listed players carry a "Pending" report status, meaning no final Friday/Saturday game designation has been filed yet as of this evidence freeze; practice participation (Did Not Participate vs. Limited) is the best signal currently available on each player's trajectory, not a confirmed Out/Questionable/Active call.

**Kansas City:**
- **Rashee Rice (WR) — Hamstring, Did Not Participate in Practice.** Significant. Rice has been KC's most efficient receiver through three games (63.33 rec yds/game, 39.67 yards-after-catch/game — both detailed in Section 4) and is listed as the team's starting WR on the current depth chart. A DNP on a hamstring is the most concerning single flag in this game for either offense's receiving corps.
- **L'Jarius Sneed (CB) — Knee, Limited Participation.** Sneed is listed as KC's starting slot corner (nickel) on the depth chart; limited reps is a lesser flag than a DNP but still worth tracking given KC's own slot-coverage weakness (Section 4).
- **Josh Simmons (T) — Back, Limited Participation.** Simmons is listed as KC's starting left tackle; a limited practice week at a line spot in front of Mahomes is worth monitoring but not alarming on its own.

**Los Angeles:** a considerably longer list, touching nearly every unit:
- **Tre Harris (WR) — Hamstring, Did Not Participate.** Harris leads LAC in targets (25, 18.1% share) and receiving yards (225) this season. A DNP for the team's clear #1 target is the single most important injury flag on either roster for the passing game specifically.
- **Donte Jackson (CB) — Hamstring, DNP**; **Derwin James (S) — Hamstring, DNP**; **Elijah Molden (S) — Hamstring, Limited**; **Kendall Williamson (S) — Ankle, Limited.** Four different members of LAC's starting secondary carrying a flag in the same week, two of them (Jackson, James) not practicing at all. James and Jackson are both listed starters on the current depth chart (SS and RCB, respectively). This matters directly against a Kansas City passing attack that already ranks top-10 in total pass offense and features one of the league's most efficient tight ends (Section 4) — a compromised secondary is a real, specific risk factor for this exact game, not a generic injury note.
- **Joe Alt (T) — Neck, DNP**; **Kayode Awosika (G) — Fibula, DNP.** Both are starting offensive linemen (RT and LG) not practicing. Combined with Herbert already carrying the league's 3rd-worst sack rate (3.4/game, 30th — Section 4), further line uncertainty is a legitimate protection concern.
- **Khalil Mack (DE) — "Not injury related - resting player," DNP.** Read as likely planned veteran rest given LAC's 0-5 record rather than a health concern, but worth flagging as uncertain regardless.
- **Bud Dupree (DE) — Neck, Limited**; **Dalvin Tomlinson (DT) — Hamstring, Limited**; **Jamaree Caldwell (DT) — Knee, Limited**; **Justin Eboigbe (DE) — Shoulder, Limited**; **Daiyan Henley (LB) — Knee, Limited.** A substantial portion of LAC's front seven carrying some flag simultaneously — individually modest (Limited, not DNP), but collectively a real depth concern against a Chiefs rushing attack already averaging a league-high-tier workload (Section 4).
- **Ladd McConkey (WR) — Foot, Limited**; **Quentin Johnston (WR) — Chest, Limited**; **KeAndre Lambert-Smith (WR) — Hamstring, Limited**; **Marquez Valdes-Scantling (WR) — Rib, Limited**; **Brenen Thompson (WR) — Quadricep, Limited.** Essentially LAC's entire healthy-body wide receiver depth chart beyond Harris carries some designation. None are DNP, which is a meaningfully better sign than Harris's status, but the cumulative picture — five different wideouts flagged in the same week — is notable on its own and discussed further in Section 6.
- **Rodney Shelley (CB) — Hamstring, Limited.** Depth secondary piece.

**Net read:** Kansas City's flags are isolated to three players, one of real consequence (Rice). Los Angeles's injury report is both longer and touches more complete units at once — secondary, both lines, and the receiving corps — which is relevant context for nearly every matchup discussed below. Confidence on actual game-day impact: LOW-MEDIUM for most Limited-participation players (practice limitations don't reliably predict game absences), MEDIUM-HIGH that the four DNP players (Harris, Jackson, James, Alt/Awosika) carry real snap-count or role risk given their practice absence this close to kickoff.

**Depth chart starters confirmed, no tension:** Justin Herbert (LAC QB1) and Patrick Mahomes (KC QB1) both match their respective team's current depth chart listing and their own game-log usage (100% snap share, every start) — no starter ambiguity at quarterback for either side. Same alignment at RB (Omarion Hampton, Kenneth Walker III both depth-chart RB1 and lead game-log producers). At tight end, LAC's depth chart lists Charlie Kolar as the starting in-line TE (ahead of the higher-pedigree David Njoku, who has only been active for two games) — consistent with Kolar's higher snap share (64.3%) in his own appearances; Njoku is addressed as a developing role player in Section 6.

---

## 3. MATCHUP STATISTICS

### LAC Offense
- **Team identity:** 16.8 ppg (30th), 315.6 total yds/gm (23rd), 187.4 pass yds/gm (29th), 128.2 rush yds/gm (9th), 14.8 first downs/gm (26th).
- **QB:** 937 pass yds, 187.4 yds/gm (29th), 59.4% completion (29th), 5 pass TD (25th), 1.4 INT/gm (31st — 2nd-worst in the league), 3.4 sacks taken/gm (30th).
- **RB:** 494 rush yds, 98.8 yds/gm (9th), 120 carries (10th), 4 rush TD (13th), 29.2 rec yds/gm (16th), 2 rec TD (4th).
- **WR:** 573 rec yds, 114.6 yds/gm (29th), 39 catches (32nd — fewest in the league), 73 targets (27th), 1 TD all season (32nd — fewest in the league), 14.7 yds/reception (5th).
- **TE:** 218 rec yds, 43.6 yds/gm (21st), 22 catches (21st), 32 targets (19th), 2 TD (18th), 9.9 yds/reception (12th).
- **Down/Distance:** 34.8% third-down conversion (26th) on 13.2 attempts/gm; 21.1% fourth-down go-for-it rate, 25.0% conversion rate when going.
- **Red Zone Play Calling:** 59.0% run / 41.0% pass once inside the 20 (run rate ranks 6th-most-run-heavy, pass rate ranks 27th — a run-leaning red-zone identity) on 7.8 plays/gm.
- **Contextual Statistics (team scoring by opponent tier faced):** 23.0 ppg vs. the lone top-tier defense faced (n=1), 17.0 ppg vs. mid-tier (n=1), 14.7 ppg vs. bottom-tier (n=3) — a counterintuitive pattern explored in Section 6.

### LAC Defense
- **Team identity:** 25.8 ppg allowed (22nd), 323.6 total yds/gm allowed (9th), 205.0 pass yds/gm allowed (6th), 118.6 rush yds/gm allowed (21st), 16.4 first downs/gm allowed (10th).
- **vs. QB:** 1,025 pass yds allowed, 205.0 yds/gm (6th), 64.5% completion allowed (17th), 7 pass TD allowed (17th), 2.2 sacks/gm generated (15th), 0.8 INT/gm (10th), 28.2 attempts faced/gm (4th — among the fewest pass attempts faced in the league).
- **vs. RB:** 495 rush yds allowed, 99.0 yds/gm (19th), 128 carries faced (29th — among the most rush volume faced in the league), 4 rush TD allowed (23rd), 25.0 rec yds/gm allowed (9th — a real strength).
- **vs. WR:** 660 rec yds allowed (12th), 132.0 yds/gm (11th), 50 catches (11th), 75 targets faced (5th — heavily targeted), 5 TD allowed (21st), 172.4 air yds/gm allowed (4th), 32.2 yards-after-catch/gm allowed (2nd — a real weakness).
- **vs. TE:** 239 rec yds allowed (14th), 47.8 yds/gm (13th), 21 catches (8th), 30 targets faced (6th — heavily targeted), 1 TD allowed (9th — a strength), 11.4 yds/reception (27th).
- **Down/Distance:** 31.2% third-down conversion allowed (5th — excellent) on 12.8 attempts faced/gm, 68.8% stop rate; 20.0% fourth-down stop rate on 12.2% go-for-it rate faced.
- **Red Zone Play Calling:** 56.9% run / 43.1% pass allowed in the red zone (run rate allowed ranks 6th-highest, pass rate allowed ranks 27th) on 10.2 plays faced/gm.
- **Contextual Statistics:** Not available in this week's evidence package (offensive-only tier splits).

### KC Offense
- **Team identity:** 29.5 ppg (5th), 417.8 total yds/gm (3rd), 259.2 pass yds/gm (10th), 158.5 rush yds/gm (4th), 19.5 first downs/gm (10th).
- **QB:** 1,037 pass yds, 259.2 yds/gm (10th), 64.1% completion (20th), 9 pass TD (12th), 12.6 yds/completion (2nd), 1.5 sacks taken/gm (5th — excellent protection), 0.5 INT/gm (10th).
- **RB:** 593 rush yds (4th), 148.2 yds/gm (2nd), 103 carries (17th), 4 rush TD (12th), 40.5 rec yds/gm (6th), 2 rec TD (3rd).
- **WR:** 559 rec yds (29th), 139.8 yds/gm (21st), 41 catches (29th), 61 targets (32nd — fewest in the league), 5 TD (15th), 13.6 yds/reception (14th).
- **TE:** 316 rec yds (9th), 79.0 yds/gm (3rd — elite), 23 catches (18th), 32 targets (18th), 2 TD (17th), 13.7 yds/reception (1st — best in the league), 49.8 yards-after-catch/gm (1st — best in the league).
- **Down/Distance:** 44.0% third-down conversion (9th) on 12.5 attempts/gm; 23.3% fourth-down go-for-it rate, 71.4% conversion rate when going.
- **Red Zone Play Calling:** 44.0% run / 56.0% pass in the red zone (run rate ranks 23rd, pass rate ranks 10th — a pass-leaning red-zone identity) on 12.5 plays/gm.
- **Contextual Statistics:** 31.0 ppg vs. the one mid-tier defense faced (n=1), 29.0 ppg vs. bottom-tier (n=3); passing offense scaled from 184 yds/gm vs. a top-tier defense (n=1) to 303.5 yds/gm vs. bottom-tier (n=2).

### KC Defense
- **Team identity:** 19.2 ppg allowed (7th), 321.8 total yds/gm allowed (8th), 229.0 pass yds/gm allowed (15th), 92.8 rush yds/gm allowed (7th), 17.2 first downs/gm allowed (13th).
- **vs. QB:** 916 pass yds allowed, 229.0 yds/gm (15th), 61.2% completion allowed (6th), 4 pass TD allowed (3rd — excellent), 1.0 sacks/gm generated (31st — among the weakest pass rushes in the league), 1.0 INT/gm (7th), 36.8 attempts faced/gm (28th — opponents throw a lot against KC, likely game-script driven given the 4-0 record).
- **vs. RB:** 276 rush yds allowed (2nd), 69.0 yds/gm (3rd — elite), 83 carries faced (2nd — among the fewest rush attempts faced in the league), 3 rush TD allowed (13th), 38.2 rec yds/gm allowed (23rd).
- **vs. WR:** 434 rec yds allowed (1st — fewest in the league), 108.5 yds/gm (2nd), 38 catches (1st — fewest in the league), 71 targets faced (2nd — few targets sent that direction), 0 TD allowed (1st — zero wide receiver touchdowns surrendered through four games), 11.4 yds/reception (4th), 37.2 yards-after-catch/gm (6th).
- **vs. TE:** 329 rec yds allowed (26th), 82.2 yds/gm (30th — a real weakness), 33 catches (27th), 46 targets faced (29th — heavily targeted), 4 TD allowed (28th), 10.0 yds/reception (18th).
- **Down/Distance:** 37.0% third-down conversion allowed (11th) on 13.5 attempts faced/gm, 63.0% stop rate; 55.6% fourth-down stop rate on 24.3% go-for-it rate faced.
- **Red Zone Play Calling:** 44.4% run / 55.6% pass allowed in the red zone (run rate allowed ranks 23rd, pass rate allowed ranks 10th) on 6.8 plays faced/gm.
- **Contextual Statistics:** Not available in this week's evidence package (offensive-only tier splits).

---

## 4. MATCHUP INTELLIGENCE

### Quarterbacks

**Justin Herbert (LAC)** has started all 5 games, averaging 187.4 pass yds/gm (29th in the league) on a 59.4% completion rate (29th), with 5 touchdowns (25th) against a 2nd-worst 1.4 interceptions/gm (31st) and a 3rd-worst 3.4 sacks taken/gm (30th). He also carries a real rushing dimension — 142 rush yards across 5 games (28.4/gm), a legitimate scramble/designed-run element rather than incidental churn. His opponent-quality splits show real variance: against the one top-tier pass defense he's faced this season (Seattle, Week 4, ranked 2nd in pass yards allowed), he threw for 189 yards — essentially his season average, not a collapse, but also not a ceiling game. Kansas City's pass defense (229.0 yds/gm allowed, 15th — more middling than Seattle's elite mark, though the underlying total yards allowed, 916, ranks 3rd) presents a muddled statistical picture: the raw total is strong, the per-game rate is average, largely a function of KC forcing a league-high 36.8 attempts/gm against it. Confidence: MEDIUM. The clearest, most alarming signal for Herbert this week isn't matchup quality — it's his own takeaway rate running directly into a Chiefs defense that already generates 1.0 INT/gm (7th).

**Patrick Mahomes (KC)** has started all 4 games, averaging 259.2 pass yds/gm (10th), 64.1% completion (20th), 9 touchdowns (12th) against just 0.5 interceptions/gm (10th), behind a line allowing only 1.5 sacks/gm (5th-best protection in the league) and producing an elite 12.6 yards/completion (2nd). His only rushing involvement is incidental (41 yards across 4 games, 10.25/gm) — not a designed component of this offense. Opponent quality so far has trended tougher as volume rose: 184 pass yds/gm against a mid-tier defense in Week 1 up to 303.5 yds/gm against bottom-tier competition (n=2) — a normal, expected gradient. Los Angeles's pass defense (205.0 yds/gm allowed, 6th in the league; 1,025 total yards allowed, 8th) is a genuinely difficult individual-game test on paper, one of the better pass defenses Mahomes will see this season. Confidence: MEDIUM — the raw defensive numbers are strong, but LAC's defensive backfield carries four separate injury flags this week (Section 2), which is the more decision-relevant variable than the season-long ranking alone.

### Running Backs

**Omarion Hampton (LAC)** is the clear lead back — 271 rush yards across 5 games (54.2/gm individually; team RB production of 98.8 yds/gm ranks 9th in the league), on a 49.7% rush share in a real committee with Keaton Mitchell (22.4% share) and Kimani Vidal (11.1% share). His red-zone role is dominant regardless of overall touch split: 60.9% of LAC's red-zone carries, 3 rushing touchdowns on the season (team RB rush-TD rate ranks 13th). His contact-efficiency marks are modest — 1.96 yards before contact and 1.75 yards after contact per carry, with 1.8 broken tackles/gm — numbers that suggest a back creating little room for himself and getting limited push from his line, consistent with LAC's offensive-line injury situation (Joe Alt and Kayode Awosika both DNP this week, Section 2). His tiered opponent splits show a tough-matchup sample: against the one top-tier run defense he's faced (Seattle, Week 4, ranked 8th in rush yards allowed), he managed 45 yards on 9 carries — below his season average. Kansas City's run defense specifically against running backs (69.0 yds/gm allowed, 3rd in the league; only 83 carries faced all season, 2nd-fewest) is a materially tougher matchup than Seattle's, and the hidden-intelligence rush-vs-pass data independently classifies this specific matchup as a "top" (tough) tier for Hampton's run production. Confidence: MEDIUM-HIGH that Hampton's ceiling is capped this week by matchup quality alone, separate from any health question.

**Kenneth Walker III (KC)** has been the workhorse of this entire offense — 537 rush yards across 4 games (134.25/gm individually; team RB production of 148.2 yds/gm ranks 2nd in the league) on a 75.7% rush share, with 537 total rushing yards against a backdrop of excellent per-touch efficiency: 3.10 yards before contact and 3.07 yards after contact per carry, with 3.0 broken tackles/gm — both a well-blocked line and a back generating extra yardage himself. His red-zone workload is nearly absolute: 86.4% of KC's red-zone carries, 2 rushing touchdowns. He also carries a real receiving role (84 rec yds, 21.0/gm, 12 catches on 19 targets). He has not yet faced a genuine top-tier run defense this season (his tiered splits show zero top-tier games, three bottom-tier, one mid-tier) — Los Angeles's run defense specifically against backs (99.0 yds/gm allowed, 19th in the league) is a middling matchup on paper, and the hidden-intelligence data independently classifies it as "mid" tier for Walker. The more extreme number is volume: LAC has faced 128 carries all season, 29th-most in the league — teams are running on this defense at a high rate, and Walker's receiving floor is modestly capped by LAC's actual strength defending backs through the air (25.0 rec yds/gm allowed, 9th). Confidence: MEDIUM-HIGH that Walker sees a heavy, favorable workload regardless of score, given KC's season-long usage pattern and LAC's rush-funnel tendency.

Complementary backs: **Keaton Mitchell (LAC)** — 135 yards on 33 carries (27.0/gm), 12 catches on 14 targets, real receiving-down role with notable slot alignment (32.4% of his routes from the slot per PFF — see below); **Kimani Vidal (LAC)** — 88 yards on 14 carries, spot complementary role; **Emmett Johnson (KC)** — 56 rush yards, 74 receiving yards across 4 games, a clear change-of-pace/passing-down piece behind Walker's dominant workload share.

### Wide Receivers / Tight Ends

**Tre Harris (LAC)** is the clear top target — 25 targets (18.1% share), 225 yards, 15 catches, 45.0 yds/gm, but zero touchdowns on the season (part of a unit-wide WR scoring drought detailed below). Per PFF, he is primarily an outside receiver (60.1% of his snaps wide, 39.9% slot) with an average depth of target of 10.7 yards and a 64.9 PFF grade. His blitz splits are striking: against the blitz this season he has produced 17.75 yards/play and a +0.977 EPA/play on 8 snaps, compared to 4.88 yards/play and -0.144 EPA/play on 17 snaps when not blitzed — a real, if small-sample, indication that single-high/man-heavy looks that often accompany pressure have been his best opportunities. Kansas City's defense specifically allows just 108.5 WR rec yds/gm (2nd in the league) with zero wide receiver touchdowns surrendered all season (1st) — an elite perimeter unit on paper. Harris's hamstring DNP this week (Section 2) is the dominant variable; confidence on his actual availability and workload is LOW given the DNP status, separate from the matchup quality question (MEDIUM, unfavorable).

**Ladd McConkey (LAC)** has played 4 of LAC's 5 games (missed Week 5, consistent with his current foot flag), averaging 45.75 yds/gm on 12 catches and 17 targets (14.5% share), with the best efficiency marks of any LAC receiver (73.6 PFF grade, 2.1 yards per route run). Per PFF he is a genuine slot/wide hybrid (49.0% slot, 51.0% wide) — notably, Kansas City's defense is excellent against perimeter WRs overall but specifically weak defending the slot: KC's slot defense ranks 28th in yards/game allowed and 18th in yards per target, per PFF slot-coverage data, a real soft spot inside KC's otherwise shutdown WR numbers. McConkey is positioned as LAC's best tool to find that specific crack — if his foot allows a full workload (Limited participation this week, not DNP, a somewhat better sign than Harris's status).

**Quentin Johnston (LAC)** has played 4 of 5 games, a lower-efficiency complementary piece — 108 yards on 7 catches, 19 targets (16.2% share), the lowest PFF grade among LAC's receivers (55.2) and lowest yards-per-route mark (0.93). Per PFF he is almost entirely an outside receiver (83.7% wide, 16.3% slot) — directly into the teeth of KC's elite perimeter coverage rather than its slot weakness. Also carries a Chest flag this week (Limited).

**Oronde Gadsden II (LAC TE)** leads LAC's tight end group — 86 yards on 9 catches, 16 targets (11.6% share), with real red-zone usage (18.8% red-zone target share, 1 TD). Kansas City's tight end defense is a clear mismatch in LAC's favor on paper: 82.2 TE rec yds/gm allowed (30th in the league), 46 TE targets faced (29th — heavily attacked), 4 TE touchdowns allowed (28th). Confidence: MEDIUM that Gadsden (and LAC's tight end group broadly, see Section 6) represents a better avenue than either outside receiver given this specific opponent profile.

**Xavier Worthy (KC)** — 133 yards on 14 catches, 22 targets (19.6% share, team-high), 33.25 yds/gm, with 4 red-zone targets and 1 TD. Per PFF he's primarily an outside receiver (68.9% wide, 30.4% slot), PFF grade 61.6. His blitz splits mirror Mahomes's own pattern closely: 77.8% completion and 10.11 yards/play against the blitz (9 snaps) vs. 53.8% completion and 3.23 yards/play unblitzed (13 snaps) — further evidence that this is a QB-driven effect across KC's top targets, not isolated to one player. Los Angeles's WR defense (132.0 yds/gm allowed, 11th) is a middling matchup, tougher than league-average but far from LAC's own defensive strength (pass yardage generally).

**Tyquan Thornton (KC)** — 219 yards on 11 catches, 15 targets (12.7% share), the clearest big-play threat in this game: 19.91 yards/reception, 18.1-yard average depth of target (deepest of any receiver cited in this report), 2 touchdowns, both on red-zone targets (100% red-zone conversion rate on 2 looks). 71.4 PFF grade, primarily outside-aligned (70.9% wide).

**Rashee Rice (KC)** — in just 3 games, the most productive per-game Chiefs receiver by rate: 190 yards, 63.33 yds/gm, 13 catches on 17 targets (18.7% share), and an exceptional 39.67 yards-after-catch/gm. Per PFF he's a true slot/wide hybrid (46.1% slot, 52.9% wide). His hamstring DNP this week (Section 2) is the dominant variable for his availability; if out or limited, expect increased target share to flow toward Worthy and Thornton.

**Travis Kelce (KC TE)** remains a focal point of this passing attack — 246 yards on 16 catches, 22 targets (18.6% share, tied for team-high with Worthy), 61.5 yds/gm, 2 touchdowns, 42.0 yards-after-catch/gm, and the best PFF grade of any pass-catcher in this evidence package (82.0). Per PFF he's primarily inline (43.8%) with real slot usage (33.1%). Los Angeles's tight end defense (47.8 yds/gm allowed, 13th; 1 TD allowed, 9th-best) is a considerably tougher matchup for Kelce than KC's own TE defense represents for LAC's tight ends — a clean individual-matchup asymmetry worth flagging directly: both teams' tight ends are featured weapons, but only one side (LAC's) is attacking a real defensive weak point.

### Coverage & Scheme

As noted above, man/zone performance splits and individual CB/DB rankings are both empty for this game in the evidence package and are not discussed. Blitz data, however, is rich and reveals a clear, actionable asymmetry: **Justin Herbert is considerably worse when blitzed** (41.5% completion, 4.34 yds/play, -0.349 EPA/play across 41 snaps) **than when not** (57.6% completion, 5.47 yds/play, -0.188 EPA/play across 118 snaps) — both splits are negative-EPA overall, reflecting his season-long struggles, but the gap under pressure is pronounced. Kansas City's own blitz rate ranks 17th in the league and its blitz success rate ranks 22nd — a middling, not overwhelming, pressure package on paper, but one that lines up well against a specific Herbert weakness regardless of raw frequency.

The inverse is true on the other side: **Mahomes is dramatically better when blitzed** (73.0% completion, 9.3 yds/play, +0.479 EPA/play across 37 snaps) **than when not** (56.1% completion, 6.68 yds/play, +0.082 EPA/play across 98 snaps) — a hallmark trait, and one that extends to his top target: Xavier Worthy shows the identical pattern (77.8% completion/10.11 yds/play blitzed vs. 53.8%/3.23 yds/play unblitzed). Los Angeles blitzes at a 21st-ranked rate but with a genuinely effective 8th-ranked blitz success rate overall — a real, above-average pressure weapon against most quarterbacks, but specifically the wrong plan against this one, based on his season-long splits. Confidence: MEDIUM-HIGH on both directional reads (Herbert worse blitzed, Mahomes better blitzed) given reasonably sized samples (37-41 snaps each) and consistency across multiple metrics (completion, yards/play, EPA, success rate) rather than a single outlier number.

---

## 5. THREAT INTELLIGENCE

**How the Threat system works:** A Threat designation fires only when a player's own SEASON rank in a specific statistical category and the upcoming opponent's defensive rank in that identical category both clear a fixed threshold at the same time — not strong individual play alone, and not a weak opponent alone, but both conditions converging on the same category simultaneously. The three tiers use fixed thresholds: **Nuclear** requires the player to rank top 3 in a category AND the opposing defense to rank 30th or worse in that same category; **Elite** requires top 5 and a defensive rank of 28th or worse; **Standard** requires top 10 and a defensive rank of 23rd or worse. A "Double" designation reflects one category meeting both thresholds; "Triple" and "Quadruple" reflect additional categories where the player's own rank clears the bar even without full defensive convergence, or multiple categories fully converging at once.

Football Intel's deterministic Threat Engine evaluated the listed starters for both teams this week — Justin Herbert, Omarion Hampton, Quentin Johnston, Tre Harris, and Charlie Kolar for Los Angeles; Patrick Mahomes, Kenneth Walker III, Xavier Worthy, Rashee Rice, and Travis Kelce for Kansas City — and **no Threat designation fired for any player on either side of this game.**

This is worth reading plainly rather than as a null result: several individual numbers in this report are genuinely extreme on their own (KC's WR defense allowing zero touchdowns, ranked 1st; KC's TE defense ranked 30th in yards allowed; Walker's 2nd-ranked rushing production) — but the specific convergence conditions the Threat system checks were not met for any individual player in the exact category pairings it screens. The advantages and tensions documented throughout Sections 3-6 are real and evidence-backed; they simply did not clear this particular deterministic system's thresholds this week. Treat the matchup analysis above, not a Threat-driven angle, as the primary source of actionable insight for this game.

---

## 6. HIDDEN INTELLIGENCE & CONTEXTUAL ANALYSIS

**Finding 1: Los Angeles's defense is quietly a top-10 unit in total yardage, yet the team is 0-5 — and the gap between those two facts traces back to Justin Herbert's own turnover rate, not scheme.** LAC's defense ranks 9th in total yards allowed and 6th in pass yards allowed (205.0/gm) — numbers that would normally support a competitive record. Instead, Herbert carries the league's 2nd-worst interception rate (1.4/gm, 31st) and 3rd-worst sack rate (3.4/gm, 30th). Context Expansion: LAC's own offensive scoring, broken down by opponent tier faced, shows a genuinely backwards pattern — the team actually scored more against the one top-tier defense it has faced this season (23 points, Week 4 vs. Seattle, a game LAC still lost 23-30) than its average against three separate bottom-tier matchups combined (14.7 ppg). A healthy offense should score more consistently against weaker competition, not less. The likely mechanism: turnovers and short fields are erasing whatever the offense and defense combination otherwise produces on a given week, in a way that neither a flat scoring average nor opponent-tier splits can cleanly isolate — this team isn't being out-schemed as much as it is beating itself. For this specific game, that mechanism matters more than Kansas City's considerable statistical edges: Herbert's own takeaway-prone tendency running directly into a KC defense that already generates takeaways at a 7th-ranked clip (1.0 INT/gm) is a realistic path to exactly the kind of result that has defined LAC's season, independent of how competitive the underlying yardage battle actually is. Confidence: MEDIUM — the turnover/scoring disconnect is clearly documented in the data, but the precise causal mechanism (field position specifically, as opposed to some other factor) is inference rather than a directly labeled statistic.

**Finding 2: Kansas City's pass defense is genuinely shutdown on the perimeter but has a clear, documented crack in the slot — and Los Angeles's best tool to exploit it may not be fully available.** KC's WR defense ranks 1st in the league in yards allowed and has surrendered zero wide receiver touchdowns through four games — about as dominant a perimeter coverage profile as exists anywhere in this evidence package. But PFF's slot-specific data tells a different story: KC's defense ranks 28th in yards/game allowed to the slot and 18th in yards per target there, a real, specific weak point hiding inside an otherwise elite unit. Context Expansion: cross-referencing this with LAC's own receiver alignment data shows Ladd McConkey is the only LAC wideout who plays close to half his snaps in the slot (49.0% per PFF) and also carries the best per-route efficiency on the roster (2.1 yards per route run, 73.6 PFF grade) — exactly the profile to attack this specific weakness. But McConkey is dealing with a foot injury this week (Limited practice participation), while LAC's clear #1 target by volume, Tre Harris, is a primarily outside receiver (60.1% wide) who did not practice at all (hamstring) — the player type matched to KC's real weakness is hurt, and the player who isn't practicing is aligned against KC's actual strength. This is a genuine tension the raw matchup numbers alone don't surface: the data says "attack the slot," but the health report complicates whether LAC can actually do that at full strength. Confidence: MEDIUM — the slot/perimeter split itself is well-documented in the PFF data, but how much game-day role McConkey actually holds is uncertain given his own injury status.

**Finding 3: Kansas City's tight end defense is a clear, if underexploited, weakness that Los Angeles's newest and most talented tight end hasn't been featured against yet.** KC's defense ranks 30th in TE yards/game allowed, 29th in TE targets faced (heavily attacked there), and has already surrendered 4 TE touchdowns (28th) — one of the more exploitable individual positional matchups in this entire report. David Njoku, acquired by LAC and active for just two games, carries the best per-route efficiency of any pass-catcher cited anywhere in this breakdown (2.68 yards per route run) and a strong 65.9 PFF grade, but has only drawn 8 targets total (6.3% target share) across his two appearances — LAC's current starting tight end by snap share is Charlie Kolar (64.3% snap rate in his own games), not Njoku. Context Expansion: LAC's own tiered TE production splits show modest but real tier sensitivity (44.7 rec yds/gm vs. bottom-tier defenses, n=3, vs. 36.0 vs. the lone top-tier matchup) — thin samples, but directionally consistent with a unit that produces more against softer competition, which this week's opponent specifically is at tight end. The opportunity here is real on paper but has not yet shown up in results, since LAC simply hasn't featured Njoku at meaningful volume — worth watching as a sleeper role expansion rather than a settled expectation. Confidence: LOW-MEDIUM given the extremely small two-game Njoku sample.

---

## 7. COEUS FINAL READ

**Keys to the Game:**

- **If Justin Herbert's turnover tendency repeats** against a Chiefs defense that already takes the ball away at a 7th-ranked clip, this game is likely to look lopsided regardless of how competitive LAC's underlying defense and yardage totals actually are — Finding 1 above is the single most important lever in this matchup.
- **If Los Angeles's compromised secondary (four hamstring/ankle flags, two DNPs) holds up reasonably well,** LAC's pass defense numbers (6th in yards allowed) suggest a genuinely difficult night is possible for Mahomes on paper; if it doesn't, Kansas City's already-explosive tight end and deep-threat profiles (Kelce, Thornton) have a clear path to a big day.
- **If Los Angeles's offensive line (Joe Alt, Kayode Awosika both DNP) cannot protect Herbert,** expect his already league-worst sack rate to compound his league-worst turnover rate — a combination that would make sustained scoring drives very difficult regardless of how LAC's skill-position matchups otherwise grade out.
- **Watch Kansas City's blitz usage specifically.** The data says blitzing Herbert is a sound individual-matchup decision (his numbers collapse under pressure) while blitzing Mahomes has historically backfired league-wide this season (his numbers spike) — if Kansas City's defensive staff leans into pressure on early downs and Los Angeles's staff holds back from it, that schematic choice alone could meaningfully shape the game independent of underlying talent gaps.

**The Verdict:** The broad thesis from Pregame Briefing — that Kansas City's structural edges are real but Los Angeles's own margin for error (turnovers, protection, secondary health) is the actual swing factor — holds up under the deeper matchup work. Kansas City is the better roster by a wide margin across nearly every clean team-level statistic, and its only notable vulnerabilities (a weak pass rush at 31st in sacks/gm, a leaky tight end defense at 30th in yards allowed, a documented slot-coverage crack) require Los Angeles to execute cleanly to exploit — something this specific roster, banged up at wideout, both lines, and across the defensive backfield, has not shown much capacity to do through five weeks. The single clearest, most specific opportunity for LAC is not its outside receivers against KC's shutdown perimeter coverage, but its tight ends (and specifically an underused David Njoku) against a genuinely poor KC TE defense — paired with staying disciplined with the football, since Herbert's turnover rate running into a Chiefs defense that already takes the ball away effectively is the most realistic way this game gets further out of hand than the underlying yardage numbers alone would suggest.

### Coeus Cheat Sheet

**Team**
- LAC: 0-5 (LLL) | 16.8 ppg (30th) scored / 25.8 ppg (22nd) allowed
- KC: 4-0 (WWW) | 29.5 ppg (5th) scored / 19.2 ppg (7th) allowed

**Passing**
- Justin Herbert (LAC): 187.4 pass yds/gm (29th), 5 TD (25th), 1.4 INT/gm (31st) — vs. KC pass defense allowing 229.0 yds/gm (15th)
- Patrick Mahomes (KC): 259.2 pass yds/gm (10th), 9 TD (12th), 0.5 INT/gm (10th) — vs. LAC pass defense allowing 205.0 yds/gm (6th)

**Rushing**
- Omarion Hampton (LAC): 54.2 rush yds/gm — vs. KC run defense (RB) allowing 69.0 yds/gm (3rd)
- Justin Herbert (LAC, rushing): 28.4 rush yds/gm (real role, not incidental)
- Kenneth Walker III (KC): 134.25 rush yds/gm — vs. LAC run defense (RB) allowing 99.0 yds/gm (19th)

**Receiving**
- Tre Harris (LAC, WR): 45.0 rec yds/gm — vs. KC WR defense allowing 108.5 yds/gm (2nd) [DNP, hamstring]
- Ladd McConkey (LAC, WR): 45.75 rec yds/gm — vs. KC WR defense allowing 108.5 yds/gm (2nd) [Limited, foot]
- Oronde Gadsden II (LAC, TE): 17.2 rec yds/gm — vs. KC TE defense allowing 82.2 yds/gm (30th)
- Xavier Worthy (KC, WR): 33.25 rec yds/gm — vs. LAC WR defense allowing 132.0 yds/gm (11th)
- Tyquan Thornton (KC, WR): 54.75 rec yds/gm — vs. LAC WR defense allowing 132.0 yds/gm (11th)
- Travis Kelce (KC, TE): 61.5 rec yds/gm — vs. LAC TE defense allowing 47.8 yds/gm (13th)

**Team Defense**
- LAC: 205.0 pass yds/gm allowed (6th) | 118.6 rush yds/gm allowed (21st) | 132.0 WR rec yds/gm allowed (11th) | 47.8 TE rec yds/gm allowed (13th)
- KC: 229.0 pass yds/gm allowed (15th) | 92.8 rush yds/gm allowed (7th) | 108.5 WR rec yds/gm allowed (2nd) | 82.2 TE rec yds/gm allowed (30th)

**Down/Distance**
- LAC offense: 34.8% third-down conv. (26th) | LAC defense: 31.2% allowed (5th)
- KC offense: 44.0% third-down conv. (9th) | KC defense: 37.0% allowed (11th)

**Red Zone Play Calling**
- LAC offense: 59.0% run / 41.0% pass (run rank 6th, pass rank 27th) | LAC defense allowed: 56.9% run / 43.1% pass
- KC offense: 44.0% run / 56.0% pass (run rank 23rd, pass rank 10th) | KC defense allowed: 44.4% run / 55.6% pass

**Head-to-Head**
- No 2026 meeting yet between these division rivals — this is the first meeting of the season.

---

EVIDENCE_CHECK
{"claims": [
{"type":"current_opponent","team":"LAC","pos":"TEAM","stat":"ppg","role":"off","claimed_rank":30},
{"type":"current_opponent","team":"LAC","pos":"TEAM","stat":"total_ypg","role":"off","claimed_rank":23},
{"type":"current_opponent","team":"LAC","pos":"TEAM","stat":"pass_ypg","role":"off","claimed_rank":29},
{"type":"current_opponent","team":"LAC","pos":"TEAM","stat":"rush_ypg","role":"off","claimed_rank":9},
{"type":"current_opponent","team":"LAC","pos":"TEAM","stat":"fd_pg","role":"off","claimed_rank":26},
{"type":"current_opponent","team":"LAC","pos":"TEAM","stat":"ppg","role":"def","claimed_rank":22},
{"type":"current_opponent","team":"LAC","pos":"TEAM","stat":"total_ypg","role":"def","claimed_rank":9},
{"type":"current_opponent","team":"LAC","pos":"TEAM","stat":"pass_ypg","role":"def","claimed_rank":6},
{"type":"current_opponent","team":"LAC","pos":"TEAM","stat":"rush_ypg","role":"def","claimed_rank":21},
{"type":"current_opponent","team":"LAC","pos":"TEAM","stat":"fd_pg","role":"def","claimed_rank":10},
{"type":"current_opponent","team":"KC","pos":"TEAM","stat":"ppg","role":"off","claimed_rank":5},
{"type":"current_opponent","team":"KC","pos":"TEAM","stat":"total_ypg","role":"off","claimed_rank":3},
{"type":"current_opponent","team":"KC","pos":"TEAM","stat":"pass_ypg","role":"off","claimed_rank":10},
{"type":"current_opponent","team":"KC","pos":"TEAM","stat":"rush_ypg","role":"off","claimed_rank":4},
{"type":"current_opponent","team":"KC","pos":"TEAM","stat":"fd_pg","role":"off","claimed_rank":10},
{"type":"current_opponent","team":"KC","pos":"TEAM","stat":"ppg","role":"def","claimed_rank":7},
{"type":"current_opponent","team":"KC","pos":"TEAM","stat":"total_ypg","role":"def","claimed_rank":8},
{"type":"current_opponent","team":"KC","pos":"TEAM","stat":"pass_ypg","role":"def","claimed_rank":15},
{"type":"current_opponent","team":"KC","pos":"TEAM","stat":"rush_ypg","role":"def","claimed_rank":7},
{"type":"current_opponent","team":"KC","pos":"TEAM","stat":"fd_pg","role":"def","claimed_rank":13},
{"type":"current_opponent","team":"LAC","pos":"QB","stat":"comp_pct","role":"off","claimed_rank":29},
{"type":"current_opponent","team":"LAC","pos":"QB","stat":"pass_td","role":"off","claimed_rank":25},
{"type":"current_opponent","team":"LAC","pos":"QB","stat":"int_pg","role":"off","claimed_rank":31},
{"type":"current_opponent","team":"LAC","pos":"QB","stat":"sacks_pg","role":"off","claimed_rank":30},
{"type":"current_opponent","team":"KC","pos":"QB","stat":"comp_pct","role":"off","claimed_rank":20},
{"type":"current_opponent","team":"KC","pos":"QB","stat":"pass_td","role":"off","claimed_rank":12},
{"type":"current_opponent","team":"KC","pos":"QB","stat":"ypc","role":"off","claimed_rank":2},
{"type":"current_opponent","team":"KC","pos":"QB","stat":"sacks_pg","role":"off","claimed_rank":5},
{"type":"current_opponent","team":"KC","pos":"QB","stat":"int_pg","role":"off","claimed_rank":10},
{"type":"current_opponent","team":"KC","pos":"QB","stat":"pass_yds","role":"def","claimed_rank":3},
{"type":"current_opponent","team":"KC","pos":"QB","stat":"comp_pct","role":"def","claimed_rank":6},
{"type":"current_opponent","team":"KC","pos":"QB","stat":"pass_td","role":"def","claimed_rank":3},
{"type":"current_opponent","team":"KC","pos":"QB","stat":"sacks_pg","role":"def","claimed_rank":31},
{"type":"current_opponent","team":"KC","pos":"QB","stat":"int_pg","role":"def","claimed_rank":7},
{"type":"current_opponent","team":"KC","pos":"QB","stat":"att_pg","role":"def","claimed_rank":28},
{"type":"current_opponent","team":"LAC","pos":"QB","stat":"pass_yds","role":"def","claimed_rank":8},
{"type":"current_opponent","team":"LAC","pos":"QB","stat":"comp_pct","role":"def","claimed_rank":17},
{"type":"current_opponent","team":"LAC","pos":"QB","stat":"pass_td","role":"def","claimed_rank":17},
{"type":"current_opponent","team":"LAC","pos":"QB","stat":"sacks_pg","role":"def","claimed_rank":15},
{"type":"current_opponent","team":"LAC","pos":"QB","stat":"int_pg","role":"def","claimed_rank":10},
{"type":"current_opponent","team":"LAC","pos":"QB","stat":"att_pg","role":"def","claimed_rank":4},
{"type":"current_opponent","team":"LAC","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":9},
{"type":"current_opponent","team":"LAC","pos":"RB","stat":"carries","role":"off","claimed_rank":10},
{"type":"current_opponent","team":"LAC","pos":"RB","stat":"rush_td","role":"off","claimed_rank":13},
{"type":"current_opponent","team":"LAC","pos":"RB","stat":"rec_ypg","role":"off","claimed_rank":16},
{"type":"current_opponent","team":"LAC","pos":"RB","stat":"rec_td","role":"off","claimed_rank":4},
{"type":"current_opponent","team":"KC","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":2},
{"type":"current_opponent","team":"KC","pos":"RB","stat":"rush_yds","role":"off","claimed_rank":4},
{"type":"current_opponent","team":"KC","pos":"RB","stat":"rush_td","role":"off","claimed_rank":12},
{"type":"current_opponent","team":"KC","pos":"RB","stat":"rec_ypg","role":"off","claimed_rank":6},
{"type":"current_opponent","team":"KC","pos":"RB","stat":"rec_td","role":"off","claimed_rank":3},
{"type":"current_opponent","team":"KC","pos":"RB","stat":"rush_yds","role":"def","claimed_rank":2},
{"type":"current_opponent","team":"KC","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":3},
{"type":"current_opponent","team":"KC","pos":"RB","stat":"carries","role":"def","claimed_rank":2},
{"type":"current_opponent","team":"KC","pos":"RB","stat":"rush_td","role":"def","claimed_rank":13},
{"type":"current_opponent","team":"KC","pos":"RB","stat":"rec_ypg","role":"def","claimed_rank":23},
{"type":"current_opponent","team":"LAC","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":19},
{"type":"current_opponent","team":"LAC","pos":"RB","stat":"carries","role":"def","claimed_rank":29},
{"type":"current_opponent","team":"LAC","pos":"RB","stat":"rush_td","role":"def","claimed_rank":23},
{"type":"current_opponent","team":"LAC","pos":"RB","stat":"rec_ypg","role":"def","claimed_rank":9},
{"type":"current_opponent","team":"LAC","pos":"WR","stat":"rec_ypg","role":"off","claimed_rank":29},
{"type":"current_opponent","team":"LAC","pos":"WR","stat":"rec","role":"off","claimed_rank":32},
{"type":"current_opponent","team":"LAC","pos":"WR","stat":"targets","role":"off","claimed_rank":27},
{"type":"current_opponent","team":"LAC","pos":"WR","stat":"td","role":"off","claimed_rank":32},
{"type":"current_opponent","team":"LAC","pos":"WR","stat":"ypr","role":"off","claimed_rank":5},
{"type":"current_opponent","team":"KC","pos":"WR","stat":"rec_ypg","role":"off","claimed_rank":21},
{"type":"current_opponent","team":"KC","pos":"WR","stat":"targets","role":"off","claimed_rank":32},
{"type":"current_opponent","team":"KC","pos":"WR","stat":"td","role":"off","claimed_rank":15},
{"type":"current_opponent","team":"KC","pos":"WR","stat":"rec_yds","role":"def","claimed_rank":1},
{"type":"current_opponent","team":"KC","pos":"WR","stat":"rec_ypg","role":"def","claimed_rank":2},
{"type":"current_opponent","team":"KC","pos":"WR","stat":"rec","role":"def","claimed_rank":1},
{"type":"current_opponent","team":"KC","pos":"WR","stat":"targets","role":"def","claimed_rank":2},
{"type":"current_opponent","team":"KC","pos":"WR","stat":"td","role":"def","claimed_rank":1},
{"type":"current_opponent","team":"KC","pos":"WR","stat":"yac_pg","role":"def","claimed_rank":6},
{"type":"current_opponent","team":"LAC","pos":"WR","stat":"rec_ypg","role":"def","claimed_rank":11},
{"type":"current_opponent","team":"LAC","pos":"WR","stat":"targets","role":"def","claimed_rank":5},
{"type":"current_opponent","team":"LAC","pos":"WR","stat":"air_pg","role":"def","claimed_rank":4},
{"type":"current_opponent","team":"LAC","pos":"WR","stat":"yac_pg","role":"def","claimed_rank":2},
{"type":"current_opponent","team":"LAC","pos":"TE","stat":"rec_ypg","role":"off","claimed_rank":21},
{"type":"current_opponent","team":"KC","pos":"TE","stat":"rec_ypg","role":"off","claimed_rank":3},
{"type":"current_opponent","team":"KC","pos":"TE","stat":"ypr","role":"off","claimed_rank":1},
{"type":"current_opponent","team":"KC","pos":"TE","stat":"yac_pg","role":"off","claimed_rank":1},
{"type":"current_opponent","team":"KC","pos":"TE","stat":"rec_ypg","role":"def","claimed_rank":30},
{"type":"current_opponent","team":"KC","pos":"TE","stat":"targets","role":"def","claimed_rank":29},
{"type":"current_opponent","team":"KC","pos":"TE","stat":"td","role":"def","claimed_rank":28},
{"type":"current_opponent","team":"LAC","pos":"TE","stat":"rec_ypg","role":"def","claimed_rank":13},
{"type":"current_opponent","team":"LAC","pos":"TE","stat":"targets","role":"def","claimed_rank":6},
{"type":"current_opponent","team":"LAC","pos":"TE","stat":"td","role":"def","claimed_rank":9},
{"type":"current_opponent","team":"LAC","pos":"TEAM","stat":"third_down_conversion_pct","role":"off","claimed_rank":26},
{"type":"current_opponent","team":"LAC","pos":"TEAM","stat":"third_down_pct_allowed","role":"def","claimed_rank":5},
{"type":"current_opponent","team":"KC","pos":"TEAM","stat":"third_down_conversion_pct","role":"off","claimed_rank":9},
{"type":"current_opponent","team":"KC","pos":"TEAM","stat":"third_down_pct_allowed","role":"def","claimed_rank":11},
{"type":"current_opponent","team":"LAC","pos":"TEAM","stat":"red_zone_run_pct","role":"off","claimed_rank":6},
{"type":"current_opponent","team":"LAC","pos":"TEAM","stat":"red_zone_pass_pct","role":"off","claimed_rank":27},
{"type":"current_opponent","team":"KC","pos":"TEAM","stat":"red_zone_run_pct","role":"off","claimed_rank":23},
{"type":"current_opponent","team":"KC","pos":"TEAM","stat":"red_zone_pass_pct","role":"off","claimed_rank":10},
{"type":"current_opponent","team":"KC","pos":"QB","stat":"opp_blitz_rate","role":"def","claimed_rank":17},
{"type":"current_opponent","team":"KC","pos":"QB","stat":"opp_blitz_success_rate","role":"def","claimed_rank":22},
{"type":"current_opponent","team":"LAC","pos":"QB","stat":"opp_blitz_rate","role":"def","claimed_rank":21},
{"type":"current_opponent","team":"LAC","pos":"QB","stat":"opp_blitz_success_rate","role":"def","claimed_rank":8},
{"type":"current_opponent","team":"KC","pos":"WR","stat":"slot_yards_pg","role":"def","claimed_rank":28},
{"type":"current_opponent","team":"KC","pos":"WR","stat":"slot_yards_per_target","role":"def","claimed_rank":18},
{"type":"log_opponent","player":"Justin Herbert","week":4,"stat":"pass_yds","claimed_rank":2},
{"type":"log_opponent","player":"Omarion Hampton","week":4,"stat":"rush_yds","claimed_rank":8}
]}