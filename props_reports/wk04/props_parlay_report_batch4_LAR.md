# WEEK 4 PROPS & PARLAY REPORT

## REAL DATA COVERAGE CHECK (confirmed before writing)
- Passing Yards: **LIVE** (16 games)
- Rushing Yards: **LIVE** (12 games)
- Receiving Yards: **LIVE** (8 games)
- Receptions: **LIVE** (10 games)
- Anytime TD: **LIVE** (16 games)

All five stat families are live and current — no stat family is excluded this week.

**Note on alt ladders:** every alt-line ladder in this week's real data is priced **Over-only**. Any pick below that lands on the Under side has no alt-line alternative to offer — stated explicitly wherever that applies.

**Note on reception lines:** for LAR@PHI and most of GB@TB's receiving-corps names, FanDuel posted **alt ladders only, no plain line** (`"line": null`). Those picks use a specific alt threshold as "the number," clearly labeled as an alt, never invented as a plain line.

---

# SECTION 1 — COEUS PROP BREAKDOWN

## LAR @ PHI

**Kyren Williams (LAR) — Rushing Yards, Over 56.5, -114**
Williams individually ranks 9th in the NFL in rush yds/gm (71.3) against Philadelphia's defense, which ranks 26th against the run specifically to running backs (110.3 rush yds/gm allowed) — the exact convergence that fired this week's lone Standard-tier/Triple Threat designation.

**Davante Adams (LAR) — Receptions, Over 6+ (alt), +140**
Adams is averaging 6.0 rec/gm this season (individually ranked 8th among WRs) on a massive 27.4% target share, against a Philadelphia WR pass defense allowing 12.0 rec/gm to wideouts (ranked 21st, below average). Plain reception line not posted by FanDuel — this is the 6+ alt rung, Over-only.

**Jalen Hurts (PHI) — Passing Yards, Under 204.5, -114**
Hurts is averaging 206.7 pass yds/gm (individually ranked 19th) against a Los Angeles pass defense ranked 2nd in the league (174.0 yds/gm allowed) — per the Game Breakdown, no sample yet exists of Hurts facing a defense this tough, and his season average barely clears this specific line even before accounting for that gap.

## GB @ TB

**Bucky Irving (TB) — Rushing Yards, Over 55.5, -114**
Irving is averaging 60.0 rush yds/gm (individually ranked 16th) against Green Bay's run defense, which allows 126.3 rush yds/gm to backs (ranked 30th, one of the worst marks in the league) — flagged directly as the cleanest matchup edge in this game's own Game Breakdown. His home + bottom-tier-run-D bucket sits at 89.0 rush yds/gm (n=1), reinforcing the Over lean.

**Christian Watson (GB) — Receiving Yards, Over 67.5, -114**
Watson is averaging 94.7 rec yds/gm (individually ranked 5th in the NFL) against a Tampa Bay WR defense that's genuinely stingy (119.0 rec yds/gm allowed, ranked 7th) — a tough individual matchup on paper, but his own raw per-game rate still clears this specific line by almost 30 yards.

**Jordan Love (GB) — Passing Yards, Over 246.5, -114**
Love is averaging 281.3 pass yds/gm (ranked 4th in the NFL, on a league-high-tied 41.3 att/gm) against Tampa Bay's pass defense allowing 220.0 pass yds/gm (ranked 14th, mid-tier) — his volume alone clears this line even accounting for his league-worst 52.4% completion rate.

## MIA @ MIN

**Malik Willis (MIA) — Passing Yards, Over 169.5, -114**
Willis is averaging 209.0 pass yds/gm (individually ranked 20th) against Minnesota's defense, which allows 265.3 pass yds/gm (ranked 26th — a weak number by raw yardage, even though MIN's completion rate allowed is elite) — the line sits nearly 40 yards below his season average.

**Aaron Jones (MIN) — Rushing Yards, Over 67.5, -114**
Jones is averaging 67.7 rush yds/gm (individually ranked 12th among backs) against Miami's run defense, allowing 98.0 rush yds/gm to backs specifically (ranked 18th, middling-to-soft) — his 2026 pace is also a real step up from 2025's 45.67 rush yds/gm, a genuine positive trend for a veteran back.

**T.J. Hockenson (MIN) — Anytime TD, +170**
Hockenson carries a real 28.6% red-zone target share (his own strongest equivalent to a scoring rate) against Miami's tight end defense, which ranks 28th in rec yds/gm allowed (70.0) and 30th in yards-per-reception allowed (14.0, worst in the league) — the softest individual matchup in this game.

## KC @ LV *(division game — no 2026 meeting has occurred yet between these two teams; no head-to-head log exists to check)*

**Patrick Mahomes (KC) — Passing Yards, Over 236.5, -114**
Mahomes is averaging 270.7 pass yds/gm (individually ranked 6th) against a Las Vegas pass defense allowing 222.3 pass yds/gm (ranked 15th, mid-tier) — his volume clears the line comfortably even against a defense that isn't soft.

**Ashton Jeanty (LV) — Rushing Yards, Under 56.5, -114**
Jeanty individually ranks 10th in rush yds/gm (68.7), but he's facing Kansas City's run defense, which ranks 7th-best specifically against backs (68.0 rush yds/gm allowed) — the toughest matchup of his season by this exact measure, directly flagged in the Game Breakdown as a real concern for Las Vegas's ground game.

**Kirk Cousins (LV) — Passing Yards, Under 223.5, -114**
Cousins is averaging 220.3 pass yds/gm (individually ranked 17th) across three mid-tier-graded matchups this season, now facing Kansas City's pass defense ranked 3rd in the league (183.7 yds/gm allowed) — his first real top-tier pass-defense test of 2026, per this game's own Game Breakdown.

### Favorite by Position (league-wide)

**QB — Patrick Mahomes, Passing Yards Over 236.5, -114** (same reasoning as above)

**RB — Kyren Williams, Rushing Yards Over 56.5, -114** (Threat-confirmed; same reasoning as above)

**WR — Christian Watson, Receiving Yards Over 67.5, -114** (same reasoning as above)

**TE — Travis Kelce, Anytime TD, +160**
Kelce individually ranks 6th in the league in receptions among TEs (4.67/gm) against Las Vegas's defense, which ranks 28th against tight ends in receptions allowed — the exact convergence behind this week's Standard-tier/Triple Threat designation on Kelce, with the additional note that LV has allowed 5 TD receptions to tight ends all season (30th-worst), compounding the scoring-equity case.

