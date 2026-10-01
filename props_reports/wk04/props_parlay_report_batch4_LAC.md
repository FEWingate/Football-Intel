# COEUS PROPS & PARLAY REPORT — Week 4, 2026
### LAC @ SEA · DEN @ SF · DET @ CAR · ATL @ NO

---

## REAL DATA COVERAGE NOTE (read before anything else)

- Passing Yards, Anytime TD: **LIVE** for all 4 games — used normally below.
- Rushing Yards, Receiving Yards, Receptions: the feed-level coverage summary reports these as "current" league-wide, but **for all four specific games on this slate, the actual market data returned is empty** — no RB/WR/TE yardage or reception lines exist in the real data provided for LAC@SEA, DEN@SF, DET@CAR, or ATL@NO. Per the No-Fabrication rule, this report does **not** invent lines for those three markets anywhere below. Every pick in this report is built only from the two markets that actually returned real data this week: **passing yards** (2 QBs/game) and **anytime TD** (full roster/game).
- This also means Section 8 (spread parlays) is capped at two real parlay sizes — see that section for why.

---

## 1. COEUS PROP BREAKDOWN

### LAC @ SEA
- **Jaxon Smith-Njigba (SEA) — Anytime TD, Over, -115** — 1st in the league in rec yards (135.0/gm) and receptions (9.0/gm), 37.9% target share, 50% RZ target share, 6 TD through 3 games; LAC's WR defense allows 159.3 rec yds/gm, ranked 22nd. Missed a formal Standard Threat by one spot (needed rank 23+), but the underlying gap is real.
- **Justin Herbert (LAC) — Under 199.5 passing yards, -114** — Herbert's QB group ranks 19th in pass yards (209.0 ypg) against Seattle's defense, the league's best at 152.0 pass yds/gm allowed (1st) — his toughest statistical test of the season. FanDuel's alt ladder here (150–325) is Over-only; no Under-side alt exists.
- **Omarion Hampton (LAC) — Anytime TD, Over, +105** — 55.6% RZ carry share, 2 rush TDs (12th among RBs); Seattle allows RBs just 65.3 rush yds/gm (6th) — a real step up in competition, but the RZ role alone sustains TD equity.

### DEN @ SF
- **Christian McCaffrey (SF) — Anytime TD, Over, -195** — 61.5% RZ carry share, 3 rush TD (8th); Denver's run defense ranks 31st vs RBs (129.7 rush yds/gm allowed) and 29th vs RB receiving — an Elite Threat convergence.
- **Brock Purdy (SF) — Over 229.5 passing yards, -114** — Purdy's QB group ranks 8th in pass yards (263.0 ypg) and 1st in TDs vs Denver's 24th-ranked pass defense — a confirmed Standard Threat. His lone bottom-tier-defense game this season produced 297 yds/4 TD. The 225+ alt (-132) is a tighter number on the same thesis.
- **George Kittle (SF) — Anytime TD, Over, +160** — 5th in rec yards (58.0/gm) vs Denver's 25th-ranked TE defense; his two bottom-tier-defense games this season average 81.0 ypg — directly Denver's caliber.

### DET @ CAR
- **Jahmyr Gibbs (DET) — Anytime TD, Over, -340** — 4th in rush yards (102.3 ypg), 90% RZ carry share; Carolina allows RBs 144.7 rush yds/gm (32nd, worst in this report) — an Elite Threat, the cleanest convergence in this week's evidence.
- **Bryce Young (CAR) — Over 246.5 passing yards, -114** — Young's QB group ranks 1st in pass yards (313.0 ypg) vs Detroit's 32nd-ranked pass defense (326.3 yds/gm allowed) — a Nuclear Threat, the strongest convergence anywhere this week. The 250+ alt (-106) is the tighter equivalent.
- **Darren Waller (CAR) — Anytime TD, Over, +260** — 2-for-2 on RZ targets this season; Detroit's TE defense is the single worst in the league (32nd in yards, catches, and TDs allowed to the position).

### ATL @ NO
- **Bijan Robinson (ATL) — Anytime TD, Over, -220** — 2nd in rush yards (116.3 ypg); New Orleans allows RBs 115.7 rush yds/gm (29th); his season-high game (194 yds) came against a bottom-tier run defense — exactly NO's bucket.
- **Chris Olave (NO) — Anytime TD, Over, +115** — 1st in receptions (9.0/gm), 2nd in rec yards (125.0/gm); Atlanta's WR defense is the worst in the league (32nd in yards allowed, 30th in catches allowed) — a Nuclear Threat.
- **Tyler Shough (NO) — Over 254.5 passing yards, -114** — 2nd in the league in pass yards (305.7 ypg); his Quadruple Threat vs Atlanta's 27th-ranked pass D is real, though his Week-1 410-yard outlier inflates the average — his two non-outlier games still average 253.5 ypg, right at this line. The 250 alt (-130) is a cleaner number.

### League-Wide Favorites by Position
- **QB: Bryce Young Over 246.5 (-114)** — Nuclear Threat, the strongest QB convergence on the slate.
- **RB: Jahmyr Gibbs Anytime TD (-340)** — cleanest, least-qualified Threat in this week's evidence.
- **WR: Chris Olave Anytime TD (+115)** — Nuclear tier, Quadruple-rated.
- **TE: George Kittle Anytime TD (+160)** — Standard tier, confirmed Threat Engine designation (unlike Waller, which is evidence-based but not formally flagged).

