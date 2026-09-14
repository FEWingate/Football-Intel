# COEUS PROPS & PARLAY REPORT
**Week 1, 2026 — DEN @ KC (single-game slate)**

**Data coverage note:** All five real FanDuel stat families — Passing Yards, Rushing Yards, Receiving Yards, Receptions, Anytime TD — are LIVE for this slate's one game. No stale or unavailable families this week; every pick below uses live, current pricing.

**Slate note:** This is a one-game slate. Every pick in every section below comes from DEN @ KC (canonical_event_id `d5f0b2436d2da19e`) — there is no other game to draw from. That also means every multi-leg parlay in Section 3 is a same-game combination; each is flagged as such rather than presented as a real FanDuel same-game-parlay quote.

---

## 1. COEUS PROP BREAKDOWN

### DEN @ KC — 3 Favorites

- **Travis Kelce** (KC) — Receiving Yards, real line 42.5, Over, -113. This is the one automatic Threat designation on the board (Standard tier, Triple type): Kelce ranks 8th among qualifying TEs at 50.1 rec yds/gm, and Denver allows 59.7 rec yds/gm to tight ends (24th) — a real, statistically soft spot inside an otherwise elite Denver defense. Suggested alt: the 50+ rung at +130 is the cleaner ceiling play if you want the same read at better value.

- **Patrick Mahomes** (KC) — Passing Yards, real line 223.5, Over, -113. His own individual per-start rate is 256.2 yds/gm (5th among qualifying QBs) against a Denver pass defense that ranks just 11th in yards allowed (moderate, not elite) — real, player-specific evidence, not a team aggregate. Caveat: Kansas City's team-level passing splits show just 213.2 yds/gm (n=5) against top-tier defenses as a whole, which argues the other way — but that number is a team position-group aggregate that isn't confirmed as Mahomes' own production specifically, so it's weighed as a real complicating factor rather than the deciding one. Confidence: MEDIUM. Suggested alt: the 250+ rung at +162 is the value-side way to play the same read.

- **Kenneth Walker** (KC) — Anytime TD, +?[see below], -115. This isn't a line prop so there's no alt ladder to suggest, only the single real anytime price. Denver's run defense is elite against backs in almost every raw category (2nd in rush yards allowed, 2nd in yards allowed, 1st in receptions allowed) but allowed 6 RB receiving touchdowns on the season — tied for 30th, worst in the league. That specific soft spot, not a broad leak, is what this pick targets. Confidence: MEDIUM (real rank split, but a six-score sample).

### League-Wide Position Favorites (from this week's only game)

- **QB — Patrick Mahomes** (KC): Passing Yards, line 223.5, Over, -113. Same read as above — his individual 256.2 yds/gm rate (5th) against a moderate (11th-ranked) Denver pass defense is the best QB prop on the board this week.
- **RB — J.K. Dobbins** (DEN): Rushing Yards, real line 49.5, Over, -113. FanDuel's own market has resolved Section 4's real Dobbins/Harvey ambiguity in Dobbins' favor (his line is nearly 3x Harvey's 18.5), and his own 10-game log (a real, unflagged individual attribution) averages 77.2 rush yds/gm against a Kansas City run defense that allows 83.2 rush yds/gm to backs (8th, solid but not special). Suggested alt: the 60+ rung at +146.
- **WR — Rashee Rice** (KC): Receiving Yards, real line 51.5, Over, -113. His own season average (71.4 rec yds/gm, 85% snap share, clear WR1 role) sits nearly 20 yards above the posted line against a Denver WR defense that is stingy on touchdowns (1st, only 6 allowed all season) but only middling on total yardage allowed (13th, 130.8/gm). Suggested alt: the 60+ rung at +130.
- **TE — Travis Kelce** (KC): Receiving Yards, line 42.5, Over, -113. Same Threat-supported read as the per-game pick above — the single cleanest matchup edge on this slate.