```json
PROP_BREAKDOWN
{
  "per_game": [
    {"away": "LAR", "home": "PHI", "picks": [
      {"player": "Kyren Williams", "market_key": "player_rushing_yards", "canonical_event_id": "0b88c15fb8b87a89", "price": 1.877, "side": "over", "line": 56.5, "reason": "Williams ranks 9th in rush yds/gm (71.3) vs PHI's 26th-ranked run D against RBs (110.3 allowed) — Threat-confirmed Standard/Triple.", "evidence_check": [{"type":"current_opponent","team":"LAR","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":9},{"type":"current_opponent","team":"PHI","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":26}]},
      {"player": "Davante Adams", "market_key": "player_receptions", "canonical_event_id": "0b88c15fb8b87a89", "price": 2.4, "side": "over", "line": 6, "reason": "Adams 6.0 rec/gm (ranked 8th) on 27.4% target share vs PHI's 21st-ranked WR reception defense (12.0/gm allowed).", "evidence_check": [{"type":"current_opponent","team":"LAR","pos":"WR","stat":"rec","role":"off","claimed_rank":8},{"type":"current_opponent","team":"PHI","pos":"WR","stat":"rec_pg","role":"def","claimed_rank":21}]},
      {"player": "Jalen Hurts", "market_key": "player_passing_yards", "canonical_event_id": "0b88c15fb8b87a89", "price": 1.877, "side": "under", "line": 204.5, "reason": "Hurts 206.7 pass yds/gm (ranked 19th) vs LAR's 2nd-ranked pass D (174.0 allowed) — toughest matchup of his season.", "evidence_check": [{"type":"current_opponent","team":"PHI","pos":"QB","stat":"pass_yds","role":"off","claimed_rank":19},{"type":"current_opponent","team":"LAR","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":2}]}
    ]},
    {"away": "GB", "home": "TB", "picks": [
      {"player": "Bucky Irving", "market_key": "player_rushing_yards", "canonical_event_id": "a223ecde7f6e4844", "price": 1.877, "side": "over", "line": 55.5, "reason": "Irving 60.0 rush yds/gm (ranked 16th) vs GB's 30th-ranked run D against backs (126.3 allowed) — the cleanest matchup in this game's report.", "evidence_check": [{"type":"current_opponent","team":"TB","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":16},{"type":"current_opponent","team":"GB","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":30}]},
      {"player": "Christian Watson", "market_key": "player_receiving_yards", "canonical_event_id": "a223ecde7f6e4844", "price": 1.877, "side": "over", "line": 67.5, "reason": "Watson 94.7 rec yds/gm (ranked 5th) vs TB's 7th-ranked WR D (119.0 allowed) — tough matchup but his rate still clears this line.", "evidence_check": [{"type":"current_opponent","team":"GB","pos":"WR","stat":"rec_yds","role":"off","claimed_rank":5},{"type":"current_opponent","team":"TB","pos":"WR","stat":"rec_ypg","role":"def","claimed_rank":7}]},
      {"player": "Jordan Love", "market_key": "player_passing_yards", "canonical_event_id": "a223ecde7f6e4844", "price": 1.877, "side": "over", "line": 246.5, "reason": "Love 281.3 pass yds/gm (ranked 4th) vs TB's 14th-ranked pass D (220.0 allowed) — volume clears the line.", "evidence_check": [{"type":"current_opponent","team":"GB","pos":"QB","stat":"pass_ypg","role":"off","claimed_rank":4},{"type":"current_opponent","team":"TB","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":14}]}
    ]},
    {"away": "MIA", "home": "MIN", "picks": [
      {"player": "Malik Willis", "market_key": "player_passing_yards", "canonical_event_id": "c2a6d9dbffca7b2e", "price": 1.877, "side": "over", "line": 169.5, "reason": "Willis 209.0 pass yds/gm (ranked 20th) vs MIN's 26th-ranked pass D (265.3 allowed) — line sits well below his average.", "evidence_check": [{"type":"current_opponent","team":"MIA","pos":"QB","stat":"pass_ypg","role":"off","claimed_rank":20},{"type":"current_opponent","team":"MIN","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":26}]},
      {"player": "Aaron Jones", "market_key": "player_rushing_yards", "canonical_event_id": "c2a6d9dbffca7b2e", "price": 1.877, "side": "over", "line": 67.5, "reason": "Jones 67.7 rush yds/gm (ranked 12th) vs MIA's 18th-ranked run D against backs (98.0 allowed), plus a real positive YoY trend.", "evidence_check": [{"type":"current_opponent","team":"MIN","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":12},{"type":"current_opponent","team":"MIA","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":18}]},
      {"player": "T.J. Hockenson", "market_key": "player_anytime_td", "canonical_event_id": "c2a6d9dbffca7b2e", "price": 2.7, "side": "over", "line": null, "reason": "Hockenson's 28.6% red-zone target share vs MIA's 28th-ranked TE D (70.0 rec yds/gm allowed, worst-in-league 14.0 ypr allowed).", "evidence_check": [{"type":"current_opponent","team":"MIN","pos":"TE","stat":"rec","role":"off","claimed_rank":17},{"type":"current_opponent","team":"MIA","pos":"TE","stat":"rec_ypg","role":"def","claimed_rank":28}]}
    ]},
    {"away": "KC", "home": "LV", "picks": [
      {"player": "Patrick Mahomes", "market_key": "player_passing_yards", "canonical_event_id": "82f1042cd9096ce2", "price": 1.877, "side": "over", "line": 236.5, "reason": "Mahomes 270.7 pass yds/gm (ranked 6th) vs LV's 15th-ranked pass D (222.3 allowed) — volume clears the line.", "evidence_check": [{"type":"current_opponent","team":"KC","pos":"QB","stat":"pass_yds","role":"off","claimed_rank":6},{"type":"current_opponent","team":"LV","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":15}]},
      {"player": "Ashton Jeanty", "market_key": "player_rushing_yards", "canonical_event_id": "82f1042cd9096ce2", "price": 1.877, "side": "under", "line": 56.5, "reason": "Jeanty ranks 10th in rush yds/gm (68.7) but KC's run D ranks 7th-best vs backs (68.0 allowed) — toughest matchup of his season.", "evidence_check": [{"type":"current_opponent","team":"LV","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":10},{"type":"current_opponent","team":"KC","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":7}]},
      {"player": "Kirk Cousins", "market_key": "player_passing_yards", "canonical_event_id": "82f1042cd9096ce2", "price": 1.877, "side": "under", "line": 223.5, "reason": "Cousins 220.3 pass yds/gm (ranked 17th) vs KC's 3rd-ranked pass D (183.7 allowed) — his first real top-tier test of the season.", "evidence_check": [{"type":"current_opponent","team":"LV","pos":"QB","stat":"pass_ypg","role":"off","claimed_rank":17},{"type":"current_opponent","team":"KC","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":3}]}
    ]}
  ],
  "per_position": {
    "QB": {"player": "Patrick Mahomes", "market_key": "player_passing_yards", "canonical_event_id": "82f1042cd9096ce2", "price": 1.877, "side": "over", "line": 236.5, "reason": "Best QB value league-wide — 270.7 pass yds/gm (ranked 6th) vs LV's 15th-ranked pass D.", "evidence_check": [{"type":"current_opponent","team":"KC","pos":"QB","stat":"pass_yds","role":"off","claimed_rank":6},{"type":"current_opponent","team":"LV","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":15}]},
    "RB": {"player": "Kyren Williams", "market_key": "player_rushing_yards", "canonical_event_id": "0b88c15fb8b87a89", "price": 1.877, "side": "over", "line": 56.5, "reason": "Threat-confirmed Standard/Triple — 9th-ranked rusher vs PHI's 26th-ranked RB run D.", "evidence_check": [{"type":"current_opponent","team":"LAR","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":9},{"type":"current_opponent","team":"PHI","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":26}]},
    "WR": {"player": "Christian Watson", "market_key": "player_receiving_yards", "canonical_event_id": "a223ecde7f6e4844", "price": 1.877, "side": "over", "line": 67.5, "reason": "5th-ranked receiver league-wide; line sits far below his 94.7 rec yds/gm season average.", "evidence_check": [{"type":"current_opponent","team":"GB","pos":"WR","stat":"rec_yds","role":"off","claimed_rank":5},{"type":"current_opponent","team":"TB","pos":"WR","stat":"rec_ypg","role":"def","claimed_rank":7}]},
    "TE": {"player": "Travis Kelce", "market_key": "player_anytime_td", "canonical_event_id": "82f1042cd9096ce2", "price": 2.6, "side": "over", "line": null, "reason": "Threat-confirmed Standard/Triple — 6th-ranked in TE receptions vs LV's 28th-ranked TE reception D, plus LV's 30th-ranked TE TD rate allowed.", "evidence_check": [{"type":"current_opponent","team":"KC","pos":"TE","stat":"rec","role":"off","claimed_rank":6},{"type":"current_opponent","team":"LV","pos":"TE","stat":"rec","role":"def","claimed_rank":28}]}
  }
}
```