```json
PROP_BREAKDOWN
{
  "per_game": [
    {"away": "LAC", "home": "SEA", "picks": [
      {"player": "Jaxon Smith-Njigba", "market_key": "player_anytime_td", "canonical_event_id": "53d9d3807e4d3e66", "price": 1.87, "side": "over", "line": null, "reason": "1st in rec yards (135.0/gm) and receptions, 50% RZ target share, 6 TD; LAC allows WRs 159.3 rec yds/gm (22nd).", "evidence_check": [{"type":"current_opponent","team":"LAC","pos":"WR","stat":"rec_yds","role":"def","claimed_rank":22}]},
      {"player": "Justin Herbert", "market_key": "player_passing_yards", "canonical_event_id": "53d9d3807e4d3e66", "price": 1.877, "side": "under", "line": 199.5, "reason": "LAC QB group ranks 19th in pass yards; Seattle's pass D ranks 1st allowing 152.0 ypg, Herbert's toughest test of the season.", "evidence_check": [{"type":"current_opponent","team":"SEA","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":1},{"type":"current_opponent","team":"LAC","pos":"QB","stat":"pass_ypg","role":"off","claimed_rank":19}]},
      {"player": "Omarion Hampton", "market_key": "player_anytime_td", "canonical_event_id": "53d9d3807e4d3e66", "price": 2.05, "side": "over", "line": null, "reason": "55.6% RZ carry share, 2 rush TD (12th); Seattle allows RBs just 65.3 rush yds/gm (6th), a tougher test but RZ role holds.", "evidence_check": [{"type":"current_opponent","team":"SEA","pos":"RB","stat":"rush_yds","role":"def","claimed_rank":6}]}
    ]},
    {"away": "DEN", "home": "SF", "picks": [
      {"player": "Christian McCaffrey", "market_key": "player_anytime_td", "canonical_event_id": "d5a0d1b78d351969", "price": 1.513, "side": "over", "line": null, "reason": "61.5% RZ carry share, 3 rush TD (8th); Denver allows RBs 129.7 rush yds/gm (31st) and ranks 29th vs RB receiving.", "evidence_check": [{"type":"current_opponent","team":"DEN","pos":"RB","stat":"rush_yds","role":"def","claimed_rank":31},{"type":"current_opponent","team":"SF","pos":"RB","stat":"rush_td","role":"off","claimed_rank":8}]},
      {"player": "Brock Purdy", "market_key": "player_passing_yards", "canonical_event_id": "d5a0d1b78d351969", "price": 1.877, "side": "over", "line": 229.5, "reason": "SF QB group ranks 8th in pass yards vs Denver's 24th-ranked pass D; his lone bottom-tier matchup produced 297 yds/4 TD.", "evidence_check": [{"type":"current_opponent","team":"DEN","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":24},{"type":"current_opponent","team":"SF","pos":"QB","stat":"pass_yds","role":"off","claimed_rank":8}]},
      {"player": "George Kittle", "market_key": "player_anytime_td", "canonical_event_id": "d5a0d1b78d351969", "price": 2.6, "side": "over", "line": null, "reason": "5th in rec yards (58.0/gm) vs Denver's 25th-ranked TE D; his two bottom-tier games this season average 81.0 ypg.", "evidence_check": [{"type":"current_opponent","team":"DEN","pos":"TE","stat":"rec_yds","role":"def","claimed_rank":25}]}
    ]},
    {"away": "DET", "home": "CAR", "picks": [
      {"player": "Jahmyr Gibbs", "market_key": "player_anytime_td", "canonical_event_id": "8f044a7004d58a5c", "price": 1.294, "side": "over", "line": null, "reason": "4th in rush yards (102.3 ypg), 90% RZ carry share; Carolina allows RBs 144.7 rush yds/gm (32nd, worst specific matchup in this report).", "evidence_check": [{"type":"current_opponent","team":"CAR","pos":"RB","stat":"rush_yds","role":"def","claimed_rank":32},{"type":"current_opponent","team":"DET","pos":"RB","stat":"rush_yds","role":"off","claimed_rank":4}]},
      {"player": "Bryce Young", "market_key": "player_passing_yards", "canonical_event_id": "8f044a7004d58a5c", "price": 1.877, "side": "over", "line": 246.5, "reason": "CAR QB group ranks 1st in pass yards vs Detroit's 32nd-ranked pass D, the strongest Nuclear convergence this week.", "evidence_check": [{"type":"current_opponent","team":"DET","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":32},{"type":"current_opponent","team":"CAR","pos":"QB","stat":"pass_ypg","role":"off","claimed_rank":1}]},
      {"player": "Darren Waller", "market_key": "player_anytime_td", "canonical_event_id": "8f044a7004d58a5c", "price": 3.6, "side": "over", "line": null, "reason": "2-for-2 on RZ targets this season; Detroit's TE D is worst in the league (32nd in yards, catches, TDs allowed).", "evidence_check": [{"type":"current_opponent","team":"DET","pos":"TE","stat":"rec_yds","role":"def","claimed_rank":32}]}
    ]},
    {"away": "ATL", "home": "NO", "picks": [
      {"player": "Bijan Robinson", "market_key": "player_anytime_td", "canonical_event_id": "ab7bde95c9d5a8fc", "price": 1.455, "side": "over", "line": null, "reason": "2nd in rush yards (116.3 ypg); NO allows RBs 115.7 rush yds/gm (29th); his season-high (194 yds) came vs a bottom-tier run D.", "evidence_check": [{"type":"current_opponent","team":"NO","pos":"RB","stat":"rush_yds","role":"def","claimed_rank":29},{"type":"current_opponent","team":"ATL","pos":"RB","stat":"rush_yds","role":"off","claimed_rank":2}]},
      {"player": "Chris Olave", "market_key": "player_anytime_td", "canonical_event_id": "ab7bde95c9d5a8fc", "price": 2.15, "side": "over", "line": null, "reason": "1st in receptions, 2nd in rec yards; Atlanta's WR D is worst in the league (32nd in yards allowed, 30th in catches allowed).", "evidence_check": [{"type":"current_opponent","team":"ATL","pos":"WR","stat":"rec_yds","role":"def","claimed_rank":32}]},
      {"player": "Tyler Shough", "market_key": "player_passing_yards", "canonical_event_id": "ab7bde95c9d5a8fc", "price": 1.877, "side": "over", "line": 254.5, "reason": "NO QB group ranks 2nd in pass yards vs Atlanta's 27th-ranked pass D; non-outlier games still average 253.5 ypg.", "evidence_check": [{"type":"current_opponent","team":"ATL","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":27},{"type":"current_opponent","team":"NO","pos":"QB","stat":"pass_yds","role":"off","claimed_rank":2}]}
    ]}
  ],
  "per_position": {
    "QB": {"player": "Bryce Young", "market_key": "player_passing_yards", "canonical_event_id": "8f044a7004d58a5c", "price": 1.877, "side": "over", "line": 246.5, "reason": "Nuclear Threat — 1st-ranked passer vs the single worst pass D in this report (32nd).", "evidence_check": [{"type":"current_opponent","team":"DET","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":32},{"type":"current_opponent","team":"CAR","pos":"QB","stat":"pass_ypg","role":"off","claimed_rank":1}]},
    "RB": {"player": "Jahmyr Gibbs", "market_key": "player_anytime_td", "canonical_event_id": "8f044a7004d58a5c", "price": 1.294, "side": "over", "line": null, "reason": "Elite Threat, cleanest convergence of the week — 4th-ranked rusher vs Carolina's 32nd-ranked run D vs RBs.", "evidence_check": [{"type":"current_opponent","team":"CAR","pos":"RB","stat":"rush_yds","role":"def","claimed_rank":32}]},
    "WR": {"player": "Chris Olave", "market_key": "player_anytime_td", "canonical_event_id": "ab7bde95c9d5a8fc", "price": 2.15, "side": "over", "line": null, "reason": "Nuclear tier, Quadruple-rated — 1st in receptions vs Atlanta's worst-in-league WR D.", "evidence_check": [{"type":"current_opponent","team":"ATL","pos":"WR","stat":"rec_yds","role":"def","claimed_rank":32}]},
    "TE": {"player": "George Kittle", "market_key": "player_anytime_td", "canonical_event_id": "d5a0d1b78d351969", "price": 2.6, "side": "over", "line": null, "reason": "Confirmed Standard Threat vs Denver's 25th-ranked TE D, with a matching bottom-tier track record.", "evidence_check": [{"type":"current_opponent","team":"DEN","pos":"TE","stat":"rec_yds","role":"def","claimed_rank":25}]}
  }
}
```

