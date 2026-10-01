# COEUS PROPS & PARLAY REPORT — WEEK 4

**Data Coverage Note:** All five stat families (passing/rushing/receiving yards, receptions, anytime TD) are LIVE league-wide. However, **TEN @ BAL has zero real FanDuel player-prop or anytime-TD data for this specific game** — only game lines (spread, total, moneyline) are posted. No prop picks are made for that game anywhere below; this is stated plainly rather than padded or invented. Mainline spreads exist for all four games.

---

## SECTION 4 — COEUS PROP BREAKDOWN

### PIT @ CLE (3 picks)

- **Jaylen Warren (PIT)** — Rushing Yards, Over 67.5, **-114**. Warren's own 72.0 rush yds/gm ranks 8th among RBs; Cleveland allows 106.0 rush yds/gm to backs, ranked 24th (bottom tier) — this exact convergence is what fired PIT's Standard-tier Threat. Division game (CLE/PIT play twice) but no 2026 head-to-head exists yet for either side. Confidence: MEDIUM.
- **Pat Freiermuth (PIT)** — Receiving Yards, Over 28.5, **-114**. Freiermuth's 36.0 rec yds/gm; Cleveland's TE defense allows 66.0 rec yds/gm, ranked 24th (bottom tier) — plus Pittsburgh's extreme pass-heavy red-zone identity (70.6% pass rate, 2nd-most) keeps his RZ role live. Confidence: MEDIUM.
- **Aaron Rodgers (PIT)** — Passing Yards, Under 212.5, **-114**. Rodgers' own 233.3 pass yds/gm ranks 16th, but Cleveland's pass defense allows just 211.0 yds/gm, ranked 10th (genuinely tougher than average) — and his lone top-tier-matchup game this year (187 yds at NE) sits well under this line. Confidence: MEDIUM.

### IND @ WAS (3 picks)

- **Josh Downs (IND)** — Receiving Yards, Over 64.5, **-114**. Downs' own 62.0 rec yds/gm ranks 19th; Washington allows 191.0 rec yds/gm to WRs, ranked 30th, and the most catches allowed to the position in the league (32nd) — the Threat Engine's own closest near-miss this week. Confidence: MEDIUM.
- **Jonathan Taylor (IND)** — Rushing Yards, Under 90.5, **-114**. Taylor's own 86.0 rush yds/gm ranks 6th, but Washington allows just 56.0 rush yds/gm to backs, ranked 3rd (elite) — the stiffest run funnel he's faced in 2026. The alt ladder for this market is Over-priced only, so there's no Under-side alternate to this 90.5 line. Confidence: MEDIUM.
- **Tyler Warren (IND)** — Receptions, Over 5.5, **-102**. Warren catches 6.0 passes/gm, ranked 3rd among TEs; Washington allows 6.7 receptions/gm to tight ends, ranked 27th (bottom tier) — elite target volume into a leaky underneath defense. Confidence: MEDIUM.

### TEN @ BAL

- **No real prop data exists for this game.** FanDuel's data feed returned empty `player_props` and an empty `anytime_td` array for this specific matchup — only the spread/total/moneyline are posted. No picks are made here; this is a genuine data gap, not an omission.

### NE @ BUF (3 picks)

- **James Cook (BUF)** — Rushing Yards, Over 87.5, **-114**. Cook's 115.33 rush yds/gm ranks 3rd; New England's run defense allows 92.3 rush yds/gm to backs, ranked 16th (mid tier) — his most directly comparable 2026 game (vs a similarly mid-ranked Detroit front) produced 135 yards. Division game; no 2026 head-to-head exists yet for either side. Confidence: MEDIUM.
- **Dalton Kincaid (BUF)** — Receiving Yards, Under 52.5, **-114**. Kincaid's 87.67 rec yds/gm ranks top of the position this year, but New England's TE defense allows just 28.0 rec yds/gm, ranked 4th (elite) — a defensive caliber he has no 2026 data point against yet. Alt ladder here is Over-only; no Under alternate exists. Confidence: MEDIUM.
- **Josh Allen (BUF)** — Passing Yards, Under 242.5, **-114**. Allen's 262.0 pass yds/gm ranks 9th, but New England's pass defense allows only 189.7 yds/gm, ranked 6th (elite) — the toughest pass defense he's seen this season. Alt ladder is Over-only. Confidence: MEDIUM.

### League-Wide Favorite by Position

- **QB: Daniel Jones (IND)** — Passing Yards, Over 224.5, **-114**. Jones' own 203.7 pass yds/gm ranks 22nd, but Washington's pass defense allows 287.0 yds/gm, ranked 31st (worst in the league) — the gap carries the pick even with a modest individual rate. Confidence: MEDIUM.
- **RB: Jonathan Taylor (IND)** — Rushing Yards, Under 90.5, **-114**. Same evidence as above (Taylor own rank 6th vs WAS run D rank 3rd). Confidence: MEDIUM.
- **WR: Josh Downs (IND)** — Receiving Yards, Over 64.5, **-114**. Same evidence as above. Confidence: MEDIUM.
- **TE: Tyler Warren (IND)** — Receiving Yards, Over 46.5, **-114**. Warren's 29.7 rec yds/gm ranks 19th; Washington's TE defense allows 67.3 rec yds/gm, ranked 26th (bottom tier) — reinforced by his 3rd-ranked reception volume. Confidence: MEDIUM.

