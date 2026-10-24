# THE BEST 10 — Week Slate

**Evidence note:** all rank claims below are pulled verbatim from the REAL TEAM OFFENSE/DEFENSE RANKINGS table (2026 data only). Prices converted to American odds for display; JSON blocks retain the real decimal prices for validator math.

---

**1. Tyler Shough — UNDER 227.5 passing yards (PIT @ NO)** — price -114
Shough's own bucket against top-tier pass defenses is just 120.0 pass yds/gm (n=2, thin but the only real evidence for this caliber matchup), and he now draws Pittsburgh's defense, which ranks top 10 (8th, 222.0 pass yds/gm allowed). Game total sits at a moderate 44.5 with Pittsburgh favored by 3 — not an explosive passing environment for the rookie starter. 6 games played in 2026.

**2. Bryce Young — OVER 253.5 passing yards (TB @ CAR)** — price -114
Young leads the entire league at 309.8 pass yds/gm this season (1st) and is averaging 345.0 ypg across his 2 home games, against a Tampa Bay pass defense that sits in the middle of the pack (19th, 237.7 yds/gm allowed). Total is 44.5 with Carolina favored by 2.5 — an environment that supports volume from the NFL's most productive passing offense. 5 games played in 2026.

**3. Tetairoa McMillan — OVER 69.5 receiving yards (TB @ CAR)** — price -114
McMillan ranks top 5 among WRs at 94.2 rec yds/gm and has gone for 133.5 ypg across his 2 home games, against a Tampa Bay WR defense that ranks 15th (145.7 rec yds/gm allowed) — no tier superlative applies, just a clean size mismatch. 5 games played in 2026.

**4. Joe Burrow — UNDER 260.5 passing yards (CIN @ BAL)** — price -114
Burrow's road average this season is just 226.3 pass yds/gm across 3 games, against a Baltimore pass defense that ranks top 10 (10th, 225.7 yds/gm allowed). Total is a healthy 48.5 with Baltimore only -1.5 favorites — a competitive script, but Burrow's actual road output hasn't approached this number. 5 games played in 2026.

**5. Bucky Irving — OVER 66.5 rushing yards (TB @ CAR)** — price -114
Irving's road average this season is 105.0 rush yds/gm across 2 games, against a Carolina run defense that sits in the bottom 10 (23rd, 103.0 rush yds/gm allowed to RBs). 6 games played in 2026.

**6. Jahmyr Gibbs — UNDER 93.5 rushing yards (GB @ DET)** — price -114
Gibbs has rushed for just 49.0 yds/gm across his two 2026 games against mid-tier run defenses, and Green Bay's run defense sits at that same caliber — 17th against RBs (90.8 rush yds/gm allowed), well off Gibbs' season-long average. 5 games played in 2026.

**7. Nico Collins — UNDER 68.5 receiving yards (NYG @ HOU)** — price -114
Collins' 80.75 rec yds/gm season rate was built almost entirely against bottom-tier WR defenses, and he now faces a Giants unit ranked top 10 (6th, 132.3 rec yds/gm allowed) — the toughest matchup of his season. 4 games played in 2026.

**8. Tucker Kraft — OVER 49.5 receiving yards (GB @ DET)** — price -114
Kraft's own 41.5 rec yds/gm (14th among TEs) runs into a Detroit defense that is dead last in the league against tight ends (32nd, 109.0 rec yds/gm allowed) — league-worst, and the single biggest position mismatch on the board. 6 games played in 2026.

**9. Jaylen Warren — Anytime TD (PIT @ NO)** — price -120
Warren leads Pittsburgh's backfield at 76.7 rush yds/gm (10th among RBs), and New Orleans has allowed 11 rushing touchdowns to running backs this season — league-worst (32nd), the softest goal-line matchup on the slate. 6 games played in 2026.

**10. Detroit Lions — Spread -3.0 (GB @ DET)** — price -122
Detroit's offense ranks top 3 (2nd, 32.8 ppg) against a Green Bay pass defense that ranks top 10 (6th, 209.2 pass yds/gm allowed) but still has to defend Detroit's whole attack, while Detroit's own defense is league-worst against the pass (32nd, 321.4 pass yds/gm allowed) in a game that projects as a track meet. Detroit has covered 59.2% of its games at home since 2020 vs. Green Bay's 44.2% on the road. 5 games played in 2026.