```json
PROP_BREAKDOWN
{
  "per_game": [
    {"away": "DEN", "home": "KC", "picks": [
      {"player": "Travis Kelce", "market_key": "player_receiving_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885, "side": "over", "reason": "Standard/Triple Threat designation: Kelce ranks 8th among TEs at 50.1 rec yds/gm, Denver allows 59.7 rec yds/gm to TEs (24th), a real soft spot inside an elite overall defense."},
      {"player": "Patrick Mahomes", "market_key": "player_passing_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885, "side": "over", "reason": "Mahomes' own individual per-start rate is 256.2 yds/gm (5th among QBs) vs a Denver pass defense ranked just 11th in yards allowed; team-level splits argue lower but are not confirmed as his personal production."},
      {"player": "Kenneth Walker", "market_key": "player_anytime_td", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.87, "side": "over", "reason": "Denver's run defense is elite against backs in yardage (2nd) and receptions (1st) but allowed 6 RB receiving TDs on the season, tied for 30th worst in the league - a real, specific goal-line/passing-down leak."}
    ]}
  ],
  "per_position": {
    "QB": {"player": "Patrick Mahomes", "market_key": "player_passing_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885, "side": "over", "reason": "His individual 256.2 yds/gm rate (5th among QBs) against Denver's moderate (11th-ranked) pass defense is the strongest QB read on this slate."},
    "RB": {"player": "J.K. Dobbins", "market_key": "player_rushing_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885, "side": "over", "reason": "FanDuel's own line (49.5, nearly 3x Harvey's 18.5) resolves the roster ambiguity in Dobbins' favor, and his real 10-game log averages 77.2 rush yds/gm vs a KC run defense ranked just 8th against backs."},
    "WR": {"player": "Rashee Rice", "market_key": "player_receiving_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885, "side": "over", "reason": "Rice's season average of 71.4 rec yds/gm on an 85% snap share sits nearly 20 yards above the posted 51.5 line against a Denver defense that is stingy on WR touchdowns but only middling on total yardage."},
    "TE": {"player": "Travis Kelce", "market_key": "player_receiving_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885, "side": "over", "reason": "The lone automatic Threat designation on this slate - Kelce's own top-10 rank meets Denver's specific soft spot at tight end (24th allowed)."}
  }
}
```

---

## 2. FAVORITE OVERS AND UNDERS FOR THE WEEK

### Overs (ranked by conviction)

1. **Travis Kelce** (KC) — Receiving Yards Over 42.5, -113. HIGH conviction — the only real Threat designation on the slate.
2. **Patrick Mahomes** (KC) — Passing Yards Over 223.5, -113. MEDIUM conviction — strong individual rate (256.2, 5th) against a moderate defense, tempered by a conflicting team-level split.
3. **Rashee Rice** (KC) — Receiving Yards Over 51.5, -113. MEDIUM conviction — clear WR1 role, season average well clear of the line.
4. **Courtland Sutton** (DEN) — Receiving Yards Over 42.5, -113. MEDIUM conviction — his own season average of 59.8 rec yds/gm on an 85.5% snap share sits 17+ yards above the line, against a KC WR defense that's solid but not shutdown (9th, 124.6 rec yds/gm allowed).
5. **J.K. Dobbins** (DEN) — Rushing Yards Over 49.5, -113. MEDIUM conviction — real 10-game log average of 77.2, with FanDuel's own market resolving the backfield-share question in his favor.
6. **Kenneth Walker** (KC) — Anytime TD, -115. MEDIUM conviction — targets Denver's specific, real RB-receiving-touchdown leak (30th, worst in the league) inside an otherwise elite run defense.

### Unders (ranked by conviction)

1. **Xavier Worthy** (KC) — Receptions Under 3.5, -154. MEDIUM conviction — his own individual season average is 3.0 receptions/gm, below the posted line, in a WR2 role (76.7% snap share) behind Rice. Note: FanDuel's real alt ladder for Worthy's receptions (2, 3, 4, 5, 6, 7, 8) is priced Over-only, so there's no Under-side alternative to this 3.5 line.
2. **Pat Bryant** (DEN) — Receptions Under 2.5, -122. LOW conviction — his own season average (2.4/gm) sits just under the line in a clear WR2/depth role (65% snap share); the margin is thin and this is a low-conviction lean, not a strong edge. Same alt-ladder caveat applies: Bryant's real receptions alt ladder (2, 3, 4, 5, 6, 7) is Over-only priced.

