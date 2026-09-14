# WEEK 1 PROPS & PARLAY REPORT
### DEN @ KC — Full Slate (1 Game)

**Real Data Coverage check (read first):** Passing Yards, Rushing Yards, Receiving Yards, Receptions, and Anytime TD are all **LIVE** for this slate (1 real game, current data, 0 stale/carried). Every pick below uses live, current FanDuel pricing — no stale or unavailable stat families to flag this week.

**Slate-size note:** This is a single-game slate (DEN @ KC only). Every pick and every parlay leg below necessarily comes from this one game — see the correlation disclosure repeated in Section 3 for what that means for parlay pricing.

---

## 1. COEUS PROP BREAKDOWN

### DEN @ KC — Top 3 Favorites

- **Travis Kelce** (KC, TE) — Receiving Yards, line **42.5**, **Over**, **-113**. The one real Threat designation in this game (Standard/Triple): Kelce ranks 8th among TEs at 50.1 rec yds/gm, and Denver allows 59.7 rec yds/gm to TEs (ranked 24th) — a real soft spot inside an otherwise elite Denver defense. Alt-line note: the ladder is Over-only; the 50+ alt (+126) is the plus-money version of the same read, the 30+ alt (-270) is the safe-floor version.

- **Patrick Mahomes** (KC, QB) — Passing Yards, line **223.5**, **Under**, **-113**. KC's own contextual splits show pass yards compress to 213.2/gm (n=5) against top-tier defenses, and Denver ranks 3rd in points allowed / 4th in total yards allowed — a real top-tier unit by those metrics; Denver already held Mahomes to 66 pass yards in their real Week 17 meeting. Alt-line note: FanDuel's alt ladder for this market is Over-only (150 through 350) — there's no separate Under alt, so the 223.5 main line is the cleanest real vehicle for this side.

- **J.K. Dobbins** (DEN, RB) — Rushing Yards, line **49.5**, **Over**, **-113**. Dobbins' real 2025 game log shows a 77.2 rush yds/gm average across 10 qualifying games, well clear of this line, against a KC run defense that ranks only 9th (105.5 rush yds/gm allowed); FanDuel's own market (Dobbins 49.5 vs. RJ Harvey 18.5) resolves the backfield-role uncertainty flagged in the Game Breakdown in Dobbins' favor. Alt-line note: the 40+ alt (-220) is the safer version of this same thesis.

### League-Wide Position Favorites

- **QB — Patrick Mahomes** (KC) — Passing Yards Under 223.5, **-113**. Same reasoning as above; this is the single best QB read on the slate given it's a one-game board.
- **RB — J.K. Dobbins** (DEN) — Rushing Yards Over 49.5, **-113**. Same reasoning as above.
- **WR — Courtland Sutton** (DEN) — Receiving Yards, line **42.5**, **Over**, **-113**. Sutton's own season average is 59.8 rec yds/gm — well above this posted line — even accounting for a moderately tough KC WR defense (124.6 rec yds/gm allowed, ranked 9th). Alt-line note: the 30+ alt (-250) is the high-floor version of this same read.
- **TE — Travis Kelce** (KC) — Receiving Yards Over 42.5, **-113**. Same reasoning as the game-level pick above — the strongest single piece of evidence on the board.

```json
PROP_BREAKDOWN
{
  "per_game": [
    {"away": "DEN", "home": "KC", "picks": [
      {"player": "Travis Kelce", "market_key": "player_receiving_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885},
      {"player": "Patrick Mahomes", "market_key": "player_passing_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885},
      {"player": "J.K. Dobbins", "market_key": "player_rushing_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885}
    ]}
  ],
  "per_position": {
    "QB": {"player": "Patrick Mahomes", "market_key": "player_passing_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885},
    "RB": {"player": "J.K. Dobbins", "market_key": "player_rushing_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885},
    "WR": {"player": "Courtland Sutton", "market_key": "player_receiving_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885},
    "TE": {"player": "Travis Kelce", "market_key": "player_receiving_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885}
  }
}
```

---

## 2. FAVORITE OVERS AND UNDERS FOR THE WEEK

### Overs (ranked by conviction)

