#!/usr/bin/env python3
"""
BUILD_COMBO_PROPS.PY
====================
Projects FanDuel's two COMBINED yardage props and compares them with the line:

  * RB  Rushing + Receiving yards   (market "rush_rec")
  * QB  Passing + Rushing yards     (market "pass_rush")

Writes intel/combo_props.json, which the "Combo Props" tab in Intel Reports reads.

WHERE THE LINES COME FROM
  1. manual_combo_lines.json  - real FanDuel combo lines you type in (always wins).
  2. fanduel_props/latest.json - only has the SEPARATE markets (pass / rush / rec). Players with both
     halves posted are listed as candidates with an "implied" line (the two halves added). The implied
     line is NOT FanDuel's line: on 2026-10-19 FanDuel's real combo lines ran 7.5-11.5 yards above the
     sum of the halves, so the page tells you to enter the real line before trusting any edge.

HOW THE PROJECTION WORKS (no AI; Coeus only comments afterwards)
  - Each half (rush, rec, pass) is a recency-weighted average of the player's real game log
    (nflverse weekly stats, this season plus last season, half-life 3 games). Games where the player
    barely played (QB < 15 attempts, RB < 6 touches+targets) are skipped so injury exits don't drag it.
  - Each half is scaled by how many yards the opponent allows to that position group versus the league
    (this season blended with last season, then shrunk halfway toward 1.0).
  - Spread of outcomes comes from the player's own game-to-game variance blended with a typical
    variance for the position, then a normal curve turns "projection vs line" into P(over).
  - Edge = P(side) minus the break-even probability of the price. It is an uncalibrated model, not a
    guarantee; results are tracked so you can see if it earns trust.

USAGE
  python3 build_combo_props.py                 # projections only
  python3 build_combo_props.py --coeus         # also ask Coeus for a pick on candidates with a real line
  python3 build_combo_props.py --coeus --model claude-sonnet-5

  # type in a real FanDuel combo line (writes manual_combo_lines.json), then rebuild:
  python3 build_combo_props.py --add "Jayden Daniels" pass_rush 254.5 -113 -113
  python3 build_combo_props.py --add "Christian McCaffrey" rush_rec 106.5 -113 -113
  (market is pass_rush for QBs, rush_rec for RBs; prices are optional and default to -113)
"""
import argparse, json, math, os, re, sys, datetime
from io import StringIO

import pandas as pd
import requests

ROOT = os.path.dirname(os.path.abspath(__file__))
FEED = os.path.join(ROOT, "fanduel_props", "latest.json")
MANUAL = os.path.join(ROOT, "manual_combo_lines.json")
OUT = os.path.join(ROOT, "intel", "combo_props.json")
PLAYERS = os.path.join(ROOT, "players", "latest.json")
CURRENT = os.path.join(ROOT, "matchup", "current.json")

URL = "https://github.com/nflverse/nflverse-data/releases/download/stats_player/stats_player_week_%d.csv"
TEAM_FIX = {"LA": "LAR", "JAC": "JAX", "WSH": "WAS", "ARZ": "ARI", "BLT": "BAL", "CLV": "CLE", "HST": "HOU"}
HALF_LIFE = 3.0
SHRINK = 0.5            # opponent factor shrunk this far toward 1.0
PRIOR_GAMES = 6         # last season counts as this many games of opponent-allowed history
CV = {"QB": 0.28, "RB": 0.38}   # typical game-to-game spread (as share of the mean) for each position
K_PSEUDO = 4
LEAN_EDGE = 0.04
STRONG_EDGE = 0.08
DEFAULT_PRICE = -113
MAX_GAP = 0.12          # projection more than 12% away from the line -> flag CHECK instead of LEAN/STRONG

MARKETS = {
    "pass_rush": {"pos": "QB", "label": "Passing + Rushing Yds", "a": "passing_yards", "b": "rushing_yards",
                  "a_name": "Passing yds", "b_name": "Rushing yds",
                  "feed_a": "passing_yards", "feed_b": "rushing_yards"},
    "rush_rec": {"pos": "RB", "label": "Rushing + Receiving Yds", "a": "rushing_yards", "b": "receiving_yards",
                 "a_name": "Rushing yds", "b_name": "Receiving yds",
                 "feed_a": "rushing_yards", "feed_b": "receiving_yards"},
}