```json
PROP_BREAKDOWN
{
  "per_game": [
    {"away": "PIT", "home": "CLE", "picks": [
      {"player": "Jaylen Warren", "market_key": "player_rushing_yards", "canonical_event_id": "1c79ffc934ef3e24", "price": 1.877, "side": "over", "line": 67.5, "reason": "Warren's 72.0 rush yds/gm ranks 8th among RBs; CLE allows 106.0 rush yds/gm to backs, ranked 24th — the exact convergence behind PIT's Standard-tier Threat.", "evidence_check": [{"type":"current_opponent","team":"CLE","pos":"RB","stat":"rush_yds","role":"def","claimed_rank":24}]},
      {"player": "Pat Freiermuth", "market_key": "player_receiving_yards", "canonical_event_id": "1c79ffc934ef3e24", "price": 1.877, "side": "over", "line": 28.5, "reason": "Freiermuth's 36.0 rec yds/gm; CLE's TE defense allows 66.0 rec yds/gm, ranked 24th, with PIT's red zone staying pass-heavy.", "evidence_check": [{"type":"current_opponent","team":"CLE","pos":"TE","stat":"rec_yds","role":"def","claimed_rank":24}]},
      {"player": "Aaron Rodgers", "market_key": "player_passing_yards", "canonical_event_id": "1c79ffc934ef3e24", "price": 1.877, "side": "under", "line": 212.5, "reason": "Rodgers' 233.3 pass yds/gm ranks 16th, but CLE's pass defense allows only 211.0 yds/gm, ranked 10th — tougher than his season rate suggests.", "evidence_check": [{"type":"current_opponent","team":"CLE","pos":"QB","stat":"pass_yds","role":"def","claimed_rank":10}]}
    ]},
    {"away": "IND", "home": "WAS", "picks": [
      {"player": "Josh Downs", "market_key": "player_receiving_yards", "canonical_event_id": "b9550fb6e56e66e2", "price": 1.877, "side": "over", "line": 64.5, "reason": "Downs' 62.0 rec yds/gm ranks 19th; WAS allows 191.0 rec yds/gm to WRs, ranked 30th, and the most catches allowed to the position (32nd).", "evidence_check": [{"type":"current_opponent","team":"WAS","pos":"WR","stat":"rec_yds","role":"def","claimed_rank":30}]},
      {"player": "Jonathan Taylor", "market_key": "player_rushing_yards", "canonical_event_id": "b9550fb6e56e66e2", "price": 1.877, "side": "under", "line": 90.5, "reason": "Taylor's 86.0 rush yds/gm ranks 6th, but WAS allows just 56.0 rush yds/gm to backs, ranked 3rd — his stiffest run funnel this year.", "evidence_check": [{"type":"current_opponent","team":"WAS","pos":"RB","stat":"rush_yds","role":"def","claimed_rank":3}]},
      {"player": "Tyler Warren", "market_key": "player_receptions", "canonical_event_id": "b9550fb6e56e66e2", "price": 1.98, "side": "over", "line": 5.5, "reason": "Warren catches 6.0/gm, ranked 3rd among TEs; WAS allows 6.7 receptions/gm to TEs, ranked 27th.", "evidence_check": [{"type":"current_opponent","team":"WAS","pos":"TE","stat":"rec","role":"def","claimed_rank":27}]}
    ]},
    {"away": "NE", "home": "BUF", "picks": [
      {"player": "James Cook", "market_key": "player_rushing_yards", "canonical_event_id": "5a6a506f9ff2a30f", "price": 1.877, "side": "over", "line": 87.5, "reason": "Cook's 115.33 rush yds/gm ranks 3rd; NE's run defense allows 92.3 rush yds/gm to backs, ranked 16th — a mid-tier matchup he's already handled well.", "evidence_check": [{"type":"current_opponent","team":"NE","pos":"RB","stat":"rush_yds","role":"def","claimed_rank":16}]},
      {"player": "Dalton Kincaid", "market_key": "player_receiving_yards", "canonical_event_id": "5a6a506f9ff2a30f", "price": 1.877, "side": "under", "line": 52.5, "reason": "Kincaid's 87.67 rec yds/gm this year, but NE's TE defense allows just 28.0 rec yds/gm, ranked 4th — a caliber he hasn't faced in 2026 yet.", "evidence_check": [{"type":"current_opponent","team":"NE","pos":"TE","stat":"rec_yds","role":"def","claimed_rank":4}]},
      {"player": "Josh Allen", "market_key": "player_passing_yards", "canonical_event_id": "5a6a506f9ff2a30f", "price": 1.877, "side": "under", "line": 242.5, "reason": "Allen's 262.0 pass yds/gm ranks 9th, but NE's pass defense allows only 189.7 yds/gm, ranked 6th — his toughest test of the season.", "evidence_check": [{"type":"current_opponent","team":"NE","pos":"QB","stat":"pass_yds","role":"def","claimed_rank":6}]}
    ]}
  ],
  "per_position": {
    "QB": {"player": "Daniel Jones", "market_key": "player_passing_yards", "canonical_event_id": "b9550fb6e56e66e2", "price": 1.877, "side": "over", "line": 224.5, "reason": "Jones' 203.7 pass yds/gm ranks 22nd, but WAS allows 287.0 pass yds/gm, ranked 31st — the worst pass defense in the league.", "evidence_check": [{"type":"current_opponent","team":"WAS","pos":"QB","stat":"pass_yds","role":"def","claimed_rank":31}]},
    "RB": {"player": "Jonathan Taylor", "market_key": "player_rushing_yards", "canonical_event_id": "b9550fb6e56e66e2", "price": 1.877, "side": "under", "line": 90.5, "reason": "Taylor's 86.0 rush yds/gm ranks 6th, but WAS allows just 56.0 rush yds/gm to backs, ranked 3rd — elite run funnel.", "evidence_check": [{"type":"current_opponent","team":"WAS","pos":"RB","stat":"rush_yds","role":"def","claimed_rank":3}]},
    "WR": {"player": "Josh Downs", "market_key": "player_receiving_yards", "canonical_event_id": "b9550fb6e56e66e2", "price": 1.877, "side": "over", "line": 64.5, "reason": "Downs' 62.0 rec yds/gm ranks 19th; WAS allows 191.0 rec yds/gm to WRs, ranked 30th.", "evidence_check": [{"type":"current_opponent","team":"WAS","pos":"WR","stat":"rec_yds","role":"def","claimed_rank":30}]},
    "TE": {"player": "Tyler Warren", "market_key": "player_receiving_yards", "canonical_event_id": "b9550fb6e56e66e2", "price": 1.877, "side": "over", "line": 46.5, "reason": "Warren's 29.7 rec yds/gm ranks 19th; WAS allows 67.3 rec yds/gm to TEs, ranked 26th, reinforced by his 3rd-ranked reception volume.", "evidence_check": [{"type":"current_opponent","team":"WAS","pos":"TE","stat":"rec_yds","role":"def","claimed_rank":26}]}
  }
}
```