1. **Travis Kelce** (KC) — Receiving Yards Over 42.5, **-113**. Confidence: **HIGH** — real Threat convergence, the cleanest single edge on the slate.
2. **Courtland Sutton** (DEN) — Receiving Yards Over 42.5, **-113**. Confidence: **MEDIUM** — season average sits ~17 yards above the line, though Jaylen Waddle's presence on Denver's roster (unconfirmed 2026 role) is a real complicating factor.
3. **J.K. Dobbins** (DEN) — Rushing Yards Over 49.5, **-113**. Confidence: **MEDIUM** — strong game-log support, tempered by KC's real run defense being merely average-to-solid (not a soft matchup).
4. **Rashee Rice** (KC) — Receiving Yards Over 55.5, **-113**. Confidence: **MEDIUM** — his 71.4 rec yds/gm season average, even scaled down for Denver's top-tier defensive compression (~65 projected), still clears this line.
5. **Kenneth Walker** — Anytime TD, **-120** (single "Yes" market, no alt ladder). Confidence: **LOW** — grounded in real Hidden Intelligence (Finding 2): Denver's defense is elite against RBs in nearly every category except RB receiving touchdowns allowed (6 on the season, ranked 30th, tied-worst) — a real, specific leak for whichever KC back handles passing-down work.

### Unders (ranked by conviction)

1. **Patrick Mahomes** (KC) — Passing Yards Under 223.5, **-113**. Confidence: **MEDIUM** — contextual splits, blitz-efficiency decline, and the real Week 17 head-to-head all point the same direction.
2. **Kenneth Walker** (KC) — Rushing Yards Under 61.5, **-113**. Confidence: **LOW** — Denver's run defense is elite in aggregate (71.8 rush yds/gm allowed, ranked 2nd), but that number is shared across the whole RB position, and real backfield-role ambiguity (Walker vs. Pacheco) limits how far this projection can be trusted.

```json
FAVORITE_OU
{
  "overs": [
    {"player": "Travis Kelce", "market_key": "player_receiving_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885},
    {"player": "Courtland Sutton", "market_key": "player_receiving_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885},
    {"player": "J.K. Dobbins", "market_key": "player_rushing_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885},
    {"player": "Rashee Rice", "market_key": "player_receiving_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885},
    {"player": "Kenneth Walker", "market_key": "player_anytime_td", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.833}
  ],
  "unders": [
    {"player": "Patrick Mahomes", "market_key": "player_passing_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885},
    {"player": "Kenneth Walker", "market_key": "player_rushing_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885}
  ]
}
```

---

## 3. FIVE PARLAYS

**Standing disclosure for every parlay below:** this is a one-game slate, so every leg in every parlay shares the same canonical event (DEN @ KC). The combined prices shown are naive cross-multiplications of each leg's individual price, **not** real FanDuel same-game-parlay (SGP) quotes — legs from the same game are correlated, and FanDuel's actual SGP pricing for this combination would differ from simple multiplication.

### 3-Team Parlay
- Travis Kelce (KC) — Receiving Yards Over 42.5, -113
- Patrick Mahomes (KC) — Passing Yards Under 223.5, -113
- J.K. Dobbins (DEN) — Rushing Yards Over 49.5, -113
- **Same-game note:** all three legs share canonical event `d5f0b2436d2da19e` — cross-game-style estimate, not a real SGP quote.
- **Combined price: +570** (validator-checked).
- **Why this combination:** these three bets are the report's central thesis compressed into three legs — Denver's defense suppresses Mahomes, Denver's offense runs through Dobbins, and Kelce is the one confirmed statistical crack in Denver's otherwise elite unit.

```json
PARLAY_3_TEAM
[
  {"player": "Travis Kelce", "market_key": "player_receiving_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885},
  {"player": "Patrick Mahomes", "market_key": "player_passing_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885},
  {"player": "J.K. Dobbins", "market_key": "player_rushing_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885}
]
```

### 4-Team Parlay
- Travis Kelce (KC) — Receiving Yards Over 42.5, -113
- Patrick Mahomes (KC) — Passing Yards Under 223.5, -113
- J.K. Dobbins (DEN) — Rushing Yards Over 49.5, -113
- Courtland Sutton (DEN) — Receiving Yards Over 42.5, -113
- **Same-game note:** all four legs share canonical event `d5f0b2436d2da19e` — cross-game-style estimate, not a real SGP quote.
- **Combined price: +1163** (validator-checked).
- **Why this combination:** extends the 3-team thesis to Denver's own passing game — Sutton's real season average sitting well above his posted line adds a fourth independent column to the same Denver-controls-the-game read.

