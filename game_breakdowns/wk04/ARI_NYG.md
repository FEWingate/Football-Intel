# GAME BREAKDOWN: Arizona Cardinals @ New York Giants
### Week 4, 2026 Season | Scheduled 10/04/2026, 1:00 PM ET

**EVIDENCE NOTE:** This game has not been played — there is no box score, line, or weather data available, and none was located via outside lookup for this generation. Importantly, this is *not* a stale prior-season bootstrap: both teams have three real 2026 games in the books (ARI 1-2, NYG 2-1), and the analytics below reflect that actual 2026 season-to-date sample, not 2025 final numbers used as a placeholder. Where 2025 figures appear, they are explicitly labeled and cited only where they add real context beyond what the 2026 sample already shows. Two data gaps are worth flagging up front, both confirmed genuinely empty rather than simply unused: man/zone coverage-rate data (team and player level) and CB/DB matchup rankings are unavailable for this matchup, so Section 4's scheme discussion is necessarily blitz-only rather than coverage-shell-based.

---

## 1. PREGAME BRIEFING

Arizona is 1-2 through three games, with a strange shape to the losses: a 26-14 road win at the Chargers in Week 1, a 7-31 blowout home loss to Seattle in Week 2 (Arizona's offense totaled only 165 yards that day — its toughest defensive test of the season by a wide margin), and a 30-36 shootout loss at San Francisco in Week 3. New York is 2-1: a 28-20 home win over Dallas in Week 1, a 6-28 road blowout loss at the Rams in Week 2, and a defensive grind-it-out 12-7 home win over Tennessee in Week 3. These two teams have not played each other this season, and this is not a division matchup, so there is no head-to-head evidence to draw from — every comparison below is built from each team's performance against its own three opponents.

The broad shape of this matchup starts from two flawed offenses and two shakier-than-their-record-suggests defenses. Arizona's offense ranks middling in scoring (21.0 points per game, 18th) but is a bottom-quartile rushing unit (93.0 rush yds/gm, 25th) that leans on a high-volume, short-area passing game. New York's offense is the least productive unit in the league by total yardage (278.0 yds/gm, 30th) and is bottom-3 in passing (159.7 pass yds/gm, 31st), but it has shown a real, functional rushing identity (118.3 rush yds/gm, 11th). Defensively, New York has held opponents to a respectable 18.3 points/gm (9th) despite the league's worst sack rate, while Arizona's defense has been generous across almost every category. On paper, this profiles as a game where New York tries to lean on its ground game and bend-don't-break defense against a team that is stronger through the air than on the ground, while Arizona looks to its passing attack to carry a matchup where its own defense has few answers if New York's offense finds its footing. Which specific levers actually decide that shape is the subject of the sections below.

---

## 2. INJURY & AVAILABILITY REPORT

No usable injury or availability data exists in the evidence package for this game. The league-wide injury feed for this week (`injuries/wk04.json`) is present but returned zero teams — the evidence package explicitly notes this reflects the file being pulled before this week's practice-report data was published, not that every player is confirmed healthy. There is also no DraftKings slate/Status column data available (`dfs.available: false`), which is Football Intel's usual fallback source for this section. No external web-search lookup was performed for this generation. **Bottom line: player availability for this game is genuinely unknown as of this evidence freeze and should be reverified closer to kickoff before treating any player below as a lock to play.**

---

## 3. MATCHUP STATISTICS

### Arizona Offense
- Scoring: 21.0 ppg (18th) | Total yards: 310.3 ypg (24th) | First downs: 18.0/gm (17th)
- Passing: 217.3 pass yds/gm (18th), 70.1% completion (6th), 4 pass TD through 3 games (1.33/gm, 17th), 0.3 INT/gm (5th, very low), 1.7 sacks allowed/gm (7th)
- Rushing: 93.0 rush yds/gm (25th) — the offense's clear weak point
- Down/distance: 40.9% third-down conversion (15th) on 14.7 attempts/gm; 100% fourth-down conversion (small sample, 8.0 situations/gm, 12.5% go-for-it rate)
- Red zone play-calling: 55.6% pass rate once inside the 20 (11th-highest) vs. 44.4% run rate (21st) — a pass-leaning red-zone identity, on 12.0 red-zone plays/gm
- Contextual splits: Arizona's passing production is opponent-sensitive — 95.0 pass yds/gm against its one top-tier defensive test this season (Seattle, Week 2) vs. 278.5 pass yds/gm against its two mid-tier tests (Chargers, 49ers); team-wide scoring followed the same pattern (18.5 ppg vs. top-tier, 26.0 vs. mid-tier, n=1).

### Arizona Defense
- Scoring allowed: 27.0 ppg (24th) | Total yards allowed: 374.7 ypg (25th) | First downs allowed: 19.0/gm (23rd)
- Pass defense: 247.0 pass yds/gm allowed (23rd), but only 26.7 attempts/gm faced (2nd-fewest) — teams aren't slinging it against Arizona in raw volume, yet 14.5 yards allowed per completion (32nd, worst in the league) and 8 pass TDs allowed through 3 games (30th) — when passes land, they land big or in the end zone. Pass rush is modest (1.3 sacks/gm, 26th).
- Run defense (team-wide): 127.7 rush yds/gm allowed (26th). Specifically against running backs, the number is a somewhat less extreme 100.3 rush yds/gm (21st) — the team-wide figure (which includes QB scrambles and broader play types) reads worse than the RB-specific number, worth keeping straight since they answer slightly different questions.
- Down/distance: 44.8% third-down conversion allowed (23rd) on 9.7 attempts/gm faced; only 55.2% stop rate
- Red zone play-calling allowed: a striking 65.0% run rate allowed (2nd-highest in the NFL) against just 35.0% pass rate allowed (31st, among the lowest) — see Section 6 for why this is more interesting than it first looks
- Contextual splits (RB): against running backs specifically, Arizona has allowed 63 rush yds (top-tier defense sample, n=1, Week 2), scaling to a mid-tier sample; the receiving-back numbers are notably stingy — only 51 rec yds and 6 total receptions allowed to RBs through 3 games (4th- and 1st-fewest, respectively)

### New York Offense
- Scoring: 15.3 ppg (28th) | Total yards: 278.0 ypg (30th) | First downs: 16.7/gm (21st)
- Passing: 159.7 pass yds/gm (31st, 3rd-worst in the league), 61.4% completion (21st), 3 pass TD through 3 games (27th), 2.3 sacks allowed/gm (19th)
- Rushing: 118.3 rush yds/gm (11th) — comfortably the offense's strength
- Down/distance: 42.1% third-down conversion (11th, solid) on 12.7 attempts/gm; 50.0% fourth-down conversion on a small sample (7.3 situations/gm, 9.1% go-for-it rate)
- Red zone play-calling: 56.5% run rate once inside the 20 (6th-highest) vs. 43.5% pass rate (27th) — the inverse identity of Arizona's offense, and consistent with a team leaning on its run game to mask a broken passing attack
- Contextual splits: passing production has actually held up against tougher defenses so far (159.7 pass yds/gm across all three "top"-tier defensive tests faced) — not because the passing game is good, but because the sample so far happens to be entirely against good-to-elite pass defenses (Rams, Titans, Cowboys all graded top-tier for New York's splits)

### New York Defense
- Scoring allowed: 18.3 ppg (9th, a real team strength) | Total yards allowed: 332.0 ypg (12th) | First downs allowed: 18.0/gm (17th)
- Pass defense: 227.7 pass yds/gm allowed (16th), 7 pass TDs allowed through 3 games (29th, concerning), but **only 0.3 sacks/gm — dead last in the NFL (31st)**. The unit is getting results (16th in yardage) without generating pressure, which matters for how it defends this specific matchup (Section 6).
- Run defense (team-wide): 104.3 rush yds/gm allowed (13th, solid). Specifically against running backs: 99.3 rush yds/gm allowed (20th) — again the position-specific number reads a bit worse than the team-wide figure, the opposite direction of Arizona's split above, but the two run-defense views tell a broadly similar "middle of the pack" story here.
- Down/distance: 54.5% third-down conversion allowed (30th, a real soft spot) on 11.0 attempts/gm faced; only 45.5% stop rate
- Red zone play-calling allowed: 64.0% pass rate allowed (6th-highest) against just 36.0% run rate allowed (27th) — opponents are choosing to throw at New York in the red zone far more than they run, the inverse of Arizona's defensive profile above

---

## 4. MATCHUP INTELLIGENCE

### Quarterbacks

**Jacoby Brissett (ARI)** is the unquestioned starter — 100% snap share in all three games, and Arizona's only real quarterback with a functioning 2026 track record (backups Gardner Minshew and Carson Beck are both roster-only with zero 2026 snaps). His season averages (217.3 pass yds/gm, 18th; 70.1% completion, 6th) sit alongside two real red flags: a 14.5 opponent-allowed ypc... actually his own ypc (yards per completion) is 8.0, ranked 32nd-worst in the league — meaning even with strong volume and accuracy, his completions are traveling short. That fits Arizona's offensive shape: a check-down-heavy attack funneling heavily through Trey McBride (below). *(2025: 240.4 pass yds/gm, 64.95% completion, 3.07 sacks/gm allowed — his sack rate has nearly halved this season, from 3.07/gm to 1.67/gm, while his completion rate has climbed 5 points, a real, meaningful efficiency jump worth noting rather than reading his hot start as a one-year mirage.)* Brissett's two road starts this season (Week 1 at the Chargers, Week 3 at San Francisco) were both against mid-tier pass defenses — exactly what New York (16th in pass yards allowed) projects as. In those two road/mid-tier starts he's averaged 278.5 pass yds/gm, 73.0% completion, and 1.5 pass TD/gm (n=2) — a notably stronger number than his season average, though the sample is thin (MEDIUM confidence). He is considerably worse under pressure (-0.208 EPA/play blitzed vs. +0.189 unblitzed, 59.3% completion blitzed vs. 70.2% unblitzed, n=27 vs. 94) — New York's own blitz tendency against this specific matchup isn't reliably computed in this evidence package (flagged below), but the vulnerability itself is real and opponent-independent.

**Jameis Winston (NYG)** is the current starter by both recent usage and depth chart (pos-rank 1, current as of 9/29). He wasn't Week 1's starter, however — Jaxson Dart opened the season (100% snap share Week 1) before playing just 12% of Week 2's snaps, with Winston taking over from that point and starting 88% and 100% of snaps in Weeks 2-3 respectively. Dart now sits at pos-rank 3 on the depth chart, behind both Winston and a newly-added J.J. McCarthy (pos-rank 2, zero snaps with New York yet — a roster-only addition worth naming but not a plausible factor this week given his depth-chart slot). Winston's two starts have been rough: 114.5 pass yds/gm, 51.0% completion, **zero passing touchdowns across two starts**, 2.5 sacks/gm allowed. *(2025: 189.0 pass yds/gm, 56.1% completion across a 3-game relief stint — even that modest bar is one he hasn't cleared yet in 2026.)* His lone home start this season (Week 3 vs. Tennessee, a top-tier pass defense) produced 118 yards on 63.6% completion. New York doesn't yet have a home start against a bottom-tier pass defense to compare to — Arizona (23rd against the pass) would be that test — so there's no precedent sample to lean on here; treat his outlook as LOW confidence given two winless-TD starts and the small sample. Pressure makes an already-poor situation worse: 29.4% completion and a brutal -0.978 EPA/play blitzed (n=17) vs. still-negative -0.161 EPA/play unblitzed (n=37) — Winston has not found answers to pressure of any kind so far this season.

### Running Backs

**Jeremiyah Love (ARI)**, the rookie lead back, has emerged as the clear early-down and passing-down option — 52.6% rush share, 53.33 rush yds/gm on the season, with a contact-efficiency profile worth flagging: 1.85 yards after contact per carry against 1.65 yards before contact, meaning more of his production is coming from what he creates himself than from blocking, with 0.5 broken tackles/gm on top of it. His road average this season (65.5 rush yds/gm, 4.1 ypc, n=2) is stronger than his season average, and his one game against a mid-tier run defense (New York projects as mid-tier, 13th team-wide) produced 90.0 rush yds/gm on 4.3 ypc (n=1, LOW confidence given the single-game sample, but directionally favorable).

**Cam Skattebo (NYG)** is comfortably New York's most complete offensive weapon — 54.9% rush share, 59.0 rush yds/gm season average, a real receiving role (19.67 rec yds/gm), and a dominant red-zone role (69.2% of the team's red-zone carries). His contact numbers are notable: 2.6 yards after contact per carry against only 1.3 yards before contact — he is creating almost twice as much yardage himself as his blocking is providing, with 1.5 broken tackles/gm. Both of his career meaningful home samples came against bottom-tier run defenses (Dallas Week 1, Tennessee Week 3) and in that exact home + bottom-tier combination he has averaged **70.5 rush yds/gm on 3.7 ypc, 19.0 carries/gm** (n=2) — and this week's matchup is almost a direct repeat: Arizona's run defense ranks 26th team-wide (bottom-tier) and sits at home for Skattebo. This is one of the cleanest matchup precedents in this report (MEDIUM-HIGH confidence). *(2025: 51.25 rush yds/gm, 53.3% red-zone carry share — he was already New York's clear lead back last year too; this isn't a new role, just a continuation.)*

Behind him, **Najee Harris** has played only two games (18-22% snap share) in a diminished complementary role, and **Devin Singletary** carries the clearer passing-down assignment (25.0% red-zone target share on limited volume).

### Wide Receivers / Tight Ends

**Michael Wilson (ARI)** is Arizona's clear WR1 by usage — 90.7% snap share, 27.4% target share, 54.33 rec yds/gm. His road/mid-tier combination this season (the exact site-and-tier combination New York represents) has produced 72.5 rec yds/gm on 8.0 rec/gm and 12.0 targets/gm (n=2) — a strong number, and it also carries this week's Threat designation (Section 5). *(2025: 59.18 rec yds/gm, 20.4% target share — his role has grown meaningfully year over year.)*

**Marvin Harrison Jr. (ARI)** presents one of this report's more surprising findings: despite a near-identical snap share to Wilson (76.7%), his target share sits at just 8.0% and 24.33 rec yds/gm — a far smaller role than his draft pedigree would suggest, and a real decline from *(2025: 50.67 rec yds/gm, 18.0% target share)*. See Section 6 for the full year-over-year context on this role split.

**Trey McBride (ARI)** is the offense's true focal point — 30.1% target share, 8.67 rec/gm (a genuinely elite per-game reception rate), 70.33 rec yds/gm, and a massive 40.0% red-zone target share. His road/mid-tier combination (again, New York's exact profile) has produced 85.0 rec yds/gm on 9.0 rec/gm and 12.0 targets/gm (n=2). *(2025: 72.88 rec yds/gm, 27.4% target share across a full 17-game season — his current role is essentially a continuation of an already-elite, already-established workload, not a hot streak.)* He carries this week's most notable Threat designation (Section 5).

**Malik Nabers (NYG)** is New York's clear WR1 (23.2% target share, 32.0 rec yds/gm), though his 2026 usage is down from *(2025: 67.75 rec yds/gm, 28.7% target share across an admittedly small 4-game sample)* — worth watching given New York's broader passing-game struggles. He has no home + bottom-tier-defense sample yet this season (his tier splits so far are "top," n=1, and "mid," n=1) — Arizona's pass defense against wide receivers (23rd, 167.7 rec yds/gm allowed) would be his first bottom-tier test, so there's real optimism in the matchup without a precedent to confirm it (LOW-MEDIUM confidence).

**Malachi Fields (NYG)**, a true rookie with no 2025 track record to cite, carries a real complementary role (14.6% target share, 24.67 rec yds/gm) but the same bottom-tier-sample gap as Nabers.

**Isaiah Likely (NYG)** is comfortably New York's most heavily used receiving weapon at any position by target share — 28.0% team target share, 7.67 targets/gm, 41.33 rec yds/gm, and a 40.0% red-zone target share. His results have been volatile: a 78-yard, 2-touchdown explosion in Week 1 (home, mid-tier defense) followed by modest 33- and 13-yard outings against two top-tier defenses. He has no home + bottom-tier sample yet (Arizona's tight end defense, 23rd, would be his first), but the red-zone role alone provides a real floor regardless of matchup tier. He carries this week's third Threat designation (Section 5).