---

## SECTION 5 — FAVORITE OVERS AND UNDERS FOR THE WEEK

**Overs (ranked):**
1. **Josh Downs** Over 64.5 rec yds, **-114** — WAS allows the most WR catches (32nd) and 30th-ranked WR yardage in the league.
2. **James Cook** Over 87.5 rush yds, **-114** — elite volume (64.4% rush share) vs a mid-tier NE front.
3. **Jaylen Warren** Over 67.5 rush yds, **-114** — Threat-confirmed matchup edge vs CLE's 24th-ranked RB run defense.
4. **Pat Freiermuth** Over 28.5 rec yds, **-114** — CLE's 24th-ranked TE defense meets a real red-zone role.
5. **Pat Freiermuth** Anytime TD, **+360** — 16.7% red-zone target share on PIT's most pass-heavy red-zone offense in the league; CLE's TE touchdown defense is only mid-tier (11th), so this is a lower-conviction lean. Confidence: LOW.

**Unders (ranked):**
1. **Jonathan Taylor** Under 90.5 rush yds, **-114** — WAS's run D ranks 3rd (elite) against backs. Alt ladder is Over-only.
2. **Josh Allen** Under 242.5 pass yds, **-114** — NE's pass D ranks 6th (elite), his toughest test this year. Alt ladder is Over-only.
3. **Dalton Kincaid** Under 52.5 rec yds, **-114** — NE's TE D ranks 4th (elite) against a role he hasn't tested that caliber against yet. Alt ladder is Over-only.
4. **Aaron Rodgers** Under 212.5 pass yds, **-114** — CLE's pass D ranks 10th, genuinely tougher than his season rate. Alt ladder is Over-only.

```json
FAVORITE_OU
{
  "overs": [
    {"player": "Josh Downs", "market_key": "player_receiving_yards", "canonical_event_id": "b9550fb6e56e66e2", "price": 1.877, "side": "over", "line": 64.5, "reason": "WAS allows the most WR catches in the league (32nd) and ranks 30th in WR yardage allowed.", "evidence_check": [{"type":"current_opponent","team":"WAS","pos":"WR","stat":"rec_yds","role":"def","claimed_rank":30}]},
    {"player": "James Cook", "market_key": "player_rushing_yards", "canonical_event_id": "5a6a506f9ff2a30f", "price": 1.877, "side": "over", "line": 87.5, "reason": "Elite 64.4% rush share into a mid-tier (16th) NE run defense.", "evidence_check": [{"type":"current_opponent","team":"NE","pos":"RB","stat":"rush_yds","role":"def","claimed_rank":16}]},
    {"player": "Jaylen Warren", "market_key": "player_rushing_yards", "canonical_event_id": "1c79ffc934ef3e24", "price": 1.877, "side": "over", "line": 67.5, "reason": "Threat-confirmed convergence vs CLE's 24th-ranked RB run defense.", "evidence_check": [{"type":"current_opponent","team":"CLE","pos":"RB","stat":"rush_yds","role":"def","claimed_rank":24}]},
    {"player": "Pat Freiermuth", "market_key": "player_receiving_yards", "canonical_event_id": "1c79ffc934ef3e24", "price": 1.877, "side": "over", "line": 28.5, "reason": "CLE's 24th-ranked TE defense meets a real red-zone role for Freiermuth.", "evidence_check": [{"type":"current_opponent","team":"CLE","pos":"TE","stat":"rec_yds","role":"def","claimed_rank":24}]},
    {"player": "Pat Freiermuth", "market_key": "player_anytime_td", "canonical_event_id": "1c79ffc934ef3e24", "price": 4.6, "side": "over", "line": null, "reason": "16.7% red-zone target share on PIT's most pass-heavy red-zone offense; CLE's TE TD defense is only mid-tier (11th).", "evidence_check": [{"type":"current_opponent","team":"CLE","pos":"TE","stat":"td","role":"def","claimed_rank":11}]}
  ],
  "unders": [
    {"player": "Jonathan Taylor", "market_key": "player_rushing_yards", "canonical_event_id": "b9550fb6e56e66e2", "price": 1.877, "side": "under", "line": 90.5, "reason": "WAS run D ranks 3rd (elite) against backs.", "evidence_check": [{"type":"current_opponent","team":"WAS","pos":"RB","stat":"rush_yds","role":"def","claimed_rank":3}]},
    {"player": "Josh Allen", "market_key": "player_passing_yards", "canonical_event_id": "5a6a506f9ff2a30f", "price": 1.877, "side": "under", "line": 242.5, "reason": "NE pass D ranks 6th (elite), his toughest test of 2026.", "evidence_check": [{"type":"current_opponent","team":"NE","pos":"QB","stat":"pass_yds","role":"def","claimed_rank":6}]},
    {"player": "Dalton Kincaid", "market_key": "player_receiving_yards", "canonical_event_id": "5a6a506f9ff2a30f", "price": 1.877, "side": "under", "line": 52.5, "reason": "NE TE D ranks 4th (elite) against a role Kincaid hasn't tested at that caliber yet.", "evidence_check": [{"type":"current_opponent","team":"NE","pos":"TE","stat":"rec_yds","role":"def","claimed_rank":4}]},
    {"player": "Aaron Rodgers", "market_key": "player_passing_yards", "canonical_event_id": "1c79ffc934ef3e24", "price": 1.877, "side": "under", "line": 212.5, "reason": "CLE pass D ranks 10th, tougher than Rodgers' season rate suggests.", "evidence_check": [{"type":"current_opponent","team":"CLE","pos":"QB","stat":"pass_yds","role":"def","claimed_rank":10}]}
  ]
}
```

---

## SECTION 6 — FIVE LINE-BASED PARLAYS

**3-Team** — Warren Over, Cook Over, Downs Over. All three legs are from different games (no same-game overlap). Thread: three independent, Threat/opponent-rank-confirmed Overs. Combined: **+561**.

