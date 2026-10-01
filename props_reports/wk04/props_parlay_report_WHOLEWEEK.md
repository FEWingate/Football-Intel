# COEUS PARLAY REPORT — FULL SLATE (WEEK OF 2026-10-01/05)

All legs below are drawn from real FanDuel data and grounded in the real season-long team rank tables provided. Confidence labels follow the Evidence Priority Rule — Threat System / season stat-and-rank comparisons lead; thin splits or recent-form-only trends are flagged LOW.

---

## SECTION 6 — FIVE LINE-BASED PARLAYS (NO Anytime TD, NO Spreads)

### 3-Team Parlay
- **Bryce Young** (CAR) — Passing Yards, Over 246.5, -114 — CAR's QB corps ranks **1st** in pass yds/gm (313.0) vs DET's **32nd**-ranked pass defense (326.3 ypg allowed, worst in the league). Confidence: HIGH.
- **Kyren Williams** (LAR) — Rushing Yards, Over 56.5, -114 — LAR's RB corps ranks **4th** in rush yds/gm (127.0) vs PHI's **26th**-ranked run D vs backs (110.3 ypg allowed). Confidence: HIGH.
- **Justin Herbert** (LAC) — Passing Yards, Under 199.5, -114 — LAC's QB corps ranks **19th** in pass yds/gm (209.0) vs SEA's **1st**-ranked pass D (152.0 ypg allowed). Confidence: HIGH.
- Thread: three independent elite rank mismatches, no shared game. Combined price: **+561**.

```json
PARLAY_3_TEAM
[
  {"player":"Bryce Young","market_key":"player_passing_yards","canonical_event_id":"8f044a7004d58a5c","price":1.877,"side":"over","line":246.5,"reason":"CAR QB corps ranks 1st in pass yds/gm (313.0) vs DET's 32nd-ranked pass D (326.3 ypg allowed).","evidence_check":[{"type":"current_opponent","team":"CAR","pos":"QB","stat":"pass_ypg","role":"off","claimed_rank":1},{"type":"current_opponent","team":"DET","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":32}]},
  {"player":"Kyren Williams","market_key":"player_rushing_yards","canonical_event_id":"0b88c15fb8b87a89","price":1.877,"side":"over","line":56.5,"reason":"LAR RB corps ranks 4th in rush yds/gm (127.0) vs PHI's 26th-ranked run D vs backs (110.3 ypg allowed).","evidence_check":[{"type":"current_opponent","team":"LAR","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":4},{"type":"current_opponent","team":"PHI","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":26}]},
  {"player":"Justin Herbert","market_key":"player_passing_yards","canonical_event_id":"53d9d3807e4d3e66","price":1.877,"side":"under","line":199.5,"reason":"LAC QB corps ranks 19th in pass yds/gm (209.0) vs SEA's 1st-ranked pass D (152.0 ypg allowed).","evidence_check":[{"type":"current_opponent","team":"LAC","pos":"QB","stat":"pass_ypg","role":"off","claimed_rank":19},{"type":"current_opponent","team":"SEA","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":1}]}
]
```

### 4-Team Parlay
- **Brock Purdy** (SF) — Passing Yards, Over 229.5, -114 — SF's QB group ranks **9th** (263.0 ypg) vs DEN's **24th**-ranked pass D (254.3 ypg allowed).
- **CeeDee Lamb** (DAL) — Receiving Yards, Over 76.5, -114 — DAL's WR corps ranks **6th** (184.3 ypg) vs HOU's **27th**-ranked WR D (176.3 ypg allowed).
- **C.J. Stroud** (HOU) — Passing Yards, Under 244.5, -114 — HOU's QB corps ranks **8th** (264.7 ypg) but DAL's pass D ranks **9th**-best (207.7 ypg allowed) — same game as Lamb.
- **Kirk Cousins** (LV) — Passing Yards, Under 223.5, -114 — LV's QB corps ranks **17th** (220.3 ypg) vs KC's **3rd**-ranked pass D (183.7 ypg allowed).
- Note: Lamb and Stroud share the DAL/HOU game — correlated, not an independent SGP quote. Thread: tracking real season-rank mismatches across four different scoring environments. Combined price: **+1141**.

```json
PARLAY_4_TEAM
[
  {"player":"Brock Purdy","market_key":"player_passing_yards","canonical_event_id":"d5a0d1b78d351969","price":1.877,"side":"over","line":229.5,"reason":"SF QB corps ranks 9th (263.0 ypg) vs DEN's 24th-ranked pass D (254.3 ypg allowed).","evidence_check":[{"type":"current_opponent","team":"SF","pos":"QB","stat":"pass_ypg","role":"off","claimed_rank":9},{"type":"current_opponent","team":"DEN","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":24}]},
  {"player":"CeeDee Lamb","market_key":"player_receiving_yards","canonical_event_id":"0eae1db34049745a","price":1.877,"side":"over","line":76.5,"reason":"DAL WR corps ranks 6th (184.3 ypg) vs HOU's 27th-ranked WR D (176.3 ypg allowed).","evidence_check":[{"type":"current_opponent","team":"DAL","pos":"WR","stat":"rec_ypg","role":"off","claimed_rank":6},{"type":"current_opponent","team":"HOU","pos":"WR","stat":"rec_ypg","role":"def","claimed_rank":27}]},
  {"player":"C.J. Stroud","market_key":"player_passing_yards","canonical_event_id":"0eae1db34049745a","price":1.877,"side":"under","line":244.5,"reason":"HOU QB corps ranks 8th (264.7 ypg) but DAL pass D ranks 9th-best (207.7 ypg allowed) - Stroud's first real top-tier test.","evidence_check":[{"type":"current_opponent","team":"HOU","pos":"QB","stat":"pass_ypg","role":"off","claimed_rank":8},{"type":"current_opponent","team":"DAL","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":9}]},
  {"player":"Kirk Cousins","market_key":"player_passing_yards","canonical_event_id":"82f1042cd9096ce2","price":1.877,"side":"under","line":223.5,"reason":"LV QB corps ranks 17th (220.3 ypg) vs KC's 3rd-ranked pass D (183.7 ypg allowed).","evidence_check":[{"type":"current_opponent","team":"LV","pos":"QB","stat":"pass_ypg","role":"off","claimed_rank":17},{"type":"current_opponent","team":"KC","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":3}]}
]
```

