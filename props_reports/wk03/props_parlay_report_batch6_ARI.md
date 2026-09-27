# COEUS WEEK 3 PROPS & PARLAY REPORT

## REAL DATA COVERAGE NOTE (read first)

- Passing Yards, Rushing Yards, Anytime TD: **LIVE**, used normally below.
- Receiving Yards, Receptions: the coverage header reports these as "current" with 9 events each — but the actual per-game FanDuel data provided for **every single game on this slate** shows an empty `{}` for `receiving_yards` and `receptions`. No player prop in either market actually populated for any of the 6 games. Per the no-fabrication rule, this is treated as **effectively unavailable this run** — no WR/TE receiving-yards or receptions picks appear anywhere below. WR/TE exposure in this report comes **only** through the `player_anytime_td` market, which is genuinely live and populated.

---

## 1. COEUS PROP BREAKDOWN

### BAL @ DAL
- **Derrick Henry** (BAL) — Anytime TD, -240 — 91.7% red-zone carry share this season; Dallas's run defense has collapsed from 23rd (2025) to 30th (2026, 173.5 rush yds/gm allowed) — one of the steepest declines on either roster, hitting the league's most concentrated goal-line back.
- **Dak Prescott** (DAL) — Under 261.5 passing yards, -113 — His own 2026 pace (227.0 ypg) is a real step down as Dallas's offense fell from the NFL's No. 1 passing attack (2025) to 15th; meanwhile Baltimore's pass defense improved from 29th to 13th over the same window. *(Alt ladder note: FanDuel's alt thresholds for this market are priced Over-only — no Under-side alternative exists to this 261.5 line.)*
- **CeeDee Lamb** (DAL) — Anytime TD, +115 — 98.5 rec yds/gm through two 2026 games, already exceeding his Elite-tier 2025 pace (82.8 ypg), against a Baltimore WR defense that ranked 32nd in the NFL in yards allowed to wideouts in 2025.

### LV @ NO
- **Ashton Jeanty** (LV) — Anytime TD, -120 — 81.8% red-zone carry share; New Orleans's run defense has slid from 19th (2025) to 27th through two 2026 games (118.5 ypg allowed).
- **Tyler Shough** (NO) — Over 252.5 passing yards, -113 — Averaging an NFL-leading 331.0 ypg in 2026 (up from 216.7 in 2025); even discounting for volume-driven inflation, his pace clears this line comfortably against a Las Vegas defense only modestly improved (13th to 11th).
- **Chris Olave** (NO) — Anytime TD, +155 — His 2025 receptions rank (6th) and receiving-yards rank (9th) both converge with Las Vegas's defense, which allowed the 29th-most catches to WRs in 2025 — a high-volume profile matching Olave's own 134.0 ypg, 9.0 rec/gm 2026 pace.

### ARI @ SF
- **George Kittle** (SF) — Anytime TD, +175 — Nuclear-tier Threat (Quadruple): his 2025 receiving-yards rank (3rd) and receptions rank (3rd) both fully converge with Arizona's tight-end defense, 30th in both categories (68.6 rec yds/gm allowed).
- **Trey McBride** (ARI) — Anytime TD, +180 — 66.7% red-zone target share; his 2025 receptions rank (1st) converges with San Francisco's tight-end defense, ranked 24th.
- **Christian McCaffrey** (SF) — Under 55.5 rushing yards, -113 — His own 2026 season rate (45.5 ypg) already sits well below this line, reflecting a real committee split with Kaelon Black (35.1% vs. 36.8% rush share) — even though Arizona's run defense allowed the 29th-most rushing yards to backs in 2025, McCaffrey's diminished workload argues the raw matchup overstates his ceiling.

### MIN @ TB
- **Bucky Irving** (TB) — Anytime TD, +130 — Tampa Bay's clear bell-cow (55.6% rush share); Minnesota allows opponents to run at it in the red zone more than any other defense in the league (59.3% run rate allowed, ranked 1st).
- **Baker Mayfield** (TB) — Over 216.5 passing yards, -113 — 199.0 ypg in 2026, but Minnesota's pass defense has collapsed from 2nd in the NFL (2025) to 29th through two 2026 games — the single largest defensive swing in this entire evidence set.
- **Justin Jefferson** (MIN) — Anytime TD, +155 — Highest target share in this evidence set (35.7%, 2026); Tampa Bay allowed 14 receiving TDs to WRs in 2025 (ranked 13th).

### LAR @ DEN
- **Kyren Williams** (LAR) — Anytime TD, -105 — 66.7% red-zone carry share; Denver's run defense has collapsed from 2nd in the NFL (2025, 91.1 ypg allowed) to 29th through two 2026 games (157.5 ypg).
- **Bo Nix** (DEN) — Under 211.5 passing yards, -113 — 209.5 ypg in 2026, in line with his 17th-ranked 2025 pace, but Los Angeles's pass defense has improved from 20th to 3rd — the sharpest single swing in this whole game.
- **J.K. Dobbins** (DEN) — Anytime TD, +140 — Best contact-creation profile of any back in this game (2.44 yards after contact/carry); Los Angeles's run defense has actually declined this season (12th to 19th).

### PHI @ CHI
- **Saquon Barkley** (PHI) — Anytime TD, -115 — Standard-tier Threat (rush yards): his 2025 rank of 10th (71.2 ypg) converges with Chicago's run defense allowing at a 23rd-ranked clip to backs.
- **Jalen Hurts** (PHI) — Over 218.5 passing yards, -114 — Averaging 233.5 ypg in 2026, comfortably clearing this line; Chicago's pass defense has actually declined slightly this season (22nd to 24th).
- **DeVonta Smith** (PHI) — Anytime TD, +180 — Largest target share of any receiver in this report (33.9%); Chicago allowed 21 receiving TDs to WRs in 2025 (30th, one of the worst marks in the league).