---

# SECTION 2 — FAVORITE OVERS AND UNDERS FOR THE WEEK

### Overs (ranked by conviction)
1. **Kyren Williams rushing Over 56.5, -114** — Threat-confirmed Standard/Triple; cleanest individual edge on the slate.
2. **Bucky Irving rushing Over 55.5, -114** — flagged directly by the Game Breakdown as this week's single best matchup.
3. **Davante Adams receptions Over 6+ (alt), +140** — elite target-share volume vs a soft perimeter D.
4. **Patrick Mahomes passing Over 236.5, -114** — volume-based offense vs a mid-tier pass D.
5. **Jordan Love passing Over 246.5, -114** — line sits well below his league-4th-ranked average, despite volatility.

### Unders
1. **Jalen Hurts passing Under 204.5, -114** — first-ever matchup with a top-2 pass defense.
2. **Kirk Cousins passing Under 223.5, -114** — first real top-tier pass-D test of the season.
3. **Ashton Jeanty rushing Under 56.5, -114** — toughest individual run-D matchup of his season.
4. **Saquon Barkley rushing Under 74.5, -114** — Barkley's own 58.0 rush yds/gm (individually ranked 19th) sits well below this line against LAR's 11th-ranked run D vs RBs (80.3 allowed) — the line is priced above his actual season rate.

```json
FAVORITE_OU
{
  "overs": [
    {"player": "Kyren Williams", "market_key": "player_rushing_yards", "canonical_event_id": "0b88c15fb8b87a89", "price": 1.877, "side": "over", "line": 56.5, "reason": "Threat-confirmed Standard/Triple — 9th-ranked rusher vs PHI's 26th-ranked RB run D.", "evidence_check": [{"type":"current_opponent","team":"LAR","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":9},{"type":"current_opponent","team":"PHI","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":26}]},
    {"player": "Bucky Irving", "market_key": "player_rushing_yards", "canonical_event_id": "a223ecde7f6e4844", "price": 1.877, "side": "over", "line": 55.5, "reason": "16th-ranked rusher vs GB's 30th-ranked RB run D — cleanest matchup on the slate.", "evidence_check": [{"type":"current_opponent","team":"TB","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":16},{"type":"current_opponent","team":"GB","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":30}]},
    {"player": "Davante Adams", "market_key": "player_receptions", "canonical_event_id": "0b88c15fb8b87a89", "price": 2.4, "side": "over", "line": 6, "reason": "27.4% target share, 8th-ranked WR in receptions, vs PHI's 21st-ranked WR reception D.", "evidence_check": [{"type":"current_opponent","team":"LAR","pos":"WR","stat":"rec","role":"off","claimed_rank":8},{"type":"current_opponent","team":"PHI","pos":"WR","stat":"rec_pg","role":"def","claimed_rank":21}]},
    {"player": "Patrick Mahomes", "market_key": "player_passing_yards", "canonical_event_id": "82f1042cd9096ce2", "price": 1.877, "side": "over", "line": 236.5, "reason": "6th-ranked passer vs LV's 15th-ranked pass D.", "evidence_check": [{"type":"current_opponent","team":"KC","pos":"QB","stat":"pass_yds","role":"off","claimed_rank":6},{"type":"current_opponent","team":"LV","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":15}]},
    {"player": "Jordan Love", "market_key": "player_passing_yards", "canonical_event_id": "a223ecde7f6e4844", "price": 1.877, "side": "over", "line": 246.5, "reason": "4th-ranked passer vs TB's 14th-ranked pass D; line sits well below his average.", "evidence_check": [{"type":"current_opponent","team":"GB","pos":"QB","stat":"pass_ypg","role":"off","claimed_rank":4},{"type":"current_opponent","team":"TB","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":14}]}
  ],
  "unders": [
    {"player": "Jalen Hurts", "market_key": "player_passing_yards", "canonical_event_id": "0b88c15fb8b87a89", "price": 1.877, "side": "under", "line": 204.5, "reason": "19th-ranked passer facing LAR's 2nd-ranked pass D for the first time all season.", "evidence_check": [{"type":"current_opponent","team":"PHI","pos":"QB","stat":"pass_yds","role":"off","claimed_rank":19},{"type":"current_opponent","team":"LAR","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":2}]},
    {"player": "Kirk Cousins", "market_key": "player_passing_yards", "canonical_event_id": "82f1042cd9096ce2", "price": 1.877, "side": "under", "line": 223.5, "reason": "17th-ranked passer facing KC's 3rd-ranked pass D, a step up from three mid-tier matchups.", "evidence_check": [{"type":"current_opponent","team":"LV","pos":"QB","stat":"pass_ypg","role":"off","claimed_rank":17},{"type":"current_opponent","team":"KC","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":3}]},
    {"player": "Ashton Jeanty", "market_key": "player_rushing_yards", "canonical_event_id": "82f1042cd9096ce2", "price": 1.877, "side": "under", "line": 56.5, "reason": "10th-ranked rusher facing KC's 7th-ranked run D vs backs — toughest test of his season.", "evidence_check": [{"type":"current_opponent","team":"LV","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":10},{"type":"current_opponent","team":"KC","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":7}]},
    {"player": "Saquon Barkley", "market_key": "player_rushing_yards", "canonical_event_id": "0b88c15fb8b87a89", "price": 1.877, "side": "under", "line": 74.5, "reason": "Barkley's 58.0 rush yds/gm (ranked 19th) sits well under this line vs LAR's 11th-ranked run D vs RBs.", "evidence_check": [{"type":"current_opponent","team":"PHI","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":19},{"type":"current_opponent","team":"LAR","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":11}]}
  ]
}
```