### Scheme Notes — Blitz Only (Coverage-Shell Data Unavailable)

Man/zone coverage splits and CB/DB rankings returned genuinely empty for this matchup (`coverage_qb`, `coverage_wr`, `coverage_te`, `team_coverage_rate`, and `cb_db_rankings` are all blank in the evidence package) — no individual coverage-shell or corner-matchup detail is possible this week. Blitz data is available but with an important caveat: the opponent-context blitz fields (`opp_blitz_rate`, `opp_blitz_rank`) attached to both teams' blitz records are tagged to each team's real *prior* opponents this season, not recomputed for this Arizona-New York pairing — they are explicitly flagged in the evidence as unreliable for this matchup and are not used below. What remains valid and opponent-independent is each player's own performance split when blitzed vs. not: Brissett's drop-off under pressure (above) and Winston's far steeper one are both real, standalone findings regardless of how often either defense actually blitzes this specific week.

---

## 5. THREAT INTELLIGENCE

Football Intel's deterministic Threat Engine flags a player when two independent conditions converge in the same statistical category: the player's own **season rank** in that category clears a threshold, **and** the upcoming opponent's defensive rank in that *same* category is weak enough to clear a matching threshold. Neither signal alone is sufficient — it's the convergence that matters. Three fixed tiers exist: **Nuclear** (player ranks top 3 in the category AND the opponent's defense ranks 30th or worse in that category), **Elite** (player top 5, defense 28th or worse), and **Standard** (player top 10, defense 23rd or worse). A "Double" designation means exactly one category fully converged; "Triple" means one category converged plus a second category where the player's own rank alone clears the threshold even though the defense side doesn't quite meet it; "Quadruple" means two or more categories fully converged.

Three Standard-tier Threats fired for this matchup, all at the receiving positions:

**Michael Wilson (ARI, WR) — Standard, Double, converged on receptions.** Wilson's 6.0 receptions/gm ranks 8th among all qualifying receivers leaguewide (clears the top-10 threshold); New York's defense ranks 25th in receptions allowed to wide receivers (12.3/gm allowed), clearing the 23rd-or-worse threshold. This is a volume signal specifically, not a yardage one — his receiving yardage rank (26th) doesn't clear the player-side threshold on its own, so only the reception category converged.

**Trey McBride (ARI, TE) — Standard, Triple, converged on receptions, extra category in receiving yards.** His 8.67 receptions/gm ranks 1st among tight ends leaguewide (comfortably top 10); New York's tight-end defense ranks 24th in receptions allowed (clears 23rd-or-worse). His receiving-yardage rank (3rd) also clears the player-side threshold on its own, but New York's yardage-allowed rank to tight ends (15th) doesn't clear 23rd-or-worse, so that category counts as an "extra" rather than a second full convergence.

**Isaiah Likely (NYG, TE) — Standard, Triple, converged on receiving yards, extra category in receptions.** His 41.3 rec yds/gm ranks 10th among tight ends (clears top 10); Arizona's tight-end defense ranks 23rd in yards allowed (62.3/gm, right at the threshold). His reception rank (4th) also clears the player-side bar alone, but Arizona's reception-allowed rank to tight ends (17th) doesn't meet the 23rd-or-worse bar, making it an extra category rather than a full second convergence.

A season-long Threat designation reflects statistical stability, not a guarantee against a specific game plan — worth flagging real tension in two of these three cases. Wilson's Threat is built on a favorable *reception-volume* matchup, but New York's yardage-allowed number to wide receivers (19th) is closer to average, meaning big plays specifically aren't obviously there even if catches are. Likely's Threat clears on yardage specifically, but his most recent two games (against top-tier tight end defenses) were both modest — the red-zone role underpinning his profile is more stable than his per-game yardage has been. No Threats fired for either starting quarterback, either running back, or Arizona's WR2 (Harrison) — their absence doesn't mean the absence of a real edge (Section 4 covers real, non-Threat-driven advantages for several of these players), only that this specific convergence system's thresholds weren't met.

---

## 6. HIDDEN INTELLIGENCE & CONTEXTUAL ANALYSIS

**Finding 1: New York's red-zone defense is being attacked almost exclusively through the air, and its league-worst pass rush is very likely why — which lines up directly with Trey McBride's Threat designation.** New York allows a red-zone pass rate of 64.0% (6th-highest in the NFL) against just 36.0% run rate allowed (27th) — opponents are choosing to throw once inside the 20 far more than league average. This isn't happening in a vacuum: New York's defense has recorded just 0.3 sacks/gm all season, dead last in the league (31st) — the shortened field of the red zone, where a pass rush's value is already compressed by the shorter throw windows a quarterback needs to beat, appears to be magnifying rather than masking that lack of pressure, and opposing play-callers have noticed. This matters directly for Arizona: its own red-zone identity already leans pass (55.6% rate, 11th-highest), and Trey McBride already carries a 40.0% red-zone target share on top of his Threat designation built on receiving-category convergence. The two offensive and defensive tendencies point at exactly the same outcome — expect Arizona to target McBride disproportionately once it reaches New York's red zone, and expect that decision to be rewarded given the funnel New York's opponents have already exploited all season. Confidence: MEDIUM — the two underlying tendency splits are real and specific, but the causal link between the sack rate and the red-zone pass rate is an inference, not a directly labeled data point.

**Finding 2: Arizona's defense gets run at disproportionately in the red zone despite ranking only middling specifically against running backs — the mirror image of Finding 1, and it lines up with Cam Skattebo's already-strong matchup precedent.** Arizona allows a red-zone run rate of 65.0% (2nd-highest in the league) against just 35.0% pass rate allowed (31st, among the lowest) — teams are choosing to run at Arizona in the red zone far more than average, even though Arizona's run defense specifically against backs (100.3 yds/gm allowed, 21st) isn't an extreme outlier the way its team-wide figure (127.7 yds/gm, 26th) is. This suggests opposing coordinators are treating Arizona's shortened-field run fits as more exploitable than the season-long, whole-field numbers alone would indicate — plausibly tied to the same lack of a disruptive pass rush (1.3 sacks/gm, 26th) that makes Arizona's defense generally vulnerable once a play develops. This directly reinforces Cam Skattebo's case: his own home + bottom-tier precedent (70.5 rush yds/gm across his only two such games, both this season) already projects favorably against Arizona's bottom-tier, team-wide run-defense rank (26th) — and his dominant 69.2% red-zone carry share means this funnel tendency should specifically inflate his goal-line opportunity, not just his between-the-20s volume. Confidence: MEDIUM-HIGH — both underlying red-zone and run-defense figures are real and specific, and the Skattebo precedent adds real corroborating evidence rather than resting on inference alone.

**Finding 3: Marvin Harrison Jr.'s role has quietly inverted year-over-year, and it isn't visible from his snap count alone.** Harrison is playing 76.7% of Arizona's offensive snaps this season — nearly identical to Michael Wilson's 90.7% — yet his target share has fallen to just 8.0% (24.33 rec yds/gm), down sharply from *(2025: 18.0% target share, 50.67 rec yds/gm)*. Over that same stretch, Wilson's target share has climbed from *(2025: 20.4%)* to 27.4% in 2026 — a real, near-complete reversal of the two receivers' pecking order, invisible to anyone checking only playing-time numbers, since both players are on the field almost equally often. This matters directly for this game: if New York's game-planning leans on scouting reports or last year's tape, it may be structured to account for a more featured Harrison than currently exists — potentially leaving extra coverage attention on Wilson's route concepts specifically, which would only reinforce the volume advantage already described in his Threat designation (Section 5), while affording Harrison quieter, lower-leverage opportunities if New York's coverage shades away from him expecting less. Confidence: MEDIUM — the season-over-season shift itself is clear and well-supported by real target-share numbers in both years, but how (or whether) New York's coaching staff has actually adjusted to it is inference, not confirmed evidence.

---

## 7. COEUS FINAL READ

**Keys to the Game:**
- If Arizona sustains drives into New York's red zone, Trey McBride profiles as the single most likely beneficiary of any team in this game — his Threat designation, his 40.0% red-zone target share, and New York's real red-zone pass-funnel tendency (Finding 1) all point the same direction.
- If New York leans on Cam Skattebo early and often, particularly in short-yardage and red-zone situations, his own home + bottom-tier precedent (70.5 rush yds/gm) and Arizona's red-zone run funnel (Finding 2) both argue this is New York's cleanest path to sustained offense, especially with Jameis Winston still without a passing touchdown through two starts.
- If either quarterback faces increased pressure, both show real, opponent-independent efficiency collapses when blitzed — and neither defense (Arizona 26th in sacks, New York dead last at 31st) is built to generate that pressure with a standard four-man rush, making blitz-call volume, not raw front-four ability, the more relevant lever for both defensive staffs.

**The Verdict:** This looks less like a game decided by which team is simply "better" on paper and more like one decided by which offense exploits its opponent's specific, identifiable funnel first. Arizona's passing operation — efficient in volume and accuracy but short in depth (32nd in yards per completion) — has its likeliest life raft in McBride against a defense that surrenders exactly the kind of red-zone passing volume he thrives on. New York's offense, meanwhile, has far less margin for error through the air (31st in the league) and needs Skattebo to be the workhorse his own matchup history already suggests he can be against this specific caliber of run defense. Given Winston's scoreless start to his 2026 tenure and Arizona's offense carrying the more proven, more productive identity of the two, Arizona enters with a real, evidence-backed edge — but not an overwhelming one, given its own defense's real generosity in exactly the phase (red zone, pressure) where New York's Skattebo-centric approach is built to live.

### Coeus Cheat Sheet

**Team**
- ARI: 1-2 (3 GP) | 21.0 ppg (18th) / 27.0 ppg allowed (24th)
- NYG: 2-1 (3 GP) | 15.3 ppg (28th) / 18.3 ppg allowed (9th)

**Passing**
- Jacoby Brissett (ARI): 217.3 pass yds/gm (18th), 70.1% comp (6th), 4 pass TD (3 gm), 0.3 INT/gm (5th) — opp D allows 227.7 pass yds/gm (16th)
- Jameis Winston (NYG): 114.5 pass yds/gm (2 starts), 51.0% comp, 0 pass TD, 0.5 INT/gm — opp D allows 247.0 pass yds/gm (23rd)

**Rushing**
- Jeremiyah Love (ARI): 53.33 rush yds/gm, 52.6% rush share — opp D allows 104.3 rush yds/gm (13th)
- Cam Skattebo (NYG): 59.0 rush yds/gm, 54.9% rush share, 69.2% RZ carry share — opp D allows 127.7 rush yds/gm (26th)

**Receiving**
- Michael Wilson (ARI): 54.33 rec yds/gm, 27.4% target share
- Trey McBride (ARI, TE): 70.33 rec yds/gm, 30.1% target share
- Malik Nabers (NYG): 32.0 rec yds/gm, 23.2% target share
- Isaiah Likely (NYG, TE): 41.33 rec yds/gm, 28.0% target share

**Team Defense**
- ARI def: 247.0 pass yds/gm allowed (23rd) | 127.7 rush yds/gm allowed (26th, team-wide) | 167.7 WR rec yds/gm allowed (23rd) | coverage rate data unavailable
- NYG def: 227.7 pass yds/gm allowed (16th) | 104.3 rush yds/gm allowed (13th, team-wide) | 155.7 WR rec yds/gm allowed (19th) | coverage rate data unavailable

**Down/Distance**
- ARI offense: 40.9% 3rd-down conv (15th) | ARI defense: 44.8% allowed (23rd)
- NYG offense: 42.1% 3rd-down conv (11th) | NYG defense: 54.5% allowed (30th)

**Red Zone Play Calling**
- ARI offense: 55.6% pass (11th) / 44.4% run (21st)
- ARI defense allowed: 35.0% pass (31st) / 65.0% run (2nd)
- NYG offense: 43.5% pass (27th) / 56.5% run (6th)
- NYG defense allowed: 64.0% pass (6th) / 36.0% run (27th)

**Head-to-Head**
- No meeting between these two teams this season; not a division game.

---

EVIDENCE_CHECK
{"claims": [
{"type": "current_opponent", "team": "ARI", "pos": "TEAM", "stat": "ppg", "role": "off", "claimed_rank": 18},
{"type": "current_opponent", "team": "ARI", "pos": "TEAM", "stat": "total_ypg", "role": "off", "claimed_rank": 24},
{"type": "current_opponent", "team": "ARI", "pos": "TEAM", "stat": "rush_ypg", "role": "off", "claimed_rank": 25},
{"type": "current_opponent", "team": "ARI", "pos": "TEAM", "stat": "fd_pg", "role": "off", "claimed_rank": 17},
{"type": "current_opponent", "team": "ARI", "pos": "QB", "stat": "pass_ypg", "role": "off", "claimed_rank": 18},
{"type": "current_opponent", "team": "ARI", "pos": "QB", "stat": "comp_pct", "role": "off", "claimed_rank": 6},
{"type": "current_opponent", "team": "ARI", "pos": "QB", "stat": "pass_td", "role": "off", "claimed_rank": 17},
{"type": "current_opponent", "team": "ARI", "pos": "QB", "stat": "int_pg", "role": "off", "claimed_rank": 5},
{"type": "current_opponent", "team": "ARI", "pos": "QB", "stat": "sacks_pg", "role": "off", "claimed_rank": 7},
{"type": "current_opponent", "team": "ARI", "pos": "QB", "stat": "ypc", "role": "off", "claimed_rank": 32},
{"type": "current_opponent", "team": "ARI", "pos": "TEAM", "stat": "ppg", "role": "def", "claimed_rank": 24},
{"type": "current_opponent", "team": "ARI", "pos": "TEAM", "stat": "total_ypg", "role": "def", "claimed_rank": 25},
{"type": "current_opponent", "team": "ARI", "pos": "TEAM", "stat": "fd_pg", "role": "def", "claimed_rank": 23},
{"type": "current_opponent", "team": "ARI", "pos": "QB", "stat": "pass_ypg", "role": "def", "claimed_rank": 23},
{"type": "current_opponent", "team": "ARI", "pos": "QB", "stat": "att_pg", "role": "def", "claimed_rank": 2},
{"type": "current_opponent", "team": "ARI", "pos": "QB", "stat": "ypc", "role": "def", "claimed_rank": 32},
{"type": "current_opponent", "team": "ARI", "pos": "QB", "stat": "pass_td", "role": "def", "claimed_rank": 30},
{"type": "current_opponent", "team": "ARI", "pos": "QB", "stat": "sacks_pg", "role": "def", "claimed_rank": 26},
{"type": "current_opponent", "team": "ARI", "pos": "TEAM", "stat": "rush_ypg", "role": "def", "claimed_rank": 26},
{"type": "current_opponent", "team": "ARI", "pos": "RB", "stat": "rush_yds", "role": "def", "claimed_rank": 21},
{"type": "current_opponent", "team": "ARI", "pos": "RB", "stat": "rec_yds", "role": "def", "claimed_rank": 4},
{"type": "current_opponent", "team": "ARI", "pos": "RB", "stat": "rec", "role": "def", "claimed_rank": 1},
{"type": "current_opponent", "team": "ARI", "pos": "WR", "stat": "rec_yds", "role": "def", "claimed_rank": 23},
{"type": "current_opponent", "team": "ARI", "pos": "WR", "stat": "rec", "role": "def", "claimed_rank": 5},
{"type": "current_opponent", "team": "ARI", "pos": "WR", "stat": "td", "role": "def", "claimed_rank": 31},
{"type": "current_opponent", "team": "ARI", "pos": "TE", "stat": "rec_yds", "role": "def", "claimed_rank": 23},
{"type": "current_opponent", "team": "ARI", "pos": "TE", "stat": "rec", "role": "def", "claimed_rank": 17},
{"type": "current_opponent", "team": "NYG", "pos": "TEAM", "stat": "ppg", "role": "off", "claimed_rank": 28},
{"type": "current_opponent", "team": "NYG", "pos": "TEAM", "stat": "total_ypg", "role": "off", "claimed_rank": 30},
{"type": "current_opponent", "team": "NYG", "pos": "TEAM", "stat": "rush_ypg", "role": "off", "claimed_rank": 11},
{"type": "current_opponent", "team": "NYG", "pos": "TEAM", "stat": "fd_pg", "role": "off", "claimed_rank": 21},
{"type": "current_opponent", "team": "NYG", "pos": "QB", "stat": "pass_ypg", "role": "off", "claimed_rank": 31},
{"type": "current_opponent", "team": "NYG", "pos": "QB", "stat": "comp_pct", "role": "off", "claimed_rank": 21},
{"type": "current_opponent", "team": "NYG", "pos": "QB", "stat": "pass_td", "role": "off", "claimed_rank": 27},
{"type": "current_opponent", "team": "NYG", "pos": "QB", "stat": "sacks_pg", "role": "off", "claimed_rank": 19},
{"type": "current_opponent", "team": "NYG", "pos": "TEAM", "stat": "ppg", "role": "def", "claimed_rank": 9},
{"type": "current_opponent", "team": "NYG", "pos": "TEAM", "stat": "total_ypg", "role": "def", "claimed_rank": 12},
{"type": "current_opponent", "team": "NYG", "pos": "TEAM", "stat": "fd_pg", "role": "def", "claimed_rank": 17},
{"type": "current_opponent", "team": "NYG", "pos": "QB", "stat": "pass_ypg", "role": "def", "claimed_rank": 16},
{"type": "current_opponent", "team": "NYG", "pos": "QB", "stat": "pass_td", "role": "def", "claimed_rank": 29},
{"type": "current_opponent", "team": "NYG", "pos": "QB", "stat": "sacks_pg", "role": "def", "claimed_rank": 31},
{"type": "current_opponent", "team": "NYG", "pos": "TEAM", "stat": "rush_ypg", "role": "def", "claimed_rank": 13},
{"type": "current_opponent", "team": "NYG", "pos": "RB", "stat": "rush_yds", "role": "def", "claimed_rank": 20},
{"type": "current_opponent", "team": "NYG", "pos": "WR", "stat": "rec_yds", "role": "def", "claimed_rank": 19},
{"type": "current_opponent", "team": "NYG", "pos": "WR", "stat": "rec", "role": "def", "claimed_rank": 25},
{"type": "current_opponent", "team": "NYG", "pos": "WR", "stat": "td", "role": "def", "claimed_rank": 27},
{"type": "current_opponent", "team": "NYG", "pos": "TE", "stat": "rec_yds", "role": "def", "claimed_rank": 15},
{"type": "current_opponent", "team": "NYG", "pos": "TE", "stat": "rec", "role": "def", "claimed_rank": 24},
{"type": "current_opponent", "team": "ARI", "pos": "TEAM", "stat": "third_down_conversion_pct", "role": "off", "claimed_rank": 15},
{"type": "current_opponent", "team": "ARI", "pos": "TEAM", "stat": "third_down_pct_allowed", "role": "def", "claimed_rank": 23},
{"type": "current_opponent", "team": "NYG", "pos": "TEAM", "stat": "third_down_conversion_pct", "role": "off", "claimed_rank": 11},
{"type": "current_opponent", "team": "NYG", "pos": "TEAM", "stat": "third_down_pct_allowed", "role": "def", "claimed_rank": 30},
{"type": "current_opponent", "team": "ARI", "pos": "TEAM", "stat": "red_zone_pass_pct", "role": "off", "claimed_rank": 11},
{"type": "current_opponent", "team": "ARI", "pos": "TEAM", "stat": "red_zone_run_pct", "role": "off", "claimed_rank": 21},
{"type": "current_opponent", "team": "ARI", "pos": "TEAM", "stat": "red_zone_run_pct_allowed", "role": "def", "claimed_rank": 2},
{"type": "current_opponent", "team": "ARI", "pos": "TEAM", "stat": "red_zone_pass_pct_allowed", "role": "def", "claimed_rank": 31},
{"type": "current_opponent", "team": "NYG", "pos": "TEAM", "stat": "red_zone_run_pct", "role": "off", "claimed_rank": 6},
{"type": "current_opponent", "team": "NYG", "pos": "TEAM", "stat": "red_zone_pass_pct", "role": "off", "claimed_rank": 27},
{"type": "current_opponent", "team": "NYG", "pos": "TEAM", "stat": "red_zone_pass_pct_allowed", "role": "def", "claimed_rank": 6},
{"type": "current_opponent", "team": "NYG", "pos": "TEAM", "stat": "red_zone_run_pct_allowed", "role": "def", "claimed_rank": 27}
]}