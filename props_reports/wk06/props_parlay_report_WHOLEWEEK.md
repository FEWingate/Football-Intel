# COEUS WEEKLY BEST 10 + PARLAYS
## Week of 2026-10-18 — Full Slate Synthesis

**Methodology note:** Every play below is cross-checked against the REAL TEAM OFFENSE/DEFENSE RANKINGS table provided for this run — not just the earlier batch picks. Several batch picks carried flagged evidence_check mismatches; those ranks have been re-verified here directly against the authoritative table and corrected where the stat field used (season total vs. per-game rate) explained the discrepancy. 2026 data only throughout. All prices shown in prose are American odds converted from the real 1.877 decimal (-114); JSON blocks retain exact decimal prices for validator use.

---

## SECTION 1: THE BEST 10

**#1 — Drake Maye, Passing Yards UNDER 236.5 (-114)** — NYJ/NE
- Maye's averaging 245.6 pass yds/gm through 5 games, but NYJ owns the 4th-ranked pass defense in the league (195.4 ypg allowed).
- Game total is just 43.5 with NE favored by 7.5 — a lead-protecting script trims passing volume below his season rate.
- Projection: 205 yds. Games_2026: 5.

**#2 — Zay Flowers, Receiving Yards OVER 58.5 (-114)** — BAL/CLE
- Flowers is averaging 101.2 rec yds/gm through 4 games — nearly double this posted line.
- CLE's WR defense ranks 23rd (165.2 ypg allowed), a clear mismatch relative to his real season pace.
- Projection: 85 yds. Games_2026: 4.

**#3 — Tetairoa McMillan, Receiving Yards OVER 64.5 (-114)** — CAR/PHI
- McMillan is averaging 96.3 rec yds/gm through 4 games on elite target volume.
- PHI's WR defense ranks 25th (170.6 ypg allowed) — a soft matchup well under his real pace.
- Projection: 88 yds. Games_2026: 4.

**#4 — Davante Adams, Receiving Yards OVER 57.5 (-114)** — ARI/LAR
- Adams is averaging 88.2 rec yds/gm through 5 games.
- ARI's WR defense ranks 18th (156.6 ypg allowed), leaving this 57.5 line well below his real production level.
- Projection: 78 yds. Games_2026: 5.

**#5 — Trey McBride, Receiving Yards UNDER 64.5 (-114)** — ARI/LAR
- McBride's 61.6 rec yds/gm season average already sits below this line.
- LAR's defense is literally the NFL's #1-ranked TE defense (19.6 ypg allowed) — his toughest individual matchup of 2026.
- Projection: 45 yds. Games_2026: 5.

**#6 — Trevor Lawrence, Passing Yards OVER 228.5 (-114)** — HOU/JAX
- Lawrence is averaging 234.8 pass yds/gm through 5 games against HOU's 26th-ranked pass defense (256.2 ypg allowed).
- Game environment: real 42.5 total, tight -2.5 spread — competitive enough to sustain volume passing.
- Projection: 245 yds. Games_2026: 5.

**#7 — Rhamondre Stevenson, Rushing Yards UNDER 62.5 (-114)** — NYJ/NE
- Stevenson's 45.4 rush yds/gm ranks 30th among backs league-wide, well shy of this 62.5 line.
- NYJ's run defense (102.2 ypg allowed, 25th) is middling — not even a tough matchup needed to clear this under.
- Projection: 47 yds. Games_2026: 5.