---

# SECTION 3 — FIVE PARLAYS (LINE-BASED, 3/4/5/6/7-TEAM)

### 3-Team Parlay — different games, no overlap
- Mahomes passing Over 236.5 (-114)
- Kyren Williams rushing Over 56.5 (-114)
- Bucky Irving rushing Over 55.5 (-114)
- Thread: three independent best bets from three different games, each matching a strong individual against a soft-to-mid matchup. Combined price: **+561**

### 4-Team Parlay
- Adds Malik Willis passing Over 169.5 (-114), MIA@MIN
- Thread: same as above plus a fourth independent volume-based Over. Combined price: **+1141**

### 5-Team Parlay
- Adds Jalen Hurts passing Under 204.5 (-114), LAR@PHI — **shares a game with Kyren Williams (same canonical_event_id 0b88c15fb8b87a89)**: if LA leans on Williams to control the clock, that's a real complementary thesis for Hurts throwing less, not purely a coincidental stack.
- Combined price: **+2230**

### 6-Team Parlay
- Adds Christian Watson receiving Over 67.5 (-114), GB@TB — **shares a game with Bucky Irving (same canonical_event_id a223ecde7f6e4844)**. The combined price below is a cross-game-style estimate, not a real FanDuel same-game-parlay quote for that pairing.
- Combined price: **+4273**

### 7-Team Parlay
- Adds Kirk Cousins passing Under 223.5 (-114), KC@LV — **shares a game with Patrick Mahomes (same canonical_event_id 82f1042cd9096ce2)**. Again, not a real SGP quote for that pair — flagged explicitly.
- Combined price: **+8108**

```json
PARLAY_3_TEAM
[
  {"player": "Patrick Mahomes", "market_key": "player_passing_yards", "canonical_event_id": "82f1042cd9096ce2", "price": 1.877, "side": "over", "line": 236.5, "reason": "6th-ranked passer vs LV's 15th-ranked pass D.", "evidence_check": [{"type":"current_opponent","team":"KC","pos":"QB","stat":"pass_yds","role":"off","claimed_rank":6},{"type":"current_opponent","team":"LV","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":15}]},
  {"player": "Kyren Williams", "market_key": "player_rushing_yards", "canonical_event_id": "0b88c15fb8b87a89", "price": 1.877, "side": "over", "line": 56.5, "reason": "Threat-confirmed Standard/Triple vs PHI's 26th-ranked RB run D.", "evidence_check": [{"type":"current_opponent","team":"LAR","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":9},{"type":"current_opponent","team":"PHI","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":26}]},
  {"player": "Bucky Irving", "market_key": "player_rushing_yards", "canonical_event_id": "a223ecde7f6e4844", "price": 1.877, "side": "over", "line": 55.5, "reason": "16th-ranked rusher vs GB's 30th-ranked RB run D.", "evidence_check": [{"type":"current_opponent","team":"TB","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":16},{"type":"current_opponent","team":"GB","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":30}]}
]
```

```json
PARLAY_4_TEAM
[
  {"player": "Patrick Mahomes", "market_key": "player_passing_yards", "canonical_event_id": "82f1042cd9096ce2", "price": 1.877, "side": "over", "line": 236.5, "reason": "6th-ranked passer vs LV's 15th-ranked pass D.", "evidence_check": [{"type":"current_opponent","team":"KC","pos":"QB","stat":"pass_yds","role":"off","claimed_rank":6},{"type":"current_opponent","team":"LV","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":15}]},
  {"player": "Kyren Williams", "market_key": "player_rushing_yards", "canonical_event_id": "0b88c15fb8b87a89", "price": 1.877, "side": "over", "line": 56.5, "reason": "Threat-confirmed Standard/Triple vs PHI's 26th-ranked RB run D.", "evidence_check": [{"type":"current_opponent","team":"LAR","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":9},{"type":"current_opponent","team":"PHI","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":26}]},
  {"player": "Bucky Irving", "market_key": "player_rushing_yards", "canonical_event_id": "a223ecde7f6e4844", "price": 1.877, "side": "over", "line": 55.5, "reason": "16th-ranked rusher vs GB's 30th-ranked RB run D.", "evidence_check": [{"type":"current_opponent","team":"TB","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":16},{"type":"current_opponent","team":"GB","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":30}]},
  {"player": "Malik Willis", "market_key": "player_passing_yards", "canonical_event_id": "c2a6d9dbffca7b2e", "price": 1.877, "side": "over", "line": 169.5, "reason": "20th-ranked passer vs MIN's 26th-ranked pass D; line well below his average.", "evidence_check": [{"type":"current_opponent","team":"MIA","pos":"QB","stat":"pass_ypg","role":"off","claimed_rank":20},{"type":"current_opponent","team":"MIN","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":26}]}
]
```