```json
BEST_10
{
  "picks": [
    {"rank": 1, "player": "Tyler Shough", "market_key": "player_passing_yards", "canonical_event_id": "518de03174b4f73a", "price": 1.877, "side": "under", "line": 227.5, "reason": "Shough's top-tier-pass-defense bucket shows just 120.0 pass yds/gm (n=2), and he now draws Pittsburgh's 8th-ranked pass defense (222.0 yds/gm allowed). Total is 44.5 with PIT favored by 3 \u2014 not an explosive passing environment.", "evidence_check": [{"type": "current_opponent", "team": "PIT", "pos": "QB", "stat": "pass_ypg", "role": "def", "claimed_rank": 8}], "projection": 180, "games_2026": 6},
    {"rank": 2, "player": "Bryce Young", "market_key": "player_passing_yards", "canonical_event_id": "e361231df87eecb1", "price": 1.877, "side": "over", "line": 253.5, "reason": "Young leads the NFL at 309.8 pass yds/gm (1st) and averages 345.0 ypg at home (2 games) against a Tampa Bay pass defense ranked 19th (237.7 yds/gm allowed). Total is 44.5 with CAR favored by 2.5.", "evidence_check": [{"type": "current_opponent", "team": "TB", "pos": "QB", "stat": "pass_ypg", "role": "def", "claimed_rank": 19}], "projection": 300, "games_2026": 5},
    {"rank": 3, "player": "Tetairoa McMillan", "market_key": "player_receiving_yards", "canonical_event_id": "e361231df87eecb1", "price": 1.877, "side": "over", "line": 69.5, "reason": "McMillan ranks 5th among WRs at 94.2 rec yds/gm and has gone for 133.5 ypg at home (2 games) against a Tampa Bay WR defense ranked 15th (145.7 rec yds/gm allowed).", "evidence_check": [{"type": "current_opponent", "team": "TB", "pos": "WR", "stat": "rec_ypg", "role": "def", "claimed_rank": 15}], "projection": 110, "games_2026": 5},
    {"rank": 4, "player": "Joe Burrow", "market_key": "player_passing_yards", "canonical_event_id": "f686a2afcc5ad5c8", "price": 1.877, "side": "under", "line": 260.5, "reason": "Burrow's road average is just 226.3 pass yds/gm (3 games) against a Baltimore pass defense ranked 10th (225.7 yds/gm allowed). Total is 48.5 with BAL only -1.5 favorites.", "evidence_check": [{"type": "current_opponent", "team": "BAL", "pos": "QB", "stat": "pass_ypg", "role": "def", "claimed_rank": 10}], "projection": 230, "games_2026": 5},
    {"rank": 5, "player": "Bucky Irving", "market_key": "player_rushing_yards", "canonical_event_id": "e361231df87eecb1", "price": 1.877, "side": "over", "line": 66.5, "reason": "Irving's road average is 105.0 rush yds/gm (2 games) against a Carolina run defense ranked 23rd, bottom 10 (103.0 rush yds/gm allowed to RBs).", "evidence_check": [{"type": "current_opponent", "team": "CAR", "pos": "RB", "stat": "rush_ypg", "role": "def", "claimed_rank": 23}], "projection": 95, "games_2026": 6},
    {"rank": 6, "player": "Jahmyr Gibbs", "market_key": "player_rushing_yards", "canonical_event_id": "315d06f1d48550c9", "price": 1.877, "side": "under", "line": 93.5, "reason": "Gibbs has rushed for just 49.0 yds/gm across his two 2026 games against mid-tier run defenses; GB's run defense sits at that same caliber, ranked 17th against RBs (90.8 rush yds/gm allowed).", "evidence_check": [{"type": "current_opponent", "team": "GB", "pos": "RB", "stat": "rush_ypg", "role": "def", "claimed_rank": 17}], "projection": 70, "games_2026": 5},
    {"rank": 7, "player": "Nico Collins", "market_key": "player_receiving_yards", "canonical_event_id": "84ea8ce9bbab584b", "price": 1.877, "side": "under", "line": 68.5, "reason": "Collins' 80.75 rec yds/gm season rate was built against bottom-tier WR defenses; he now faces a Giants unit ranked 6th, top 10 (132.3 rec yds/gm allowed), his toughest test of the season.", "evidence_check": [{"type": "current_opponent", "team": "NYG", "pos": "WR", "stat": "rec_ypg", "role": "def", "claimed_rank": 6}], "projection": 55, "games_2026": 4},
    {"rank": 8, "player": "Tucker Kraft", "market_key": "player_receiving_yards", "canonical_event_id": "315d06f1d48550c9", "price": 1.877, "side": "over", "line": 49.5, "reason": "Kraft's 41.5 rec yds/gm (14th among TEs) runs into a Detroit defense that is league-worst against tight ends (32nd, 109.0 rec yds/gm allowed), the largest position mismatch on the board.", "evidence_check": [{"type": "current_opponent", "team": "DET", "pos": "TE", "stat": "rec_ypg", "role": "def", "claimed_rank": 32}], "projection": 58, "games_2026": 6},
    {"rank": 9, "player": "Jaylen Warren", "market_key": "player_anytime_td", "canonical_event_id": "518de03174b4f73a", "price": 1.833, "side": "over", "line": null, "reason": "Warren leads Pittsburgh's backfield at 76.7 rush yds/gm (10th among RBs), and New Orleans has allowed a league-worst 11 rushing TDs to RBs this season (32nd), the softest goal-line matchup on the slate.", "evidence_check": [{"type": "current_opponent", "team": "NO", "pos": "RB", "stat": "rush_td", "role": "def", "claimed_rank": 32}], "projection": 0.58, "games_2026": 6},
    {"rank": 10, "player": "Detroit Lions", "market_key": "spreads", "canonical_event_id": "315d06f1d48550c9", "price": 1.82, "side": null, "line": -3.0, "point": -3.0, "reason": "Detroit's offense ranks 2nd, top 3 (32.8 ppg) against a GB pass defense ranked 6th, top 10 (209.2 yds/gm allowed), while Detroit's own defense is league-worst against the pass (32nd, 321.4 yds/gm allowed) in a projected track meet. DET is 29-20 (59.2%) ATS at home since 2020 vs. GB's 23-29 (44.2%) on the road.", "evidence_check": [{"type": "current_opponent", "team": "DET", "pos": "TEAM", "stat": "ppg", "role": "off", "claimed_rank": 2}, {"type": "current_opponent", "team": "DET", "pos": "TEAM", "stat": "pass_ypg", "role": "def", "claimed_rank": 32}, {"type": "current_opponent", "team": "GB", "pos": "TEAM", "stat": "pass_ypg", "role": "def", "claimed_rank": 6}], "projection": 7, "games_2026": 5}
  ]
}
```