### 5-Team Parlay
- **Jaylen Warren** (PIT) — Rushing Yards, Over 67.5, -114 — PIT RB corps ranks **17th** (89.7 ypg) vs CLE's **24th**-ranked run D vs backs (106.0 ypg allowed).
- **Pat Freiermuth** (PIT) — Receiving Yards, Over 28.5, -114 — PIT TE corps ranks **9th** (67.3 ypg) vs CLE's **24th**-ranked TE D (66.0 ypg allowed) — same game as Warren.
- **Josh Downs** (IND) — Receiving Yards, Over 64.5, -114 — IND WR corps ranks **18th** (146.3 ypg) vs WAS's **30th**-ranked WR D (191.0 ypg allowed).
- **Jonathan Taylor** (IND) — Rushing Yards, Under 90.5, -114 — IND RB corps ranks **16th** (90.7 ypg) but WAS's run D ranks **3rd**-best vs backs (56.0 ypg allowed) — same game as Downs.
- **Javonte Williams** (HOU) — Rushing Yards, Under 59.5, -114 — HOU RB corps ranks **30th** (56.0 ypg, worst-tier) even vs DAL's **28th**-ranked run D (114.3 ypg allowed) — offense's own weakness caps the ceiling.
- Thread: PIT/CLE and IND/WAS each contribute an over/under pair; combined price: **+2230**.

```json
PARLAY_5_TEAM
[
  {"player":"Jaylen Warren","market_key":"player_rushing_yards","canonical_event_id":"1c79ffc934ef3e24","price":1.877,"side":"over","line":67.5,"reason":"PIT RB corps ranks 17th (89.7 ypg) vs CLE's 24th-ranked run D vs backs (106.0 ypg allowed).","evidence_check":[{"type":"current_opponent","team":"PIT","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":17},{"type":"current_opponent","team":"CLE","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":24}]},
  {"player":"Pat Freiermuth","market_key":"player_receiving_yards","canonical_event_id":"1c79ffc934ef3e24","price":1.877,"side":"over","line":28.5,"reason":"PIT TE corps ranks 9th (67.3 ypg) vs CLE's 24th-ranked TE D (66.0 ypg allowed).","evidence_check":[{"type":"current_opponent","team":"PIT","pos":"TE","stat":"rec_ypg","role":"off","claimed_rank":9},{"type":"current_opponent","team":"CLE","pos":"TE","stat":"rec_ypg","role":"def","claimed_rank":24}]},
  {"player":"Josh Downs","market_key":"player_receiving_yards","canonical_event_id":"b9550fb6e56e66e2","price":1.877,"side":"over","line":64.5,"reason":"IND WR corps ranks 18th (146.3 ypg) vs WAS's 30th-ranked WR D (191.0 ypg allowed).","evidence_check":[{"type":"current_opponent","team":"IND","pos":"WR","stat":"rec_ypg","role":"off","claimed_rank":18},{"type":"current_opponent","team":"WAS","pos":"WR","stat":"rec_ypg","role":"def","claimed_rank":30}]},
  {"player":"Jonathan Taylor","market_key":"player_rushing_yards","canonical_event_id":"b9550fb6e56e66e2","price":1.877,"side":"under","line":90.5,"reason":"IND RB corps ranks 16th (90.7 ypg) but WAS run D ranks 3rd-best vs backs (56.0 ypg allowed).","evidence_check":[{"type":"current_opponent","team":"IND","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":16},{"type":"current_opponent","team":"WAS","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":3}]},
  {"player":"Javonte Williams","market_key":"player_rushing_yards","canonical_event_id":"0eae1db34049745a","price":1.877,"side":"under","line":59.5,"reason":"HOU RB corps ranks 30th (56.0 ypg) even vs DAL's 28th-ranked run D (114.3 ypg allowed) - offense's own weakness caps the ceiling.","evidence_check":[{"type":"current_opponent","team":"HOU","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":30},{"type":"current_opponent","team":"DAL","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":28}]}
]
```

### 6-Team Parlay
- **Geno Smith** (NYJ) — Passing Yards, Over 227.5, -114 — NYJ QB corps ranks **11th** (261.0 ypg) vs CHI's **13th**-ranked pass D (219.0 ypg allowed). Confidence: MEDIUM (near-neutral matchup).
- **Braelon Allen** (NYJ) — Rushing Yards, Under 56.5, -114 — NYJ RB corps ranks **25th** (74.7 ypg) vs CHI's middling **17th**-ranked run D (95.3 ypg allowed) — same game as Smith.
- **Christian Watson** (GB) — Receiving Yards, Over 67.5, -114 — GB WR corps ranks **1st** (210.0 ypg) vs TB's **7th**-ranked WR D (119.0 ypg allowed). Confidence: MEDIUM (tough individual matchup, volume carries it).
- **Jordan Love** (GB) — Passing Yards, Over 246.5, -114 — GB QB corps ranks **4th** (281.3 ypg) vs TB's **14th**-ranked pass D (220.0 ypg allowed) — same game as Watson.
- **Michael Wilson** (ARI) — Receptions 5+ (alt), Over, -182 — ARI WR corps ranks **14th** in rec/gm (11.3) vs NYG's **30th**-ranked WR D by catches allowed (14.3/gm).
- **Cam Skattebo** (NYG) — Receiving Yards, Under 17.5, -114 — NYG RB corps ranks **18th** (27.0 ypg) vs ARI's elite **4th**-ranked RB-receiving D (17.0 ypg allowed) — same game as Wilson.
- Thread: three game-paired over/under combos stacked together. Combined price: **+3509**.

```json
PARLAY_6_TEAM
[
  {"player":"Geno Smith","market_key":"player_passing_yards","canonical_event_id":"aa99633d7fc75bb4","price":1.877,"side":"over","line":227.5,"reason":"NYJ QB corps ranks 11th (261.0 ypg) vs CHI's 13th-ranked pass D (219.0 ypg allowed).","evidence_check":[{"type":"current_opponent","team":"NYJ","pos":"QB","stat":"pass_ypg","role":"off","claimed_rank":11},{"type":"current_opponent","team":"CHI","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":13}]},
  {"player":"Braelon Allen","market_key":"player_rushing_yards","canonical_event_id":"aa99633d7fc75bb4","price":1.877,"side":"under","line":56.5,"reason":"NYJ RB corps ranks 25th (74.7 ypg) vs CHI's 17th-ranked run D (95.3 ypg allowed).","evidence_check":[{"type":"current_opponent","team":"NYJ","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":25},{"type":"current_opponent","team":"CHI","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":17}]},
  {"player":"Christian Watson","market_key":"player_receiving_yards","canonical_event_id":"a223ecde7f6e4844","price":1.877,"side":"over","line":67.5,"reason":"GB WR corps ranks 1st (210.0 ypg) vs TB's 7th-ranked WR D (119.0 ypg allowed).","evidence_check":[{"type":"current_opponent","team":"GB","pos":"WR","stat":"rec_ypg","role":"off","claimed_rank":1},{"type":"current_opponent","team":"TB","pos":"WR","stat":"rec_ypg","role":"def","claimed_rank":7}]},
  {"player":"Jordan Love","market_key":"player_passing_yards","canonical_event_id":"a223ecde7f6e4844","price":1.877,"side":"over","line":246.5,"reason":"GB QB corps ranks 4th (281.3 ypg) vs TB's 14th-ranked pass D (220.0 ypg allowed).","evidence_check":[{"type":"current_opponent","team":"GB","pos":"QB","stat":"pass_ypg","role":"off","claimed_rank":4},{"type":"current_opponent","team":"TB","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":14}]},
  {"player":"Michael Wilson","market_key":"player_receptions_milestones_5_or_more","canonical_event_id":"fefdcc7bd476a375","price":1.549,"side":"over","line":5,"reason":"ARI WR corps ranks 14th in rec/gm (11.3) vs NYG's 30th-ranked WR D by catches allowed (14.3/gm).","evidence_check":[{"type":"current_opponent","team":"ARI","pos":"WR","stat":"rec_pg","role":"off","claimed_rank":14},{"type":"current_opponent","team":"NYG","pos":"WR","stat":"rec_pg","role":"def","claimed_rank":30}]},
  {"player":"Cam Skattebo","market_key":"player_receiving_yards","canonical_event_id":"fefdcc7bd476a375","price":1.877,"side":"under","line":17.5,"reason":"NYG RB corps ranks 18th (27.0 ypg) vs ARI's 4th-ranked RB-receiving D (17.0 ypg allowed).","evidence_check":[{"type":"current_opponent","team":"NYG","pos":"RB","stat":"rec_ypg","role":"off","claimed_rank":18},{"type":"current_opponent","team":"ARI","pos":"RB","stat":"rec_ypg","role":"def","claimed_rank":4}]}
]
```