```json
PARLAY_5_TEAM
[
  {"player": "Patrick Mahomes", "market_key": "player_passing_yards", "canonical_event_id": "82f1042cd9096ce2", "price": 1.877, "side": "over", "line": 236.5, "reason": "6th-ranked passer vs LV's 15th-ranked pass D.", "evidence_check": [{"type":"current_opponent","team":"KC","pos":"QB","stat":"pass_yds","role":"off","claimed_rank":6},{"type":"current_opponent","team":"LV","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":15}]},
  {"player": "Malik Willis", "market_key": "player_passing_yards", "canonical_event_id": "c2a6d9dbffca7b2e", "price": 1.877, "side": "over", "line": 169.5, "reason": "20th-ranked passer vs MIN's 26th-ranked pass D.", "evidence_check": [{"type":"current_opponent","team":"MIA","pos":"QB","stat":"pass_ypg","role":"off","claimed_rank":20},{"type":"current_opponent","team":"MIN","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":26}]},
  {"player": "Kyren Williams", "market_key": "player_rushing_yards", "canonical_event_id": "0b88c15fb8b87a89", "price": 1.877, "side": "over", "line": 56.5, "reason": "Threat-confirmed Standard/Triple vs PHI's 26th-ranked RB run D.", "evidence_check": [{"type":"current_opponent","team":"LAR","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":9},{"type":"current_opponent","team":"PHI","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":26}]},
  {"player": "Jalen Hurts", "market_key": "player_passing_yards", "canonical_event_id": "0b88c15fb8b87a89", "price": 1.877, "side": "under", "line": 204.5, "reason": "19th-ranked passer vs LAR's 2nd-ranked pass D; same game as Williams leg.", "evidence_check": [{"type":"current_opponent","team":"PHI","pos":"QB","stat":"pass_yds","role":"off","claimed_rank":19},{"type":"current_opponent","team":"LAR","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":2}]},
  {"player": "Bucky Irving", "market_key": "player_rushing_yards", "canonical_event_id": "a223ecde7f6e4844", "price": 1.877, "side": "over", "line": 55.5, "reason": "16th-ranked rusher vs GB's 30th-ranked RB run D.", "evidence_check": [{"type":"current_opponent","team":"TB","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":16},{"type":"current_opponent","team":"GB","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":30}]}
]
```

```json
PARLAY_6_TEAM
[
  {"player": "Patrick Mahomes", "market_key": "player_passing_yards", "canonical_event_id": "82f1042cd9096ce2", "price": 1.877, "side": "over", "line": 236.5, "reason": "6th-ranked passer vs LV's 15th-ranked pass D.", "evidence_check": [{"type":"current_opponent","team":"KC","pos":"QB","stat":"pass_yds","role":"off","claimed_rank":6},{"type":"current_opponent","team":"LV","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":15}]},
  {"player": "Malik Willis", "market_key": "player_passing_yards", "canonical_event_id": "c2a6d9dbffca7b2e", "price": 1.877, "side": "over", "line": 169.5, "reason": "20th-ranked passer vs MIN's 26th-ranked pass D.", "evidence_check": [{"type":"current_opponent","team":"MIA","pos":"QB","stat":"pass_ypg","role":"off","claimed_rank":20},{"type":"current_opponent","team":"MIN","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":26}]},
  {"player": "Kyren Williams", "market_key": "player_rushing_yards", "canonical_event_id": "0b88c15fb8b87a89", "price": 1.877, "side": "over", "line": 56.5, "reason": "Threat-confirmed Standard/Triple vs PHI's 26th-ranked RB run D.", "evidence_check": [{"type":"current_opponent","team":"LAR","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":9},{"type":"current_opponent","team":"PHI","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":26}]},
  {"player": "Jalen Hurts", "market_key": "player_passing_yards", "canonical_event_id": "0b88c15fb8b87a89", "price": 1.877, "side": "under", "line": 204.5, "reason": "19th-ranked passer vs LAR's 2nd-ranked pass D; same game as Williams leg.", "evidence_check": [{"type":"current_opponent","team":"PHI","pos":"QB","stat":"pass_yds","role":"off","claimed_rank":19},{"type":"current_opponent","team":"LAR","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":2}]},
  {"player": "Bucky Irving", "market_key": "player_rushing_yards", "canonical_event_id": "a223ecde7f6e4844", "price": 1.877, "side": "over", "line": 55.5, "reason": "16th-ranked rusher vs GB's 30th-ranked RB run D.", "evidence_check": [{"type":"current_opponent","team":"TB","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":16},{"type":"current_opponent","team":"GB","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":30}]},
  {"player": "Christian Watson", "market_key": "player_receiving_yards", "canonical_event_id": "a223ecde7f6e4844", "price": 1.877, "side": "over", "line": 67.5, "reason": "5th-ranked receiver vs TB's 7th-ranked WR D; same game as Irving leg.", "evidence_check": [{"type":"current_opponent","team":"GB","pos":"WR","stat":"rec_yds","role":"off","claimed_rank":5},{"type":"current_opponent","team":"TB","pos":"WR","stat":"rec_ypg","role":"def","claimed_rank":7}]}
]
```