### Favorite Prop by Position (league-wide)
- **QB — Baker Mayfield** (TB), Over 216.5 passing yards, -113 — same reasoning as above; the single largest quarterback-matchup swing on the slate.
- **RB — Derrick Henry** (BAL), Anytime TD, -240 — same reasoning as above.
- **WR — CeeDee Lamb** (DAL), Anytime TD, +115 — same reasoning as above.
- **TE — George Kittle** (SF), Anytime TD, +175 — same reasoning as above; Nuclear-tier, the cleanest single mismatch on the board.

```json
PROP_BREAKDOWN
{
  "per_game": [
    {"away": "BAL", "home": "DAL", "picks": [
      {"player": "Derrick Henry", "market_key": "player_anytime_td", "canonical_event_id": "2f5531b7c22a7a0d", "price": 1.417, "side": "over", "line": null, "reason": "91.7% red-zone carry share vs. Dallas's run defense, which has collapsed from 23rd (2025) to 30th (2026, 173.5 rush yds/gm allowed).", "evidence_check": [{"type":"rank_shift","team":"DAL","side":"def","stat":"rush_ypg","claimed_rank_2025":23,"claimed_rank_2026":30}]},
      {"player": "Dak Prescott", "market_key": "player_passing_yards", "canonical_event_id": "2f5531b7c22a7a0d", "price": 1.885, "side": "under", "line": 261.5, "reason": "Prescott's 227.0 ypg 2026 pace reflects Dallas's offense falling from 1st to 15th in passing rank, opposite a Baltimore pass defense that improved from 29th to 13th.", "evidence_check": [{"type":"rank_shift","team":"DAL","side":"off","stat":"pass_ypg","claimed_rank_2025":1,"claimed_rank_2026":15},{"type":"rank_shift","team":"BAL","side":"def","stat":"pass_ypg","claimed_rank_2025":29,"claimed_rank_2026":13}]},
      {"player": "CeeDee Lamb", "market_key": "player_anytime_td", "canonical_event_id": "2f5531b7c22a7a0d", "price": 2.15, "side": "over", "line": null, "reason": "98.5 rec yds/gm 2026, exceeding an already Elite-tier 2025 pace, vs. Baltimore's 32nd-ranked WR pass defense.", "evidence_check": [{"type":"current_opponent","team":"BAL","pos":"WR","stat":"rec_yds","role":"def","claimed_rank":32}]}
    ]},
    {"away": "LV", "home": "NO", "picks": [
      {"player": "Ashton Jeanty", "market_key": "player_anytime_td", "canonical_event_id": "f4f6cd4ffcfac50b", "price": 1.833, "side": "over", "line": null, "reason": "81.8% red-zone carry share vs. a New Orleans run defense that has slid from 19th to 27th in 2026.", "evidence_check": [{"type":"rank_shift","team":"NO","side":"def","stat":"rush_ypg","claimed_rank_2025":19,"claimed_rank_2026":27}]},
      {"player": "Tyler Shough", "market_key": "player_passing_yards", "canonical_event_id": "f4f6cd4ffcfac50b", "price": 1.885, "side": "over", "line": 252.5, "reason": "331.0 ypg NFL-leading 2026 pace clears this line despite volume-driven regression risk, vs. an LV pass defense only modestly improved (13th to 11th).", "evidence_check": [{"type":"rank_shift","team":"LV","side":"def","stat":"pass_ypg","claimed_rank_2025":13,"claimed_rank_2026":11}]},
      {"player": "Chris Olave", "market_key": "player_anytime_td", "canonical_event_id": "f4f6cd4ffcfac50b", "price": 2.55, "side": "over", "line": null, "reason": "6th-ranked 2025 receptions rate converges with LV's defense, 29th in catches allowed to WRs.", "evidence_check": [{"type":"current_opponent","team":"LV","pos":"WR","stat":"rec","role":"def","claimed_rank":29}]}
    ]},
    {"away": "ARI", "home": "SF", "picks": [
      {"player": "George Kittle", "market_key": "player_anytime_td", "canonical_event_id": "272a59c2ac53fad2", "price": 2.75, "side": "over", "line": null, "reason": "Nuclear-tier Threat: 2025 rec_yds (3rd) and receptions (3rd) ranks both converge with Arizona's TE defense, 30th in both categories.", "evidence_check": [{"type":"current_opponent","team":"ARI","pos":"TE","stat":"rec_yds","role":"def","claimed_rank":30},{"type":"current_opponent","team":"ARI","pos":"TE","stat":"rec","role":"def","claimed_rank":30}]},
      {"player": "Trey McBride", "market_key": "player_anytime_td", "canonical_event_id": "272a59c2ac53fad2", "price": 2.8, "side": "over", "line": null, "reason": "66.7% red-zone target share; 2025 receptions rank (1st) converges with SF's TE defense, ranked 24th.", "evidence_check": [{"type":"current_opponent","team":"SF","pos":"TE","stat":"rec","role":"def","claimed_rank":24}]},
      {"player": "Christian McCaffrey", "market_key": "player_rushing_yards", "canonical_event_id": "272a59c2ac53fad2", "price": 1.885, "side": "under", "line": 55.5, "reason": "45.5 rush ypg 2026 season rate already sits below this line given a real committee split with Kaelon Black, despite ARI's 29th-ranked run defense to backs.", "evidence_check": [{"type":"current_opponent","team":"ARI","pos":"RB","stat":"rush_yds","role":"def","claimed_rank":29}]}
    ]},
    {"away": "MIN", "home": "TB", "picks": [
      {"player": "Bucky Irving", "market_key": "player_anytime_td", "canonical_event_id": "b13806c09a159b08", "price": 2.3, "side": "over", "line": null, "reason": "55.6% rush share vs. Minnesota's defense, which allows the highest RZ run rate in the league (1st).", "evidence_check": [{"type":"current_opponent","team":"MIN","pos":"TEAM","stat":"red_zone_run_pct_allowed","role":"def","claimed_rank":1}]},
      {"player": "Baker Mayfield", "market_key": "player_passing_yards", "canonical_event_id": "b13806c09a159b08", "price": 1.885, "side": "over", "line": 216.5, "reason": "MIN's pass defense collapsed from 2nd (2025) to 29th (2026) — the largest defensive swing in this whole slate.", "evidence_check": [{"type":"rank_shift","team":"MIN","side":"def","stat":"pass_ypg","claimed_rank_2025":2,"claimed_rank_2026":29}]},
      {"player": "Justin Jefferson", "market_key": "player_anytime_td", "canonical_event_id": "b13806c09a159b08", "price": 2.55, "side": "over", "line": null, "reason": "Highest target share on this slate (35.7%) vs. a TB defense that allowed 14 WR TDs in 2025 (ranked 13th).", "evidence_check": [{"type":"current_opponent","team":"TB","pos":"WR","stat":"td","role":"def","claimed_rank":13}]}
    ]},
    {"away": "LAR", "home": "DEN", "picks": [
      {"player": "Kyren Williams", "market_key": "player_anytime_td", "canonical_event_id": "94730ebf6b509215", "price": 1.952, "side": "over", "line": null, "reason": "66.7% RZ carry share vs. Denver's run defense, which collapsed from 2nd (2025) to 29th (2026).", "evidence_check": [{"type":"rank_shift","team":"DEN","side":"def","stat":"rush_ypg","claimed_rank_2025":2,"claimed_rank_2026":29}]},
      {"player": "Bo Nix", "market_key": "player_passing_yards", "canonical_event_id": "94730ebf6b509215", "price": 1.885, "side": "under", "line": 211.5, "reason": "LAR's pass defense improved from 20th to 3rd, the sharpest single swing in this game.", "evidence_check": [{"type":"rank_shift","team":"LAR","side":"def","stat":"pass_ypg","claimed_rank_2025":20,"claimed_rank_2026":3}]},
      {"player": "J.K. Dobbins", "market_key": "player_anytime_td", "canonical_event_id": "94730ebf6b509215", "price": 2.4, "side": "over", "line": null, "reason": "Best contact-creation profile in this game (2.44 YAC/carry) vs. LAR's declining run defense (12th to 19th).", "evidence_check": [{"type":"rank_shift","team":"LAR","side":"def","stat":"rush_ypg","claimed_rank_2025":12,"claimed_rank_2026":19}]}
    ]},
    {"away": "PHI", "home": "CHI", "picks": [
      {"player": "Saquon Barkley", "market_key": "player_anytime_td", "canonical_event_id": "f67d76e1f1c11441", "price": 1.87, "side": "over", "line": null, "reason": "Standard-tier Threat: 2025 rank 10th (71.2 rush ypg) converges with Chicago's run defense, 23rd against backs.", "evidence_check": [{"type":"current_opponent","team":"CHI","pos":"RB","stat":"rush_yds","role":"def","claimed_rank":23}]},
      {"player": "Jalen Hurts", "market_key": "player_passing_yards", "canonical_event_id": "f67d76e1f1c11441", "price": 1.877, "side": "over", "line": 218.5, "reason": "233.5 ypg 2026 pace clears this line; Chicago's pass defense declined slightly this season (22nd to 24th).", "evidence_check": [{"type":"rank_shift","team":"CHI","side":"def","stat":"pass_ypg","claimed_rank_2025":22,"claimed_rank_2026":24}]},
      {"player": "DeVonta Smith", "market_key": "player_anytime_td", "canonical_event_id": "f67d76e1f1c11441", "price": 2.8, "side": "over", "line": null, "reason": "33.9% target share, the largest in this report, vs. Chicago's 30th-ranked WR-TD defense.", "evidence_check": [{"type":"current_opponent","team":"CHI","pos":"WR","stat":"td","role":"def","claimed_rank":30}]}
    ]}
  ],
  "per_position": {
    "QB": {"player": "Baker Mayfield", "market_key": "player_passing_yards", "canonical_event_id": "b13806c09a159b08", "price": 1.885, "side": "over", "line": 216.5, "reason": "MIN's pass defense collapsed from 2nd to 29th in 2026 — the largest QB-matchup swing on the slate.", "evidence_check": [{"type":"rank_shift","team":"MIN","side":"def","stat":"pass_ypg","claimed_rank_2025":2,"claimed_rank_2026":29}]},
    "RB": {"player": "Derrick Henry", "market_key": "player_anytime_td", "canonical_event_id": "2f5531b7c22a7a0d", "price": 1.417, "side": "over", "line": null, "reason": "91.7% RZ carry share vs. Dallas's run defense, collapsed from 23rd to 30th.", "evidence_check": [{"type":"rank_shift","team":"DAL","side":"def","stat":"rush_ypg","claimed_rank_2025":23,"claimed_rank_2026":30}]},
    "WR": {"player": "CeeDee Lamb", "market_key": "player_anytime_td", "canonical_event_id": "2f5531b7c22a7a0d", "price": 2.15, "side": "over", "line": null, "reason": "98.5 rec yds/gm 2026 vs. Baltimore's 32nd-ranked WR pass defense.", "evidence_check": [{"type":"current_opponent","team":"BAL","pos":"WR","stat":"rec_yds","role":"def","claimed_rank":32}]},
    "TE": {"player": "George Kittle", "market_key": "player_anytime_td", "canonical_event_id": "272a59c2ac53fad2", "price": 2.75, "side": "over", "line": null, "reason": "Nuclear-tier Threat vs. Arizona's TE defense, 30th in both rec_yds and receptions allowed.", "evidence_check": [{"type":"current_opponent","team":"ARI","pos":"TE","stat":"rec_yds","role":"def","claimed_rank":30}]}
  }
}
```