### 7-Team Parlay
- **James Cook** (BUF) — Rushing Yards, Over 87.5, -114 — BUF RB corps ranks **6th** (117.3 ypg) vs NE's **16th**-ranked run D (92.3 ypg allowed).
- **Josh Allen** (BUF) — Passing Yards, Under 242.5, -114 — BUF QB corps ranks **10th** (262.0 ypg) vs NE's **6th**-ranked pass D (189.7 ypg allowed) — same game as Cook.
- **Dalton Kincaid** (BUF) — Receiving Yards, Under 52.5, -114 — BUF TE corps ranks **2nd** (93.3 ypg) vs NE's **4th**-ranked TE D (28.0 ypg allowed) — same game.
- **Trevor Lawrence** (JAX) — Passing Yards, Under 263.5, -114 — JAX QB corps ranks **22nd** (205.3 ypg) vs CIN's **29th**-ranked pass D (287.0 ypg allowed) — JAX's own low volume caps the number anyway.
- **Bhayshul Tuten** (JAX) — Rushing Yards, Under 53.5, -114 — JAX RB corps ranks **8th** (107.3 ypg) vs CIN's **8th**-best run D vs backs (68.3 ypg allowed) — same game as Lawrence.
- **Brian Thomas Jr.** (JAX) — Receiving Yards, Under 26.5, -114 — JAX WR corps ranks **11th** (157.7 ypg) vs CIN's **14th**-ranked WR D (140.3 ypg allowed); neutral team ranks, but Thomas's own recent role has collapsed behind Washington's 30.7% target share — same game.
- **Aaron Jones** (MIN) — Rushing Yards, Over 67.5, -114 — MIN RB corps ranks **15th** (91.0 ypg) vs MIA's **18th**-ranked run D (98.0 ypg allowed).
- Thread: NE/BUF trio and JAX/CIN trio stacked with one standalone MIN leg. Combined price: **+8108**.

```json
PARLAY_7_TEAM
[
  {"player":"James Cook","market_key":"player_rushing_yards","canonical_event_id":"5a6a506f9ff2a30f","price":1.877,"side":"over","line":87.5,"reason":"BUF RB corps ranks 6th (117.3 ypg) vs NE's 16th-ranked run D (92.3 ypg allowed).","evidence_check":[{"type":"current_opponent","team":"BUF","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":6},{"type":"current_opponent","team":"NE","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":16}]},
  {"player":"Josh Allen","market_key":"player_passing_yards","canonical_event_id":"5a6a506f9ff2a30f","price":1.877,"side":"under","line":242.5,"reason":"BUF QB corps ranks 10th (262.0 ypg) vs NE's 6th-ranked pass D (189.7 ypg allowed).","evidence_check":[{"type":"current_opponent","team":"BUF","pos":"QB","stat":"pass_ypg","role":"off","claimed_rank":10},{"type":"current_opponent","team":"NE","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":6}]},
  {"player":"Dalton Kincaid","market_key":"player_receiving_yards","canonical_event_id":"5a6a506f9ff2a30f","price":1.877,"side":"under","line":52.5,"reason":"BUF TE corps ranks 2nd (93.3 ypg) vs NE's 4th-ranked TE D (28.0 ypg allowed).","evidence_check":[{"type":"current_opponent","team":"BUF","pos":"TE","stat":"rec_ypg","role":"off","claimed_rank":2},{"type":"current_opponent","team":"NE","pos":"TE","stat":"rec_ypg","role":"def","claimed_rank":4}]},
  {"player":"Trevor Lawrence","market_key":"player_passing_yards","canonical_event_id":"d7ab040d22994748","price":1.877,"side":"under","line":263.5,"reason":"JAX QB corps ranks 22nd (205.3 ypg) vs CIN's 29th-ranked pass D (287.0 ypg allowed); JAX's own low volume caps the ceiling.","evidence_check":[{"type":"current_opponent","team":"JAX","pos":"QB","stat":"pass_ypg","role":"off","claimed_rank":22},{"type":"current_opponent","team":"CIN","pos":"QB","stat":"pass_ypg","role":"def","claimed_rank":29}]},
  {"player":"Bhayshul Tuten","market_key":"player_rushing_yards","canonical_event_id":"d7ab040d22994748","price":1.877,"side":"under","line":53.5,"reason":"JAX RB corps ranks 8th (107.3 ypg) vs CIN's 8th-best run D vs backs (68.3 ypg allowed).","evidence_check":[{"type":"current_opponent","team":"JAX","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":8},{"type":"current_opponent","team":"CIN","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":8}]},
  {"player":"Brian Thomas Jr.","market_key":"player_receiving_yards","canonical_event_id":"d7ab040d22994748","price":1.877,"side":"under","line":26.5,"reason":"JAX WR corps ranks 11th (157.7 ypg) vs CIN's 14th-ranked WR D (140.3 ypg allowed); Thomas's own recent role has collapsed behind Washington's 30.7% target share.","evidence_check":[{"type":"current_opponent","team":"JAX","pos":"WR","stat":"rec_ypg","role":"off","claimed_rank":11},{"type":"current_opponent","team":"CIN","pos":"WR","stat":"rec_ypg","role":"def","claimed_rank":14}]},
  {"player":"Aaron Jones","market_key":"player_rushing_yards","canonical_event_id":"c2a6d9dbffca7b2e","price":1.877,"side":"over","line":67.5,"reason":"MIN RB corps ranks 15th (91.0 ypg) vs MIA's 18th-ranked run D (98.0 ypg allowed).","evidence_check":[{"type":"current_opponent","team":"MIN","pos":"RB","stat":"rush_ypg","role":"off","claimed_rank":15},{"type":"current_opponent","team":"MIA","pos":"RB","stat":"rush_ypg","role":"def","claimed_rank":18}]}
]
```

---

## SECTION 7 — FIVE FAVORITE ANYTIME TD PARLAYS