```json
PARLAY_7_TEAM
[
  {"player": "Patrick Mahomes", "market_key": "player_passing_yards", "canonical_event_id": "82f1042cd9096ce2", "price": 1.877, "side": "over", "line": 236.5, "reason": "6th-ranked passer vs LV's 15th-ranked pass D.", "evidence_check": [{"type":"current_opponent","team":"KC","pos":"QB","stat":"pass_yds","role":"off","claimed_rank":6},{"type":"current_opponent","team":"LV","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":15}]},
  {"player": "Kirk Cousins", "market_key": "player_passing_yards", "canonical_event_id": "82f1042cd9096ce2", "price": 1.877, "side": "under", "line": 223.5, "reason": "17th-ranked passer vs KC's 3rd-ranked pass D; same game as Mahomes leg.", "evidence_check": [{"type":"current_opponent","team":"LV","pos":"QB","stat":"pass_ypg","role":"off","claimed_rank":17},{"type":"current_opponent","team":"KC","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":3}]},
  {"player": "Malik Willis", "market_key": "player_passing_yards", "canonical_event_id": "c2a6d9dbffca7b2e", "price": 1.877, "side": "over", "line": 169.5, "reason": "20th-ranked passer vs MIN's 26th-ranked pass D.", "evidence_check": [{"type":"current_opponent","team":"MIA","pos":"QB","stat":"pass_ypg","role":"off","claimed_rank":20},{"type":"current_opponent","team":"MIN","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":26}]},
  {"player": "Kyren Williams", "market_key": "player_rushing_yards", "canonical_event_id": "0b88c15fb8b87a89", "price": 1.877, "side": "over", "line": 56.5, "reason": "Threat-confirmed Standard/Triple vs PHI's 26th-ranked RB run D.", "evidence_check": [{"type":"current_opponent","team":"LAR","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":9},{"type":"current_opponent","team":"PHI","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":26}]},
  {"player": "Jalen Hurts", "market_key": "player_passing_yards", "canonical_event_id": "0b88c15fb8b87a89", "price": 1.877, "side": "under", "line": 204.5, "reason": "19th-ranked passer vs LAR's 2nd-ranked pass D; same game as Williams leg.", "evidence_check": [{"type":"current_opponent","team":"PHI","pos":"QB","stat":"pass_yds","role":"off","claimed_rank":19},{"type":"current_opponent","team":"LAR","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":2}]},
  {"player": "Bucky Irving", "market_key": "player_rushing_yards", "canonical_event_id": "a223ecde7f6e4844", "price": 1.877, "side": "over", "line": 55.5, "reason": "16th-ranked rusher vs GB's 30th-ranked RB run D.", "evidence_check": [{"type":"current_opponent","team":"TB","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":16},{"type":"current_opponent","team":"GB","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":30}]},
  {"player": "Christian Watson", "market_key": "player_receiving_yards", "canonical_event_id": "a223ecde7f6e4844", "price": 1.877, "side": "over", "line": 67.5, "reason": "5th-ranked receiver vs TB's 7th-ranked WR D; same game as Irving leg.", "evidence_check": [{"type":"current_opponent","team":"GB","pos":"WR","stat":"rec_yds","role":"off","claimed_rank":5},{"type":"current_opponent","team":"TB","pos":"WR","stat":"rec_ypg","role":"def","claimed_rank":7}]}
]
```

---

# SECTION 4 — FAVORITE ANYTIME TD PARLAYS (3/4/5/6/7-TEAM)

### 3-Team TD Parlay
- Kenneth Walker III (-175) — KC
- Aaron Jones (+170 as decimal 1.588 → -170) — MIN
- Kyren Williams (-110) — LAR
- Thread: three real RB TD favorites from three different games, each with real red-zone role support. Combined price: **+376**

### 4-Team TD Parlay
- Adds Bucky Irving (+175), TB
- Combined price: **+1210**

### 5-Team TD Parlay
- Adds T.J. Hockenson (+170), MIN — **shares a game with Aaron Jones (same canonical_event_id c2a6d9dbffca7b2e)**
- Combined price: **+3436**

### 6-Team TD Parlay
- Adds Travis Kelce (+160), KC — **shares a game with Kenneth Walker III (same canonical_event_id 82f1042cd9096ce2)**
- Combined price: **+8994**

### 7-Team TD Parlay
- Adds Christian Watson (+155), GB — **shares a game with Bucky Irving (same canonical_event_id a223ecde7f6e4844)**
- Combined price: **+23345**

```json
TD_PARLAY_3_TEAM
[
  {"player": "Kenneth Walker III", "market_key": "player_anytime_td", "canonical_event_id": "82f1042cd9096ce2", "price": 1.571, "side": "over", "line": null, "reason": "83.3% red-zone carry share, KC's bellcow, vs LV's RB rush-TD rate (1 allowed, ranked 11th).", "evidence_check": [{"type":"current_opponent","team":"KC","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":1},{"type":"current_opponent","team":"LV","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":14}]},
  {"player": "Aaron Jones", "market_key": "player_anytime_td", "canonical_event_id": "c2a6d9dbffca7b2e", "price": 1.588, "side": "over", "line": null, "reason": "50% red-zone carry share vs Miami's 28th-ranked rush-TD-allowed rate to backs (3 TD allowed).", "evidence_check": [{"type":"current_opponent","team":"MIN","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":12},{"type":"current_opponent","team":"MIA","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":18}]},
  {"player": "Kyren Williams", "market_key": "player_anytime_td", "canonical_event_id": "0b88c15fb8b87a89", "price": 1.909, "side": "over", "line": null, "reason": "66.7% red-zone carry share and Threat-confirmed vs PHI's RB rush-TD rate (1 allowed, ranked 13th).", "evidence_check": [{"type":"current_opponent","team":"LAR","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":9},{"type":"current_opponent","team":"PHI","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":26}]}
]
```

```json
TD_PARLAY_4_TEAM
[
  {"player": "Kenneth Walker III", "market_key": "player_anytime_td", "canonical_event_id": "82f1042cd9096ce2", "price": 1.571, "side": "over", "line": null, "reason": "83.3% red-zone carry share vs LV's RB rush-TD rate (1 allowed, ranked 11th).", "evidence_check": [{"type":"current_opponent","team":"KC","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":1},{"type":"current_opponent","team":"LV","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":14}]},
  {"player": "Aaron Jones", "market_key": "player_anytime_td", "canonical_event_id": "c2a6d9dbffca7b2e", "price": 1.588, "side": "over", "line": null, "reason": "50% red-zone carry share vs Miami's 28th-ranked rush-TD-allowed rate to backs.", "evidence_check": [{"type":"current_opponent","team":"MIN","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":12},{"type":"current_opponent","team":"MIA","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":18}]},
  {"player": "Kyren Williams", "market_key": "player_anytime_td", "canonical_event_id": "0b88c15fb8b87a89", "price": 1.909, "side": "over", "line": null, "reason": "66.7% red-zone carry share and Threat-confirmed vs PHI's RB rush-TD rate.", "evidence_check": [{"type":"current_opponent","team":"LAR","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":9},{"type":"current_opponent","team":"PHI","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":26}]},
  {"player": "Bucky Irving", "market_key": "player_anytime_td", "canonical_event_id": "a223ecde7f6e4844", "price": 2.75, "side": "over", "line": null, "reason": "33.3% red-zone carry share vs GB's 32nd-ranked rush-TD-allowed rate to backs (6 allowed).", "evidence_check": [{"type":"current_opponent","team":"TB","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":16},{"type":"current_opponent","team":"GB","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":30}]}
]
```