```json
FAVORITE_OU
{
  "overs": [
    {"player": "Travis Kelce", "market_key": "player_receiving_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885, "side": "over", "reason": "Only automatic Threat designation on the slate - top-10 individual rank meeting a specific 24th-ranked TE soft spot."},
    {"player": "Patrick Mahomes", "market_key": "player_passing_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885, "side": "over", "reason": "Individual per-start rate of 256.2 yds/gm (5th) against a moderate 11th-ranked pass defense, tempered by a conflicting team-level split."},
    {"player": "Rashee Rice", "market_key": "player_receiving_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885, "side": "over", "reason": "Season average of 71.4 rec yds/gm on an 85% snap share sits well clear of the 51.5 line."},
    {"player": "Courtland Sutton", "market_key": "player_receiving_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885, "side": "over", "reason": "Season average of 59.8 rec yds/gm on an 85.5% snap share sits 17+ yards clear of the 42.5 line against a solid-not-shutdown KC WR defense."},
    {"player": "J.K. Dobbins", "market_key": "player_rushing_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885, "side": "over", "reason": "Real 10-game log average of 77.2 rush yds/gm, with FanDuel's own market crowning him the lead back over RJ Harvey."},
    {"player": "Kenneth Walker", "market_key": "player_anytime_td", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.87, "side": "over", "reason": "Targets Denver's real, specific RB-receiving-touchdown leak (30th, worst in the league) inside an otherwise elite run defense."}
  ],
  "unders": [
    {"player": "Xavier Worthy", "market_key": "player_receptions", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.649, "side": "under", "reason": "His own individual season average is 3.0 receptions/gm, below the posted 3.5 line, in a clear WR2 role behind Rice."},
    {"player": "Pat Bryant", "market_key": "player_receptions", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.82, "side": "under", "reason": "Season average of 2.4 receptions/gm sits just under the 2.5 line in a limited WR2/depth role; a thin, low-conviction edge."}
  ]
}
```

---

## 3. FIVE PARLAYS

**Same-game notice, applies to every parlay below:** every leg in every parlay comes from DEN @ KC — the only game on this slate. The combined prices shown are cross-game-style estimates built by multiplying each leg's independent price; they are NOT real FanDuel same-game-parlay (SGP) quotes, since legs from the same game are correlated rather than independent.

### 3-Team Parlay
- **Travis Kelce** (KC) Receiving Yards Over 42.5, -113 — the Threat-supported anchor leg.
- **Patrick Mahomes** (KC) Passing Yards Over 223.5, -113 — his individual rate (256.2, 5th) against a moderate Denver pass defense.
- **Kenneth Walker** (KC) Anytime TD, -115 — targets Denver's specific RB-receiving-TD leak.
- **Combined price: +564** (decimal 6.645). Thread: three independent reads that all point toward a productive Kansas City passing operation this specific week, even while the team as a whole struggles to finish drives.

```json
PARLAY_3_TEAM
[
  {"player": "Travis Kelce", "market_key": "player_receiving_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885, "side": "over", "reason": "Standard/Triple Threat designation vs Denver's 24th-ranked TE defense."},
  {"player": "Patrick Mahomes", "market_key": "player_passing_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885, "side": "over", "reason": "Individual 256.2 yds/gm rate (5th) vs a moderate 11th-ranked pass defense."},
  {"player": "Kenneth Walker", "market_key": "player_anytime_td", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.87, "side": "over", "reason": "Denver allowed 6 RB receiving TDs on the season, tied for 30th worst, a real specific leak."}
]
```

### 4-Team Parlay
- Same three legs above, plus:
- **Courtland Sutton** (DEN) Receiving Yards Over 42.5, -113 — season average 17+ yards clear of the line against KC's 9th-ranked WR defense.
- **Combined price: +1152** (decimal 12.525). Thread: adds Denver's own clearest receiving edge to the KC-passing-game stack, betting on both offenses moving the ball through the air.

```json
PARLAY_4_TEAM
[
  {"player": "Travis Kelce", "market_key": "player_receiving_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885, "side": "over", "reason": "Standard/Triple Threat designation vs Denver's 24th-ranked TE defense."},
  {"player": "Patrick Mahomes", "market_key": "player_passing_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885, "side": "over", "reason": "Individual 256.2 yds/gm rate (5th) vs a moderate 11th-ranked pass defense."},
  {"player": "Kenneth Walker", "market_key": "player_anytime_td", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.87, "side": "over", "reason": "Denver allowed 6 RB receiving TDs on the season, tied for 30th worst, a real specific leak."},
  {"player": "Courtland Sutton", "market_key": "player_receiving_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885, "side": "over", "reason": "Season average of 59.8 rec yds/gm sits 17+ yards clear of the 42.5 line vs KC's 9th-ranked WR defense."}
]
```

### 5-Team Parlay
- Same four legs above, plus:
- **Rashee Rice** (KC) Receiving Yards Over 51.5, -113 — clear WR1 role, season average nearly 20 yards clear of the line.
- **Combined price: +2261** (decimal 23.610). Thread: now both games' clear WR1s are stacked alongside the two QB/TE reads — a bet that this game is a genuine shootout rather than the Week 17-style defensive rout from these two teams' last meeting.