### 3-Team
- **Jahmyr Gibbs** (DET) +29 (1.294) — 90% RZ carry share, DET RB corps ranks **3rd** in rush TDs; CAR's D ranks **29th** against RB rush TDs (4 allowed).
- **Bijan Robinson** (ATL) -220 (1.455) — ATL's clear goal-line back (**5th** in rush TDs); NO's D ranks **31st** against RB rush TDs (4 allowed).
- **Derrick Henry** (BAL) -220 (1.455) — BAL RB corps leads the NFL in rush TDs (**1st**); TEN's D ranks **24th** against RB rush TDs.
- Combined price: **+174**.

```json
TD_PARLAY_3_TEAM
[
  {"player":"Jahmyr Gibbs","market_key":"player_anytime_td","canonical_event_id":"8f044a7004d58a5c","price":1.294,"side":"over","line":null,"reason":"90% RZ carry share, DET RB corps ranks 3rd in rush TDs; CAR's D ranks 29th against RB rush TDs.","evidence_check":[{"type":"current_opponent","team":"DET","pos":"RB","stat":"rush_td","role":"off","claimed_rank":3},{"type":"current_opponent","team":"CAR","pos":"RB","stat":"rush_td","role":"def","claimed_rank":29}]},
  {"player":"Bijan Robinson","market_key":"player_anytime_td","canonical_event_id":"ab7bde95c9d5a8fc","price":1.455,"side":"over","line":null,"reason":"ATL's clear goal-line back, RB corps ranks 5th in rush TDs; NO's D ranks 31st against RB rush TDs.","evidence_check":[{"type":"current_opponent","team":"ATL","pos":"RB","stat":"rush_td","role":"off","claimed_rank":5},{"type":"current_opponent","team":"NO","pos":"RB","stat":"rush_td","role":"def","claimed_rank":31}]},
  {"player":"Derrick Henry","market_key":"player_anytime_td","canonical_event_id":"ac76e69da9802c5f","price":1.455,"side":"over","line":null,"reason":"BAL RB corps leads the NFL in rush TDs (1st); TEN's D ranks 24th against RB rush TDs.","evidence_check":[{"type":"current_opponent","team":"BAL","pos":"RB","stat":"rush_td","role":"off","claimed_rank":1},{"type":"current_opponent","team":"TEN","pos":"RB","stat":"rush_td","role":"def","claimed_rank":24}]}
]
```

### 4-Team
- Adds **Christian McCaffrey** (SF) -195 — 61.5% RZ share, SF RB corps **8th** in rush TDs; DEN's D ranks **19th** vs RB rush TDs.
- Adds **Jaxon Smith-Njigba** (SEA) -115 — 50% RZ target share, SEA WR corps leads NFL in TDs (**1st**); LAC's D ranks **28th** vs WR TDs.
- Plus Gibbs and Henry from above.
- Combined price: **+433**.

```json
TD_PARLAY_4_TEAM
[
  {"player":"Christian McCaffrey","market_key":"player_anytime_td","canonical_event_id":"d5a0d1b78d351969","price":1.513,"side":"over","line":null,"reason":"61.5% RZ share, SF RB corps ranks 8th in rush TDs; DEN's D ranks 19th against RB rush TDs.","evidence_check":[{"type":"current_opponent","team":"SF","pos":"RB","stat":"rush_td","role":"off","claimed_rank":8},{"type":"current_opponent","team":"DEN","pos":"RB","stat":"rush_td","role":"def","claimed_rank":19}]},
  {"player":"Jaxon Smith-Njigba","market_key":"player_anytime_td","canonical_event_id":"53d9d3807e4d3e66","price":1.87,"side":"over","line":null,"reason":"50% RZ target share, SEA WR corps leads the league in TDs (1st); LAC's D ranks 28th against WR TDs.","evidence_check":[{"type":"current_opponent","team":"SEA","pos":"WR","stat":"td","role":"off","claimed_rank":1},{"type":"current_opponent","team":"LAC","pos":"WR","stat":"td","role":"def","claimed_rank":28}]},
  {"player":"Jahmyr Gibbs","market_key":"player_anytime_td","canonical_event_id":"8f044a7004d58a5c","price":1.294,"side":"over","line":null,"reason":"90% RZ carry share, DET RB corps ranks 3rd in rush TDs; CAR's D ranks 29th against RB rush TDs.","evidence_check":[{"type":"current_opponent","team":"DET","pos":"RB","stat":"rush_td","role":"off","claimed_rank":3},{"type":"current_opponent","team":"CAR","pos":"RB","stat":"rush_td","role":"def","claimed_rank":29}]},
  {"player":"Derrick Henry","market_key":"player_anytime_td","canonical_event_id":"ac76e69da9802c5f","price":1.455,"side":"over","line":null,"reason":"BAL RB corps leads the NFL in rush TDs (1st); TEN's D ranks 24th against RB rush TDs.","evidence_check":[{"type":"current_opponent","team":"BAL","pos":"RB","stat":"rush_td","role":"off","claimed_rank":1},{"type":"current_opponent","team":"TEN","pos":"RB","stat":"rush_td","role":"def","claimed_rank":24}]}
]
```

### 5-Team
- Adds **Chris Olave** (NO) +115 — NO's #2-ranked WR corps vs ATL's **32nd**-ranked WR yardage D (201.3 ypg allowed, most catches allowed too); ATL's TD-rate rank (7th) is a thin-sample caveat — same game as Bijan.
- Adds **Darren Waller** (CAR) +260 — 2-for-2 on RZ targets; DET's TE D ranks **32nd** (worst in the league, 6 TDs allowed) — same game as Gibbs.
- Combined price: **+2250**.