```json
TD_PARLAY_5_TEAM
[
  {"player": "Kenneth Walker III", "market_key": "player_anytime_td", "canonical_event_id": "82f1042cd9096ce2", "price": 1.571, "side": "over", "line": null, "reason": "83.3% red-zone carry share vs LV's RB rush-TD rate (1 allowed, ranked 11th).", "evidence_check": [{"type":"current_opponent","team":"KC","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":1},{"type":"current_opponent","team":"LV","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":14}]},
  {"player": "Aaron Jones", "market_key": "player_anytime_td", "canonical_event_id": "c2a6d9dbffca7b2e", "price": 1.588, "side": "over", "line": null, "reason": "50% red-zone carry share vs Miami's 28th-ranked rush-TD-allowed rate to backs.", "evidence_check": [{"type":"current_opponent","team":"MIN","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":12},{"type":"current_opponent","team":"MIA","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":18}]},
  {"player": "Kyren Williams", "market_key": "player_anytime_td", "canonical_event_id": "0b88c15fb8b87a89", "price": 1.909, "side": "over", "line": null, "reason": "66.7% red-zone carry share and Threat-confirmed vs PHI's RB rush-TD rate.", "evidence_check": [{"type":"current_opponent","team":"LAR","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":9},{"type":"current_opponent","team":"PHI","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":26}]},
  {"player": "Bucky Irving", "market_key": "player_anytime_td", "canonical_event_id": "a223ecde7f6e4844", "price": 2.75, "side": "over", "line": null, "reason": "33.3% red-zone carry share vs GB's 30th-ranked rush-TD-allowed rate to backs.", "evidence_check": [{"type":"current_opponent","team":"TB","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":16},{"type":"current_opponent","team":"GB","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":30}]},
  {"player": "T.J. Hockenson", "market_key": "player_anytime_td", "canonical_event_id": "c2a6d9dbffca7b2e", "price": 2.7, "side": "over", "line": null, "reason": "28.6% red-zone target share vs MIA's 28th-ranked TE reception D; same game as Jones leg.", "evidence_check": [{"type":"current_opponent","team":"MIN","pos":"TE","stat":"rec","role":"off","claimed_rank":17},{"type":"current_opponent","team":"MIA","pos":"TE","stat":"rec_ypg","role":"def","claimed_rank":28}]}
]
```

```json
TD_PARLAY_6_TEAM
[
  {"player": "Kenneth Walker III", "market_key": "player_anytime_td", "canonical_event_id": "82f1042cd9096ce2", "price": 1.571, "side": "over", "line": null, "reason": "83.3% red-zone carry share vs LV's RB rush-TD rate.", "evidence_check": [{"type":"current_opponent","team":"KC","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":1},{"type":"current_opponent","team":"LV","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":14}]},
  {"player": "Aaron Jones", "market_key": "player_anytime_td", "canonical_event_id": "c2a6d9dbffca7b2e", "price": 1.588, "side": "over", "line": null, "reason": "50% red-zone carry share vs Miami's 28th-ranked rush-TD-allowed rate.", "evidence_check": [{"type":"current_opponent","team":"MIN","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":12},{"type":"current_opponent","team":"MIA","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":18}]},
  {"player": "Kyren Williams", "market_key": "player_anytime_td", "canonical_event_id": "0b88c15fb8b87a89", "price": 1.909, "side": "over", "line": null, "reason": "66.7% red-zone carry share and Threat-confirmed.", "evidence_check": [{"type":"current_opponent","team":"LAR","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":9},{"type":"current_opponent","team":"PHI","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":26}]},
  {"player": "Bucky Irving", "market_key": "player_anytime_td", "canonical_event_id": "a223ecde7f6e4844", "price": 2.75, "side": "over", "line": null, "reason": "33.3% red-zone carry share vs GB's 30th-ranked rush-TD-allowed rate.", "evidence_check": [{"type":"current_opponent","team":"TB","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":16},{"type":"current_opponent","team":"GB","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":30}]},
  {"player": "T.J. Hockenson", "market_key": "player_anytime_td", "canonical_event_id": "c2a6d9dbffca7b2e", "price": 2.7, "side": "over", "line": null, "reason": "28.6% red-zone target share vs MIA's 28th-ranked TE reception D; same game as Jones leg.", "evidence_check": [{"type":"current_opponent","team":"MIN","pos":"TE","stat":"rec","role":"off","claimed_rank":17},{"type":"current_opponent","team":"MIA","pos":"TE","stat":"rec_ypg","role":"def","claimed_rank":28}]},
  {"player": "Travis Kelce", "market_key": "player_anytime_td", "canonical_event_id": "82f1042cd9096ce2", "price": 2.6, "side": "over", "line": null, "reason": "Threat-confirmed Standard/Triple; 6th-ranked TE receiver vs LV's 28th-ranked TE reception D, plus LV's 30th-ranked TE TD-allowed rate; same game as Walker leg.", "evidence_check": [{"type":"current_opponent","team":"KC","pos":"TE","stat":"rec","role":"off","claimed_rank":6},{"type":"current_opponent","team":"LV","pos":"TE","stat":"rec","role":"def","claimed_rank":28}]}
]
```