---

## 2. FAVORITE OVERS AND UNDERS FOR THE WEEK

**Overs (ranked):**
1. **Bryce Young Over 246.5 (-114)** — Nuclear Threat (HIGH).
2. **Jahmyr Gibbs Anytime TD (-340)** — Elite Threat, cleanest in report (HIGH).
3. **Chris Olave Anytime TD (+115)** — Nuclear/Quadruple (HIGH).
4. **Bijan Robinson Anytime TD (-220)** — Elite Threat, bottom-tier run D (HIGH).
5. **Christian McCaffrey Anytime TD (-195)** — Elite Threat, league's worst specific run-D match (HIGH).
6. **Brock Purdy Over 229.5 (-114)** — Standard Threat (MEDIUM-HIGH).
7. **Tyler Shough Over 254.5 (-114)** — Quadruple Threat, tempered by Week-1 outlier (MEDIUM).

**Unders (ranked):**
1. **Justin Herbert Under 199.5 (-114)** — Seattle's #1-ranked pass D, zero top-tier sample this year (MEDIUM-HIGH).
2. **Jared Goff Under 260.5 (-114)** — Carolina's 5th-ranked pass D (3rd vs WRs); real but his lone prior top-tier game actually exceeded his season pace, so this is mixed evidence (MEDIUM).