---

# THREE PARLAYS (built only from the 10 above; every leg from a different game)

**2-Team Parlay** — Tyler Shough Under 227.5 (PIT@NO) + Bryce Young Over 253.5 (TB@CAR). Two defense-driven environment reads on opposite sides of the Over/Under ledger — combined price **+252**.

**3-Team Parlay** — Tyler Shough Under 227.5 (PIT@NO) + Bryce Young Over 253.5 (TB@CAR) + Joe Burrow Under 260.5 (CIN@BAL). Three independent QB-yardage reads across three different games, each backed by a real opponent-rank mismatch — combined price **+561**.

**4-Team Parlay** — Tyler Shough Under 227.5 (PIT@NO) + Bryce Young Over 253.5 (TB@CAR) + Joe Burrow Under 260.5 (CIN@BAL) + Jahmyr Gibbs Under 93.5 (GB@DET). Adds a run-game Under to the three passing plays, all four from separate games with no shared correlation — combined price **+1141**.

```json
PARLAY_2_TEAM
[
  {"player": "Tyler Shough", "market_key": "player_passing_yards", "canonical_event_id": "518de03174b4f73a", "price": 1.877, "side": "under", "line": 227.5, "reason": "Shough's top-tier-pass-defense bucket shows just 120.0 pass yds/gm (n=2), and he now draws Pittsburgh's 8th-ranked pass defense (222.0 yds/gm allowed). Total is 44.5 with PIT favored by 3 \u2014 not an explosive passing environment.", "evidence_check": [{"type": "current_opponent", "team": "PIT", "pos": "QB", "stat": "pass_ypg", "role": "def", "claimed_rank": 8}], "projection": 180, "games_2026": 6},
  {"player": "Bryce Young", "market_key": "player_passing_yards", "canonical_event_id": "e361231df87eecb1", "price": 1.877, "side": "over", "line": 253.5, "reason": "Young leads the NFL at 309.8 pass yds/gm (1st) and averages 345.0 ypg at home (2 games) against a Tampa Bay pass defense ranked 19th (237.7 yds/gm allowed). Total is 44.5 with CAR favored by 2.5.", "evidence_check": [{"type": "current_opponent", "team": "TB", "pos": "QB", "stat": "pass_ypg", "role": "def", "claimed_rank": 19}], "projection": 300, "games_2026": 5}
]
```