```json
PARLAY_5_TEAM
[
  {"player": "Travis Kelce", "market_key": "player_receiving_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885, "side": "over", "reason": "Standard/Triple Threat designation vs Denver's 24th-ranked TE defense."},
  {"player": "Patrick Mahomes", "market_key": "player_passing_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885, "side": "over", "reason": "Individual 256.2 yds/gm rate (5th) vs a moderate 11th-ranked pass defense."},
  {"player": "Kenneth Walker", "market_key": "player_anytime_td", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.87, "side": "over", "reason": "Denver allowed 6 RB receiving TDs on the season, tied for 30th worst, a real specific leak."},
  {"player": "Courtland Sutton", "market_key": "player_receiving_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885, "side": "over", "reason": "Season average of 59.8 rec yds/gm sits 17+ yards clear of the 42.5 line vs KC's 9th-ranked WR defense."},
  {"player": "Rashee Rice", "market_key": "player_receiving_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885, "side": "over", "reason": "Season average of 71.4 rec yds/gm on an 85% snap share sits well clear of the 51.5 line."}
]
```

### 6-Team Parlay
- Same five legs above, plus:
- **J.K. Dobbins** (DEN) Rushing Yards Over 49.5, -113 — real 10-game log average of 77.2, market-confirmed lead back.
- **Combined price: +4350** (decimal 44.504). Thread: now a full-game "everything hits" ticket — both team's top WR, the KC QB and TE, KC's TD-leak target, and Denver's lead back all going over, betting on total game volume rather than any one storyline.

```json
PARLAY_6_TEAM
[
  {"player": "Travis Kelce", "market_key": "player_receiving_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885, "side": "over", "reason": "Standard/Triple Threat designation vs Denver's 24th-ranked TE defense."},
  {"player": "Patrick Mahomes", "market_key": "player_passing_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885, "side": "over", "reason": "Individual 256.2 yds/gm rate (5th) vs a moderate 11th-ranked pass defense."},
  {"player": "Kenneth Walker", "market_key": "player_anytime_td", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.87, "side": "over", "reason": "Denver allowed 6 RB receiving TDs on the season, tied for 30th worst, a real specific leak."},
  {"player": "Courtland Sutton", "market_key": "player_receiving_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885, "side": "over", "reason": "Season average of 59.8 rec yds/gm sits 17+ yards clear of the 42.5 line vs KC's 9th-ranked WR defense."},
  {"player": "Rashee Rice", "market_key": "player_receiving_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885, "side": "over", "reason": "Season average of 71.4 rec yds/gm on an 85% snap share sits well clear of the 51.5 line."},
  {"player": "J.K. Dobbins", "market_key": "player_rushing_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885, "side": "over", "reason": "Real 10-game log average of 77.2 rush yds/gm, with FanDuel's own market crowning him the lead back over RJ Harvey."}
]
```

### 7-Team Parlay
- Same six legs above, plus:
- **Xavier Worthy** (KC) Receptions Under 3.5, -154 — his own individual season average (3.0/gm) sits below the line.
- **Combined price: +7239** (decimal 73.387). Thread: adds the one real Under on the board as a hedge against Rice/Kelce eating a disproportionate share of Kansas City's targets — the same passing-volume thesis as the 6-team, with a target-distribution check built in.

```json
PARLAY_7_TEAM
[
  {"player": "Travis Kelce", "market_key": "player_receiving_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885, "side": "over", "reason": "Standard/Triple Threat designation vs Denver's 24th-ranked TE defense."},
  {"player": "Patrick Mahomes", "market_key": "player_passing_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885, "side": "over", "reason": "Individual 256.2 yds/gm rate (5th) vs a moderate 11th-ranked pass defense."},
  {"player": "Kenneth Walker", "market_key": "player_anytime_td", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.87, "side": "over", "reason": "Denver allowed 6 RB receiving TDs on the season, tied for 30th worst, a real specific leak."},
  {"player": "Courtland Sutton", "market_key": "player_receiving_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885, "side": "over", "reason": "Season average of 59.8 rec yds/gm sits 17+ yards clear of the 42.5 line vs KC's 9th-ranked WR defense."},
  {"player": "Rashee Rice", "market_key": "player_receiving_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885, "side": "over", "reason": "Season average of 71.4 rec yds/gm on an 85% snap share sits well clear of the 51.5 line."},
  {"player": "J.K. Dobbins", "market_key": "player_rushing_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885, "side": "over", "reason": "Real 10-game log average of 77.2 rush yds/gm, with FanDuel's own market crowning him the lead back over RJ Harvey."},
  {"player": "Xavier Worthy", "market_key": "player_receptions", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.649, "side": "under", "reason": "His own individual season average is 3.0 receptions/gm, below the posted 3.5 line, in a clear WR2 role behind Rice."}
]
```