```json
FAVORITE_OU
{
  "overs": [
    {"player": "Bryce Young", "market_key": "player_passing_yards", "canonical_event_id": "8f044a7004d58a5c", "price": 1.877, "side": "over", "line": 246.5, "reason": "Nuclear Threat — 1st-ranked passer vs Detroit's 32nd-ranked pass D.", "evidence_check": [{"type":"current_opponent","team":"DET","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":32}]},
    {"player": "Jahmyr Gibbs", "market_key": "player_anytime_td", "canonical_event_id": "8f044a7004d58a5c", "price": 1.294, "side": "over", "line": null, "reason": "Elite Threat, cleanest convergence of the week vs Carolina's 32nd-ranked run D vs RBs.", "evidence_check": [{"type":"current_opponent","team":"CAR","pos":"RB","stat":"rush_yds","role":"def","claimed_rank":32}]},
    {"player": "Chris Olave", "market_key": "player_anytime_td", "canonical_event_id": "ab7bde95c9d5a8fc", "price": 2.15, "side": "over", "line": null, "reason": "Nuclear/Quadruple Threat vs Atlanta's worst-in-league WR defense.", "evidence_check": [{"type":"current_opponent","team":"ATL","pos":"WR","stat":"rec_yds","role":"def","claimed_rank":32}]},
    {"player": "Bijan Robinson", "market_key": "player_anytime_td", "canonical_event_id": "ab7bde95c9d5a8fc", "price": 1.455, "side": "over", "line": null, "reason": "Elite Threat vs New Orleans' 29th-ranked run D vs RBs.", "evidence_check": [{"type":"current_opponent","team":"NO","pos":"RB","stat":"rush_yds","role":"def","claimed_rank":29}]},
    {"player": "Christian McCaffrey", "market_key": "player_anytime_td", "canonical_event_id": "d5a0d1b78d351969", "price": 1.513, "side": "over", "line": null, "reason": "Elite Threat vs Denver's 31st-ranked run D vs RBs, the most generous RB matchup in this report.", "evidence_check": [{"type":"current_opponent","team":"DEN","pos":"RB","stat":"rush_yds","role":"def","claimed_rank":31}]},
    {"player": "Brock Purdy", "market_key": "player_passing_yards", "canonical_event_id": "d5a0d1b78d351969", "price": 1.877, "side": "over", "line": 229.5, "reason": "Standard Threat vs Denver's 24th-ranked pass D.", "evidence_check": [{"type":"current_opponent","team":"DEN","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":24}]},
    {"player": "Tyler Shough", "market_key": "player_passing_yards", "canonical_event_id": "ab7bde95c9d5a8fc", "price": 1.877, "side": "over", "line": 254.5, "reason": "Quadruple Threat vs Atlanta's 27th-ranked pass D, tempered by a Week-1 outlier game.", "evidence_check": [{"type":"current_opponent","team":"ATL","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":27}]}
  ],
  "unders": [
    {"player": "Justin Herbert", "market_key": "player_passing_yards", "canonical_event_id": "53d9d3807e4d3e66", "price": 1.877, "side": "under", "line": 199.5, "reason": "Seattle's pass D ranks 1st in the league (152.0 ypg allowed); Herbert has zero top-tier-opponent sample this year.", "evidence_check": [{"type":"current_opponent","team":"SEA","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":1}]},
    {"player": "Jared Goff", "market_key": "player_passing_yards", "canonical_event_id": "8f044a7004d58a5c", "price": 1.877, "side": "under", "line": 260.5, "reason": "Carolina's pass D ranks 5th overall, 3rd vs WRs — his toughest matchup of the season, though mixed by a prior strong top-tier game.", "evidence_check": [{"type":"current_opponent","team":"CAR","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":5}]}
  ]
}
```

---

## 3. FIVE PARLAYS (Line-Based, 3/4/5/6/7 Team)

No Anytime TD legs here — every leg below is a real `player_passing_yards` market, the only non-ATD market this slate's data supports.

**3-Team:** Young O 246.5, Shough O 254.5, Herbert U 199.5 — three different games, three clean Threat/matchup convictions. No same-game overlap. Combined: **≈+561**.

**4-Team:** adds Purdy O 229.5 (SF game) — four different games, still no overlap. Combined: **≈+1141**.

**5-Team:** adds Goff U 260.5 (DET@CAR) — **Young and Goff are from the same game (DET@CAR, event 8f044a7004d58a5c)** — the combined price below is a cross-game-style estimate, not a real FanDuel SGP quote for that pair. Combined: **≈+2230**.

**6-Team:** adds Darnold O 233.5 (SEA) — **Herbert and Darnold are from the same game (LAC@SEA, event 53d9d3807e4d3e66)**, on top of the existing Young/Goff overlap. Combined: **≈+4274**.

**7-Team:** adds Nix O 221.5 (DEN) — **Purdy and Nix are from the same game (DEN@SF, event d5a0d1b78d351969)**, on top of both prior overlaps — this is now a parlay with three same-game pairs; treat the combined number purely as an independent-legs estimate, not a true SGP price. Combined: **≈+8110**.

```json
PARLAY_3_TEAM
[
  {"player": "Bryce Young", "market_key": "player_passing_yards", "canonical_event_id": "8f044a7004d58a5c", "price": 1.877, "side": "over", "line": 246.5, "reason": "Nuclear Threat vs Detroit's 32nd-ranked pass D.", "evidence_check": [{"type":"current_opponent","team":"DET","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":32}]},
  {"player": "Tyler Shough", "market_key": "player_passing_yards", "canonical_event_id": "ab7bde95c9d5a8fc", "price": 1.877, "side": "over", "line": 254.5, "reason": "Quadruple Threat vs Atlanta's 27th-ranked pass D.", "evidence_check": [{"type":"current_opponent","team":"ATL","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":27}]},
  {"player": "Justin Herbert", "market_key": "player_passing_yards", "canonical_event_id": "53d9d3807e4d3e66", "price": 1.877, "side": "under", "line": 199.5, "reason": "Seattle's pass D ranks 1st in the league allowing 152.0 ypg.", "evidence_check": [{"type":"current_opponent","team":"SEA","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":1}]}
]
```

```json
PARLAY_4_TEAM
[
  {"player": "Bryce Young", "market_key": "player_passing_yards", "canonical_event_id": "8f044a7004d58a5c", "price": 1.877, "side": "over", "line": 246.5, "reason": "Nuclear Threat vs Detroit's 32nd-ranked pass D.", "evidence_check": [{"type":"current_opponent","team":"DET","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":32}]},
  {"player": "Tyler Shough", "market_key": "player_passing_yards", "canonical_event_id": "ab7bde95c9d5a8fc", "price": 1.877, "side": "over", "line": 254.5, "reason": "Quadruple Threat vs Atlanta's 27th-ranked pass D.", "evidence_check": [{"type":"current_opponent","team":"ATL","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":27}]},
  {"player": "Justin Herbert", "market_key": "player_passing_yards", "canonical_event_id": "53d9d3807e4d3e66", "price": 1.877, "side": "under", "line": 199.5, "reason": "Seattle's pass D ranks 1st in the league allowing 152.0 ypg.", "evidence_check": [{"type":"current_opponent","team":"SEA","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":1}]},
  {"player": "Brock Purdy", "market_key": "player_passing_yards", "canonical_event_id": "d5a0d1b78d351969", "price": 1.877, "side": "over", "line": 229.5, "reason": "Standard Threat vs Denver's 24th-ranked pass D.", "evidence_check": [{"type":"current_opponent","team":"DEN","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":24}]}
]
```