```json
TD_PARLAY_5_TEAM
[
  {"player":"Bijan Robinson","market_key":"player_anytime_td","canonical_event_id":"ab7bde95c9d5a8fc","price":1.455,"side":"over","line":null,"reason":"ATL's clear goal-line back, RB corps ranks 5th in rush TDs; NO's D ranks 31st against RB rush TDs.","evidence_check":[{"type":"current_opponent","team":"ATL","pos":"RB","stat":"rush_td","role":"off","claimed_rank":5},{"type":"current_opponent","team":"NO","pos":"RB","stat":"rush_td","role":"def","claimed_rank":31}]},
  {"player":"Chris Olave","market_key":"player_anytime_td","canonical_event_id":"ab7bde95c9d5a8fc","price":2.15,"side":"over","line":null,"reason":"NO's #2-ranked WR corps vs ATL's 32nd-ranked WR yardage D (201.3 ypg allowed); ATL's TD-rate rank (7th) is a thin-sample caveat against an otherwise historically bad unit.","evidence_check":[{"type":"current_opponent","team":"ATL","pos":"WR","stat":"rec_ypg","role":"def","claimed_rank":32}]},
  {"player":"Jahmyr Gibbs","market_key":"player_anytime_td","canonical_event_id":"8f044a7004d58a5c","price":1.294,"side":"over","line":null,"reason":"90% RZ carry share, DET RB corps ranks 3rd in rush TDs; CAR's D ranks 29th against RB rush TDs.","evidence_check":[{"type":"current_opponent","team":"DET","pos":"RB","stat":"rush_td","role":"off","claimed_rank":3},{"type":"current_opponent","team":"CAR","pos":"RB","stat":"rush_td","role":"def","claimed_rank":29}]},
  {"player":"Darren Waller","market_key":"player_anytime_td","canonical_event_id":"8f044a7004d58a5c","price":3.6,"side":"over","line":null,"reason":"2-for-2 on RZ targets; DET's TE D ranks 32nd, worst in the league (6 TDs allowed).","evidence_check":[{"type":"current_opponent","team":"DET","pos":"TE","stat":"td","role":"def","claimed_rank":32}]},
  {"player":"Derrick Henry","market_key":"player_anytime_td","canonical_event_id":"ac76e69da9802c5f","price":1.455,"side":"over","line":null,"reason":"BAL RB corps leads the NFL in rush TDs (1st); TEN's D ranks 24th against RB rush TDs.","evidence_check":[{"type":"current_opponent","team":"BAL","pos":"RB","stat":"rush_td","role":"off","claimed_rank":1},{"type":"current_opponent","team":"TEN","pos":"RB","stat":"rush_td","role":"def","claimed_rank":24}]}
]
```

### 6-Team
- Adds **George Kittle** (SF) +160 — SF TE corps **5th** in TDs; DEN's TE D ranks **12th** (moderate confidence, same game as McCaffrey) and **Travis Kelce** (KC) +160 — KC TE corps **11th** in TDs; LV's TE D ranks **30th** (5 allowed).
- Combined price: **+3500**.

```json
TD_PARLAY_6_TEAM
[
  {"player":"Christian McCaffrey","market_key":"player_anytime_td","canonical_event_id":"d5a0d1b78d351969","price":1.513,"side":"over","line":null,"reason":"61.5% RZ share, SF RB corps ranks 8th in rush TDs; DEN's D ranks 19th against RB rush TDs.","evidence_check":[{"type":"current_opponent","team":"SF","pos":"RB","stat":"rush_td","role":"off","claimed_rank":8},{"type":"current_opponent","team":"DEN","pos":"RB","stat":"rush_td","role":"def","claimed_rank":19}]},
  {"player":"George Kittle","market_key":"player_anytime_td","canonical_event_id":"d5a0d1b78d351969","price":2.6,"side":"over","line":null,"reason":"SF TE corps ranks 5th in TDs; DEN's TE D ranks 12th - tougher matchup than role alone suggests, but target share carries it.","evidence_check":[{"type":"current_opponent","team":"SF","pos":"TE","stat":"td","role":"off","claimed_rank":5},{"type":"current_opponent","team":"DEN","pos":"TE","stat":"td","role":"def","claimed_rank":12}]},
  {"player":"Jaxon Smith-Njigba","market_key":"player_anytime_td","canonical_event_id":"53d9d3807e4d3e66","price":1.87,"side":"over","line":null,"reason":"50% RZ target share, SEA WR corps leads the league in TDs (1st); LAC's D ranks 28th against WR TDs.","evidence_check":[{"type":"current_opponent","team":"SEA","pos":"WR","stat":"td","role":"off","claimed_rank":1},{"type":"current_opponent","team":"LAC","pos":"WR","stat":"td","role":"def","claimed_rank":28}]},
  {"player":"Jahmyr Gibbs","market_key":"player_anytime_td","canonical_event_id":"8f044a7004d58a5c","price":1.294,"side":"over","line":null,"reason":"90% RZ carry share, DET RB corps ranks 3rd in rush TDs; CAR's D ranks 29th against RB rush TDs.","evidence_check":[{"type":"current_opponent","team":"DET","pos":"RB","stat":"rush_td","role":"off","claimed_rank":3},{"type":"current_opponent","team":"CAR","pos":"RB","stat":"rush_td","role":"def","claimed_rank":29}]},
  {"player":"Derrick Henry","market_key":"player_anytime_td","canonical_event_id":"ac76e69da9802c5f","price":1.455,"side":"over","line":null,"reason":"BAL RB corps leads the NFL in rush TDs (1st); TEN's D ranks 24th against RB rush TDs.","evidence_check":[{"type":"current_opponent","team":"BAL","pos":"RB","stat":"rush_td","role":"off","claimed_rank":1},{"type":"current_opponent","team":"TEN","pos":"RB","stat":"rush_td","role":"def","claimed_rank":24}]},
  {"player":"Travis Kelce","market_key":"player_anytime_td","canonical_event_id":"82f1042cd9096ce2","price":2.6,"side":"over","line":null,"reason":"KC TE corps ranks 11th in TDs; LV's D has allowed the league's 3rd-most TE TDs (5, rank 30th).","evidence_check":[{"type":"current_opponent","team":"KC","pos":"TE","stat":"td","role":"off","claimed_rank":11},{"type":"current_opponent","team":"LV","pos":"TE","stat":"td","role":"def","claimed_rank":30}]}
]
```

### 7-Team
- Adds **Trey McBride** (ARI) +150 — ARI TE corps **6th** in TDs; NYG's TE D ranks **16th** and **Isaiah Likely** (NYG) +280 — NYG TE corps **14th** in TDs; ARI's TE D ranks **18th** (same game as McBride).
- Combined price: **+22223**.