**4-Team** — adds Josh Allen Under. Allen and Cook share the NE@BUF game — the combined price below is a cross-game-style estimate, not a real FanDuel same-game-parlay quote. Combined: **+1141**.

**5-Team** — Warren, Freiermuth (same game, PIT@CLE), Cook, Downs, Taylor (Downs & Taylor share IND@WAS). Two same-game pairs disclosed. Combined: **+2230**.

**6-Team** — adds Allen (same game as Cook, NE@BUF — third same-game pair). Combined: **+4273**.

**7-Team** — adds Rodgers Under (same game as Warren/Freiermuth — PIT@CLE now carries 3 legs). Combined: **+8108**.

```json
PARLAY_3_TEAM
[
  {"player": "Jaylen Warren", "market_key": "player_rushing_yards", "canonical_event_id": "1c79ffc934ef3e24", "price": 1.877, "side": "over", "line": 67.5, "reason": "Threat-confirmed vs CLE's 24th-ranked RB run D.", "evidence_check": [{"type":"current_opponent","team":"CLE","pos":"RB","stat":"rush_yds","role":"def","claimed_rank":24}]},
  {"player": "James Cook", "market_key": "player_rushing_yards", "canonical_event_id": "5a6a506f9ff2a30f", "price": 1.877, "side": "over", "line": 87.5, "reason": "Elite volume vs NE's mid-tier (16th) run D.", "evidence_check": [{"type":"current_opponent","team":"NE","pos":"RB","stat":"rush_yds","role":"def","claimed_rank":16}]},
  {"player": "Josh Downs", "market_key": "player_receiving_yards", "canonical_event_id": "b9550fb6e56e66e2", "price": 1.877, "side": "over", "line": 64.5, "reason": "WAS 30th-ranked WR defense.", "evidence_check": [{"type":"current_opponent","team":"WAS","pos":"WR","stat":"rec_yds","role":"def","claimed_rank":30}]}
]
```
```json
PARLAY_4_TEAM
[
  {"player": "Jaylen Warren", "market_key": "player_rushing_yards", "canonical_event_id": "1c79ffc934ef3e24", "price": 1.877, "side": "over", "line": 67.5, "reason": "Threat-confirmed vs CLE's 24th-ranked RB run D.", "evidence_check": [{"type":"current_opponent","team":"CLE","pos":"RB","stat":"rush_yds","role":"def","claimed_rank":24}]},
  {"player": "James Cook", "market_key": "player_rushing_yards", "canonical_event_id": "5a6a506f9ff2a30f", "price": 1.877, "side": "over", "line": 87.5, "reason": "Elite volume vs NE's mid-tier run D.", "evidence_check": [{"type":"current_opponent","team":"NE","pos":"RB","stat":"rush_yds","role":"def","claimed_rank":16}]},
  {"player": "Josh Downs", "market_key": "player_receiving_yards", "canonical_event_id": "b9550fb6e56e66e2", "price": 1.877, "side": "over", "line": 64.5, "reason": "WAS 30th-ranked WR defense.", "evidence_check": [{"type":"current_opponent","team":"WAS","pos":"WR","stat":"rec_yds","role":"def","claimed_rank":30}]},
  {"player": "Josh Allen", "market_key": "player_passing_yards", "canonical_event_id": "5a6a506f9ff2a30f", "price": 1.877, "side": "under", "line": 242.5, "reason": "NE pass D ranks 6th, his toughest test this year.", "evidence_check": [{"type":"current_opponent","team":"NE","pos":"QB","stat":"pass_yds","role":"def","claimed_rank":6}]}
]
```
```json
PARLAY_5_TEAM
[
  {"player": "Jaylen Warren", "market_key": "player_rushing_yards", "canonical_event_id": "1c79ffc934ef3e24", "price": 1.877, "side": "over", "line": 67.5, "reason": "Threat-confirmed vs CLE's 24th-ranked RB run D.", "evidence_check": [{"type":"current_opponent","team":"CLE","pos":"RB","stat":"rush_yds","role":"def","claimed_rank":24}]},
  {"player": "Pat Freiermuth", "market_key": "player_receiving_yards", "canonical_event_id": "1c79ffc934ef3e24", "price": 1.877, "side": "over", "line": 28.5, "reason": "CLE 24th-ranked TE D; real red-zone role.", "evidence_check": [{"type":"current_opponent","team":"CLE","pos":"TE","stat":"rec_yds","role":"def","claimed_rank":24}]},
  {"player": "James Cook", "market_key": "player_rushing_yards", "canonical_event_id": "5a6a506f9ff2a30f", "price": 1.877, "side": "over", "line": 87.5, "reason": "Elite volume vs NE's mid-tier run D.", "evidence_check": [{"type":"current_opponent","team":"NE","pos":"RB","stat":"rush_yds","role":"def","claimed_rank":16}]},
  {"player": "Josh Downs", "market_key": "player_receiving_yards", "canonical_event_id": "b9550fb6e56e66e2", "price": 1.877, "side": "over", "line": 64.5, "reason": "WAS 30th-ranked WR defense.", "evidence_check": [{"type":"current_opponent","team":"WAS","pos":"WR","stat":"rec_yds","role":"def","claimed_rank":30}]},
  {"player": "Jonathan Taylor", "market_key": "player_rushing_yards", "canonical_event_id": "b9550fb6e56e66e2", "price": 1.877, "side": "under", "line": 90.5, "reason": "WAS run D ranks 3rd, elite.", "evidence_check": [{"type":"current_opponent","team":"WAS","pos":"RB","stat":"rush_yds","role":"def","claimed_rank":3}]}
]
```
```json
PARLAY_6_TEAM
[
  {"player": "Jaylen Warren", "market_key": "player_rushing_yards", "canonical_event_id": "1c79ffc934ef3e24", "price": 1.877, "side": "over", "line": 67.5, "reason": "Threat-confirmed vs CLE's 24th-ranked RB run D.", "evidence_check": [{"type":"current_opponent","team":"CLE","pos":"RB","stat":"rush_yds","role":"def","claimed_rank":24}]},
  {"player": "Pat Freiermuth", "market_key": "player_receiving_yards", "canonical_event_id": "1c79ffc934ef3e24", "price": 1.877, "side": "over", "line": 28.5, "reason": "CLE 24th-ranked TE D; real red-zone role.", "evidence_check": [{"type":"current_opponent","team":"CLE","pos":"TE","stat":"rec_yds","role":"def","claimed_rank":24}]},
  {"player": "James Cook", "market_key": "player_rushing_yards", "canonical_event_id": "5a6a506f9ff2a30f", "price": 1.877, "side": "over", "line": 87.5, "reason": "Elite volume vs NE's mid-tier run D.", "evidence_check": [{"type":"current_opponent","team":"NE","pos":"RB","stat":"rush_yds","role":"def","claimed_rank":16}]},
  {"player": "Josh Allen", "market_key": "player_passing_yards", "canonical_event_id": "5a6a506f9ff2a30f", "price": 1.877, "side": "under", "line": 242.5, "reason": "NE pass D ranks 6th, elite.", "evidence_check": [{"type":"current_opponent","team":"NE","pos":"QB","stat":"pass_yds","role":"def","claimed_rank":6}]},
  {"player": "Josh Downs", "market_key": "player_receiving_yards", "canonical_event_id": "b9550fb6e56e66e2", "price": 1.877, "side": "over", "line": 64.5, "reason": "WAS 30th-ranked WR defense.", "evidence_check": [{"type":"current_opponent","team":"WAS","pos":"WR","stat":"rec_yds","role":"def","claimed_rank":30}]},
  {"player": "Jonathan Taylor", "market_key": "player_rushing_yards", "canonical_event_id": "b9550fb6e56e66e2", "price": 1.877, "side": "under", "line": 90.5, "reason": "WAS run D ranks 3rd, elite.", "evidence_check": [{"type":"current_opponent","team":"WAS","pos":"RB","stat":"rush_yds","role":"def","claimed_rank":3}]}
]
```
```json
PARLAY_7_TEAM
[
  {"player": "Jaylen Warren", "market_key": "player_rushing_yards", "canonical_event_id": "1c79ffc934ef3e24", "price": 1.877, "side": "over", "line": 67.5, "reason": "Threat-confirmed vs CLE's 24th-ranked RB run D.", "evidence_check": [{"type":"current_opponent","team":"CLE","pos":"RB","stat":"rush_yds","role":"def","claimed_rank":24}]},
  {"player": "Pat Freiermuth", "market_key": "player_receiving_yards", "canonical_event_id": "1c79ffc934ef3e24", "price": 1.877, "side": "over", "line": 28.5, "reason": "CLE 24th-ranked TE D; real red-zone role.", "evidence_check": [{"type":"current_opponent","team":"CLE","pos":"TE","stat":"rec_yds","role":"def","claimed_rank":24}]},
  {"player": "Aaron Rodgers", "market_key": "player_passing_yards", "canonical_event_id": "1c79ffc934ef3e24", "price": 1.877, "side": "under", "line": 212.5, "reason": "CLE pass D ranks 10th, tougher than Rodgers' rate.", "evidence_check": [{"type":"current_opponent","team":"CLE","pos":"QB","stat":"pass_yds","role":"def","claimed_rank":10}]},
  {"player": "James Cook", "market_key": "player_rushing_yards", "canonical_event_id": "5a6a506f9ff2a30f", "price": 1.877, "side": "over", "line": 87.5, "reason": "Elite volume vs NE's mid-tier run D.", "evidence_check": [{"type":"current_opponent","team":"NE","pos":"RB","stat":"rush_yds","role":"def","claimed_rank":16}]},
  {"player": "Josh Allen", "market_key": "player_passing_yards", "canonical_event_id": "5a6a506f9ff2a30f", "price": 1.877, "side": "under", "line": 242.5, "reason": "NE pass D ranks 6th, elite.", "evidence_check": [{"type":"current_opponent","team":"NE","pos":"QB","stat":"pass_yds","role":"def","claimed_rank":6}]},
  {"player": "Josh Downs", "market_key": "player_receiving_yards", "canonical_event_id": "b9550fb6e56e66e2", "price": 1.877, "side": "over", "line": 64.5, "reason": "WAS 30th-ranked WR defense.", "evidence_check": [{"type":"current_opponent","team":"WAS","pos":"WR","stat":"rec_yds","role":"def","claimed_rank":30}]},
  {"player": "Jonathan Taylor", "market_key": "player_rushing_yards", "canonical_event_id": "b9550fb6e56e66e2", "price": 1.877, "side": "under", "line": 90.5, "reason": "WAS run D ranks 3rd, elite.", "evidence_check": [{"type":"current_opponent","team":"WAS","pos":"RB","stat":"rush_yds","role":"def","claimed_rank":3}]}
]
```