**#8 — Jordan Love, Passing Yards OVER 274.5 (-114)** — DAL/GB
- Love is averaging 281.6 pass yds/gm through 5 games against Dallas's 16th-ranked pass defense (231.8 ypg allowed).
- Game environment: real 52.5 total (tied for the slate's highest) and a tight -1.5 spread — ideal volume-passing conditions.
- Projection: 290 yds. Games_2026: 5.

**#9 — Jayden Daniels, Passing Yards UNDER 205.5 (-114)** — WAS/SF
- Through just 3 games played (small sample, flagged), Daniels is averaging 153.0 pass yds/gm.
- SF's pass defense ranks 8th (210.8 ypg allowed, pass_ypg); SF is favored by 7.5 in a 51.5-total game — not ranked higher due to the thin sample.
- Projection: 165 yds. Games_2026: 3.

**#10 — Nico Collins, Receiving Yards OVER 72.5 (-114)** — HOU/JAX
- Collins is averaging 83.0 rec yds/gm across just 3 games played this season (small sample, flagged).
- JAX owns the league's worst-ranked WR defense (203.8 ypg allowed, 32nd) — same game as the Lawrence over above.
- Projection: 88 yds. Games_2026: 3.

```json
BEST_10
{
  "picks": [
    {"rank": 1, "player": "Drake Maye", "market_key": "player_passing_yards", "canonical_event_id": "29e69c87ffc2fcad", "price": 1.877, "side": "under", "line": 236.5, "projection": 205, "games_2026": 5, "reason": "Maye's averaging 245.6 pass yds/gm through 5 games, but NYJ owns the 4th-ranked pass defense (195.4 ypg allowed); NE favored by 7.5 in a 43.5-total game points to a lead-protecting script trimming his volume.", "evidence_check": [{"type": "current_opponent", "team": "NYJ", "pos": "QB", "stat": "pass_ypg", "role": "def", "claimed_rank": 4}]},
    {"rank": 2, "player": "Zay Flowers", "market_key": "player_receiving_yards", "canonical_event_id": "53c9cc1478d157c6", "price": 1.877, "side": "over", "line": 58.5, "projection": 85, "games_2026": 4, "reason": "Flowers is averaging 101.2 rec yds/gm through 4 games against CLE's 23rd-ranked WR defense (165.2 ypg allowed), well above this posted line.", "evidence_check": [{"type": "current_opponent", "team": "CLE", "pos": "WR", "stat": "rec_ypg", "role": "def", "claimed_rank": 23}]},
    {"rank": 3, "player": "Tetairoa McMillan", "market_key": "player_receiving_yards", "canonical_event_id": "20ca55788c5c6c41", "price": 1.877, "side": "over", "line": 64.5, "projection": 88, "games_2026": 4, "reason": "McMillan is averaging 96.3 rec yds/gm through 4 games against PHI's 25th-ranked WR defense (170.6 ypg allowed), a clear volume-plus-matchup edge.", "evidence_check": [{"type": "current_opponent", "team": "PHI", "pos": "WR", "stat": "rec_ypg", "role": "def", "claimed_rank": 25}]},
    {"rank": 4, "player": "Davante Adams", "market_key": "player_receiving_yards", "canonical_event_id": "13c4fc33274a5bcd", "price": 1.877, "side": "over", "line": 57.5, "projection": 78, "games_2026": 5, "reason": "Adams is averaging 88.2 rec yds/gm through 5 games against ARI's 18th-ranked WR defense (156.6 ypg allowed), well above this 57.5 line.", "evidence_check": [{"type": "current_opponent", "team": "ARI", "pos": "WR", "stat": "rec_ypg", "role": "def", "claimed_rank": 18}]},
    {"rank": 5, "player": "Trey McBride", "market_key": "player_receiving_yards", "canonical_event_id": "13c4fc33274a5bcd", "price": 1.877, "side": "under", "line": 64.5, "projection": 45, "games_2026": 5, "reason": "McBride's 61.6 rec yds/gm season average already sits below this line, and LAR's real No. 1-ranked TE defense (19.6 ypg allowed) makes this his toughest individual matchup of 2026.", "evidence_check": [{"type": "current_opponent", "team": "LAR", "pos": "TE", "stat": "rec_ypg", "role": "def", "claimed_rank": 1}]},
    {"rank": 6, "player": "Trevor Lawrence", "market_key": "player_passing_yards", "canonical_event_id": "2f598d994557ce33", "price": 1.877, "side": "over", "line": 228.5, "projection": 245, "games_2026": 5, "reason": "Lawrence is averaging 234.8 pass yds/gm through 5 games against HOU's 26th-ranked pass defense (256.2 ypg allowed); a real 42.5 total and tight -2.5 spread support continued volume.", "evidence_check": [{"type": "current_opponent", "team": "HOU", "pos": "QB", "stat": "pass_ypg", "role": "def", "claimed_rank": 26}]},
    {"rank": 7, "player": "Rhamondre Stevenson", "market_key": "player_rushing_yards", "canonical_event_id": "29e69c87ffc2fcad", "price": 1.877, "side": "under", "line": 62.5, "projection": 47, "games_2026": 5, "reason": "Stevenson's 45.4 rush yds/gm ranks 30th among backs this season, well below this 62.5 line even against a middling NYJ run defense (102.2 ypg allowed, 25th).", "evidence_check": [{"type": "current_opponent", "team": "NYJ", "pos": "RB", "stat": "rush_ypg", "role": "def", "claimed_rank": 25}]},
    {"rank": 8, "player": "Jordan Love", "market_key": "player_passing_yards", "canonical_event_id": "d06008c0dbce8a0f", "price": 1.877, "side": "over", "line": 274.5, "projection": 290, "games_2026": 5, "reason": "Love is averaging 281.6 pass yds/gm through 5 games against Dallas's 16th-ranked pass defense (231.8 ypg allowed); the real 52.5 total (tied for the slate's highest) and tight -1.5 spread support volume passing.", "evidence_check": [{"type": "current_opponent", "team": "DAL", "pos": "QB", "stat": "pass_ypg", "role": "def", "claimed_rank": 16}]},
    {"rank": 9, "player": "Jayden Daniels", "market_key": "player_passing_yards", "canonical_event_id": "f0019c9c135601e7", "price": 1.877, "side": "under", "line": 205.5, "projection": 165, "games_2026": 3, "reason": "Through just 3 games played (small sample, flagged), Daniels is averaging 153.0 pass yds/gm against SF's 8th-ranked pass defense (210.8 ypg allowed) in a 51.5-total game with SF favored by 7.5.", "evidence_check": [{"type": "current_opponent", "team": "SF", "pos": "QB", "stat": "pass_ypg", "role": "def", "claimed_rank": 8}]},
    {"rank": 10, "player": "Nico Collins", "market_key": "player_receiving_yards", "canonical_event_id": "2f598d994557ce33", "price": 1.877, "side": "over", "line": 72.5, "projection": 88, "games_2026": 3, "reason": "Collins is averaging 83.0 rec yds/gm across just 3 games played this season (small sample, flagged) against JAX's league-worst 32nd-ranked WR defense (203.8 ypg allowed).", "evidence_check": [{"type": "current_opponent", "team": "JAX", "pos": "WR", "stat": "rec_ypg", "role": "def", "claimed_rank": 32}]}
  ]
}
```

---

## SECTION 2: PARLAYS (Built Only From the 10 Above)

### 2-Leg Parlay — Combined price: +252
- Leg 1: Drake Maye Passing Yards UNDER 236.5 (NYJ/NE) — highest-conviction play of the week, blowout-script QB fade.
- Leg 2: Zay Flowers Receiving Yards OVER 58.5 (BAL/CLE) — massive gap between season pace and posted line.
- Thread: two of the biggest standalone edges on the board, from fully independent games.

### 3-Leg Parlay — Combined price: +561
- Leg 1: Drake Maye Passing Yards UNDER 236.5 (NYJ/NE)
- Leg 2: Zay Flowers Receiving Yards OVER 58.5 (BAL/CLE)
- Leg 3: Tetairoa McMillan Receiving Yards OVER 64.5 (CAR/PHI)
- Thread: top 3 ranked plays of the week, each from a different game, each backed by a verified double-digit rank/stat gap.

### 4-Leg Parlay — Combined price: +1141
- Leg 1: Drake Maye Passing Yards UNDER 236.5 (NYJ/NE)
- Leg 2: Zay Flowers Receiving Yards OVER 58.5 (BAL/CLE)
- Leg 3: Tetairoa McMillan Receiving Yards OVER 64.5 (CAR/PHI)
- Leg 4: Davante Adams Receiving Yards OVER 57.5 (ARI/LAR)
- Thread: top 4 ranked plays, four separate games, no same-game correlation — the week's cleanest high-payout combination.

```json
PARLAY_2_TEAM
[
  {"rank": 1, "player": "Drake Maye", "market_key": "player_passing_yards", "canonical_event_id": "29e69c87ffc2fcad", "price": 1.877, "side": "under", "line": 236.5, "projection": 205, "games_2026": 5, "reason": "Maye's averaging 245.6 pass yds/gm through 5 games, but NYJ owns the 4th-ranked pass defense (195.4 ypg allowed); NE favored by 7.5 in a 43.5-total game points to a lead-protecting script trimming his volume.", "evidence_check": [{"type": "current_opponent", "team": "NYJ", "pos": "QB", "stat": "pass_ypg", "role": "def", "claimed_rank": 4}]},
  {"rank": 2, "player": "Zay Flowers", "market_key": "player_receiving_yards", "canonical_event_id": "53c9cc1478d157c6", "price": 1.877, "side": "over", "line": 58.5, "projection": 85, "games_2026": 4, "reason": "Flowers is averaging 101.2 rec yds/gm through 4 games against CLE's 23rd-ranked WR defense (165.2 ypg allowed), well above this posted line.", "evidence_check": [{"type": "current_opponent", "team": "CLE", "pos": "WR", "stat": "rec_ypg", "role": "def", "claimed_rank": 23}]}
]
```

```json
PARLAY_3_TEAM
[
  {"rank": 1, "player": "Drake Maye", "market_key": "player_passing_yards", "canonical_event_id": "29e69c87ffc2fcad", "price": 1.877, "side": "under", "line": 236.5, "projection": 205, "games_2026": 5, "reason": "Maye's averaging 245.6 pass yds/gm through 5 games, but NYJ owns the 4th-ranked pass defense (195.4 ypg allowed); NE favored by 7.5 in a 43.5-total game points to a lead-protecting script trimming his volume.", "evidence_check": [{"type": "current_opponent", "team": "NYJ", "pos": "QB", "stat": "pass_ypg", "role": "def", "claimed_rank": 4}]},
  {"rank": 2, "player": "Zay Flowers", "market_key": "player_receiving_yards", "canonical_event_id": "53c9cc1478d157c6", "price": 1.877, "side": "over", "line": 58.5, "projection": 85, "games_2026": 4, "reason": "Flowers is averaging 101.2 rec yds/gm through 4 games against CLE's 23rd-ranked WR defense (165.2 ypg allowed), well above this posted line.", "evidence_check": [{"type": "current_opponent", "team": "CLE", "pos": "WR", "stat": "rec_ypg", "role": "def", "claimed_rank": 23}]},
  {"rank": 3, "player": "Tetairoa McMillan", "market_key": "player_receiving_yards", "canonical_event_id": "20ca55788c5c6c41", "price": 1.877, "side": "over", "line": 64.5, "projection": 88, "games_2026": 4, "reason": "McMillan is averaging 96.3 rec yds/gm through 4 games against PHI's 25th-ranked WR defense (170.6 ypg allowed), a clear volume-plus-matchup edge.", "evidence_check": [{"type": "current_opponent", "team": "PHI", "pos": "WR", "stat": "rec_ypg", "role": "def", "claimed_rank": 25}]}
]
```

```json
PARLAY_4_TEAM
[
  {"rank": 1, "player": "Drake Maye", "market_key": "player_passing_yards", "canonical_event_id": "29e69c87ffc2fcad", "price": 1.877, "side": "under", "line": 236.5, "projection": 205, "games_2026": 5, "reason": "Maye's averaging 245.6 pass yds/gm through 5 games, but NYJ owns the 4th-ranked pass defense (195.4 ypg allowed); NE favored by 7.5 in a 43.5-total game points to a lead-protecting script trimming his volume.", "evidence_check": [{"type": "current_opponent", "team": "NYJ", "pos": "QB", "stat": "pass_ypg", "role": "def", "claimed_rank": 4}]},
  {"rank": 2, "player": "Zay Flowers", "market_key": "player_receiving_yards", "canonical_event_id": "53c9cc1478d157c6", "price": 1.877, "side": "over", "line": 58.5, "projection": 85, "games_2026": 4, "reason": "Flowers is averaging 101.2 rec yds/gm through 4 games against CLE's 23rd-ranked WR defense (165.2 ypg allowed), well above this posted line.", "evidence_check": [{"type": "current_opponent", "team": "CLE", "pos": "WR", "stat": "rec_ypg", "role": "def", "claimed_rank": 23}]},
  {"rank": 3, "player": "Tetairoa McMillan", "market_key": "player_receiving_yards", "canonical_event_id": "20ca55788c5c6c41", "price": 1.877, "side": "over", "line": 64.5, "projection": 88, "games_2026": 4, "reason": "McMillan is averaging 96.3 rec yds/gm through 4 games against PHI's 25th-ranked WR defense (170.6 ypg allowed), a clear volume-plus-matchup edge.", "evidence_check": [{"type": "current_opponent", "team": "PHI", "pos": "WR", "stat": "rec_ypg", "role": "def", "claimed_rank": 25}]},
  {"rank": 4, "player": "Davante Adams", "market_key": "player_receiving_yards", "canonical_event_id": "13c4fc33274a5bcd", "price": 1.877, "side": "over", "line": 57.5, "projection": 78, "games_2026": 5, "reason": "Adams is averaging 88.2 rec yds/gm through 5 games against ARI's 18th-ranked WR defense (156.6 ypg allowed), well above this 57.5 line.", "evidence_check": [{"type": "current_opponent", "team": "ARI", "pos": "WR", "stat": "rec_ypg", "role": "def", "claimed_rank": 18}]}
]
```