def tm(t):
    t = str(t or "").upper()
    return TEAM_FIX.get(t, t)


def norm(n):
    return re.sub(r"\s+", " ", re.sub(r"[^a-z ]", " ", re.sub(r"[.'’]", "", str(n or "").lower())
                  .replace(" jr", "").replace(" sr", "").replace(" iii", "").replace(" ii", ""))).strip()


def phi(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def price_to_prob(p):
    """American (|p|>=100) or decimal price -> break-even probability."""
    if p is None:
        p = DEFAULT_PRICE
    p = float(p)
    if abs(p) >= 100:
        return (-p) / (-p + 100) if p < 0 else 100 / (p + 100)
    return 1 / p if p > 1 else 0.5


def fetch_season(season):
    r = requests.get(URL % season, timeout=120)
    if r.status_code != 200:
        print("  no nflverse weekly file for %d (HTTP %s)" % (season, r.status_code))
        return None
    df = pd.read_csv(StringIO(r.text), low_memory=False)
    df = df[df["season_type"] == "REG"].copy()
    df["team"] = df["team"].map(tm)
    df["opponent_team"] = df["opponent_team"].map(tm)
    return df


def load_json(path, default=None):
    try:
        with open(path) as f:
            return json.load(f)
    except (OSError, ValueError):
        return default


# ---------------------------------------------------------------- opponent allowed
def allowed_table(frames, pos, cols):
    """Per defense: yards allowed per game to that position group, per stat, blending seasons."""
    out = {}
    cur, prev = frames.get("cur"), frames.get("prev")
    for stat in cols:
        per = {}
        for tag, df in (("cur", cur), ("prev", prev)):
            if df is None:
                continue
            x = df[df["position"] == pos]
            g = x.groupby(["opponent_team", "season", "week"])[stat].sum().reset_index()
            per[tag] = g.groupby("opponent_team")[stat].agg(["sum", "count"])
        teams = set()
        for v in per.values():
            teams |= set(v.index)
        blended = {}
        for t in teams:
            s_c, n_c = (per["cur"].loc[t] if "cur" in per and t in per["cur"].index else (0.0, 0))
            s_p, n_p = (per["prev"].loc[t] if "prev" in per and t in per["prev"].index else (0.0, 0))
            prior_mean = (s_p / n_p) if n_p else None
            if prior_mean is None and not n_c:
                continue
            if prior_mean is None:
                blended[t] = (s_c / n_c, n_c)
            else:
                blended[t] = ((s_c + PRIOR_GAMES * prior_mean) / (n_c + PRIOR_GAMES), n_c)
        lg = sum(v[0] for v in blended.values()) / max(1, len(blended))
        out[stat] = {t: {"allowed_pg": round(v[0], 1), "games": int(v[1]),
                         "factor": round(1 + SHRINK * (v[0] / lg - 1), 3) if lg else 1.0,
                         "raw_ratio": round(v[0] / lg, 3) if lg else 1.0} for t, v in blended.items()}
        out[stat]["_league_pg"] = round(lg, 1)
    return out


# ---------------------------------------------------------------- player game logs
def player_log(frames, pid, mk):
    cfg = MARKETS[mk]
    rows = []
    for tag in ("prev", "cur"):
        df = frames.get(tag)
        if df is None:
            continue
        x = df[df["player_id"] == pid].sort_values("week")
        for _, r in x.iterrows():
            if cfg["pos"] == "QB":
                usage = r.get("attempts", 0) or 0
                if usage < 15:
                    continue
            else:
                usage = (r.get("carries", 0) or 0) + (r.get("targets", 0) or 0)
                if usage < 6:
                    continue
            a, b = float(r.get(cfg["a"], 0) or 0), float(r.get(cfg["b"], 0) or 0)
            rows.append({"season": int(r["season"]), "week": int(r["week"]), "opp": r["opponent_team"],
                         "a": a, "b": b, "total": a + b})
    return rows


def weighted(values):
    n = len(values)
    ws = [0.5 ** ((n - 1 - i) / HALF_LIFE) for i in range(n)]
    sw = sum(ws)
    mean = sum(w * v for w, v in zip(ws, values)) / sw if sw else 0.0
    var = sum(w * (v - mean) ** 2 for w, v in zip(ws, values)) / sw if sw else 0.0
    return mean, math.sqrt(var), sw


def project(log, mk, opp, allowed):
    cfg = MARKETS[mk]
    if not log:
        return None
    a_vals, b_vals, t_vals = [x["a"] for x in log], [x["b"] for x in log], [x["total"] for x in log]
    a_mean, _, _ = weighted(a_vals)
    b_mean, _, _ = weighted(b_vals)
    t_mean, t_sd, sw = weighted(t_vals)
    fa = (allowed.get(cfg["a"], {}).get(opp) or {}).get("factor", 1.0)
    fb = (allowed.get(cfg["b"], {}).get(opp) or {}).get("factor", 1.0)
    proj = a_mean * fa + b_mean * fb
    n = len(log)
    typical = CV[cfg["pos"]] * proj
    sd = math.sqrt((n * t_sd ** 2 + K_PSEUDO * typical ** 2) / (n + K_PSEUDO))
    sd = max(sd, 0.18 * proj, 5.0)
    return {"proj_total": round(proj, 1), "sd": round(sd, 1), "games_used": n,
            "components": [
                {"name": cfg["a_name"], "weighted_avg": round(a_mean, 1), "opp_factor": fa, "proj": round(a_mean * fa, 1),
                 "opp_allowed_pg": (allowed.get(cfg["a"], {}).get(opp) or {}).get("allowed_pg"),
                 "league_pg": allowed.get(cfg["a"], {}).get("_league_pg")},
                {"name": cfg["b_name"], "weighted_avg": round(b_mean, 1), "opp_factor": fb, "proj": round(b_mean * fb, 1),
                 "opp_allowed_pg": (allowed.get(cfg["b"], {}).get(opp) or {}).get("allowed_pg"),
                 "league_pg": allowed.get(cfg["b"], {}).get("_league_pg")}]}


def evaluate(mean, sd, point, over_price, under_price):
    z = (point - mean) / sd
    p_over = 1 - phi(z)
    p_under = phi(z)
    be_o, be_u = price_to_prob(over_price), price_to_prob(under_price)
    e_o, e_u = p_over - be_o, p_under - be_u
    side, edge, p = ("OVER", e_o, p_over) if e_o >= e_u else ("UNDER", e_u, p_under)
    lean = "STRONG" if edge >= STRONG_EDGE else ("LEAN" if edge >= LEAN_EDGE else "PASS")
    gap = abs(mean - point) / point if point else 0.0
    if lean != "PASS" and gap > MAX_GAP:
        lean = "CHECK"   # the model is far from the market: more likely a model blind spot than a real edge
    return {"market_gap_pct": round(100 * gap, 1), "p_over": round(p_over, 3), "p_under": round(p_under, 3), "best_side": side, "best_p": round(p, 3),
            "edge": round(edge, 3), "edge_yards": round(mean - point, 1), "lean": lean}


def game_context(feed):
    ctx = {}
    for g in (feed or {}).get("games", []):
        gl = g.get("game_lines") or {}
        spread = {}
        for o in gl.get("spreads") or []:
            spread[o.get("name")] = o.get("point")
        tot = next((o.get("point") for o in (gl.get("totals") or []) if o.get("name") == "Over"), None)
        away, home = g.get("away_code"), g.get("home_code")
        sa = spread.get(g.get("away_team"))
        sh = spread.get(g.get("home_team"))
        ctx[(away, home)] = {"away": away, "home": home, "commence_time": g.get("commence_time"),
                             "away_spread": sa, "home_spread": sh, "total": tot,
                             "away_implied": round(tot / 2 + (-sa) / 2, 1) if tot is not None and sa is not None else None,
                             "home_implied": round(tot / 2 + (-sh) / 2, 1) if tot is not None and sh is not None else None}
    return ctx


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--coeus", action="store_true", help="ask Coeus for a pick on every row that has a real line")
    ap.add_argument("--model", default="claude-sonnet-5")
    ap.add_argument("--add", nargs="+", metavar=("PLAYER", "MARKET"),
                    help='PLAYER MARKET LINE [OVER_PRICE [UNDER_PRICE]] - save a real FanDuel combo line, then continue')
    a = ap.parse_args()
    if a.add:
        add_manual_line(a.add)
        print("Now rebuild with: python3 build_combo_props.py")
        return

    cur = load_json(CURRENT, {}) or {}
    season = int(cur.get("season") or datetime.date.today().year)
    week = int(cur.get("week") or 0)
    feed = load_json(FEED, {}) or {}
    manual = load_json(MANUAL, {}) or {}
    pl = load_json(PLAYERS, {}) or {}
    heads = {}
    for lst in (pl.get("players") or {}).values():
        for p in lst or []:
            if p.get("headshot"):
                heads[norm(p.get("name"))] = p["headshot"]

    print("Downloading nflverse weekly stats (%d and %d)..." % (season, season - 1))
    frames = {"cur": fetch_season(season), "prev": fetch_season(season - 1)}
    if frames["cur"] is None and frames["prev"] is None:
        sys.exit("FATAL: no nflverse weekly player stats available.")
    base = frames["cur"] if frames["cur"] is not None else frames["prev"]
    ident = {}
    for _, r in base.sort_values(["season", "week"]).iterrows():
        ident[norm(r["player_display_name"])] = {"id": r["player_id"], "pos": r["position"], "team": r["team"],
                                                 "name": r["player_display_name"]}
    if frames["cur"] is not None and frames["prev"] is not None:
        for _, r in frames["prev"].sort_values("week").iterrows():
            k = norm(r["player_display_name"])
            if k not in ident:
                ident[k] = {"id": r["player_id"], "pos": r["position"], "team": r["team"], "name": r["player_display_name"]}

    allowed = {"QB": allowed_table(frames, "QB", ["passing_yards", "rushing_yards"]),
               "RB": allowed_table(frames, "RB", ["rushing_yards", "receiving_yards"])}
    ctx = game_context(feed)

    # --- candidate list: every manual line + every feed player with both halves posted
    cands = {}

    def add(name, mk, game):
        key = (norm(name), mk)
        if key not in cands:
            cands[key] = {"name": name, "market": mk, "game": game, "line": None, "feed_a": None, "feed_b": None}
        return cands[key]

    for g in feed.get("games", []):
        pp = g.get("player_props") or {}
        game = (g.get("away_code"), g.get("home_code"))
        for mk, cfg in MARKETS.items():
            A = pp.get(cfg["feed_a"]) or {}
            B = pp.get(cfg["feed_b"]) or {}
            for name in set(A) & set(B):
                info = ident.get(norm(name))
                if not info or info["pos"] != cfg["pos"]:
                    continue
                c = add(name, mk, game)
                c["feed_a"] = (A[name].get("line") or {}).get("point")
                c["feed_b"] = (B[name].get("line") or {}).get("point")
    for ln in manual.get("lines", []):
        mk = ln.get("market")
        if mk not in MARKETS:
            continue
        info = ident.get(norm(ln.get("player")))
        game = None
        if info:
            for (aw, hm) in ctx:
                if info["team"] in (aw, hm):
                    game = (aw, hm)
        c = add(ln["player"], mk, game)
        c["line"] = {"point": ln.get("line"), "over_price": ln.get("over_price"), "under_price": ln.get("under_price"),
                     "alts": ln.get("alts") or [], "source": ln.get("source", "manual")}
        if game is None and ln.get("team"):
            c["game"] = next(((aw, hm) for (aw, hm) in ctx if ln["team"] in (aw, hm)), None)

    rows = []
    for (_, mk), c in sorted(cands.items(), key=lambda kv: kv[0]):
        info = ident.get(norm(c["name"]))
        if not info:
            print("  skipped %s: not found in nflverse weekly stats" % c["name"])
            continue
        game = c["game"]
        g = ctx.get(game) if game else None
        team = info["team"]
        opp = home = None
        if game:
            opp = game[1] if team == game[0] else game[0]
            home = (team == game[1])
        log = player_log(frames, info["id"], mk)
        proj = project(log, mk, opp, allowed[MARKETS[mk]["pos"]]) if opp else None
        row = {"player": info["name"], "team": team, "opp": opp, "home": home, "pos": info["pos"], "market": mk,
               "market_label": MARKETS[mk]["label"], "headshot": heads.get(norm(info["name"]), ""),
               "game": ({"commence_time": g["commence_time"],
                         "team_spread": (g["home_spread"] if home else g["away_spread"]),
                         "total": g["total"],
                         "team_implied": (g["home_implied"] if home else g["away_implied"])} if g else None),
               "feed_halves": {"a": c["feed_a"], "b": c["feed_b"]},
               "implied_line": (round(c["feed_a"] + c["feed_b"], 1) if c["feed_a"] is not None and c["feed_b"] is not None else None),
               "line": c["line"], "projection": proj,
               "log": [{"season": x["season"], "week": x["week"], "opp": x["opp"], "a": x["a"], "b": x["b"], "total": x["total"]}
                       for x in log[-10:]]}
        if proj and c["line"] and c["line"].get("point") is not None:
            row["eval"] = evaluate(proj["proj_total"], proj["sd"], float(c["line"]["point"]),
                                   c["line"].get("over_price"), c["line"].get("under_price"))
            row["under_price_assumed"] = c["line"].get("under_price") is None
            alts = []
            for al in c["line"].get("alts") or []:
                if al.get("line") is None:
                    continue
                ev = evaluate(proj["proj_total"], proj["sd"], float(al["line"]), al.get("over_price"), al.get("under_price"))
                alts.append({**al, "eval": ev})
            row["alts_eval"] = alts
        rows.append(row)
        if row.get("eval"):
            print("  %-22s %-9s proj %-6s sd %-5s line %-6s -> %s %s (edge %+.1f pts, gap %.0f%%)" % (
                info["name"], mk, proj["proj_total"], proj["sd"], c["line"]["point"], row["eval"]["lean"],
                row["eval"]["best_side"], 100 * row["eval"]["edge"], row["eval"]["market_gap_pct"]))

    print("  (%d more candidates have both halves posted but no real combo line yet)" % sum(1 for r in rows if not r.get("eval")))
    out = {"generated_at": datetime.datetime.utcnow().isoformat(timespec="seconds") + "Z", "season": season, "week": week,
           "method": {"half_life_games": HALF_LIFE, "opp_shrink": SHRINK, "lean_edge": LEAN_EDGE, "strong_edge": STRONG_EDGE,
                      "note": "Uncalibrated projection; outcomes are tracked in results/combo_picks.json"},
           "allowed": {pos: {stat: {"league_pg": v.get("_league_pg")} for stat, v in d.items()} for pos, d in allowed.items()},
           "rows": rows}

    if a.coeus:
        coeus_picks(out, a.model)

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as f:
        json.dump(out, f, indent=1)
    print("\nWrote %s - %d rows (%d with a real line)" % (OUT, len(rows), sum(1 for r in rows if r.get("eval"))))
    save_picks(out)


def add_manual_line(args):
    if len(args) < 3 or args[1] not in MARKETS:
        sys.exit('Usage: --add "Player Name" pass_rush|rush_rec LINE [OVER_PRICE [UNDER_PRICE]]')
    name, mk, line = args[0], args[1], float(args[2])
    over = float(args[3]) if len(args) > 3 else None
    under = float(args[4]) if len(args) > 4 else None
    cur = load_json(CURRENT, {}) or {}
    data = load_json(MANUAL, {}) or {}
    data.setdefault("lines", [])
    data["lines"] = [x for x in data["lines"] if not (norm(x.get("player")) == norm(name) and x.get("market") == mk)]
    data["lines"].append({"player": name, "market": mk, "line": line, "over_price": over, "under_price": under,
                          "source": "manual (typed from FanDuel)", "week": cur.get("week")})
    with open(MANUAL, "w") as f:
        json.dump(data, f, indent=1)
    print("Saved %s %s %s" % (name, mk, line))


def save_picks(out):
    """Keep a pick history so the results can be graded after the games."""
    path = os.path.join(ROOT, "results", "combo_picks.json")
    hist = load_json(path, {"picks": []}) or {"picks": []}
    by = {(p["season"], p["week"], p["player"], p["market"]): p for p in hist["picks"]}
    for r in out["rows"]:
        ev = r.get("eval")
        if not ev:
            continue
        k = (out["season"], out["week"], r["player"], r["market"])
        old = by.get(k)
        if old and old.get("graded"):
            continue
        by[k] = {"season": out["season"], "week": out["week"], "player": r["player"], "team": r["team"], "opp": r["opp"],
                 "market": r["market"], "line": r["line"]["point"], "over_price": r["line"].get("over_price"),
                 "under_price": r["line"].get("under_price"), "proj": r["projection"]["proj_total"],
                 "sd": r["projection"]["sd"], "model_side": ev["best_side"], "model_lean": ev["lean"], "model_edge": ev["edge"],
                 "coeus_pick": (r.get("coeus") or {}).get("pick"), "saved_at": out["generated_at"], "graded": False}
    hist["picks"] = sorted(by.values(), key=lambda p: (p["season"], p["week"], p["player"], p["market"]))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(hist, f, indent=1)
    print("Pick history saved to results/combo_picks.json (%d entries)" % len(hist["picks"]))


COEUS_SYSTEM = """You are Coeus, the NFL prop analyst inside Football Intel. You are given rows for FanDuel's combined
yardage props (QB passing + rushing yards, RB rushing + receiving yards). Each row has a statistical projection,
the FanDuel line, the player's recent games, opponent factors and game script (spread, total, team implied points).

For every row return a pick: OVER, UNDER or PASS. Rules:
- Treat the model projection as one input, not the answer. It does not know about injuries, role changes, blowout
  risk or game script beyond what is shown; weigh those and say so when they change your view.
- Use only the numbers provided. Never invent injuries, news or stats. Do not mention data that is absent.
- A model lean of CHECK means the projection is more than 12% away from FanDuel's line; treat that as a warning
  that the model may be missing something (role change, game script) and only side with the model if the data shown supports it.
- If edge is under about 3 percentage points or the sample is thin, prefer PASS unless a clear football reason
  supports a side.
- confidence is an integer 1-5 (5 = strongest).
- reasoning: 2-4 plain sentences naming the specific numbers that drive the pick (projection vs line, recent
  totals, opponent allowance, script).
Return ONLY JSON: {"picks": [{"player": "...", "market": "pass_rush|rush_rec", "pick": "OVER|UNDER|PASS",
"confidence": 1-5, "reasoning": "..."}]}"""


def coeus_picks(out, model):
    try:
        import anthropic
    except ImportError:
        sys.exit("FATAL: pip install anthropic --break-system-packages")
    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("FATAL: ANTHROPIC_API_KEY not set.")
    items = []
    for r in out["rows"]:
        if not r.get("eval"):
            continue
        items.append({"player": r["player"], "team": r["team"], "opp": r["opp"], "home": r["home"], "market": r["market"],
                      "fanduel_line": r["line"]["point"], "over_price": r["line"].get("over_price"),
                      "under_price": r["line"].get("under_price"), "game": r["game"],
                      "projection": r["projection"], "model": r["eval"], "recent_games_oldest_to_newest": r["log"]})
    if not items:
        print("Coeus: no rows with a real FanDuel line yet - nothing to pick.")
        return
    client = anthropic.Anthropic()
    print("Asking Coeus about %d rows..." % len(items))
    resp = client.messages.create(model=model, max_tokens=4000, system=COEUS_SYSTEM,
                                  messages=[{"role": "user", "content": json.dumps({"rows": items})}])
    txt = "".join(b.text for b in resp.content if getattr(b, "type", "") == "text")
    m = re.search(r"\{.*\}", txt, re.S)
    try:
        picks = json.loads(m.group(0))["picks"]
    except Exception:
        print("WARNING: could not parse Coeus's reply; saving raw text.")
        out["coeus_raw"] = txt
        return
    by = {(norm(p.get("player")), p.get("market")): p for p in picks}
    for r in out["rows"]:
        p = by.get((norm(r["player"]), r["market"]))
        if p:
            r["coeus"] = {"pick": p.get("pick"), "confidence": p.get("confidence"), "reasoning": p.get("reasoning"),
                          "model": model}
    u = getattr(resp, "usage", None)
    if u:
        print("Coeus tokens: %s in / %s out" % (u.input_tokens, u.output_tokens))


if __name__ == "__main__":
    main()