---

## SECTION 7 — FAVORITE ANYTIME TD PARLAYS

**3-Team** — Jonathan Taylor, James Cook, Quinshon Judkins. Three different games, all RBs with dominant red-zone roles. Combined: **+421**.

**4-Team** — adds Jacory Croskey-Merritt. Croskey-Merritt and Taylor share IND@WAS. Combined: **+1045**.

**5-Team** — adds Stefon Diggs (IND@WAS now carries 3 legs). Combined: **+4022**.

**6-Team** — adds Denzel Boston (shares PIT@CLE with Judkins). Combined: **+16,802**.

**7-Team** — adds Pat Freiermuth (PIT@CLE now carries 3 legs). Combined: **+77,650**.

```json
TD_PARLAY_3_TEAM
[
  {"player": "Jonathan Taylor", "market_key": "player_anytime_td", "canonical_event_id": "b9550fb6e56e66e2", "price": 1.345, "side": "over", "line": null, "reason": "80% of IND's red-zone carries; WAS's RB rush-TD defense ranks 7th, tough but Taylor's workload share dominates regardless.", "evidence_check": [{"type":"current_opponent","team":"WAS","pos":"RB","stat":"rush_td","role":"def","claimed_rank":7}]},
  {"player": "James Cook", "market_key": "player_anytime_td", "canonical_event_id": "5a6a506f9ff2a30f", "price": 1.8, "side": "over", "line": null, "reason": "56.2% of BUF's red-zone carries, 2 rush TDs already; NE's RB rush-TD defense ranks a mid-tier 22nd.", "evidence_check": [{"type":"current_opponent","team":"NE","pos":"RB","stat":"rush_td","role":"def","claimed_rank":22}]},
  {"player": "Quinshon Judkins", "market_key": "player_anytime_td", "canonical_event_id": "1c79ffc934ef3e24", "price": 2.15, "side": "over", "line": null, "reason": "54.5% of CLE's red-zone carries; PIT's RB rush-TD defense ranks a moderate 14th.", "evidence_check": [{"type":"current_opponent","team":"PIT","pos":"RB","stat":"rush_td","role":"def","claimed_rank":14}]}
]
```
```json
TD_PARLAY_4_TEAM
[
  {"player": "Jonathan Taylor", "market_key": "player_anytime_td", "canonical_event_id": "b9550fb6e56e66e2", "price": 1.345, "side": "over", "line": null, "reason": "80% of IND's red-zone carries vs WAS's 7th-ranked rush-TD D.", "evidence_check": [{"type":"current_opponent","team":"WAS","pos":"RB","stat":"rush_td","role":"def","claimed_rank":7}]},
  {"player": "James Cook", "market_key": "player_anytime_td", "canonical_event_id": "5a6a506f9ff2a30f", "price": 1.8, "side": "over", "line": null, "reason": "56.2% red-zone carry share vs NE's 22nd-ranked rush-TD D.", "evidence_check": [{"type":"current_opponent","team":"NE","pos":"RB","stat":"rush_td","role":"def","claimed_rank":22}]},
  {"player": "Quinshon Judkins", "market_key": "player_anytime_td", "canonical_event_id": "1c79ffc934ef3e24", "price": 2.15, "side": "over", "line": null, "reason": "54.5% red-zone carry share vs PIT's 14th-ranked rush-TD D.", "evidence_check": [{"type":"current_opponent","team":"PIT","pos":"RB","stat":"rush_td","role":"def","claimed_rank":14}]},
  {"player": "Jacory Croskey-Merritt", "market_key": "player_anytime_td", "canonical_event_id": "b9550fb6e56e66e2", "price": 2.2, "side": "over", "line": null, "reason": "29.4% red-zone carry share; IND's RB rush-TD defense ranks 30th, one of the worst in the league.", "evidence_check": [{"type":"current_opponent","team":"IND","pos":"RB","stat":"rush_td","role":"def","claimed_rank":30}]}
]
```
```json
TD_PARLAY_5_TEAM
[
  {"player": "Jonathan Taylor", "market_key": "player_anytime_td", "canonical_event_id": "b9550fb6e56e66e2", "price": 1.345, "side": "over", "line": null, "reason": "80% of IND's red-zone carries vs WAS's 7th-ranked rush-TD D.", "evidence_check": [{"type":"current_opponent","team":"WAS","pos":"RB","stat":"rush_td","role":"def","claimed_rank":7}]},
  {"player": "James Cook", "market_key": "player_anytime_td", "canonical_event_id": "5a6a506f9ff2a30f", "price": 1.8, "side": "over", "line": null, "reason": "56.2% red-zone carry share vs NE's 22nd-ranked rush-TD D.", "evidence_check": [{"type":"current_opponent","team":"NE","pos":"RB","stat":"rush_td","role":"def","claimed_rank":22}]},
  {"player": "Quinshon Judkins", "market_key": "player_anytime_td", "canonical_event_id": "1c79ffc934ef3e24", "price": 2.15, "side": "over", "line": null, "reason": "54.5% red-zone carry share vs PIT's 14th-ranked rush-TD D.", "evidence_check": [{"type":"current_opponent","team":"PIT","pos":"RB","stat":"rush_td","role":"def","claimed_rank":14}]},
  {"player": "Jacory Croskey-Merritt", "market_key": "player_anytime_td", "canonical_event_id": "b9550fb6e56e66e2", "price": 2.2, "side": "over", "line": null, "reason": "29.4% red-zone carry share vs IND's 30th-ranked rush-TD D.", "evidence_check": [{"type":"current_opponent","team":"IND","pos":"RB","stat":"rush_td","role":"def","claimed_rank":30}]},
  {"player": "Stefon Diggs", "market_key": "player_anytime_td", "canonical_event_id": "b9550fb6e56e66e2", "price": 3.6, "side": "over", "line": null, "reason": "4 red-zone targets, 3 TDs already (near-automatic conversion); IND's WR TD defense ranks a mid 20th.", "evidence_check": [{"type":"current_opponent","team":"IND","pos":"WR","stat":"td","role":"def","claimed_rank":20}]}
]
```
```json
TD_PARLAY_6_TEAM
[
  {"player": "Jonathan Taylor", "market_key": "player_anytime_td", "canonical_event_id": "b9550fb6e56e66e2", "price": 1.345, "side": "over", "line": null, "reason": "80% of IND's red-zone carries vs WAS's 7th-ranked rush-TD D.", "evidence_check": [{"type":"current_opponent","team":"WAS","pos":"RB","stat":"rush_td","role":"def","claimed_rank":7}]},
  {"player": "James Cook", "market_key": "player_anytime_td", "canonical_event_id": "5a6a506f9ff2a30f", "price": 1.8, "side": "over", "line": null, "reason": "56.2% red-zone carry share vs NE's 22nd-ranked rush-TD D.", "evidence_check": [{"type":"current_opponent","team":"NE","pos":"RB","stat":"rush_td","role":"def","claimed_rank":22}]},
  {"player": "Quinshon Judkins", "market_key": "player_anytime_td", "canonical_event_id": "1c79ffc934ef3e24", "price": 2.15, "side": "over", "line": null, "reason": "54.5% red-zone carry share vs PIT's 14th-ranked rush-TD D.", "evidence_check": [{"type":"current_opponent","team":"PIT","pos":"RB","stat":"rush_td","role":"def","claimed_rank":14}]},
  {"player": "Jacory Croskey-Merritt", "market_key": "player_anytime_td", "canonical_event_id": "b9550fb6e56e66e2", "price": 2.2, "side": "over", "line": null, "reason": "29.4% red-zone carry share vs IND's 30th-ranked rush-TD D.", "evidence_check": [{"type":"current_opponent","team":"IND","pos":"RB","stat":"rush_td","role":"def","claimed_rank":30}]},
  {"player": "Stefon Diggs", "market_key": "player_anytime_td", "canonical_event_id": "b9550fb6e56e66e2", "price": 3.6, "side": "over", "line": null, "reason": "4 red-zone targets, 3 TDs already vs IND's 20th-ranked WR TD D.", "evidence_check": [{"type":"current_opponent","team":"IND","pos":"WR","stat":"td","role":"def","claimed_rank":20}]},
  {"player": "Denzel Boston", "market_key": "player_anytime_td", "canonical_event_id": "1c79ffc934ef3e24", "price": 4.1, "side": "over", "line": null, "reason": "30.8% red-zone target share, the highest of any player in this game; PIT's WR TD defense ranks a tougher 10th.", "evidence_check": [{"type":"current_opponent","team":"PIT","pos":"WR","stat":"td","role":"def","claimed_rank":10}]}
]
```
```json
TD_PARLAY_7_TEAM
[
  {"player": "Jonathan Taylor", "market_key": "player_anytime_td", "canonical_event_id": "b9550fb6e56e66e2", "price": 1.345, "side": "over", "line": null, "reason": "80% of IND's red-zone carries vs WAS's 7th-ranked rush-TD D.", "evidence_check": [{"type":"current_opponent","team":"WAS","pos":"RB","stat":"rush_td","role":"def","claimed_rank":7}]},
  {"player": "James Cook", "market_key": "player_anytime_td", "canonical_event_id": "5a6a506f9ff2a30f", "price": 1.8, "side": "over", "line": null, "reason": "56.2% red-zone carry share vs NE's 22nd-ranked rush-TD D.", "evidence_check": [{"type":"current_opponent","team":"NE","pos":"RB","stat":"rush_td","role":"def","claimed_rank":22}]},
  {"player": "Quinshon Judkins", "market_key": "player_anytime_td", "canonical_event_id": "1c79ffc934ef3e24", "price": 2.15, "side": "over", "line": null, "reason": "54.5% red-zone carry share vs PIT's 14th-ranked rush-TD D.", "evidence_check": [{"type":"current_opponent","team":"PIT","pos":"RB","stat":"rush_td","role":"def","claimed_rank":14}]},
  {"player": "Jacory Croskey-Merritt", "market_key": "player_anytime_td", "canonical_event_id": "b9550fb6e56e66e2", "price": 2.2, "side": "over", "line": null, "reason": "29.4% red-zone carry share vs IND's 30th-ranked rush-TD D.", "evidence_check": [{"type":"current_opponent","team":"IND","pos":"RB","stat":"rush_td","role":"def","claimed_rank":30}]},
  {"player": "Stefon Diggs", "market_key": "player_anytime_td", "canonical_event_id": "b9550fb6e56e66e2", "price": 3.6, "side": "over", "line": null, "reason": "4 red-zone targets, 3 TDs already vs IND's 20th-ranked WR TD D.", "evidence_check": [{"type":"current_opponent","team":"IND","pos":"WR","stat":"td","role":"def","claimed_rank":20}]},
  {"player": "Denzel Boston", "market_key": "player_anytime_td", "canonical_event_id": "1c79ffc934ef3e24", "price": 4.1, "side": "over", "line": null, "reason": "30.8% red-zone target share vs PIT's 10th-ranked WR TD D.", "evidence_check": [{"type":"current_opponent","team":"PIT","pos":"WR","stat":"td","role":"def","claimed_rank":10}]},
  {"player": "Pat Freiermuth", "market_key": "player_anytime_td", "canonical_event_id": "1c79ffc934ef3e24", "price": 4.6, "side": "over", "line": null, "reason": "16.7% red-zone target share vs CLE's 11th-ranked TE TD D.", "evidence_check": [{"type":"current_opponent","team":"CLE","pos":"TE","stat":"td","role":"def","claimed_rank":11}]}
]
```