```json
PARLAY_5_TEAM
[
  {"player": "Bryce Young", "market_key": "player_passing_yards", "canonical_event_id": "8f044a7004d58a5c", "price": 1.877, "side": "over", "line": 246.5, "reason": "Nuclear Threat vs Detroit's 32nd-ranked pass D.", "evidence_check": [{"type":"current_opponent","team":"DET","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":32}]},
  {"player": "Tyler Shough", "market_key": "player_passing_yards", "canonical_event_id": "ab7bde95c9d5a8fc", "price": 1.877, "side": "over", "line": 254.5, "reason": "Quadruple Threat vs Atlanta's 27th-ranked pass D.", "evidence_check": [{"type":"current_opponent","team":"ATL","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":27}]},
  {"player": "Justin Herbert", "market_key": "player_passing_yards", "canonical_event_id": "53d9d3807e4d3e66", "price": 1.877, "side": "under", "line": 199.5, "reason": "Seattle's pass D ranks 1st in the league allowing 152.0 ypg.", "evidence_check": [{"type":"current_opponent","team":"SEA","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":1}]},
  {"player": "Brock Purdy", "market_key": "player_passing_yards", "canonical_event_id": "d5a0d1b78d351969", "price": 1.877, "side": "over", "line": 229.5, "reason": "Standard Threat vs Denver's 24th-ranked pass D.", "evidence_check": [{"type":"current_opponent","team":"DEN","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":24}]},
  {"player": "Jared Goff", "market_key": "player_passing_yards", "canonical_event_id": "8f044a7004d58a5c", "price": 1.877, "side": "under", "line": 260.5, "reason": "Carolina's pass D ranks 5th overall, 3rd vs WRs — same game as the Young leg above.", "evidence_check": [{"type":"current_opponent","team":"CAR","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":5}]}
]
```

```json
PARLAY_6_TEAM
[
  {"player": "Bryce Young", "market_key": "player_passing_yards", "canonical_event_id": "8f044a7004d58a5c", "price": 1.877, "side": "over", "line": 246.5, "reason": "Nuclear Threat vs Detroit's 32nd-ranked pass D.", "evidence_check": [{"type":"current_opponent","team":"DET","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":32}]},
  {"player": "Tyler Shough", "market_key": "player_passing_yards", "canonical_event_id": "ab7bde95c9d5a8fc", "price": 1.877, "side": "over", "line": 254.5, "reason": "Quadruple Threat vs Atlanta's 27th-ranked pass D.", "evidence_check": [{"type":"current_opponent","team":"ATL","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":27}]},
  {"player": "Justin Herbert", "market_key": "player_passing_yards", "canonical_event_id": "53d9d3807e4d3e66", "price": 1.877, "side": "under", "line": 199.5, "reason": "Seattle's pass D ranks 1st in the league allowing 152.0 ypg.", "evidence_check": [{"type":"current_opponent","team":"SEA","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":1}]},
  {"player": "Brock Purdy", "market_key": "player_passing_yards", "canonical_event_id": "d5a0d1b78d351969", "price": 1.877, "side": "over", "line": 229.5, "reason": "Standard Threat vs Denver's 24th-ranked pass D.", "evidence_check": [{"type":"current_opponent","team":"DEN","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":24}]},
  {"player": "Jared Goff", "market_key": "player_passing_yards", "canonical_event_id": "8f044a7004d58a5c", "price": 1.877, "side": "under", "line": 260.5, "reason": "Carolina's pass D ranks 5th overall, 3rd vs WRs — same game as the Young leg above.", "evidence_check": [{"type":"current_opponent","team":"CAR","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":5}]},
  {"player": "Sam Darnold", "market_key": "player_passing_yards", "canonical_event_id": "53d9d3807e4d3e66", "price": 1.877, "side": "over", "line": 233.5, "reason": "Likely current starter after a 379-yard, 100%-snap Week 3; same game as the Herbert leg above.", "evidence_check": []}
]
```