```json
PARLAY_3_TEAM
[
  {"player": "Tyler Shough", "market_key": "player_passing_yards", "canonical_event_id": "518de03174b4f73a", "price": 1.877, "side": "under", "line": 227.5, "reason": "Shough's top-tier-pass-defense bucket shows just 120.0 pass yds/gm (n=2), and he now draws Pittsburgh's 8th-ranked pass defense (222.0 yds/gm allowed). Total is 44.5 with PIT favored by 3 \u2014 not an explosive passing environment.", "evidence_check": [{"type": "current_opponent", "team": "PIT", "pos": "QB", "stat": "pass_ypg", "role": "def", "claimed_rank": 8}], "projection": 180, "games_2026": 6},
  {"player": "Bryce Young", "market_key": "player_passing_yards", "canonical_event_id": "e361231df87eecb1", "price": 1.877, "side": "over", "line": 253.5, "reason": "Young leads the NFL at 309.8 pass yds/gm (1st) and averages 345.0 ypg at home (2 games) against a Tampa Bay pass defense ranked 19th (237.7 yds/gm allowed). Total is 44.5 with CAR favored by 2.5.", "evidence_check": [{"type": "current_opponent", "team": "TB", "pos": "QB", "stat": "pass_ypg", "role": "def", "claimed_rank": 19}], "projection": 300, "games_2026": 5},
  {"player": "Joe Burrow", "market_key": "player_passing_yards", "canonical_event_id": "f686a2afcc5ad5c8", "price": 1.877, "side": "under", "line": 260.5, "reason": "Burrow's road average is just 226.3 pass yds/gm (3 games) against a Baltimore pass defense ranked 10th (225.7 yds/gm allowed). Total is 48.5 with BAL only -1.5 favorites.", "evidence_check": [{"type": "current_opponent", "team": "BAL", "pos": "QB", "stat": "pass_ypg", "role": "def", "claimed_rank": 10}], "projection": 230, "games_2026": 5}
]
```

```json
PARLAY_4_TEAM
[
  {"player": "Tyler Shough", "market_key": "player_passing_yards", "canonical_event_id": "518de03174b4f73a", "price": 1.877, "side": "under", "line": 227.5, "reason": "Shough's top-tier-pass-defense bucket shows just 120.0 pass yds/gm (n=2), and he now draws Pittsburgh's 8th-ranked pass defense (222.0 yds/gm allowed). Total is 44.5 with PIT favored by 3 \u2014 not an explosive passing environment.", "evidence_check": [{"type": "current_opponent", "team": "PIT", "pos": "QB", "stat": "pass_ypg", "role": "def", "claimed_rank": 8}], "projection": 180, "games_2026": 6},
  {"player": "Bryce Young", "market_key": "player_passing_yards", "canonical_event_id": "e361231df87eecb1", "price": 1.877, "side": "over", "line": 253.5, "reason": "Young leads the NFL at 309.8 pass yds/gm (1st) and averages 345.0 ypg at home (2 games) against a Tampa Bay pass defense ranked 19th (237.7 yds/gm allowed). Total is 44.5 with CAR favored by 2.5.", "evidence_check": [{"type": "current_opponent", "team": "TB", "pos": "QB", "stat": "pass_ypg", "role": "def", "claimed_rank": 19}], "projection": 300, "games_2026": 5},
  {"player": "Joe Burrow", "market_key": "player_passing_yards", "canonical_event_id": "f686a2afcc5ad5c8", "price": 1.877, "side": "under", "line": 260.5, "reason": "Burrow's road average is just 226.3 pass yds/gm (3 games) against a Baltimore pass defense ranked 10th (225.7 yds/gm allowed). Total is 48.5 with BAL only -1.5 favorites.", "evidence_check": [{"type": "current_opponent", "team": "BAL", "pos": "QB", "stat": "pass_ypg", "role": "def", "claimed_rank": 10}], "projection": 230, "games_2026": 5},
  {"player": "Jahmyr Gibbs", "market_key": "player_rushing_yards", "canonical_event_id": "315d06f1d48550c9", "price": 1.877, "side": "under", "line": 93.5, "reason": "Gibbs has rushed for just 49.0 yds/gm across his two 2026 games against mid-tier run defenses; GB's run defense sits at that same caliber, ranked 17th against RBs (90.8 rush yds/gm allowed).", "evidence_check": [{"type": "current_opponent", "team": "GB", "pos": "RB", "stat": "rush_ypg", "role": "def", "claimed_rank": 17}], "projection": 70, "games_2026": 5}
]
```