---

## SECTION 8 — FAVORITE SPREAD PARLAYS

**Real-data limitation (stated plainly):** this slate has exactly **four** real mainline spread markets — one per game — and both sides of each are mutually exclusive, so only four genuinely independent real legs exist this week. A real 5-, 6-, or 7-team mainline spread parlay cannot be built from real data without reusing a market already used on its opposite side, which is incoherent. Rather than fabricate additional markets, the 5/6/7-team blocks below are left at the same 4-leg maximum, explicitly flagged as not a genuinely larger combination.

- **PIT -2.5** (-112) — PIT's defense and Finding 1/2 rushing-matchup edge are the stronger supported side; PIT's real ATS record is **58.8%** overall (60-42-2) and **56.0%** on the road (28-22-1).
- **BAL -11.5** (-110) — statistically overwhelming mismatch (Henry's Threat, TEN's red-zone run funnel); BAL's real ATS record is a more modest **51.5%** overall, and notably **45.1%** at home (23-28-1) — a real tension worth flagging against laying this many points.
- **BUF -6.5** (-115) — BUF's offense and real ATS record both support this: **56.0%** overall, **56.9%** at home (29-22-2).
- **WAS +3.5** (-110) — genuine game-script uncertainty (Daniels' availability, IND's own 30th-ranked defense) argues for the points; WAS's real ATS record is close to a coin flip at **48.5%** overall, **49.0%** at home (24-25-2).

