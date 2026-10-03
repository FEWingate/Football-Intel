# GAME BREAKDOWN: Los Angeles Chargers @ Seattle Seahawks
### Week 4, 2026 Season | Scheduled 10/04/2026, 4:25 PM ET

**EVIDENCE NOTICE:** This game has not been played. The evidence package supplied for this matchup is internally labeled "BOOTSTRAP," but unlike a typical bootstrap package (a hypothetical pairing propped up entirely on a prior season's final numbers), the underlying data here is each team's own actual **2026 season-to-date performance through three games** — real Weeks 1-3 results, not backfilled 2025 stats. Where 2025 figures are cited below, they are explicitly labeled as such and used only where they add genuine context to a real 2026 trend. Separately: this package's rank-shift fields (`rank_shifts`) have no computed 2026 half for any category — every `rank_2026` value returned null — so no season-over-season rank-shift claims appear anywhere in this report; only real, current 2026 ranks are cited. No CB/DB ranking data and no man/zone coverage-shell data (player-level or team-level `team_coverage_rate`) were present in this evidence package for either team — both fields returned genuinely empty, not merely unchecked, so neither appears in this report.

---

## 1. PREGAME BRIEFING

Los Angeles arrives at 0-3, having lost three straight to open the season. The offense ranks 29th in scoring at 14.7 points per game, and the defense hasn't offered much of a lifeline either, allowing 25.3 points per game (20th). Seattle is 2-1, riding one of the more lopsided statistical profiles in the league: a top-half offense (25.0 ppg, 13th) paired with a defense that is, through three games, the best in football by total yardage allowed (239.0 yards/game, 1st) and pass defense specifically (152.0 pass yards/game allowed, 1st).

This is not a division matchup, and there is no meeting between these two teams earlier this season to draw head-to-head evidence from — this will be their first meeting of 2026.

Broad thesis, not yet the verdict: this profiles as a game shaped by a genuine mismatch between LA's already-struggling offense and a historically dominant Seattle defense, while Seattle's own situation carries real internal uncertainty — a muddled quarterback picture between Drew Lock and Sam Darnold, and a three-man backfield committee that hasn't settled into a clear pecking order. Whether Seattle's own messiness is enough to keep this competitive against a Chargers team that is average-to-below-average nearly everywhere is the central question this report works through.

---

## 2. INJURY & AVAILABILITY REPORT

The evidence package's injury feed returned **no usable data for this week** — the source notes explicitly state that `injuries/wk04.json` exists but reports zero teams leaguewide, meaning the real practice-week injury report likely had not been published yet when this evidence was compiled. This should be read as **genuinely unavailable, not as a clean bill of health** for either roster. No supplementary source was available to fill this specific gap.

One real availability-adjacent question does exist in the evidence, though it is a role/starter question rather than an injury question: Seattle's quarterback situation is unsettled between Drew Lock and Sam Darnold (see Matchup Intelligence, Quarterbacks, for the full breakdown) and Seattle's running back committee has shifted week to week between Jadarian Price and Emanuel Wilson. Neither is a health story in this evidence package, but both affect who is actually on the field Sunday, and are treated with appropriate hedging throughout.

---

## 3. MATCHUP STATISTICS

### LAC Offense
- Scoring: 14.7 points/game (29th)
- Total offense: 322.0 yards/game (19th)
- Passing: 209.0 yards/game (20th), 59.1% completion (27th), 12.06 yards/completion (10th)
- Rushing: 113.0 yards/game (12th)
- First downs: 15.7/game (23rd)
- Third down: 35.1% conversion (24th) on 12.3 attempts/game
- Fourth down: 19.0% go-for-it rate, 0.0% conversion rate (thin sample)
- Red zone play-calling (tendency, not quality): 60.0% run (4th), 40.0% pass (29th) — one of the most run-heavy red-zone offenses in the league
- Contextual (opponent-quality splits, team scoring): 14 points against a top-tier scoring defense faced (n=1), 16 against a mid-tier scoring defense (n=1), 14 against a bottom-tier scoring defense (n=1) — flat regardless of matchup quality, a small-sample (LOW confidence) but notable pattern explored further in Hidden Intelligence.

### LAC Defense
- Scoring allowed: 25.3 points/game (20th)
- Total yards allowed: 361.0 yards/game (23rd)
- Passing allowed: 244.7 yards/game (21st)
- Rushing allowed: 116.3 yards/game (19th)
- First downs allowed: 18.7/game (22nd)
- Third down allowed: 40.0% (16th), 60.0% stop rate, 13.3 attempts faced/game
- Fourth down allowed: 25.0% stop rate
- Red zone play-calling allowed (tendency): 57.6% run allowed (6th), 42.4% pass allowed (27th)
- Position-specific: allows running backs 104.0 rush yards/game (23rd), wide receivers 159.3 receiving yards/game (22nd), tight ends 57.3 receiving yards/game (20th) — an across-the-board middle-to-back-of-the-pack unit with no clear individual strength.

### SEA Offense
- Scoring: 25.0 points/game (13th)
- Total offense: 377.0 yards/game (10th)
- Passing: 276.0 yards/game (5th), 70.5% completion (5th), 12.1 yards/completion (8th), only 1.0 sacks allowed/game (3rd) — a clean pocket
- Rushing: 101.0 yards/game (18th)
- First downs: 19.7/game (11th)
- Third down: 33.3% conversion (26th) on 11.0 attempts/game — inefficient relative to the raw passing numbers
- Fourth down: 22.7% go-for-it rate, 40.0% conversion
- Red zone play-calling (tendency): 53.8% run (7th), 46.2% pass (26th)
- Contextual (opponent-quality splits, team scoring): 13 points against the one top-tier scoring defense faced this season (New England, n=1), 31 points in each of the two games against bottom-tier scoring defenses faced (n=2) — a genuinely steep scoring split explored further in Hidden Intelligence.

### SEA Defense
- Scoring allowed: 16.7 points/game (4th)
- Total yards allowed: 239.0 yards/game (1st)
- Passing allowed: 152.0 yards/game (1st), 7.7 yards/completion allowed (1st), only 7.7 first downs allowed/game via pass (1st), 5.3 completions of 10+ yards allowed/game (1st) — the most suffocating pass defense in this evidence set by a wide margin
- Rushing allowed: 87.0 yards/game (6th)
- First downs allowed: 13.0/game (1st)
- Third down allowed: 26.8% (2nd), 73.2% stop rate, 13.7 attempts faced/game
- Fourth down allowed: 0.0% stop rate (on a very small sample — only 9.0 situations/game faced, 14.8% opponent go-for-it rate)
- Red zone play-calling allowed (tendency): 57.1% run allowed (7th), 42.9% pass allowed (26th), and notably faces only 4.7 red-zone plays/game — the fewest red-zone snaps of any unit in this report, a byproduct of forcing stops well before the goal line
- Position-specific: allows running backs just 65.3 rush yards/game (5th), wide receivers just 95.0 receiving yards/game (1st), tight ends just 26.7 receiving yards/game (3rd) — elite at every skill position, not just in the aggregate.

---

## 4. MATCHUP INTELLIGENCE

### Quarterbacks

**Justin Herbert (LAC).** Herbert has started all three games (100% snap share, depth chart pos-rank 1, uncontested starter). His 2026 numbers are a genuine step back: 209.0 pass yards/game (20th), 59.1% completion (27th), 12.06 yards/completion (10th, still efficient on a per-catch basis), but only 3 total passing touchdowns through three games (26th) against a bloated 1.33 interceptions/game (28th) and 2.67 sacks/game allowed (22nd). *(2025: 232.9 pass yds/gm, 66.4% completion, 0.81 int/gm)* — both the completion rate and turnover rate have moved clearly in the wrong direction relative to his own recent track record, not just relative to the league. His three 2026 opponents (Arizona's 23rd-ranked pass defense, Las Vegas's 15th, Buffalo's 28th) have all graded mid-to-bottom tier — he has not faced a genuinely elite pass defense all season. Seattle's is the best in the league (152.0 yards/game allowed, 1st). Home/road: his lone true road start this season came in Week 3 at Buffalo (226 pass yards, a 76.3 rating) — the only road data point available, and there is no top-tier-defense sample at all in his 2026 or road splits to draw on. This is a genuinely uncharted level of difficulty for him this year. Confidence: MEDIUM-HIGH that this is Seattle's toughest defensive test yet for Herbert, based on a clean, unambiguous gap between his season-to-date competition and Seattle's actual rank.

Herbert's backups (DJ Uiagalelei, pos-rank 3, zero 2026 or 2025 game action; Trey Lance, pos-rank 2, no 2026 action and a thin 2025 relief sample at 56.5 pass yards/game) carry no real standalone relevance this week.

**Seattle's quarterback picture is genuinely unsettled, and this matters.** Drew Lock started and played the majority of snaps in Weeks 1-2 (95% season snap share across his two appearances: 187 yards vs. New England in Week 1, 235 yards and 3 touchdowns vs. Arizona in Week 2). But Week 3 tells a different story: Sam Darnold played every snap (100%) in the loss at Washington, throwing for 379 yards and 4 touchdowns on 31-of-45 passing, while Lock did not appear in that game's log at all. Darnold's lone other appearance was 2 mop-up-duty attempts in the Week 1 blowout win. Per Football Intel's depth-chart signal (`depth_chart_as_of` 2026-09-29, one day before this evidence freeze), **Sam Darnold currently sits at QB pos-rank 1, with Lock at pos-rank 2** — and this matches the most recent actual start (Week 3, Darnold). Both signals point the same direction: Darnold, not Lock, projects as the more likely starter for this game. Darnold's own track record supports him handling a real workload: *(2025: 17 games started, 238.1 pass yds/gm, 67.7% completion)* — a full, established starter season, a materially deeper résumé than Lock's own 2025 line (3 games, 5.0 pass yds/gm, clear inactive/emergency duty). Confidence: MEDIUM that Darnold starts — per Football Intel's current-starter protocol this is capped below HIGH by rule, since it is inherently a same-week judgment call, but the game-log and depth-chart signals here agree rather than conflict.

Neither Lock's nor Darnold's tier splits offer a clean read on facing a mid-tier pass defense (LAC ranks 21st against the pass, a mid-tier opponent) — Lock's only career home sample came against a top-tier defense (New England, 187 yards); Darnold's only real start (Washington) came against a bottom-tier defense. Whichever Seahawk QB plays, this is a genuinely new opponent-quality bucket for both of them in 2026.

### Running Backs

**Omarion Hampton (LAC)** is the clear early-down and red-zone back — 61.7% rush share, an outsized 55.6% share of Chargers red-zone carries, 3.5 broken tackles per game. His season averages 64.3 rush yards/game on 16.7 carries/game with 2 rushing touchdowns. Required contact-efficiency detail: his 1.94 yards-before-contact average and 1.97 yards-after-contact average are nearly even — roughly half his production is created by blocking, half by his own work after first contact, a balanced rather than blocking-dependent profile. All three of his opponents this season (Arizona, Las Vegas, Buffalo) graded mid-tier against the run — he has not faced a genuinely elite run defense yet. Seattle's run defense (87.0 yards/game allowed, 6th) is his toughest test of the season. His lone road data point (Week 3 at Buffalo: 56 yards on 15 carries, 3.7 yards/carry) is the only road number available, and like Herbert, he has zero top-tier-opponent sample this year to lean on — a genuine blind spot given this week's matchup. Confidence: MEDIUM that his workload holds (usage is stable and secure) but LOW on hitting his season average given the step up in opponent quality.

**Keaton Mitchell (LAC)** is the clear complementary piece — 21.0% rush share, 28.3 rush yards/game, with a growing receiving role (3 catches on 3 targets, including a touchdown, in Week 3 alone). **Kimani Vidal** is a clear third option with almost no standalone role (1.7% rush share across 2 games). **Alec Ingold** is a blocking fullback with a marginal receiving role (3 catches, 35 yards on the season).

**Seattle's backfield is a genuinely muddled committee, and it's worth naming plainly.** The depth chart (as of 2026-09-29) lists **Jadarian Price at RB pos-rank 1** and **Emanuel Wilson at pos-rank 2** — but the actual game-log usage runs the other way over Seattle's last two games: Wilson carried a 52.5% rush share in Week 2 (92 yards on 21 carries) and a 50.0% share in Week 3, while Price's share fell to 32.5% and 27.8% across those same two games after opening the season as the clear lead back in Week 1 (45.5% share, 52 yards). Per Football Intel's current-starter protocol, this is a case where the depth chart and recent usage genuinely disagree rather than agree — the most current signal (depth chart) still favors Price, but the more recent on-field trend favors Wilson. Treat the lead-back question at LOW-to-MEDIUM confidence; this is not a settled one-role backfield. **George Holani** has carved out a real receiving/passing-down role (2.0 catches/game, a 48-yard Week 3 game against Washington) even with a modest rushing share (18.8%).

Home/road and tier context for this trio is thin (Seattle has played exactly one true home game so far, Week 1 vs. New England, a top-tier run defense) — none of the three backs has a home-and-mid-tier-opponent combination on record yet, which is the exact bucket this week's Chargers defense (116.3 rush yards/game allowed, 19th, a mid-tier unit) calls for. Worth noting as a genuine gap rather than guessing at it.

### Wide Receivers / Tight Ends

**Ladd McConkey (LAC)** remains the target leader on paper (17.4% target share, 61.0 rec yards/game, 5.0 targets/game) but his role has visibly shrunk relative to last year — *(2025: 21.2% target share, 77.5% snap share)* versus this year's 61.0% snap share — worth watching as either a health/rotation change or simply early-season variance. His only road data point (Week 3 at Buffalo: 66 yards, 4 catches on 5 targets) is against a bottom-tier pass defense; he has no top-tier-opponent sample this year, which is exactly what Seattle represents (95.0 receiving yards/game allowed to the position group, 1st).

**Quentin Johnston (LAC)** has a concerning efficiency gap this season — 19.8% target share (close to his 2025 rate of 20.2%) but a 21.3 rec yards/game average that is barely half his 2025 pace *(2025: 56.5 rec yds/gm)*, on just 6 catches from 17 targets (a 35% catch rate). Whether that's scheme, drops, or quarterback play, it's a real decline worth flagging.

**Tre Harris (LAC)** is the one Chargers receiver trending the right direction — a jump from an 8.5% target share and 20.3 rec yards/game as a rookie in 2025 to an 18.6% share and 49.7 rec yards/game so far in 2026, including a 76-yard, 6-catch Week 3 game with heavy red-zone usage (3 of his team's red-zone targets that game). A real role expansion.

All three Chargers receivers face a pass defense (Seattle) that leads the league in receiving yards allowed to the position (95.0/game, 1st) and has no top-tier-opponent sample of their own to draw confidence from — a genuinely difficult projection across the board. Confidence: LOW-MEDIUM for all three hitting their season averages.

**Jaxon Smith-Njigba (SEA)** is the engine of this offense and then some — a 37.9% target share, 135.0 receiving yards/game (1st in this evidence set), 9.0 catches/game (1st), and 6 touchdowns through three games, including a 50% red-zone target share. *(2025: 35.8% target share, 105.5 rec yds/gm)* — this is not a one-year spike; it's a sustained, dominant target-share profile. His lone home data point (122 yards, Week 1 vs. a top-tier defense) is his only same-side sample; he carries no mid-tier-opponent data at any site, which is the bucket the Chargers' 21st-ranked pass defense represents. Confidence: HIGH on continued heavy usage regardless of which quarterback starts, MEDIUM on hitting his full season pace against a defense of unknown true quality to him specifically.

**Rashid Shaheed (SEA)** has seen his role compress as JSN's target share has ballooned — 17.67 rec yards/game this season against *(2025: 16.7% target share, 38.2 rec yds/gm)* — a real year-over-year erosion worth connecting to JSN's target monopoly. **Cooper Kupp** is now a clear complementary/situational piece at this stage of his career (10.5% target share, 33.7 rec yards/game), a continued step down from his already-diminished 2025 role. **Tory Horton** flashed in his lone appearance (48 yards on 3 targets, 16.0 yards/reception) but remains a bit-part player in the rotation.

**Charlie Kolar (LAC)** nominally sits atop the depth chart at tight end (pos-rank 1) but the room is a genuine rotation — **David Njoku** has actually been the most efficient target when in (33.5 rec yards/game on a 75% catch rate across 2 games) despite a declining snap share (55% to 16%), while **Oronde Gadsden II** is trending the opposite direction, climbing from an 18% to 57% snap share over three weeks with real red-zone usage (a Week 2 touchdown on his only red-zone target). This is a muddled committee without a clean lead option; treat any single name's workload as LOW confidence.

**AJ Barner (SEA)** is the unambiguous starter at tight end — 86.3% snap share, a clear and rising role (69 yards on 9 targets in Week 3 alone, up from single-digit yardage the two weeks prior), facing a Chargers defense that allows tight ends 57.3 receiving yards/game (20th) — a middling matchup that should let his positive usage trend continue. **Eric Saubert** is purely a red-zone specialist (2 touchdowns on just 3 total targets on the season) with no real standalone volume.

---

## 5. THREAT INTELLIGENCE

Football Intel's deterministic Threat Engine flags a player when two conditions converge in the same statistical category: the player's own season rank clears a threshold, AND the upcoming opponent's defensive rank in that same category is weak enough to clear a matching threshold. The three tiers, by exact threshold (player rank counts from 1st-best; defense rank counts from 1st-toughest, so a high defense-rank number means a weak unit): **Nuclear** requires a player ranked top 3 AND an opponent defense ranked 30th or worse in that category; **Elite** requires top 5 AND opponent ranked 28th or worse; **Standard** requires top 10 AND opponent ranked 23rd or worse. A Double/Triple/Quadruple label reflects how many categories converged for that player.

**No Threat designation fired for any evaluated starter on either side of this game** — Justin Herbert, Omarion Hampton, Quentin Johnston, and Tre Harris for the Chargers; Drew Lock, Jadarian Price, Jaxon Smith-Njigba, Cooper Kupp, and AJ Barner for the Seahawks. (Sam Darnold and Emanuel Wilson, despite the real usage questions discussed above, were not part of the evaluated starter set in this evidence package.)

One result is worth explaining in detail rather than passing over: **Jaxon Smith-Njigba missed a Standard-tier passing threat by the narrowest possible margin.** His own season rank in receiving yards (1st) clears every threshold in this system with room to spare. The blocking factor was the opponent side — Standard tier requires the opposing defense to rank 23rd or worse in that category, and the Chargers' pass defense (against wide receivers specifically) ranks 22nd. One spot short. This is about as close as a non-designation gets, and it should be read as a real, near-miss signal of matchup risk for LA's coverage unit, not as evidence that JSN is a weak play this week — his own production floor (135.0 rec yds/gm, 9.0 catches/gm, a 37.9% target share) does not depend on the Threat system's convergence rule to be dangerous. It simply means the formal designation didn't clear its own bar.

No other player came close. Herbert's passing categories don't threaten a Threat this week precisely because Seattle's pass defense is elite rather than weak (the opposite of what this system looks for) — the absence of a designation here is not a gap in the evidence, it's confirmation of what Matchup Intelligence already lays out: this is a bad statistical matchup for LA's passing game, not a favorable one.

---

## 6. HIDDEN INTELLIGENCE & CONTEXTUAL ANALYSIS

**Finding 1: Seattle's offense has been almost entirely a function of opponent quality so far — and Los Angeles's defense sits squarely in the bucket that has produced Seattle's best output.** Seattle's only game against a top-tier scoring defense this season (New England, Week 1) produced just 13 points. Its two games against bottom-tier scoring defenses (Arizona, Washington) each produced 31 points — more than double. That's not a subtle gap; it's close to the entire spread available in a three-game sample. Los Angeles's defense ranks 20th in points allowed (25.3/game) and 21st against the pass (244.7 yards/game) — solidly mid-to-bottom tier by both measures, nowhere close to New England's caliber. If Seattle's offense continues behaving the way it has all season, the Chargers' defensive profile is a far closer match to the two games that produced 31 points than to the one that produced 13. This isn't a restatement of either team's raw ranking — it's the cross-reference between Seattle's own opponent-quality scoring split and Los Angeles's actual defensive caliber that makes the forward-looking case. Confidence: MEDIUM — the sample is only three games, but the spread within it is unusually wide and directionally consistent with the underlying talent gap.

**Finding 2: Los Angeles's offense has a real, career-spanning tendency where rushing success and passing success rarely happen in the same game — and Seattle's defense is built to deny both simultaneously anyway.** Across a much larger (career-length, n=19 per side) sample than this season alone, Herbert's passing-output hit rate is 55.6% in games where the Chargers' rushing attack is running hot, but drops to just 30.0% when the rushing attack is also hot in the same game — and the same inverse pattern holds from the other direction: the team's rush-output hit rate is 63.6% when Herbert's passing is cold, but only 37.5% when his passing is also hot. In other words, this is not a "lean on the run to cover for a bad passing game" offense — historically, on the occasions both facets have clicked together, it happens less often than chance would suggest. Layered against Seattle's own profile — a top-6 run defense (87.0 yards/game allowed) and the league's best pass defense (152.0 yards/game allowed) at the same time — the concern compounds rather than offsets: there is no complementary escape valve here if one half of the offense stalls, because historically the other half hasn't reliably picked up the slack anyway, and the opponent is equipped to take away both regardless. A smaller, secondary version of this same relationship shows up between Herbert and Hampton specifically (a modest positive correlation, 50.0% vs. 33.3% hit rate depending on whether the other is hot) — a much weaker effect than the team-wide inverse pattern, worth noting as a contrast in scale rather than a separate story. Confidence: MEDIUM — the core team-level sample (n=19 per side) is reasonably large and the pattern is symmetric in both directions, which argues against it being noise.

---

## 7. COEUS FINAL READ

**Keys to the Game.** If Los Angeles cannot solve its third-down problem (35.1% conversion, 24th) against a Seattle defense built specifically to end drives there (26.8% allowed, 2nd-best in the league), expect the Chargers' offense to spend most of the game in obvious, predictable situations — exactly the conditions Herbert has already struggled in even against far weaker competition. If Seattle settles on Sam Darnold (the depth-chart and most-recent-start signal both point his way) rather than reverting to Drew Lock, expect a more stable, established veteran presence under center than Lock's thin track record offers, though neither passer has faced a genuinely mid-tier pass defense like LA's in 2026 yet. If Seattle's run-game committee (Price vs. Wilson) doesn't clarify itself this week, expect a continued split workload that caps any single back's ceiling — watch early rush shares for a signal of who's actually driving that Thursday.

**The Verdict.** The broad shape floated in the Pregame Briefing — a mismatch defined by a struggling Chargers offense running into an elite Seahawks defense — holds up under the deeper evidence, and arguably strengthens once Seattle's own opponent-quality scoring split (13 points against a good defense, 31 twice against weak ones) is weighed against exactly how mediocre LA's defense actually is. The single biggest swing factor working against a clean Seattle advantage is Seattle's own internal uncertainty — an unsettled QB chair and an unresolved backfield committee — but none of that uncertainty changes who's on the other side of the ball. Los Angeles must solve third down, protect a quarterback already trending toward more mistakes rather than fewer, and ask a receiving corps with almost no experience against elite competition to perform against the best pass defense in this evidence set. That is a tall enough order that the structural advantage sits clearly with Seattle, even accounting for its own rough edges.

### Coeus Cheat Sheet

**Team**
- LAC: 0-3 | 14.7 ppg (29th) / 25.3 ppg allowed (20th)
- SEA: 2-1 | 25.0 ppg (13th) / 16.7 ppg allowed (4th)

**Passing**
- Justin Herbert (LAC): 209.0 pass yds/gm (20th), 59.1% comp (27th), 3 TD, 1.33 INT/gm (28th) — opp D allows 152.0 pass yds/gm (1st)
- Drew Lock (SEA, Wks 1-2): 211.0 pass yds/gm, 72.92% comp, 4 TD, 0 INT
- Sam Darnold (SEA, likely current starter): 196.0 pass yds/gm, 68.09% comp, 4 TD, 1.0 INT/gm

**Rushing**
- Omarion Hampton (LAC): 64.3 rush yds/gm, 16.7 car/gm, 2 rush TD, 61.7% rush share — opp D allows 87.0 rush yds/gm (6th)
- Emanuel Wilson (SEA): 36.3 rush yds/gm, 40.0% rush share (trending up last 2 games) — opp D allows 116.3 rush yds/gm (19th)
- Jadarian Price (SEA): 39.7 rush yds/gm, 35.0% rush share, listed RB1 on depth chart — opp D allows 116.3 rush yds/gm (19th)

**Receiving**
- Ladd McConkey (LAC): 61.0 rec yds/gm, 17.4% target share
- Tre Harris (LAC): 49.7 rec yds/gm, 18.6% target share, role expanding
- David Njoku (LAC, TE): 33.5 rec yds/gm across 2 games
- Jaxon Smith-Njigba (SEA): 135.0 rec yds/gm (1st), 37.9% target share, 6 TD
- Rashid Shaheed (SEA): 17.7 rec yds/gm, role eroding
- AJ Barner (SEA, TE): 30.0 rec yds/gm, 86.3% snap share, rising usage

**Team Defense**
- LAC def: 244.7 pass yds/gm allowed (21st), 116.3 rush yds/gm allowed (19th), 159.3 WR rec yds/gm allowed (22nd)
- SEA def: 152.0 pass yds/gm allowed (1st), 87.0 rush yds/gm allowed (6th), 95.0 WR rec yds/gm allowed (1st)
- Team coverage rate (man%/zone%): not available in this evidence package for either team

**Down/Distance**
- LAC offense: 35.1% third-down conv (24th) | LAC defense: 40.0% allowed (16th)
- SEA offense: 33.3% third-down conv (26th) | SEA defense: 26.8% allowed (2nd)

**Red Zone Play Calling**
- LAC offense: 60.0% run (4th), 40.0% pass (29th) | LAC defense allowed: 57.6% run (6th)
- SEA offense: 53.8% run (7th), 46.2% pass (26th) | SEA defense allowed: 57.1% run (7th)

**Head-to-Head**
- No meeting between these two teams in 2026; first matchup of the season.

---

EVIDENCE_CHECK
{"claims": [
{"type": "current_opponent", "team": "LAC", "pos": "TEAM", "stat": "ppg", "role": "off", "claimed_rank": 29},
{"type": "current_opponent", "team": "LAC", "pos": "TEAM", "stat": "total_ypg", "role": "off", "claimed_rank": 19},
{"type": "current_opponent", "team": "LAC", "pos": "TEAM", "stat": "pass_ypg", "role": "off", "claimed_rank": 20},
{"type": "current_opponent", "team": "LAC", "pos": "TEAM", "stat": "rush_ypg", "role": "off", "claimed_rank": 12},
{"type": "current_opponent", "team": "LAC", "pos": "TEAM", "stat": "fd_pg", "role": "off", "claimed_rank": 23},
{"type": "current_opponent", "team": "LAC", "pos": "TEAM", "stat": "ppg", "role": "def", "claimed_rank": 20},
{"type": "current_opponent", "team": "LAC", "pos": "TEAM", "stat": "total_ypg", "role": "def", "claimed_rank": 23},
{"type": "current_opponent", "team": "LAC", "pos": "TEAM", "stat": "pass_ypg", "role": "def", "claimed_rank": 21},
{"type": "current_opponent", "team": "LAC", "pos": "TEAM", "stat": "rush_ypg", "role": "def", "claimed_rank": 19},
{"type": "current_opponent", "team": "LAC", "pos": "TEAM", "stat": "fd_pg", "role": "def", "claimed_rank": 22},
{"type": "current_opponent", "team": "SEA", "pos": "TEAM", "stat": "ppg", "role": "off", "claimed_rank": 13},
{"type": "current_opponent", "team": "SEA", "pos": "TEAM", "stat": "total_ypg", "role": "off", "claimed_rank": 10},
{"type": "current_opponent", "team": "SEA", "pos": "TEAM", "stat": "pass_ypg", "role": "off", "claimed_rank": 5},
{"type": "current_opponent", "team": "SEA", "pos": "TEAM", "stat": "rush_ypg", "role": "off", "claimed_rank": 18},
{"type": "current_opponent", "team": "SEA", "pos": "TEAM", "stat": "fd_pg", "role": "off", "claimed_rank": 11},
{"type": "current_opponent", "team": "SEA", "pos": "TEAM", "stat": "ppg", "role": "def", "claimed_rank": 4},
{"type": "current_opponent", "team": "SEA", "pos": "TEAM", "stat": "total_ypg", "role": "def", "claimed_rank": 1},
{"type": "current_opponent", "team": "SEA", "pos": "TEAM", "stat": "pass_ypg", "role": "def", "claimed_rank": 1},
{"type": "current_opponent", "team": "SEA", "pos": "TEAM", "stat": "rush_ypg", "role": "def", "claimed_rank": 6},
{"type": "current_opponent", "team": "SEA", "pos": "TEAM", "stat": "fd_pg", "role": "def", "claimed_rank": 1},
{"type": "current_opponent", "team": "LAC", "pos": "TEAM", "stat": "third_down_conversion_pct", "role": "off", "claimed_rank": 24},
{"type": "current_opponent", "team": "LAC", "pos": "TEAM", "stat": "third_down_pct_allowed", "role": "def", "claimed_rank": 16},
{"type": "current_opponent", "team": "SEA", "pos": "TEAM", "stat": "third_down_conversion_pct", "role": "off", "claimed_rank": 26},
{"type": "current_opponent", "team": "SEA", "pos": "TEAM", "stat": "third_down_pct_allowed", "role": "def", "claimed_rank": 2},
{"type": "current_opponent", "team": "LAC", "pos": "TEAM", "stat": "red_zone_run_pct", "role": "off", "claimed_rank": 4},
{"type": "current_opponent", "team": "LAC", "pos": "TEAM", "stat": "red_zone_pass_pct", "role": "off", "claimed_rank": 29},
{"type": "current_opponent", "team": "LAC", "pos": "TEAM", "stat": "red_zone_run_pct_allowed", "role": "def", "claimed_rank": 6},
{"type": "current_opponent", "team": "LAC", "pos": "TEAM", "stat": "red_zone_pass_pct_allowed", "role": "def", "claimed_rank": 27},
{"type": "current_opponent", "team": "SEA", "pos": "TEAM", "stat": "red_zone_run_pct", "role": "off", "claimed_rank": 7},
{"type": "current_opponent", "team": "SEA", "pos": "TEAM", "stat": "red_zone_pass_pct", "role": "off", "claimed_rank": 26},
{"type": "current_opponent", "team": "SEA", "pos": "TEAM", "stat": "red_zone_run_pct_allowed", "role": "def", "claimed_rank": 7},
{"type": "current_opponent", "team": "SEA", "pos": "TEAM", "stat": "red_zone_pass_pct_allowed", "role": "def", "claimed_rank": 26},
{"type": "current_opponent", "team": "LAC", "pos": "RB", "stat": "rush_yds", "role": "def", "claimed_rank": 23},
{"type": "current_opponent", "team": "LAC", "pos": "WR", "stat": "rec_yds", "role": "def", "claimed_rank": 22},
{"type": "current_opponent", "team": "LAC", "pos": "TE", "stat": "rec_yds", "role": "def", "claimed_rank": 20},
{"type": "current_opponent", "team": "SEA", "pos": "RB", "stat": "rush_yds", "role": "def", "claimed_rank": 5},
{"type": "current_opponent", "team": "SEA", "pos": "WR", "stat": "rec_yds", "role": "def", "claimed_rank": 1},
{"type": "current_opponent", "team": "SEA", "pos": "TE", "stat": "rec_yds", "role": "def", "claimed_rank": 3},
{"type": "current_opponent", "team": "LAC", "pos": "QB", "stat": "pass_yds", "role": "off", "claimed_rank": 20},
{"type": "current_opponent", "team": "LAC", "pos": "QB", "stat": "comp_pct", "role": "off", "claimed_rank": 27},
{"type": "current_opponent", "team": "LAC", "pos": "QB", "stat": "ypc", "role": "off", "claimed_rank": 10},
{"type": "current_opponent", "team": "LAC", "pos": "QB", "stat": "int_pg", "role": "off", "claimed_rank": 28},
{"type": "current_opponent", "team": "LAC", "pos": "QB", "stat": "sacks_pg", "role": "off", "claimed_rank": 22},
{"type": "log_opponent", "player": "Justin Herbert", "week": 1, "stat": "pass_yds", "claimed_rank": 23},
{"type": "log_opponent", "player": "Justin Herbert", "week": 3, "stat": "pass_yds", "claimed_rank": 28},
{"type": "log_opponent", "player": "Jaxon Smith-Njigba", "week": 1, "stat": "rec_yds", "claimed_rank": 9},
{"type": "log_opponent", "player": "Jaxon Smith-Njigba", "week": 2, "stat": "rec_yds", "claimed_rank": 23}
]}