```json
PARLAY_7_TEAM
[
  {"player": "Bryce Young", "market_key": "player_passing_yards", "canonical_event_id": "8f044a7004d58a5c", "price": 1.877, "side": "over", "line": 246.5, "reason": "Nuclear Threat vs Detroit's 32nd-ranked pass D.", "evidence_check": [{"type":"current_opponent","team":"DET","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":32}]},
  {"player": "Tyler Shough", "market_key": "player_passing_yards", "canonical_event_id": "ab7bde95c9d5a8fc", "price": 1.877, "side": "over", "line": 254.5, "reason": "Quadruple Threat vs Atlanta's 27th-ranked pass D.", "evidence_check": [{"type":"current_opponent","team":"ATL","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":27}]},
  {"player": "Justin Herbert", "market_key": "player_passing_yards", "canonical_event_id": "53d9d3807e4d3e66", "price": 1.877, "side": "under", "line": 199.5, "reason": "Seattle's pass D ranks 1st in the league allowing 152.0 ypg.", "evidence_check": [{"type":"current_opponent","team":"SEA","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":1}]},
  {"player": "Brock Purdy", "market_key": "player_passing_yards", "canonical_event_id": "d5a0d1b78d351969", "price": 1.877, "side": "over", "line": 229.5, "reason": "Standard Threat vs Denver's 24th-ranked pass D.", "evidence_check": [{"type":"current_opponent","team":"DEN","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":24}]},
  {"player": "Jared Goff", "market_key": "player_passing_yards", "canonical_event_id": "8f044a7004d58a5c", "price": 1.877, "side": "under", "line": 260.5, "reason": "Carolina's pass D ranks 5th overall, 3rd vs WRs — same game as the Young leg above.", "evidence_check": [{"type":"current_opponent","team":"CAR","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":5}]},
  {"player": "Sam Darnold", "market_key": "player_passing_yards", "canonical_event_id": "53d9d3807e4d3e66", "price": 1.877, "side": "over", "line": 233.5, "reason": "Likely current starter after a 379-yard, 100%-snap Week 3; same game as the Herbert leg above.", "evidence_check": []},
  {"player": "Bo Nix", "market_key": "player_passing_yards", "canonical_event_id": "d5a0d1b78d351969", "price": 1.877, "side": "over", "line": 221.5, "reason": "His one mid-tier-opponent game this season (vs JAX) produced 288 yards, well above this line; same game as the Purdy leg above.", "evidence_check": []}
]
```

---

## 4. FAVORITE ANYTIME TD PARLAYS (3/4/5/6/7 Team)

**3-Team:** Gibbs, Bijan, McCaffrey — three different games, three of the slate's cleanest Threat convergences. Combined: **≈+185**.

**4-Team:** adds Jaxon Smith-Njigba — four different games, no overlap. Combined: **≈+433**.

**5-Team:** adds Amon-Ra St. Brown — **St. Brown and Gibbs are both in the DET@CAR game (event 8f044a7004d58a5c)**, correlated. Combined: **≈+859**.

**6-Team:** adds Chuba Hubbard — now **three legs (Gibbs, St. Brown, Hubbard) share the DET@CAR game**; this is a heavily correlated same-game stack and the combined number below is purely an independent-legs estimate, not a real SGP quote. Combined: **≈+1569**.

**7-Team:** adds Chris Olave — **Olave and Bijan now also share the ATL@NO game**, on top of the DET@CAR stack. Combined: **≈+3488**.

```json
TD_PARLAY_3_TEAM
[
  {"player": "Jahmyr Gibbs", "market_key": "player_anytime_td", "canonical_event_id": "8f044a7004d58a5c", "price": 1.294, "side": "over", "line": null, "reason": "Elite Threat vs Carolina's 32nd-ranked run D vs RBs.", "evidence_check": [{"type":"current_opponent","team":"CAR","pos":"RB","stat":"rush_yds","role":"def","claimed_rank":32}]},
  {"player": "Bijan Robinson", "market_key": "player_anytime_td", "canonical_event_id": "ab7bde95c9d5a8fc", "price": 1.455, "side": "over", "line": null, "reason": "Elite Threat vs New Orleans' 29th-ranked run D vs RBs.", "evidence_check": [{"type":"current_opponent","team":"NO","pos":"RB","stat":"rush_yds","role":"def","claimed_rank":29}]},
  {"player": "Christian McCaffrey", "market_key": "player_anytime_td", "canonical_event_id": "d5a0d1b78d351969", "price": 1.513, "side": "over", "line": null, "reason": "Elite Threat vs Denver's 31st-ranked run D vs RBs.", "evidence_check": [{"type":"current_opponent","team":"DEN","pos":"RB","stat":"rush_yds","role":"def","claimed_rank":31}]}
]
```

```json
TD_PARLAY_4_TEAM
[
  {"player": "Jahmyr Gibbs", "market_key": "player_anytime_td", "canonical_event_id": "8f044a7004d58a5c", "price": 1.294, "side": "over", "line": null, "reason": "Elite Threat vs Carolina's 32nd-ranked run D vs RBs.", "evidence_check": [{"type":"current_opponent","team":"CAR","pos":"RB","stat":"rush_yds","role":"def","claimed_rank":32}]},
  {"player": "Bijan Robinson", "market_key": "player_anytime_td", "canonical_event_id": "ab7bde95c9d5a8fc", "price": 1.455, "side": "over", "line": null, "reason": "Elite Threat vs New Orleans' 29th-ranked run D vs RBs.", "evidence_check": [{"type":"current_opponent","team":"NO","pos":"RB","stat":"rush_yds","role":"def","claimed_rank":29}]},
  {"player": "Christian McCaffrey", "market_key": "player_anytime_td", "canonical_event_id": "d5a0d1b78d351969", "price": 1.513, "side": "over", "line": null, "reason": "Elite Threat vs Denver's 31st-ranked run D vs RBs.", "evidence_check": [{"type":"current_opponent","team":"DEN","pos":"RB","stat":"rush_yds","role":"def","claimed_rank":31}]},
  {"player": "Jaxon Smith-Njigba", "market_key": "player_anytime_td", "canonical_event_id": "53d9d3807e4d3e66", "price": 1.87, "side": "over", "line": null, "reason": "1st in rec yards and receptions, 50% RZ target share vs LAC's 22nd-ranked WR D.", "evidence_check": [{"type":"current_opponent","team":"LAC","pos":"WR","stat":"rec_yds","role":"def","claimed_rank":22}]}
]
```