**3-Team** — PIT, BAL, BUF (the three strongest convictions). Combined: **+576**.

**4-Team** — adds WAS +3.5 (all four real spread markets on the slate). Combined: **+1190**.

**5/6/7-Team** — not constructible from real data this week; see limitation note above.

```json
SPREAD_PARLAY_3_TEAM
[
  {"player": "Pittsburgh Steelers", "market_key": "spreads", "canonical_event_id": "1c79ffc934ef3e24", "price": 1.893, "point": -2.5, "reason": "Stronger, more stable defense and rushing-matchup edge; PIT is 58.8% ATS overall, 56.0% ATS on the road.", "evidence_check": []},
  {"player": "Baltimore Ravens", "market_key": "spreads", "canonical_event_id": "ac76e69da9802c5f", "price": 1.909, "point": -11.5, "reason": "Statistically dominant matchup vs TEN's run funnel; BAL is 51.5% ATS overall but only 45.1% ATS at home — a real caution flag at this number.", "evidence_check": []},
  {"player": "Buffalo Bills", "market_key": "spreads", "canonical_event_id": "5a6a506f9ff2a30f", "price": 1.87, "point": -6.5, "reason": "Top-scoring offense facing a shaky NE pass D long-term floor; BUF is 56.0% ATS overall, 56.9% ATS at home.", "evidence_check": []}
]
```
```json
SPREAD_PARLAY_4_TEAM
[
  {"player": "Pittsburgh Steelers", "market_key": "spreads", "canonical_event_id": "1c79ffc934ef3e24", "price": 1.893, "point": -2.5, "reason": "Stronger defense and rushing edge; 58.8% ATS overall, 56.0% ATS on the road.", "evidence_check": []},
  {"player": "Baltimore Ravens", "market_key": "spreads", "canonical_event_id": "ac76e69da9802c5f", "price": 1.909, "point": -11.5, "reason": "Dominant matchup vs TEN; 51.5% ATS overall, only 45.1% ATS at home.", "evidence_check": []},
  {"player": "Buffalo Bills", "market_key": "spreads", "canonical_event_id": "5a6a506f9ff2a30f", "price": 1.87, "point": -6.5, "reason": "Top-scoring offense; 56.0% ATS overall, 56.9% ATS at home.", "evidence_check": []},
  {"player": "Washington Commanders", "market_key": "spreads", "canonical_event_id": "b9550fb6e56e66e2", "price": 1.909, "point": 3.5, "reason": "Genuine game-script uncertainty (Daniels availability, IND's 30th-ranked D) argues for the points; WAS is 48.5% ATS overall, 49.0% ATS at home.", "evidence_check": []}
]
```
```json
SPREAD_PARLAY_5_TEAM
[
  {"player": "Pittsburgh Steelers", "market_key": "spreads", "canonical_event_id": "1c79ffc934ef3e24", "price": 1.893, "point": -2.5, "reason": "Stronger defense and rushing edge; 58.8% ATS overall, 56.0% ATS on the road. NOTE: only 4 real spread markets exist on this slate — no 5th independent leg is available.", "evidence_check": []},
  {"player": "Baltimore Ravens", "market_key": "spreads", "canonical_event_id": "ac76e69da9802c5f", "price": 1.909, "point": -11.5, "reason": "Dominant matchup vs TEN; 51.5% ATS overall, only 45.1% ATS at home.", "evidence_check": []},
  {"player": "Buffalo Bills", "market_key": "spreads", "canonical_event_id": "5a6a506f9ff2a30f", "price": 1.87, "point": -6.5, "reason": "Top-scoring offense; 56.0% ATS overall, 56.9% ATS at home.", "evidence_check": []},
  {"player": "Washington Commanders", "market_key": "spreads", "canonical_event_id": "b9550fb6e56e66e2", "price": 1.909, "point": 3.5, "reason": "Game-script uncertainty argues for the points; 48.5% ATS overall, 49.0% ATS at home.", "evidence_check": []}
]
```
```json
SPREAD_PARLAY_6_TEAM
[
  {"player": "Pittsburgh Steelers", "market_key": "spreads", "canonical_event_id": "1c79ffc934ef3e24", "price": 1.893, "point": -2.5, "reason": "Stronger defense and rushing edge; 58.8% ATS overall, 56.0% ATS on the road. NOTE: only 4 real spread markets exist on this slate — no 6th independent leg is available.", "evidence_check": []},
  {"player": "Baltimore Ravens", "market_key": "spreads", "canonical_event_id": "ac76e69da9802c5f", "price": 1.909, "point": -11.5, "reason": "Dominant matchup vs TEN; 51.5% ATS overall, only 45.1% ATS at home.", "evidence_check": []},
  {"player": "Buffalo Bills", "market_key": "spreads", "canonical_event_id": "5a6a506f9ff2a30f", "price": 1.87, "point": -6.5, "reason": "Top-scoring offense; 56.0% ATS overall, 56.9% ATS at home.", "evidence_check": []},
  {"player": "Washington Commanders", "market_key": "spreads", "canonical_event_id": "b9550fb6e56e66e2", "price": 1.909, "point": 3.5, "reason": "Game-script uncertainty argues for the points; 48.5% ATS overall, 49.0% ATS at home.", "evidence_check": []}
]
```
```json
SPREAD_PARLAY_7_TEAM
[
  {"player": "Pittsburgh Steelers", "market_key": "spreads", "canonical_event_id": "1c79ffc934ef3e24", "price": 1.893, "point": -2.5, "reason": "Stronger defense and rushing edge; 58.8% ATS overall, 56.0% ATS on the road. NOTE: only 4 real spread markets exist on this slate — no 7th independent leg is available.", "evidence_check": []},
  {"player": "Baltimore Ravens", "market_key": "spreads", "canonical_event_id": "ac76e69da9802c5f", "price": 1.909, "point": -11.5, "reason": "Dominant matchup vs TEN; 51.5% ATS overall, only 45.1% ATS at home.", "evidence_check": []},
  {"player": "Buffalo Bills", "market_key": "spreads", "canonical_event_id": "5a6a506f9ff2a30f", "price": 1.87, "point": -6.5, "reason": "Top-scoring offense; 56.0% ATS overall, 56.9% ATS at home.", "evidence_check": []},
  {"player": "Washington Commanders", "market_key": "spreads", "canonical_event_id": "b9550fb6e56e66e2", "price": 1.909, "point": 3.5, "reason": "Game-script uncertainty argues for the points; 48.5% ATS overall, 49.0% ATS at home.", "evidence_check": []}
]
```