---

## 2. FAVORITE OVERS AND UNDERS FOR THE WEEK

**Overs**
- George Kittle (SF) Anytime TD, +175 — Nuclear-tier, cleanest mismatch on the board.
- CeeDee Lamb (DAL) Anytime TD, +115 — Elite-tier, current form exceeds the tier's own basis.
- Tyler Shough (NO) Over 252.5 passing yards, -113 — NFL-leading pace.
- Derrick Henry (BAL) Anytime TD, -240 — RZ role + declining defense.
- Baker Mayfield (TB) Over 216.5 passing yards, -113 — largest defensive swing on the slate.
- Jalen Hurts (PHI) Over 218.5 passing yards, -114 — steady defensive decline vs. own uptick.

**Unders**
- Bo Nix (DEN) Under 211.5 passing yards, -113 — LAR pass D swing (20th→3rd).
- Jacoby Brissett (ARI) Under 225.5 passing yards, -113 — SF pass D swing (23rd→7th); own 186.0 ypg pace sits well below the line.
- Dak Prescott (DAL) Under 261.5 passing yards, -113 — DAL offense collapse (1st→15th) vs. BAL D improvement.
- Christian McCaffrey (SF) Under 55.5 rushing yards, -113 — committee-limited role.

```json
FAVORITE_OU
{
  "overs": [
    {"player": "George Kittle", "market_key": "player_anytime_td", "canonical_event_id": "272a59c2ac53fad2", "price": 2.75, "side": "over", "line": null, "reason": "Nuclear-tier Threat vs. Arizona's 30th-ranked TE defense in both rec_yds and receptions.", "evidence_check": [{"type":"current_opponent","team":"ARI","pos":"TE","stat":"rec_yds","role":"def","claimed_rank":30}]},
    {"player": "CeeDee Lamb", "market_key": "player_anytime_td", "canonical_event_id": "2f5531b7c22a7a0d", "price": 2.15, "side": "over", "line": null, "reason": "98.5 rec yds/gm 2026 vs. Baltimore's 32nd-ranked WR pass defense.", "evidence_check": [{"type":"current_opponent","team":"BAL","pos":"WR","stat":"rec_yds","role":"def","claimed_rank":32}]},
    {"player": "Tyler Shough", "market_key": "player_passing_yards", "canonical_event_id": "f4f6cd4ffcfac50b", "price": 1.885, "side": "over", "line": 252.5, "reason": "331.0 ypg NFL-leading 2026 pace clears this line.", "evidence_check": [{"type":"rank_shift","team":"LV","side":"def","stat":"pass_ypg","claimed_rank_2025":13,"claimed_rank_2026":11}]},
    {"player": "Derrick Henry", "market_key": "player_anytime_td", "canonical_event_id": "2f5531b7c22a7a0d", "price": 1.417, "side": "over", "line": null, "reason": "91.7% RZ carry share vs. Dallas's run defense, collapsed from 23rd to 30th.", "evidence_check": [{"type":"rank_shift","team":"DAL","side":"def","stat":"rush_ypg","claimed_rank_2025":23,"claimed_rank_2026":30}]},
    {"player": "Baker Mayfield", "market_key": "player_passing_yards", "canonical_event_id": "b13806c09a159b08", "price": 1.885, "side": "over", "line": 216.5, "reason": "MIN's pass defense collapsed from 2nd to 29th.", "evidence_check": [{"type":"rank_shift","team":"MIN","side":"def","stat":"pass_ypg","claimed_rank_2025":2,"claimed_rank_2026":29}]},
    {"player": "Jalen Hurts", "market_key": "player_passing_yards", "canonical_event_id": "f67d76e1f1c11441", "price": 1.877, "side": "over", "line": 218.5, "reason": "233.5 ypg pace vs. a CHI pass defense that declined 22nd to 24th.", "evidence_check": [{"type":"rank_shift","team":"CHI","side":"def","stat":"pass_ypg","claimed_rank_2025":22,"claimed_rank_2026":24}]}
  ],
  "unders": [
    {"player": "Bo Nix", "market_key": "player_passing_yards", "canonical_event_id": "94730ebf6b509215", "price": 1.885, "side": "under", "line": 211.5, "reason": "LAR pass D improved sharply, 20th to 3rd.", "evidence_check": [{"type":"rank_shift","team":"LAR","side":"def","stat":"pass_ypg","claimed_rank_2025":20,"claimed_rank_2026":3}]},
    {"player": "Jacoby Brissett", "market_key": "player_passing_yards", "canonical_event_id": "272a59c2ac53fad2", "price": 1.885, "side": "under", "line": 225.5, "reason": "SF pass D improved 23rd to 7th; his own 186.0 ypg 2026 pace already sits below this line.", "evidence_check": [{"type":"rank_shift","team":"SF","side":"def","stat":"pass_ypg","claimed_rank_2025":23,"claimed_rank_2026":7}]},
    {"player": "Dak Prescott", "market_key": "player_passing_yards", "canonical_event_id": "2f5531b7c22a7a0d", "price": 1.885, "side": "under", "line": 261.5, "reason": "DAL offense fell from 1st to 15th passing rank; BAL D improved 29th to 13th.", "evidence_check": [{"type":"rank_shift","team":"DAL","side":"off","stat":"pass_ypg","claimed_rank_2025":1,"claimed_rank_2026":15},{"type":"rank_shift","team":"BAL","side":"def","stat":"pass_ypg","claimed_rank_2025":29,"claimed_rank_2026":13}]},
    {"player": "Christian McCaffrey", "market_key": "player_rushing_yards", "canonical_event_id": "272a59c2ac53fad2", "price": 1.885, "side": "under", "line": 55.5, "reason": "Season rate (45.5 ypg) already below this line given a real committee split.", "evidence_check": [{"type":"current_opponent","team":"ARI","pos":"RB","stat":"rush_yds","role":"def","claimed_rank":29}]}
  ]
}
```