```json
PARLAY_4_TEAM
[
  {"player": "Travis Kelce", "market_key": "player_receiving_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885},
  {"player": "Patrick Mahomes", "market_key": "player_passing_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885},
  {"player": "J.K. Dobbins", "market_key": "player_rushing_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885},
  {"player": "Courtland Sutton", "market_key": "player_receiving_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885}
]
```

### 5-Team Parlay
- Travis Kelce (KC) — Receiving Yards Over 42.5, -113
- Patrick Mahomes (KC) — Passing Yards Under 223.5, -113
- J.K. Dobbins (DEN) — Rushing Yards Over 49.5, -113
- Courtland Sutton (DEN) — Receiving Yards Over 42.5, -113
- Rashee Rice (KC) — Receiving Yards Over 55.5, -113
- **Same-game note:** all five legs share canonical event `d5f0b2436d2da19e` — cross-game-style estimate, not a real SGP quote.
- **Combined price: +2280** (validator-checked).
- **Why this combination:** adds the counter-read from KC's own contextual splits — Kansas City's passing offense loses touchdowns against good defenses far more than it loses yardage, so Rice's volume holding up is compatible with Mahomes going Under on yards.

```json
PARLAY_5_TEAM
[
  {"player": "Travis Kelce", "market_key": "player_receiving_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885},
  {"player": "Patrick Mahomes", "market_key": "player_passing_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885},
  {"player": "J.K. Dobbins", "market_key": "player_rushing_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885},
  {"player": "Courtland Sutton", "market_key": "player_receiving_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885},
  {"player": "Rashee Rice", "market_key": "player_receiving_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885}
]
```

### 6-Team Parlay
- Travis Kelce (KC) — Receiving Yards Over 42.5, -113
- Patrick Mahomes (KC) — Passing Yards Under 223.5, -113
- J.K. Dobbins (DEN) — Rushing Yards Over 49.5, -113
- Courtland Sutton (DEN) — Receiving Yards Over 42.5, -113
- Rashee Rice (KC) — Receiving Yards Over 55.5, -113
- Kenneth Walker (KC) — Anytime TD, -120
- **Same-game note:** all six legs share canonical event `d5f0b2436d2da19e` — cross-game-style estimate, not a real SGP quote.
- **Combined price: +4262** (validator-checked).
- **Why this combination:** layers in the report's real Hidden Intelligence finding (Denver's specific weakness to RB receiving touchdowns) as the highest-variance piece of an otherwise evidence-dense parlay.

```json
PARLAY_6_TEAM
[
  {"player": "Travis Kelce", "market_key": "player_receiving_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885},
  {"player": "Patrick Mahomes", "market_key": "player_passing_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885},
  {"player": "J.K. Dobbins", "market_key": "player_rushing_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885},
  {"player": "Courtland Sutton", "market_key": "player_receiving_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885},
  {"player": "Rashee Rice", "market_key": "player_receiving_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885},
  {"player": "Kenneth Walker", "market_key": "player_anytime_td", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.833}
]
```

### 7-Team Parlay
- Travis Kelce (KC) — Receiving Yards Over 42.5, -113
- Patrick Mahomes (KC) — Passing Yards Under 223.5, -113
- J.K. Dobbins (DEN) — Rushing Yards Over 49.5, -113
- Courtland Sutton (DEN) — Receiving Yards Over 42.5, -113
- Rashee Rice (KC) — Receiving Yards Over 55.5, -113
- Kenneth Walker (KC) — Anytime TD, -120
- Xavier Worthy (KC) — Receiving Yards Over 35.5, -113
- **Same-game note:** all seven legs share canonical event `d5f0b2436d2da19e` — cross-game-style estimate, not a real SGP quote.
- **Combined price: +8123** (validator-checked).
- **Why this combination:** the full-slate maximalist version — every real, evidence-backed lean from this report stacked together, closing with Worthy to extend the same KC-passing-volume-survives read down to the WR2 spot.

```json
PARLAY_7_TEAM
[
  {"player": "Travis Kelce", "market_key": "player_receiving_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885},
  {"player": "Patrick Mahomes", "market_key": "player_passing_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885},
  {"player": "J.K. Dobbins", "market_key": "player_rushing_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885},
  {"player": "Courtland Sutton", "market_key": "player_receiving_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885},
  {"player": "Rashee Rice", "market_key": "player_receiving_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885},
  {"player": "Kenneth Walker", "market_key": "player_anytime_td", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.833},
  {"player": "Xavier Worthy", "market_key": "player_receiving_yards", "canonical_event_id": "d5f0b2436d2da19e", "price": 1.885}
]
```