```json
TD_PARLAY_5_TEAM
[
  {"player": "Jahmyr Gibbs", "market_key": "player_anytime_td", "canonical_event_id": "8f044a7004d58a5c", "price": 1.294, "side": "over", "line": null, "reason": "Elite Threat vs Carolina's 32nd-ranked run D vs RBs.", "evidence_check": [{"type":"current_opponent","team":"CAR","pos":"RB","stat":"rush_yds","role":"def","claimed_rank":32}]},
  {"player": "Bijan Robinson", "market_key": "player_anytime_td", "canonical_event_id": "ab7bde95c9d5a8fc", "price": 1.455, "side": "over", "line": null, "reason": "Elite Threat vs New Orleans' 29th-ranked run D vs RBs.", "evidence_check": [{"type":"current_opponent","team":"NO","pos":"RB","stat":"rush_yds","role":"def","claimed_rank":29}]},
  {"player": "Christian McCaffrey", "market_key": "player_anytime_td", "canonical_event_id": "d5a0d1b78d351969", "price": 1.513, "side": "over", "line": null, "reason": "Elite Threat vs Denver's 31st-ranked run D vs RBs.", "evidence_check": [{"type":"current_opponent","team":"DEN","pos":"RB","stat":"rush_yds","role":"def","claimed_rank":31}]},
  {"player": "Jaxon Smith-Njigba", "market_key": "player_anytime_td", "canonical_event_id": "53d9d3807e4d3e66", "price": 1.87, "side": "over", "line": null, "reason": "1st in rec yards and receptions, 50% RZ target share vs LAC's 22nd-ranked WR D.", "evidence_check": [{"type":"current_opponent","team":"LAC","pos":"WR","stat":"rec_yds","role":"def","claimed_rank":22}]},
  {"player": "Amon-Ra St. Brown", "market_key": "player_anytime_td", "canonical_event_id": "8f044a7004d58a5c", "price": 1.8, "side": "over", "line": null, "reason": "37.5% RZ target share, 4 TD on 9 RZ targets; same game as the Gibbs leg above.", "evidence_check": []}
]
```

```json
TD_PARLAY_6_TEAM
[
  {"player": "Jahmyr Gibbs", "market_key": "player_anytime_td", "canonical_event_id": "8f044a7004d58a5c", "price": 1.294, "side": "over", "line": null, "reason": "Elite Threat vs Carolina's 32nd-ranked run D vs RBs.", "evidence_check": [{"type":"current_opponent","team":"CAR","pos":"RB","stat":"rush_yds","role":"def","claimed_rank":32}]},
  {"player": "Bijan Robinson", "market_key": "player_anytime_td", "canonical_event_id": "ab7bde95c9d5a8fc", "price": 1.455, "side": "over", "line": null, "reason": "Elite Threat vs New Orleans' 29th-ranked run D vs RBs.", "evidence_check": [{"type":"current_opponent","team":"NO","pos":"RB","stat":"rush_yds","role":"def","claimed_rank":29}]},
  {"player": "Christian McCaffrey", "market_key": "player_anytime_td", "canonical_event_id": "d5a0d1b78d351969", "price": 1.513, "side": "over", "line": null, "reason": "Elite Threat vs Denver's 31st-ranked run D vs RBs.", "evidence_check": [{"type":"current_opponent","team":"DEN","pos":"RB","stat":"rush_yds","role":"def","claimed_rank":31}]},
  {"player": "Jaxon Smith-Njigba", "market_key": "player_anytime_td", "canonical_event_id": "53d9d3807e4d3e66", "price": 1.87, "side": "over", "line": null, "reason": "1st in rec yards and receptions, 50% RZ target share vs LAC's 22nd-ranked WR D.", "evidence_check": [{"type":"current_opponent","team":"LAC","pos":"WR","stat":"rec_yds","role":"def","claimed_rank":22}]},
  {"player": "Amon-Ra St. Brown", "market_key": "player_anytime_td", "canonical_event_id": "8f044a7004d58a5c", "price": 1.8, "side": "over", "line": null, "reason": "37.5% RZ target share, 4 TD on 9 RZ targets; same game as the Gibbs leg above.", "evidence_check": []},
  {"player": "Chuba Hubbard", "market_key": "player_anytime_td", "canonical_event_id": "8f044a7004d58a5c", "price": 1.741, "side": "over", "line": null, "reason": "53.8% RZ touch share; a third leg now sharing the DET@CAR game with Gibbs and St. Brown above.", "evidence_check": []}
]
```