```json
TD_PARLAY_7_TEAM
[
  {"player":"Bijan Robinson","market_key":"player_anytime_td","canonical_event_id":"ab7bde95c9d5a8fc","price":1.455,"side":"over","line":null,"reason":"ATL's clear goal-line back, RB corps ranks 5th in rush TDs; NO's D ranks 31st against RB rush TDs.","evidence_check":[{"type":"current_opponent","team":"ATL","pos":"RB","stat":"rush_td","role":"off","claimed_rank":5},{"type":"current_opponent","team":"NO","pos":"RB","stat":"rush_td","role":"def","claimed_rank":31}]},
  {"player":"Chris Olave","market_key":"player_anytime_td","canonical_event_id":"ab7bde95c9d5a8fc","price":2.15,"side":"over","line":null,"reason":"NO's #2-ranked WR corps vs ATL's 32nd-ranked WR yardage D (201.3 ypg allowed); ATL's TD-rate rank (7th) is a thin-sample caveat.","evidence_check":[{"type":"current_opponent","team":"ATL","pos":"WR","stat":"rec_ypg","role":"def","claimed_rank":32}]},
  {"player":"Jahmyr Gibbs","market_key":"player_anytime_td","canonical_event_id":"8f044a7004d58a5c","price":1.294,"side":"over","line":null,"reason":"90% RZ carry share, DET RB corps ranks 3rd in rush TDs; CAR's D ranks 29th against RB rush TDs.","evidence_check":[{"type":"current_opponent","team":"DET","pos":"RB","stat":"rush_td","role":"off","claimed_rank":3},{"type":"current_opponent","team":"CAR","pos":"RB","stat":"rush_td","role":"def","claimed_rank":29}]},
  {"player":"Darren Waller","market_key":"player_anytime_td","canonical_event_id":"8f044a7004d58a5c","price":3.6,"side":"over","line":null,"reason":"2-for-2 on RZ targets; DET's TE D ranks 32nd, worst in the league (6 TDs allowed).","evidence_check":[{"type":"current_opponent","team":"DET","pos":"TE","stat":"td","role":"def","claimed_rank":32}]},
  {"player":"Derrick Henry","market_key":"player_anytime_td","canonical_event_id":"ac76e69da9802c5f","price":1.455,"side":"over","line":null,"reason":"BAL RB corps leads the NFL in rush TDs (1st); TEN's D ranks 24th against RB rush TDs.","evidence_check":[{"type":"current_opponent","team":"BAL","pos":"RB","stat":"rush_td","role":"off","claimed_rank":1},{"type":"current_opponent","team":"TEN","pos":"RB","stat":"rush_td","role":"def","claimed_rank":24}]},
  {"player":"Trey McBride","market_key":"player_anytime_td","canonical_event_id":"fefdcc7bd476a375","price":2.5,"side":"over","line":null,"reason":"ARI TE corps ranks 6th in TDs; NYG's TE D ranks 16th.","evidence_check":[{"type":"current_opponent","team":"ARI","pos":"TE","stat":"td","role":"off","claimed_rank":6},{"type":"current_opponent","team":"NYG","pos":"TE","stat":"td","role":"def","claimed_rank":16}]},
  {"player":"Isaiah Likely","market_key":"player_anytime_td","canonical_event_id":"fefdcc7bd476a375","price":3.8,"side":"over","line":null,"reason":"NYG TE corps ranks 14th in TDs; ARI's TE D ranks 18th.","evidence_check":[{"type":"current_opponent","team":"NYG","pos":"TE","stat":"td","role":"off","claimed_rank":14},{"type":"current_opponent","team":"ARI","pos":"TE","stat":"td","role":"def","claimed_rank":18}]}
]
```

---

## SECTION 8 — FIVE FAVORITE SPREAD PARLAYS

### 3-Team
- **DET -3.5** -118 (CAR/DET) — DET is **60.4%** ATS overall, **61.5%** ATS on the road; offense ranks **3rd** in ppg (31.0) vs CAR's **26th**-ranked scoring D (27.7 allowed).
- **LAR -3.0** -115 (LAR/PHI) — LAR is **54.9%** ATS overall, **54.0%** on the road; LAR's offense ranks **1st** in total yds/gm (428.7) vs PHI's offense ranked just **23rd** in ppg (18.3).
- **ARI -2.5** -110 (ARI/NYG) — ARI is an excellent **60.4%** ATS on the road; ARI ranks **18th** in ppg (21.0) vs NYG's offense ranked **28th** (15.3 ppg).
- Combined price: **+559**.

```json
SPREAD_PARLAY_3_TEAM
[
  {"player":"Detroit Lions","market_key":"spreads","canonical_event_id":"8f044a7004d58a5c","price":1.847,"point":-3.5,"reason":"DET is 60.4% ATS overall / 61.5% on the road since 2020; offense ranks 3rd in ppg (31.0) vs CAR's 26th-ranked scoring D (27.7 allowed).","evidence_check":[{"type":"current_opponent","team":"DET","pos":"TEAM","stat":"ppg","role":"off","claimed_rank":3},{"type":"current_opponent","team":"CAR","pos":"TEAM","stat":"ppg","role":"def","claimed_rank":26}]},
  {"player":"Los Angeles Rams","market_key":"spreads","canonical_event_id":"0b88c15fb8b87a89","price":1.87,"point":-3.0,"reason":"LAR is 54.9% ATS overall / 54.0% on the road since 2020; LAR's offense ranks 1st in total yds/gm (428.7) vs PHI's offense ranked 23rd in ppg (18.3).","evidence_check":[{"type":"current_opponent","team":"LAR","pos":"TEAM","stat":"total_ypg","role":"off","claimed_rank":1},{"type":"current_opponent","team":"PHI","pos":"TEAM","stat":"ppg","role":"off","claimed_rank":23}]},
  {"player":"Arizona Cardinals","market_key":"spreads","canonical_event_id":"fefdcc7bd476a375","price":1.909,"point":-2.5,"reason":"ARI is 60.4% ATS on the road since 2020; ARI ranks 18th in ppg (21.0) vs NYG's offense ranked 28th (15.3 ppg).","evidence_check":[{"type":"current_opponent","team":"ARI","pos":"TEAM","stat":"ppg","role":"off","claimed_rank":18},{"type":"current_opponent","team":"NYG","pos":"TEAM","stat":"ppg","role":"off","claimed_rank":28}]}
]
```

### 4-Team
- Adds **PIT -2.5** -120 (PIT/CLE) — PIT is **58.8%** ATS overall, **56.0%** on the road; defense ranks **11th** in points allowed (20.0) vs CLE's offense ranked **24th** (18.0 ppg).
- Adds **IND -3.5** -110 (IND/WAS) — IND is **56.9%** ATS on the road; offense ranks **15th** in ppg (24.0) vs WAS's defense ranked **31st** (30.7 allowed, 2nd-worst in the league).
- Combined price: **+1109**.

```json
SPREAD_PARLAY_4_TEAM
[
  {"player":"Pittsburgh Steelers","market_key":"spreads","canonical_event_id":"1c79ffc934ef3e24","price":1.833,"point":-2.5,"reason":"PIT is 58.8% ATS overall / 56.0% on the road; defense ranks 11th in points allowed (20.0) vs CLE's offense ranked 24th (18.0 ppg).","evidence_check":[{"type":"current_opponent","team":"PIT","pos":"TEAM","stat":"ppg","role":"def","claimed_rank":11},{"type":"current_opponent","team":"CLE","pos":"TEAM","stat":"ppg","role":"off","claimed_rank":24}]},
  {"player":"Indianapolis Colts","market_key":"spreads","canonical_event_id":"b9550fb6e56e66e2","price":1.909,"point":-3.5,"reason":"IND is 56.9% ATS on the road since 2020; offense ranks 15th in ppg (24.0) vs WAS's defense ranked 31st (30.7 allowed).","evidence_check":[{"type":"current_opponent","team":"IND","pos":"TEAM","stat":"ppg","role":"off","claimed_rank":15},{"type":"current_opponent","team":"WAS","pos":"TEAM","stat":"ppg","role":"def","claimed_rank":31}]},
  {"player":"Detroit Lions","market_key":"spreads","canonical_event_id":"8f044a7004d58a5c","price":1.847,"point":-3.5,"reason":"DET is 60.4% ATS overall / 61.5% on the road; offense ranks 3rd in ppg (31.0) vs CAR's 26th-ranked scoring D (27.7 allowed).","evidence_check":[{"type":"current_opponent","team":"DET","pos":"TEAM","stat":"ppg","role":"off","claimed_rank":3},{"type":"current_opponent","team":"CAR","pos":"TEAM","stat":"ppg","role":"def","claimed_rank":26}]},
  {"player":"Los Angeles Rams","market_key":"spreads","canonical_event_id":"0b88c15fb8b87a89","price":1.87,"point":-3.0,"reason":"LAR is 54.9% ATS overall / 54.0% on the road; LAR's offense ranks 1st in total yds/gm (428.7) vs PHI's offense ranked 23rd in ppg (18.3).","evidence_check":[{"type":"current_opponent","team":"LAR","pos":"TEAM","stat":"total_ypg","role":"off","claimed_rank":1},{"type":"current_opponent","team":"PHI","pos":"TEAM","stat":"ppg","role":"off","claimed_rank":23}]}
]
```