---

## 3. FIVE LINE-BASED PARLAYS (3, 4, 5, 6, 7 TEAM)

**3-Team** — Jacoby Brissett Under 225.5, Baker Mayfield Over 216.5, Bo Nix Under 211.5. No shared games. Combined: ~6.698 decimal → **+570**. Thread: three defenses that have moved sharply in one clear direction in 2026 (SF and LAR improving, MIN collapsing), each read against the current-season pace of the quarterback facing them, not 2025 reputation.

**4-Team** — adds Tyler Shough Over 252.5. Still no shared games. Combined: ~12.625 → **+1163**. Adds the one leg here built on pure production (Shough's own volume) rather than a defensive swing.

**5-Team** — adds Dak Prescott Under 261.5 (BAL@DAL). No shared games. Combined: ~23.799 → **+2280**. Fifth passing-yardage leg, all five built on identifying whose 2026 defensive form is the real signal.

**6-Team** — adds Jalen Hurts Over 218.5 (PHI@CHI). All six legs now span all six games on the slate with zero overlap. Combined: ~44.671 → **+4367**. Diversifies the parlay's risk beyond only the most extreme defensive swings.

**7-Team** — adds Alvin Kamara Under 27.5 (LV@NO). **Legs 4 (Shough) and 7 (Kamara) share the same game (LV@NO)** — the combined price below is a cross-game-style estimate, not a real FanDuel same-game-parlay quote for that pairing. Combined: ~84.204 → **+8320**.

```json
PARLAY_3_TEAM
[
  {"player": "Jacoby Brissett", "market_key": "player_passing_yards", "canonical_event_id": "272a59c2ac53fad2", "price": 1.885, "side": "under", "line": 225.5, "reason": "SF pass D improved 23rd to 7th; own 186.0 ypg pace already sits below this line.", "evidence_check": [{"type":"rank_shift","team":"SF","side":"def","stat":"pass_ypg","claimed_rank_2025":23,"claimed_rank_2026":7}]},
  {"player": "Baker Mayfield", "market_key": "player_passing_yards", "canonical_event_id": "b13806c09a159b08", "price": 1.885, "side": "over", "line": 216.5, "reason": "MIN pass D collapsed 2nd to 29th.", "evidence_check": [{"type":"rank_shift","team":"MIN","side":"def","stat":"pass_ypg","claimed_rank_2025":2,"claimed_rank_2026":29}]},
  {"player": "Bo Nix", "market_key": "player_passing_yards", "canonical_event_id": "94730ebf6b509215", "price": 1.885, "side": "under", "line": 211.5, "reason": "LAR pass D improved 20th to 3rd.", "evidence_check": [{"type":"rank_shift","team":"LAR","side":"def","stat":"pass_ypg","claimed_rank_2025":20,"claimed_rank_2026":3}]}
]
```
```json
PARLAY_4_TEAM
[
  {"player": "Jacoby Brissett", "market_key": "player_passing_yards", "canonical_event_id": "272a59c2ac53fad2", "price": 1.885, "side": "under", "line": 225.5, "reason": "SF pass D improved 23rd to 7th.", "evidence_check": [{"type":"rank_shift","team":"SF","side":"def","stat":"pass_ypg","claimed_rank_2025":23,"claimed_rank_2026":7}]},
  {"player": "Baker Mayfield", "market_key": "player_passing_yards", "canonical_event_id": "b13806c09a159b08", "price": 1.885, "side": "over", "line": 216.5, "reason": "MIN pass D collapsed 2nd to 29th.", "evidence_check": [{"type":"rank_shift","team":"MIN","side":"def","stat":"pass_ypg","claimed_rank_2025":2,"claimed_rank_2026":29}]},
  {"player": "Bo Nix", "market_key": "player_passing_yards", "canonical_event_id": "94730ebf6b509215", "price": 1.885, "side": "under", "line": 211.5, "reason": "LAR pass D improved 20th to 3rd.", "evidence_check": [{"type":"rank_shift","team":"LAR","side":"def","stat":"pass_ypg","claimed_rank_2025":20,"claimed_rank_2026":3}]},
  {"player": "Tyler Shough", "market_key": "player_passing_yards", "canonical_event_id": "f4f6cd4ffcfac50b", "price": 1.885, "side": "over", "line": 252.5, "reason": "331.0 ypg NFL-leading pace clears this line.", "evidence_check": [{"type":"rank_shift","team":"LV","side":"def","stat":"pass_ypg","claimed_rank_2025":13,"claimed_rank_2026":11}]}
]
```
```json
PARLAY_5_TEAM
[
  {"player": "Jacoby Brissett", "market_key": "player_passing_yards", "canonical_event_id": "272a59c2ac53fad2", "price": 1.885, "side": "under", "line": 225.5, "reason": "SF pass D improved 23rd to 7th.", "evidence_check": [{"type":"rank_shift","team":"SF","side":"def","stat":"pass_ypg","claimed_rank_2025":23,"claimed_rank_2026":7}]},
  {"player": "Baker Mayfield", "market_key": "player_passing_yards", "canonical_event_id": "b13806c09a159b08", "price": 1.885, "side": "over", "line": 216.5, "reason": "MIN pass D collapsed 2nd to 29th.", "evidence_check": [{"type":"rank_shift","team":"MIN","side":"def","stat":"pass_ypg","claimed_rank_2025":2,"claimed_rank_2026":29}]},
  {"player": "Bo Nix", "market_key": "player_passing_yards", "canonical_event_id": "94730ebf6b509215", "price": 1.885, "side": "under", "line": 211.5, "reason": "LAR pass D improved 20th to 3rd.", "evidence_check": [{"type":"rank_shift","team":"LAR","side":"def","stat":"pass_ypg","claimed_rank_2025":20,"claimed_rank_2026":3}]},
  {"player": "Tyler Shough", "market_key": "player_passing_yards", "canonical_event_id": "f4f6cd4ffcfac50b", "price": 1.885, "side": "over", "line": 252.5, "reason": "331.0 ypg NFL-leading pace clears this line.", "evidence_check": [{"type":"rank_shift","team":"LV","side":"def","stat":"pass_ypg","claimed_rank_2025":13,"claimed_rank_2026":11}]},
  {"player": "Dak Prescott", "market_key": "player_passing_yards", "canonical_event_id": "2f5531b7c22a7a0d", "price": 1.885, "side": "under", "line": 261.5, "reason": "DAL offense fell 1st to 15th passing rank; BAL D improved 29th to 13th.", "evidence_check": [{"type":"rank_shift","team":"DAL","side":"off","stat":"pass_ypg","claimed_rank_2025":1,"claimed_rank_2026":15},{"type":"rank_shift","team":"BAL","side":"def","stat":"pass_ypg","claimed_rank_2025":29,"claimed_rank_2026":13}]}
]
```
```json
PARLAY_6_TEAM
[
  {"player": "Jacoby Brissett", "market_key": "player_passing_yards", "canonical_event_id": "272a59c2ac53fad2", "price": 1.885, "side": "under", "line": 225.5, "reason": "SF pass D improved 23rd to 7th.", "evidence_check": [{"type":"rank_shift","team":"SF","side":"def","stat":"pass_ypg","claimed_rank_2025":23,"claimed_rank_2026":7}]},
  {"player": "Baker Mayfield", "market_key": "player_passing_yards", "canonical_event_id": "b13806c09a159b08", "price": 1.885, "side": "over", "line": 216.5, "reason": "MIN pass D collapsed 2nd to 29th.", "evidence_check": [{"type":"rank_shift","team":"MIN","side":"def","stat":"pass_ypg","claimed_rank_2025":2,"claimed_rank_2026":29}]},
  {"player": "Bo Nix", "market_key": "player_passing_yards", "canonical_event_id": "94730ebf6b509215", "price": 1.885, "side": "under", "line": 211.5, "reason": "LAR pass D improved 20th to 3rd.", "evidence_check": [{"type":"rank_shift","team":"LAR","side":"def","stat":"pass_ypg","claimed_rank_2025":20,"claimed_rank_2026":3}]},
  {"player": "Tyler Shough", "market_key": "player_passing_yards", "canonical_event_id": "f4f6cd4ffcfac50b", "price": 1.885, "side": "over", "line": 252.5, "reason": "331.0 ypg NFL-leading pace clears this line.", "evidence_check": [{"type":"rank_shift","team":"LV","side":"def","stat":"pass_ypg","claimed_rank_2025":13,"claimed_rank_2026":11}]},
  {"player": "Dak Prescott", "market_key": "player_passing_yards", "canonical_event_id": "2f5531b7c22a7a0d", "price": 1.885, "side": "under", "line": 261.5, "reason": "DAL offense fell 1st to 15th passing rank; BAL D improved 29th to 13th.", "evidence_check": [{"type":"rank_shift","team":"DAL","side":"off","stat":"pass_ypg","claimed_rank_2025":1,"claimed_rank_2026":15},{"type":"rank_shift","team":"BAL","side":"def","stat":"pass_ypg","claimed_rank_2025":29,"claimed_rank_2026":13}]},
  {"player": "Jalen Hurts", "market_key": "player_passing_yards", "canonical_event_id": "f67d76e1f1c11441", "price": 1.877, "side": "over", "line": 218.5, "reason": "233.5 ypg pace vs. a CHI pass defense that declined 22nd to 24th.", "evidence_check": [{"type":"rank_shift","team":"CHI","side":"def","stat":"pass_ypg","claimed_rank_2025":22,"claimed_rank_2026":24}]}
]
```
```json
PARLAY_7_TEAM
[
  {"player": "Jacoby Brissett", "market_key": "player_passing_yards", "canonical_event_id": "272a59c2ac53fad2", "price": 1.885, "side": "under", "line": 225.5, "reason": "SF pass D improved 23rd to 7th.", "evidence_check": [{"type":"rank_shift","team":"SF","side":"def","stat":"pass_ypg","claimed_rank_2025":23,"claimed_rank_2026":7}]},
  {"player": "Baker Mayfield", "market_key": "player_passing_yards", "canonical_event_id": "b13806c09a159b08", "price": 1.885, "side": "over", "line": 216.5, "reason": "MIN pass D collapsed 2nd to 29th.", "evidence_check": [{"type":"rank_shift","team":"MIN","side":"def","stat":"pass_ypg","claimed_rank_2025":2,"claimed_rank_2026":29}]},
  {"player": "Bo Nix", "market_key": "player_passing_yards", "canonical_event_id": "94730ebf6b509215", "price": 1.885, "side": "under", "line": 211.5, "reason": "LAR pass D improved 20th to 3rd.", "evidence_check": [{"type":"rank_shift","team":"LAR","side":"def","stat":"pass_ypg","claimed_rank_2025":20,"claimed_rank_2026":3}]},
  {"player": "Tyler Shough", "market_key": "player_passing_yards", "canonical_event_id": "f4f6cd4ffcfac50b", "price": 1.885, "side": "over", "line": 252.5, "reason": "331.0 ypg NFL-leading pace clears this line.", "evidence_check": [{"type":"rank_shift","team":"LV","side":"def","stat":"pass_ypg","claimed_rank_2025":13,"claimed_rank_2026":11}]},
  {"player": "Dak Prescott", "market_key": "player_passing_yards", "canonical_event_id": "2f5531b7c22a7a0d", "price": 1.885, "side": "under", "line": 261.5, "reason": "DAL offense fell 1st to 15th passing rank; BAL D improved 29th to 13th.", "evidence_check": [{"type":"rank_shift","team":"DAL","side":"off","stat":"pass_ypg","claimed_rank_2025":1,"claimed_rank_2026":15},{"type":"rank_shift","team":"BAL","side":"def","stat":"pass_ypg","claimed_rank_2025":29,"claimed_rank_2026":13}]},
  {"player": "Jalen Hurts", "market_key": "player_passing_yards", "canonical_event_id": "f67d76e1f1c11441", "price": 1.877, "side": "over", "line": 218.5, "reason": "233.5 ypg pace vs. a CHI pass defense that declined 22nd to 24th.", "evidence_check": [{"type":"rank_shift","team":"CHI","side":"def","stat":"pass_ypg","claimed_rank_2025":22,"claimed_rank_2026":24}]},
  {"player": "Alvin Kamara", "market_key": "player_rushing_yards", "canonical_event_id": "f4f6cd4ffcfac50b", "price": 1.885, "side": "under", "line": 27.5, "reason": "Thin, sub-30-yard workload in his only 2026 game to date (33.3% rush share); LV run D also modestly improved (17th to 15th).", "evidence_check": [{"type":"rank_shift","team":"LV","side":"def","stat":"rush_ypg","claimed_rank_2025":17,"claimed_rank_2026":15}]}
]
```

---

## 4. FAVORITE ANYTIME TD PARLAYS (3, 4, 5, 6, 7 TEAM)

**3-Team** — Derrick Henry, George Kittle, Chris Olave. No shared games. Combined: ~9.937 → **+894**. Three of the strongest individually-supported TD roles/Threats this week, across three different games.

**4-Team** — adds Kyren Williams. Combined: ~19.396 → **+1840**. Adds a fourth red-zone role back facing the league's steepest run-defense decline.

**5-Team** — adds Saquon Barkley. Combined: ~36.271 → **+3527**. Extends to Barkley's own Standard-tier rush-yards Threat.

**6-Team** — adds Trey McBride. **McBride and Kittle share the same game (ARI@SF)** — the combined price below is a cross-game-style estimate for that pairing, not a real FanDuel same-game-parlay quote. Combined: ~101.560 → **+10056**.

**7-Team** — adds Justin Jefferson. Combined: ~258.978 → **+25798**. Rounds the parlay out across five of the six games on this slate.

```json
TD_PARLAY_3_TEAM
[
  {"player": "Derrick Henry", "market_key": "player_anytime_td", "canonical_event_id": "2f5531b7c22a7a0d", "price": 1.417, "side": "over", "line": null, "reason": "91.7% RZ carry share vs. Dallas's run defense, collapsed 23rd to 30th.", "evidence_check": [{"type":"rank_shift","team":"DAL","side":"def","stat":"rush_ypg","claimed_rank_2025":23,"claimed_rank_2026":30}]},
  {"player": "George Kittle", "market_key": "player_anytime_td", "canonical_event_id": "272a59c2ac53fad2", "price": 2.75, "side": "over", "line": null, "reason": "Nuclear-tier Threat vs. Arizona's 30th-ranked TE defense.", "evidence_check": [{"type":"current_opponent","team":"ARI","pos":"TE","stat":"rec_yds","role":"def","claimed_rank":30}]},
  {"player": "Chris Olave", "market_key": "player_anytime_td", "canonical_event_id": "f4f6cd4ffcfac50b", "price": 2.55, "side": "over", "line": null, "reason": "2025 receptions rank (6th) converges with LV's 29th-ranked WR-catch defense.", "evidence_check": [{"type":"current_opponent","team":"LV","pos":"WR","stat":"rec","role":"def","claimed_rank":29}]}
]
```
```json
TD_PARLAY_4_TEAM
[
  {"player": "Derrick Henry", "market_key": "player_anytime_td", "canonical_event_id": "2f5531b7c22a7a0d", "price": 1.417, "side": "over", "line": null, "reason": "91.7% RZ carry share vs. Dallas's declining run defense.", "evidence_check": [{"type":"rank_shift","team":"DAL","side":"def","stat":"rush_ypg","claimed_rank_2025":23,"claimed_rank_2026":30}]},
  {"player": "George Kittle", "market_key": "player_anytime_td", "canonical_event_id": "272a59c2ac53fad2", "price": 2.75, "side": "over", "line": null, "reason": "Nuclear-tier Threat vs. Arizona's 30th-ranked TE defense.", "evidence_check": [{"type":"current_opponent","team":"ARI","pos":"TE","stat":"rec_yds","role":"def","claimed_rank":30}]},
  {"player": "Chris Olave", "market_key": "player_anytime_td", "canonical_event_id": "f4f6cd4ffcfac50b", "price": 2.55, "side": "over", "line": null, "reason": "2025 receptions rank converges with LV's 29th-ranked WR-catch defense.", "evidence_check": [{"type":"current_opponent","team":"LV","pos":"WR","stat":"rec","role":"def","claimed_rank":29}]},
  {"player": "Kyren Williams", "market_key": "player_anytime_td", "canonical_event_id": "94730ebf6b509215", "price": 1.952, "side": "over", "line": null, "reason": "66.7% RZ carry share vs. Denver's run defense, collapsed 2nd to 29th.", "evidence_check": [{"type":"rank_shift","team":"DEN","side":"def","stat":"rush_ypg","claimed_rank_2025":2,"claimed_rank_2026":29}]}
]
```
```json
TD_PARLAY_5_TEAM
[
  {"player": "Derrick Henry", "market_key": "player_anytime_td", "canonical_event_id": "2f5531b7c22a7a0d", "price": 1.417, "side": "over", "line": null, "reason": "91.7% RZ carry share vs. Dallas's declining run defense.", "evidence_check": [{"type":"rank_shift","team":"DAL","side":"def","stat":"rush_ypg","claimed_rank_2025":23,"claimed_rank_2026":30}]},
  {"player": "George Kittle", "market_key": "player_anytime_td", "canonical_event_id": "272a59c2ac53fad2", "price": 2.75, "side": "over", "line": null, "reason": "Nuclear-tier Threat vs. Arizona's 30th-ranked TE defense.", "evidence_check": [{"type":"current_opponent","team":"ARI","pos":"TE","stat":"rec_yds","role":"def","claimed_rank":30}]},
  {"player": "Chris Olave", "market_key": "player_anytime_td", "canonical_event_id": "f4f6cd4ffcfac50b", "price": 2.55, "side": "over", "line": null, "reason": "2025 receptions rank converges with LV's 29th-ranked WR-catch defense.", "evidence_check": [{"type":"current_opponent","team":"LV","pos":"WR","stat":"rec","role":"def","claimed_rank":29}]},
  {"player": "Kyren Williams", "market_key": "player_anytime_td", "canonical_event_id": "94730ebf6b509215", "price": 1.952, "side": "over", "line": null, "reason": "66.7% RZ carry share vs. Denver's collapsed run defense.", "evidence_check": [{"type":"rank_shift","team":"DEN","side":"def","stat":"rush_ypg","claimed_rank_2025":2,"claimed_rank_2026":29}]},
  {"player": "Saquon Barkley", "market_key": "player_anytime_td", "canonical_event_id": "f67d76e1f1c11441", "price": 1.87, "side": "over", "line": null, "reason": "Standard-tier Threat: 2025 rank 10th (71.2 ypg) vs. Chicago's 23rd-ranked run defense to backs.", "evidence_check": [{"type":"current_opponent","team":"CHI","pos":"RB","stat":"rush_yds","role":"def","claimed_rank":23}]}
]
```
```json
TD_PARLAY_6_TEAM
[
  {"player": "Derrick Henry", "market_key": "player_anytime_td", "canonical_event_id": "2f5531b7c22a7a0d", "price": 1.417, "side": "over", "line": null, "reason": "91.7% RZ carry share vs. Dallas's declining run defense.", "evidence_check": [{"type":"rank_shift","team":"DAL","side":"def","stat":"rush_ypg","claimed_rank_2025":23,"claimed_rank_2026":30}]},
  {"player": "George Kittle", "market_key": "player_anytime_td", "canonical_event_id": "272a59c2ac53fad2", "price": 2.75, "side": "over", "line": null, "reason": "Nuclear-tier Threat vs. Arizona's 30th-ranked TE defense.", "evidence_check": [{"type":"current_opponent","team":"ARI","pos":"TE","stat":"rec_yds","role":"def","claimed_rank":30}]},
  {"player": "Chris Olave", "market_key": "player_anytime_td", "canonical_event_id": "f4f6cd4ffcfac50b", "price": 2.55, "side": "over", "line": null, "reason": "2025 receptions rank converges with LV's 29th-ranked WR-catch defense.", "evidence_check": [{"type":"current_opponent","team":"LV","pos":"WR","stat":"rec","role":"def","claimed_rank":29}]},
  {"player": "Kyren Williams", "market_key": "player_anytime_td", "canonical_event_id": "94730ebf6b509215", "price": 1.952, "side": "over", "line": null, "reason": "66.7% RZ carry share vs. Denver's collapsed run defense.", "evidence_check": [{"type":"rank_shift","team":"DEN","side":"def","stat":"rush_ypg","claimed_rank_2025":2,"claimed_rank_2026":29}]},
  {"player": "Saquon Barkley", "market_key": "player_anytime_td", "canonical_event_id": "f67d76e1f1c11441", "price": 1.87, "side": "over", "line": null, "reason": "Standard-tier Threat vs. Chicago's 23rd-ranked run defense to backs.", "evidence_check": [{"type":"current_opponent","team":"CHI","pos":"RB","stat":"rush_yds","role":"def","claimed_rank":23}]},
  {"player": "Trey McBride", "market_key": "player_anytime_td", "canonical_event_id": "272a59c2ac53fad2", "price": 2.8, "side": "over", "line": null, "reason": "66.7% RZ target share; 2025 receptions rank (1st) converges with SF's 24th-ranked TE defense.", "evidence_check": [{"type":"current_opponent","team":"SF","pos":"TE","stat":"rec","role":"def","claimed_rank":24}]}
]
```
```json
TD_PARLAY_7_TEAM
[
  {"player": "Derrick Henry", "market_key": "player_anytime_td", "canonical_event_id": "2f5531b7c22a7a0d", "price": 1.417, "side": "over", "line": null, "reason": "91.7% RZ carry share vs. Dallas's declining run defense.", "evidence_check": [{"type":"rank_shift","team":"DAL","side":"def","stat":"rush_ypg","claimed_rank_2025":23,"claimed_rank_2026":30}]},
  {"player": "George Kittle", "market_key": "player_anytime_td", "canonical_event_id": "272a59c2ac53fad2", "price": 2.75, "side": "over", "line": null, "reason": "Nuclear-tier Threat vs. Arizona's 30th-ranked TE defense.", "evidence_check": [{"type":"current_opponent","team":"ARI","pos":"TE","stat":"rec_yds","role":"def","claimed_rank":30}]},
  {"player": "Chris Olave", "market_key": "player_anytime_td", "canonical_event_id": "f4f6cd4ffcfac50b", "price": 2.55, "side": "over", "line": null, "reason": "2025 receptions rank converges with LV's 29th-ranked WR-catch defense.", "evidence_check": [{"type":"current_opponent","team":"LV","pos":"WR","stat":"rec","role":"def","claimed_rank":29}]},
  {"player": "Kyren Williams", "market_key": "player_anytime_td", "canonical_event_id": "94730ebf6b509215", "price": 1.952, "side": "over", "line": null, "reason": "66.7% RZ carry share vs. Denver's collapsed run defense.", "evidence_check": [{"type":"rank_shift","team":"DEN","side":"def","stat":"rush_ypg","claimed_rank_2025":2,"claimed_rank_2026":29}]},
  {"player": "Saquon Barkley", "market_key": "player_anytime_td", "canonical_event_id": "f67d76e1f1c11441", "price": 1.87, "side": "over", "line": null, "reason": "Standard-tier Threat vs. Chicago's 23rd-ranked run defense to backs.", "evidence_check": [{"type":"current_opponent","team":"CHI","pos":"RB","stat":"rush_yds","role":"def","claimed_rank":23}]},
  {"player": "Trey McBride", "market_key": "player_anytime_td", "canonical_event_id": "272a59c2ac53fad2", "price": 2.8, "side": "over", "line": null, "reason": "66.7% RZ target share vs. SF's 24th-ranked TE defense.", "evidence_check": [{"type":"current_opponent","team":"SF","pos":"TE","stat":"rec","role":"def","claimed_rank":24}]},
  {"player": "Justin Jefferson", "market_key": "player_anytime_td", "canonical_event_id": "b13806c09a159b08", "price": 2.55, "side": "over", "line": null, "reason": "Highest target share on the slate (35.7%) vs. TB's 13th-ranked WR-TD defense.", "evidence_check": [{"type":"current_opponent","team":"TB","pos":"WR","stat":"td","role":"def","claimed_rank":13}]}
]
```