```json
TD_PARLAY_7_TEAM
[
  {"player": "Jahmyr Gibbs", "market_key": "player_anytime_td", "canonical_event_id": "8f044a7004d58a5c", "price": 1.294, "side": "over", "line": null, "reason": "Elite Threat vs Carolina's 32nd-ranked run D vs RBs.", "evidence_check": [{"type":"current_opponent","team":"CAR","pos":"RB","stat":"rush_yds","role":"def","claimed_rank":32}]},
  {"player": "Bijan Robinson", "market_key": "player_anytime_td", "canonical_event_id": "ab7bde95c9d5a8fc", "price": 1.455, "side": "over", "line": null, "reason": "Elite Threat vs New Orleans' 29th-ranked run D vs RBs.", "evidence_check": [{"type":"current_opponent","team":"NO","pos":"RB","stat":"rush_yds","role":"def","claimed_rank":29}]},
  {"player": "Christian McCaffrey", "market_key": "player_anytime_td", "canonical_event_id": "d5a0d1b78d351969", "price": 1.513, "side": "over", "line": null, "reason": "Elite Threat vs Denver's 31st-ranked run D vs RBs.", "evidence_check": [{"type":"current_opponent","team":"DEN","pos":"RB","stat":"rush_yds","role":"def","claimed_rank":31}]},
  {"player": "Jaxon Smith-Njigba", "market_key": "player_anytime_td", "canonical_event_id": "53d9d3807e4d3e66", "price": 1.87, "side": "over", "line": null, "reason": "1st in rec yards and receptions, 50% RZ target share vs LAC's 22nd-ranked WR D.", "evidence_check": [{"type":"current_opponent","team":"LAC","pos":"WR","stat":"rec_yds","role":"def","claimed_rank":22}]},
  {"player": "Amon-Ra St. Brown", "market_key": "player_anytime_td", "canonical_event_id": "8f044a7004d58a5c", "price": 1.8, "side": "over", "line": null, "reason": "37.5% RZ target share, 4 TD on 9 RZ targets; same game as the Gibbs leg above.", "evidence_check": []},
  {"player": "Chuba Hubbard", "market_key": "player_anytime_td", "canonical_event_id": "8f044a7004d58a5c", "price": 1.741, "side": "over", "line": null, "reason": "53.8% RZ touch share; a third leg now sharing the DET@CAR game with Gibbs and St. Brown above.", "evidence_check": []},
  {"player": "Chris Olave", "market_key": "player_anytime_td", "canonical_event_id": "ab7bde95c9d5a8fc", "price": 2.15, "side": "over", "line": null, "reason": "Nuclear Threat vs Atlanta's worst-in-league WR D; same game as the Bijan leg above.", "evidence_check": [{"type":"current_opponent","team":"ATL","pos":"WR","stat":"rec_yds","role":"def","claimed_rank":32}]}
]
```

---

## 5. FAVORITE SPREAD PARLAYS — DATA LIMITATION NOTE

This slate has exactly **4 real mainline spread markets** (one per game). Building honest 5-, 6-, and 7-team spread parlays would require reusing a market or inventing one — this report does neither. Only a **3-team** and **4-team** spread parlay are offered below; 5/6/7-team spread parlays are not provided this week.

- **Detroit Lions -3.5 (-114)** — DET's road ATS is 61.5% (32-20), overall 60.4% — the best ATS team on the slate; matchup evidence (elite Lions offense vs Carolina's historically broken run D) reinforces it.
- **San Francisco 49ers -2.5 (-120)** — SF's home ATS is a middling 48.1% (25-27), but the matchup specifics (3rd-down disparity, Denver's 30th-ranked total defense) argue this game should outperform that historical home rate.
- **Atlanta Falcons +2.5 (-102)** — fading New Orleans at home given the Saints' weak 41.2% home ATS mark (21-30); Atlanta's away ATS sits a more respectable 48.1% (25-27), and Bijan Robinson's individual matchup edge supports live-dog value.
- **Seattle Seahawks -7.0 (-115)** — Seattle's home ATS is middling (46.9%, 23-26), but the specific matchup (elite SEA defense vs a historically bad Chargers passing offense) argues this game breaks from that trend; Herbert projects for one of his worst slates of the season.

**3-Team:** DET -3.5, SF -2.5, ATL +2.5 — three different games, best overall convictions combining matchup edge and real ATS context. Combined: **≈+564**.

**4-Team:** adds SEA -7.0 — four different games, no overlap. Combined: **≈+1142**.

```json
SPREAD_PARLAY_3_TEAM
[
  {"player": "Detroit Lions", "market_key": "spreads", "canonical_event_id": "8f044a7004d58a5c", "price": 1.847, "point": -3.5, "reason": "DET's road ATS is 61.5% (32-20), the best mark on this slate; Carolina's run D is the worst specific matchup in this week's evidence.", "evidence_check": []},
  {"player": "San Francisco 49ers", "market_key": "spreads", "canonical_event_id": "d5a0d1b78d351969", "price": 1.833, "point": -2.5, "reason": "SF's home ATS sits at a middling 48.1%, but a 3rd-down disparity and Denver's 30th-ranked defense argue this specific game outperforms that trend.", "evidence_check": []},
  {"player": "Atlanta Falcons", "market_key": "spreads", "canonical_event_id": "ab7bde95c9d5a8fc", "price": 1.962, "point": 2.5, "reason": "New Orleans' home ATS is just 41.2% (21-30), one of the worst on the slate, while Atlanta's road ATS (48.1%) is more respectable.", "evidence_check": []}
]
```

```json
SPREAD_PARLAY_4_TEAM
[
  {"player": "Detroit Lions", "market_key": "spreads", "canonical_event_id": "8f044a7004d58a5c", "price": 1.847, "point": -3.5, "reason": "DET's road ATS is 61.5% (32-20), the best mark on this slate; Carolina's run D is the worst specific matchup in this week's evidence.", "evidence_check": []},
  {"player": "San Francisco 49ers", "market_key": "spreads", "canonical_event_id": "d5a0d1b78d351969", "price": 1.833, "point": -2.5, "reason": "SF's home ATS sits at a middling 48.1%, but a 3rd-down disparity and Denver's 30th-ranked defense argue this specific game outperforms that trend.", "evidence_check": []},
  {"player": "Atlanta Falcons", "market_key": "spreads", "canonical_event_id": "ab7bde95c9d5a8fc", "price": 1.962, "point": 2.5, "reason": "New Orleans' home ATS is just 41.2% (21-30), one of the worst on the slate, while Atlanta's road ATS (48.1%) is more respectable.", "evidence_check": []},
  {"player": "Seattle Seahawks", "market_key": "spreads", "canonical_event_id": "53d9d3807e4d3e66", "price": 1.87, "point": -7.0, "reason": "SEA's home ATS is only 46.9% (23-26), but the specific matchup (elite SEA D vs a historically bad LAC passing game) argues this breaks that trend.", "evidence_check": []}
]
```