### 5-Team
- Adds **MIN -10.5** -115 (MIA/MIN) — MIN defense ranks **2nd** in points allowed (13.7); MIA's offense ranks dead last (**31st**, 12.0 ppg) and is 0-3 — MIN's home ATS (47.1%) is a mild caution.
- Adds **DAL +3.0** -110 (DAL/HOU) — DAL is **51.0%** ATS overall; offense ranks **7th** in ppg (29.3) vs winless (0-3) HOU's offense ranked **25th** (18.0 ppg).
- Combined price: **+2208**.

```json
SPREAD_PARLAY_5_TEAM
[
  {"player":"Minnesota Vikings","market_key":"spreads","canonical_event_id":"c2a6d9dbffca7b2e","price":1.87,"point":-10.5,"reason":"MIN defense ranks 2nd in points allowed (13.7); MIA's offense ranks dead last (31st, 12.0 ppg) and is 0-3; MIN's home ATS (47.1%) is a mild caution against laying double digits.","evidence_check":[{"type":"current_opponent","team":"MIN","pos":"TEAM","stat":"ppg","role":"def","claimed_rank":2},{"type":"current_opponent","team":"MIA","pos":"TEAM","stat":"ppg","role":"off","claimed_rank":31}]},
  {"player":"Dallas Cowboys","market_key":"spreads","canonical_event_id":"0eae1db34049745a","price":1.909,"point":3.0,"reason":"DAL is 51.0% ATS overall since 2020; offense ranks 7th in ppg (29.3) vs winless HOU's offense ranked 25th (18.0 ppg).","evidence_check":[{"type":"current_opponent","team":"DAL","pos":"TEAM","stat":"ppg","role":"off","claimed_rank":7},{"type":"current_opponent","team":"HOU","pos":"TEAM","stat":"ppg","role":"off","claimed_rank":25}]},
  {"player":"Arizona Cardinals","market_key":"spreads","canonical_event_id":"fefdcc7bd476a375","price":1.909,"point":-2.5,"reason":"ARI is 60.4% ATS on the road since 2020; ARI ranks 18th in ppg (21.0) vs NYG's offense ranked 28th (15.3 ppg).","evidence_check":[{"type":"current_opponent","team":"ARI","pos":"TEAM","stat":"ppg","role":"off","claimed_rank":18},{"type":"current_opponent","team":"NYG","pos":"TEAM","stat":"ppg","role":"off","claimed_rank":28}]},
  {"player":"Pittsburgh Steelers","market_key":"spreads","canonical_event_id":"1c79ffc934ef3e24","price":1.833,"point":-2.5,"reason":"PIT is 58.8% ATS overall / 56.0% on the road; defense ranks 11th in points allowed (20.0) vs CLE's offense ranked 24th (18.0 ppg).","evidence_check":[{"type":"current_opponent","team":"PIT","pos":"TEAM","stat":"ppg","role":"def","claimed_rank":11},{"type":"current_opponent","team":"CLE","pos":"TEAM","stat":"ppg","role":"off","claimed_rank":24}]},
  {"player":"Detroit Lions","market_key":"spreads","canonical_event_id":"8f044a7004d58a5c","price":1.847,"point":-3.5,"reason":"DET is 60.4% ATS overall / 61.5% on the road; offense ranks 3rd in ppg (31.0) vs CAR's 26th-ranked scoring D (27.7 allowed).","evidence_check":[{"type":"current_opponent","team":"DET","pos":"TEAM","stat":"ppg","role":"off","claimed_rank":3},{"type":"current_opponent","team":"CAR","pos":"TEAM","stat":"ppg","role":"def","claimed_rank":26}]}
]
```

### 6-Team
- Adds **LV +4.5** -108 (KC/LV) — LV is 3-0 and **54.9%** ATS at home; LV ranks **9th** in ppg (29.3) and **8th** in points allowed (18.0) — a legitimately competitive team getting points.
- Adds **JAX +2.5** -108 (JAX/CIN) — JAX defense ranks **1st** in points allowed (12.0); CIN's offense ranks just **12th** in ppg (26.7) — the elite JAX defense is the stronger real signal here despite CIN's 54.2% home ATS mark.
- Adds **NE +6.5** +100 (NE/BUF) — NE defense ranks **6th** in points allowed (17.0) and **6th** in pass yards allowed; BUF's own defense ranks **22nd** in points allowed and **28th** in pass yards allowed — this projects closer than 6.5.
- Adds **TB +3.5** -110 (GB/TB) — GB is just **44.2%** ATS on the road; TB's defense ranks **23rd** in points allowed vs GB's offense ranked **22nd** in ppg — near-even, take the home points.
- Combined price: **+4853**.