```json
TD_PARLAY_7_TEAM
[
  {"player": "Kenneth Walker III", "market_key": "player_anytime_td", "canonical_event_id": "82f1042cd9096ce2", "price": 1.571, "side": "over", "line": null, "reason": "83.3% red-zone carry share vs LV's RB rush-TD rate.", "evidence_check": [{"type":"current_opponent","team":"KC","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":1},{"type":"current_opponent","team":"LV","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":14}]},
  {"player": "Aaron Jones", "market_key": "player_anytime_td", "canonical_event_id": "c2a6d9dbffca7b2e", "price": 1.588, "side": "over", "line": null, "reason": "50% red-zone carry share vs Miami's 28th-ranked rush-TD-allowed rate.", "evidence_check": [{"type":"current_opponent","team":"MIN","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":12},{"type":"current_opponent","team":"MIA","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":18}]},
  {"player": "Kyren Williams", "market_key": "player_anytime_td", "canonical_event_id": "0b88c15fb8b87a89", "price": 1.909, "side": "over", "line": null, "reason": "66.7% red-zone carry share and Threat-confirmed.", "evidence_check": [{"type":"current_opponent","team":"LAR","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":9},{"type":"current_opponent","team":"PHI","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":26}]},
  {"player": "Bucky Irving", "market_key": "player_anytime_td", "canonical_event_id": "a223ecde7f6e4844", "price": 2.75, "side": "over", "line": null, "reason": "33.3% red-zone carry share vs GB's 30th-ranked rush-TD-allowed rate.", "evidence_check": [{"type":"current_opponent","team":"TB","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":16},{"type":"current_opponent","team":"GB","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":30}]},
  {"player": "T.J. Hockenson", "market_key": "player_anytime_td", "canonical_event_id": "c2a6d9dbffca7b2e", "price": 2.7, "side": "over", "line": null, "reason": "28.6% red-zone target share vs MIA's 28th-ranked TE reception D; same game as Jones leg.", "evidence_check": [{"type":"current_opponent","team":"MIN","pos":"TE","stat":"rec","role":"off","claimed_rank":17},{"type":"current_opponent","team":"MIA","pos":"TE","stat":"rec_ypg","role":"def","claimed_rank":28}]},
  {"player": "Travis Kelce", "market_key": "player_anytime_td", "canonical_event_id": "82f1042cd9096ce2", "price": 2.6, "side": "over", "line": null, "reason": "Threat-confirmed Standard/Triple; same game as Walker leg.", "evidence_check": [{"type":"current_opponent","team":"KC","pos":"TE","stat":"rec","role":"off","claimed_rank":6},{"type":"current_opponent","team":"LV","pos":"TE","stat":"rec","role":"def","claimed_rank":28}]},
  {"player": "Christian Watson", "market_key": "player_anytime_td", "canonical_event_id": "a223ecde7f6e4844", "price": 2.55, "side": "over", "line": null, "reason": "33.3% red-zone target share vs TB's WR TD-allowed rate (5 TD, ranked 6th-tightest, a real counter-signal worth flagging even as a volume-based inclusion); same game as Irving leg.", "evidence_check": [{"type":"current_opponent","team":"GB","pos":"WR","stat":"rec_yds","role":"off","claimed_rank":5},{"type":"current_opponent","team":"TB","pos":"WR","stat":"rec_ypg","role":"def","claimed_rank":7}]}
]
```

---

# SECTION 5 — FAVORITE SPREAD PARLAYS (3/4/5/6/7-TEAM)

**Real data limitation, stated plainly rather than fabricated:** this slate has exactly 4 games, each offering exactly one real mainline spread market (two sides). That caps the total pool of non-contradictory real spread legs at **4** — one per game. A 5, 6, or 7-team spread parlay would require either repeating a team's own spread leg (nonsensical — can't bet both sides, or the same side twice) or inventing a market that doesn't exist on this slate. Per this Standard's prohibition on fabrication, **no 5-team, 6-team, or 7-team spread parlay JSON block is produced this week.** Only the 3-team and 4-team real combinations are presented below, using all 4 available spreads.

### 3-Team Spread Parlay
- **Las Vegas Raiders +4.5 (-108)** — LV's home ATS record is 54.9% (28-23-1) since 2020, a real strength; KC's road ATS record is a weak 44.0% (22-28-1) over the same span.
- **Philadelphia Eagles +3.0 (-105)** — PHI's home ATS record is 53.1% (26-23-2); LAR's road ATS record is a comparably strong 54.0% (27-23-2) — a genuinely split signal, consistent with the Game Breakdown's "coin-flip" read on this game; taken as the home side given PHI's own situational-football identity.
- **Green Bay Packers -3.5 (-110)** — TB's home ATS record is a weak 43.1% (22-29-1), the softest home number on this slate; GB's road ATS record is also soft (44.2%, 23-29-1), so this is a mixed signal overall, but TB's home number is the single worst on the board.
- Thread: three independent spread leans, with real, cited ATS context on both sides of every leg. Combined price: **+618**

### 4-Team Spread Parlay
- Adds **Miami Dolphins +10.5 (-105)** — MIN's home ATS record is a modest 47.1% (24-27-0), below .500 at home against the spread; MIA's road ATS record is also modest (45.1%, 23-28-1) — the weakest-signal leg on the board, included mainly for the real points cushion on a 10.5-point spread.
- Combined price: **+1301**

```json
SPREAD_PARLAY_3_TEAM
[
  {"player": "Las Vegas Raiders", "market_key": "spreads", "canonical_event_id": "82f1042cd9096ce2", "price": 1.926, "point": 4.5, "reason": "LV home ATS 54.9% (28-23-1) vs KC road ATS 44.0% (22-28-1) since 2020.", "evidence_check": []},
  {"player": "Philadelphia Eagles", "market_key": "spreads", "canonical_event_id": "0b88c15fb8b87a89", "price": 1.952, "point": 3.0, "reason": "PHI home ATS 53.1% (26-23-2) vs LAR road ATS 54.0% (27-23-2) — genuinely split signal, consistent with a projected toss-up.", "evidence_check": []},
  {"player": "Green Bay Packers", "market_key": "spreads", "canonical_event_id": "a223ecde7f6e4844", "price": 1.909, "point": -3.5, "reason": "TB home ATS 43.1% (22-29-1), the weakest home number on this slate, vs GB road ATS 44.2% (23-29-1).", "evidence_check": []}
]
```

```json
SPREAD_PARLAY_4_TEAM
[
  {"player": "Las Vegas Raiders", "market_key": "spreads", "canonical_event_id": "82f1042cd9096ce2", "price": 1.926, "point": 4.5, "reason": "LV home ATS 54.9% (28-23-1) vs KC road ATS 44.0% (22-28-1) since 2020.", "evidence_check": []},
  {"player": "Philadelphia Eagles", "market_key": "spreads", "canonical_event_id": "0b88c15fb8b87a89", "price": 1.952, "point": 3.0, "reason": "PHI home ATS 53.1% (26-23-2) vs LAR road ATS 54.0% (27-23-2) — genuinely split signal.", "evidence_check": []},
  {"player": "Green Bay Packers", "market_key": "spreads", "canonical_event_id": "a223ecde7f6e4844", "price": 1.909, "point": -3.5, "reason": "TB home ATS 43.1% (22-29-1) vs GB road ATS 44.2% (23-29-1).", "evidence_check": []},
  {"player": "Miami Dolphins", "market_key": "spreads", "canonical_event_id": "c2a6d9dbffca7b2e", "price": 1.952, "point": 10.5, "reason": "MIN home ATS 47.1% (24-27-0) vs MIA road ATS 45.1% (23-28-1) — weakest-signal leg, included for the real points cushion.", "evidence_check": []}
]
```