```json
SPREAD_PARLAY_6_TEAM
[
  {"player":"Las Vegas Raiders","market_key":"spreads","canonical_event_id":"82f1042cd9096ce2","price":1.926,"point":4.5,"reason":"LV is 3-0 and 54.9% ATS at home since 2020; offense ranks 9th in ppg (29.3) and defense ranks 8th in points allowed (18.0).","evidence_check":[{"type":"current_opponent","team":"LV","pos":"TEAM","stat":"ppg","role":"off","claimed_rank":9},{"type":"current_opponent","team":"LV","pos":"TEAM","stat":"ppg","role":"def","claimed_rank":8}]},
  {"player":"Jacksonville Jaguars","market_key":"spreads","canonical_event_id":"d7ab040d22994748","price":1.926,"point":2.5,"reason":"JAX defense ranks 1st in the league in points allowed (12.0); CIN's offense ranks just 12th in ppg (26.7) despite CIN's 54.2% home ATS mark.","evidence_check":[{"type":"current_opponent","team":"JAX","pos":"TEAM","stat":"ppg","role":"def","claimed_rank":1},{"type":"current_opponent","team":"CIN","pos":"TEAM","stat":"ppg","role":"off","claimed_rank":12}]},
  {"player":"New England Patriots","market_key":"spreads","canonical_event_id":"5a6a506f9ff2a30f","price":2.0,"point":6.5,"reason":"NE defense ranks 6th in points allowed (17.0) and 6th in pass yards allowed; BUF's own defense ranks just 22nd in points allowed and 28th in pass yards allowed.","evidence_check":[{"type":"current_opponent","team":"NE","pos":"TEAM","stat":"ppg","role":"def","claimed_rank":6},{"type":"current_opponent","team":"BUF","pos":"TEAM","stat":"ppg","role":"def","claimed_rank":22}]},
  {"player":"Tampa Bay Buccaneers","market_key":"spreads","canonical_event_id":"a223ecde7f6e4844","price":1.909,"point":3.5,"reason":"GB is just 44.2% ATS on the road since 2020; TB's defense ranks 23rd in points allowed vs GB's offense ranked 22nd in ppg - a near-even matchup, take the home points.","evidence_check":[{"type":"current_opponent","team":"GB","pos":"TEAM","stat":"ppg","role":"off","claimed_rank":22},{"type":"current_opponent","team":"TB","pos":"TEAM","stat":"ppg","role":"def","claimed_rank":23}]},
  {"player":"Minnesota Vikings","market_key":"spreads","canonical_event_id":"c2a6d9dbffca7b2e","price":1.87,"point":-10.5,"reason":"MIN defense ranks 2nd in points allowed (13.7); MIA's offense ranks dead last (31st, 12.0 ppg) and is 0-3.","evidence_check":[{"type":"current_opponent","team":"MIN","pos":"TEAM","stat":"ppg","role":"def","claimed_rank":2},{"type":"current_opponent","team":"MIA","pos":"TEAM","stat":"ppg","role":"off","claimed_rank":31}]},
  {"player":"Los Angeles Rams","market_key":"spreads","canonical_event_id":"0b88c15fb8b87a89","price":1.87,"point":-3.0,"reason":"LAR is 54.9% ATS overall / 54.0% on the road; LAR's offense ranks 1st in total yds/gm (428.7) vs PHI's offense ranked 23rd in ppg (18.3).","evidence_check":[{"type":"current_opponent","team":"LAR","pos":"TEAM","stat":"total_ypg","role":"off","claimed_rank":1},{"type":"current_opponent","team":"PHI","pos":"TEAM","stat":"ppg","role":"off","claimed_rank":23}]}
]
```

### 7-Team
- Adds **ATL +2.5** -104 (ATL/NO) — NO is just **41.2%** ATS at home; ATL defense ranks **1st** against the run (47.7 ypg allowed) and can keep this low-scoring against a NO team ranked **11th** in ppg but **27th** in points allowed.
- Combined price: **+9500**.

```json
SPREAD_PARLAY_7_TEAM
[
  {"player":"Atlanta Falcons","market_key":"spreads","canonical_event_id":"ab7bde95c9d5a8fc","price":1.962,"point":2.5,"reason":"NO is just 41.2% ATS at home since 2020; ATL's defense ranks 1st in the league against the run (47.7 ypg allowed), facing a NO offense ranked 11th in ppg (27.0) but 27th in points allowed (27.7).","evidence_check":[{"type":"current_opponent","team":"ATL","pos":"TEAM","stat":"rush_ypg","role":"def","claimed_rank":1},{"type":"current_opponent","team":"NO","pos":"TEAM","stat":"ppg","role":"off","claimed_rank":11}]},
  {"player":"Las Vegas Raiders","market_key":"spreads","canonical_event_id":"82f1042cd9096ce2","price":1.926,"point":4.5,"reason":"LV is 3-0 and 54.9% ATS at home since 2020; offense ranks 9th in ppg (29.3) and defense ranks 8th in points allowed (18.0).","evidence_check":[{"type":"current_opponent","team":"LV","pos":"TEAM","stat":"ppg","role":"off","claimed_rank":9},{"type":"current_opponent","team":"LV","pos":"TEAM","stat":"ppg","role":"def","claimed_rank":8}]},
  {"player":"Jacksonville Jaguars","market_key":"spreads","canonical_event_id":"d7ab040d22994748","price":1.926,"point":2.5,"reason":"JAX defense ranks 1st in the league in points allowed (12.0); CIN's offense ranks just 12th in ppg (26.7).","evidence_check":[{"type":"current_opponent","team":"JAX","pos":"TEAM","stat":"ppg","role":"def","claimed_rank":1},{"type":"current_opponent","team":"CIN","pos":"TEAM","stat":"ppg","role":"off","claimed_rank":12}]},
  {"player":"New England Patriots","market_key":"spreads","canonical_event_id":"5a6a506f9ff2a30f","price":2.0,"point":6.5,"reason":"NE defense ranks 6th in points allowed (17.0) and 6th in pass yards allowed; BUF's own defense ranks just 22nd in points allowed and 28th in pass yards allowed.","evidence_check":[{"type":"current_opponent","team":"NE","pos":"TEAM","stat":"ppg","role":"def","claimed_rank":6},{"type":"current_opponent","team":"BUF","pos":"TEAM","stat":"ppg","role":"def","claimed_rank":22}]},
  {"player":"Tampa Bay Buccaneers","market_key":"spreads","canonical_event_id":"a223ecde7f6e4844","price":1.909,"point":3.5,"reason":"GB is just 44.2% ATS on the road since 2020; TB's defense ranks 23rd in points allowed vs GB's offense ranked 22nd in ppg.","evidence_check":[{"type":"current_opponent","team":"GB","pos":"TEAM","stat":"ppg","role":"off","claimed_rank":22},{"type":"current_opponent","team":"TB","pos":"TEAM","stat":"ppg","role":"def","claimed_rank":23}]},
  {"player":"Minnesota Vikings","market_key":"spreads","canonical_event_id":"c2a6d9dbffca7b2e","price":1.87,"point":-10.5,"reason":"MIN defense ranks 2nd in points allowed (13.7); MIA's offense ranks dead last (31st, 12.0 ppg) and is 0-3.","evidence_check":[{"type":"current_opponent","team":"MIN","pos":"TEAM","stat":"ppg","role":"def","claimed_rank":2},{"type":"current_opponent","team":"MIA","pos":"TEAM","stat":"ppg","role":"off","claimed_rank":31}]},
  {"player":"Detroit Lions","market_key":"spreads","canonical_event_id":"8f044a7004d58a5c","price":1.847,"point":-3.5,"reason":"DET is 60.4% ATS overall / 61.5% on the road; offense ranks 3rd in ppg (31.0) vs CAR's 26th-ranked scoring D (27.7 allowed).","evidence_check":[{"type":"current_opponent","team":"DET","pos":"TEAM","stat":"ppg","role":"off","claimed_rank":3},{"type":"current_opponent","team":"CAR","pos":"TEAM","stat":"ppg","role":"def","claimed_rank":26}]}
]
```

---

**Same-game disclosure summary:** Section 6 parlays contain multiple same-game leg pairs (flagged individually above in each parlay's notes) — their combined prices are cross-market estimates, not real FanDuel SGP quotes. Section 7 TD parlays similarly stack same-game legs where noted (DET/CAR, ATL/NO, DEN/SF, ARI/NYG pairs). Section 8 spread parlays contain no same-game legs by construction (one spread per game, no team picked twice).