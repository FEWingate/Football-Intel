#!/usr/bin/env python3
"""
build_pick_breakdowns.py  -  the "VS" breakdown for every player-stat pick in the week's prop reports.

For each Passing / Rushing / Receiving yards or Receptions pick found in props_reports/wkNN (every batch plus
the whole-week file), this builds the same two-sided picture the Combo Props modal shows:
  left  = the player: season / last 3 / last 5 averages and his average against this tier of defense
  right = the defense: season / last 3 / last 5 allowed to his position and what it allows to players in his tier
Anytime TD, spread, moneyline and total picks are skipped (no yards-per-game comparison).

Free: no Coeus / API calls. Reads nflverse weekly stats (same download the combo builder uses) plus the
site's own matchup file, so ranks match the rest of the site.

    python3 build_pick_breakdowns.py            # writes intel/pick_breakdowns.json
Run it after generate_props_report.py (and again whenever new batches are added).
"""
import datetime
import json
import os
import sys

import build_combo_props as B

ROOT = B.ROOT
OUT = os.path.join(ROOT, "intel", "pick_breakdowns.json")
REPORTS = os.path.join(ROOT, "props_reports")

# market_key -> (nflverse column, label, matchup-file key per position)
SPEC = {
    "player_passing_yards": ("passing_yards", "Passing yds", {"QB": "pass_ypg"}),
    "player_rushing_yards": ("rushing_yards", "Rushing yds", {"RB": "rush_ypg", "QB": None}),
    "player_receiving_yards": ("receiving_yards", "Receiving yds", {"RB": "rec_ypg", "WR": "rec_ypg", "TE": "rec_ypg"}),
    "player_receptions": ("receptions", "Receptions", {"RB": "rec_pg", "WR": "rec_pg", "TE": "rec_pg"}),
}
UNIT = {"player_receptions": 1}


def collect_picks(week):
    """Every player-stat pick in this week's reports, de-duplicated by (player, market)."""
    wkdir = os.path.join(REPORTS, "wk%02d" % week)
    found = {}

    def walk(x):
        if isinstance(x, dict):
            if x.get("market_key") in SPEC and x.get("player"):
                found.setdefault((B.norm(x["player"]), x["market_key"]),
                                 {"player": x["player"], "market_key": x["market_key"],
                                  "eid": x.get("canonical_event_id")})
            for v in x.values():
                walk(v)
        elif isinstance(x, list):
            for v in x:
                walk(v)

    if not os.path.isdir(wkdir):
        return []
    for fn in sorted(os.listdir(wkdir)):
        if not fn.endswith(".json") or fn == "manifest.json" or fn.endswith("_graded.json"):
            continue
        d = B.load_json(os.path.join(wkdir, fn))
        if d:
            for k in ("prop_breakdown", "favorite_ou", "best_10", "parlays"):
                walk(d.get(k))
    return list(found.values())


def floor_ok(r, pos):
    if pos == "QB":
        return (r.get("attempts", 0) or 0) >= 10
    return (r.get("carries", 0) or 0) + (r.get("targets", 0) or 0) >= 3


def build():
    cur = B.load_json(B.CURRENT, {}) or {}
    season = int(cur.get("season") or datetime.date.today().year)
    week = int(cur.get("week") or 0)
    picks = collect_picks(week)
    if not picks:
        sys.exit("No player-stat picks found in props_reports/wk%02d - run generate_props_report.py first." % week)
    print("Found %d distinct player-stat picks for week %d." % (len(picks), week))

    print("Downloading nflverse weekly stats (%d)..." % season)
    full = B.fetch_season(season)
    if full is None:
        sys.exit("FATAL: no nflverse weekly stats for %d." % season)
    # Everything is computed as of BEFORE this week's games, so a played game never leaks into its own pick.
    df = full[full["week"] < week].copy()
    mu = B.load_matchup(week)
    threats = B.load_json(os.path.join(ROOT, "threats", "wk%02d.json" % week), {}) or {}
    feed = B.load_json(B.FEED, {}) or {}
    pl = B.load_json(B.PLAYERS, {}) or {}
    heads = {}
    for lst in (pl.get("players") or {}).values():
        for p in lst or []:
            if p.get("headshot"):
                heads[B.norm(p.get("name"))] = p["headshot"]
    events = {g.get("canonical_event_id"): (g.get("away_code"), g.get("home_code")) for g in feed.get("games", [])}

    ident = {}
    for _, r in full.sort_values("week").iterrows():
        ident[B.norm(r["player_display_name"])] = {"id": r["player_id"], "pos": r["position"], "team": r["team"],
                                                  "name": r["player_display_name"]}

    through = B.horizon_week(mu) or (week - 1)
    qb_rush = B.qb_rush_allowed(df, through)

    cache_def = {}

    def defense_tables(pos, stat):
        """season pg / last3 / last5 allowed to this position group, per defense, plus ranks (1 = toughest)."""
        key = (pos, stat)
        if key in cache_def:
            return cache_def[key]
        x = df[df["position"] == pos]
        g = x.groupby(["opponent_team", "week"])[stat].sum()
        weeks = df.groupby("opponent_team")["week"].apply(lambda w: sorted(set(int(v) for v in w)))

        def per(n):
            out = {}
            for t, wks in weeks.items():
                use = wks[-n:] if n else wks
                if len(use) < (2 if n else 1):
                    continue
                out[t] = {"pg": sum(float(g.get((t, w), 0.0)) for w in use) / len(use), "games": len(use)}
            return out
        season_t, l3, l5 = per(0), per(3), per(5)
        res = {"season": season_t, "last3": l3, "last5": l5,
               "r_season": B.rank_asc({t: v["pg"] for t, v in season_t.items()}),
               "r3": B.rank_asc({t: v["pg"] for t, v in l3.items()}),
               "r5": B.rank_asc({t: v["pg"] for t, v in l5.items()})}
        cache_def[key] = res
        return res

    def site_defense(pos, mk, stat):
        """The site's own season ranks/values (matchup file) when available, else the computed ones."""
        mkey = SPEC[mk][2].get(pos)
        vals, ranks = {}, {}
        if mu and mkey:
            for t, v in mu.get("teams", {}).items():
                e = ((v.get("def") or {}).get(pos) or {}).get(mkey) or {}
                if e.get("v") is not None and e.get("r") is not None:
                    vals[t], ranks[t] = e["v"], int(e["r"])
        if pos == "QB" and stat == "rushing_yards":
            vals, ranks = dict(qb_rush), B.rank_asc(qb_rush)
        if len(vals) < 20:
            tb = defense_tables(pos, stat)
            vals = {t: v["pg"] for t, v in tb["season"].items()}
            ranks = tb["r_season"]
        return vals, ranks

    cache_pr = {}

    def player_ranks(pos, stat):
        key = (pos, stat)
        if key in cache_pr:
            return cache_pr[key]
        x = df[df["position"] == pos].copy()
        if pos == "QB":
            x = x[x["attempts"].fillna(0) >= 15]
        else:
            x = x[(x["carries"].fillna(0) + x["targets"].fillna(0)) >= 6]
        x = x.sort_values("week")
        per = {}
        for pid, g in x.groupby("player_id"):
            v = [float(a or 0) for a in g[stat]]
            if len(v) < 3:
                continue
            per[pid] = {"season_avg": sum(v) / len(v), "l5_avg": sum(v[-5:]) / len(v[-5:]), "games": len(v)}

        def rk(k):
            order = sorted(per, key=lambda p: -per[p][k])
            return {p: i + 1 for i, p in enumerate(order)}
        rs, rl = rk("season_avg"), rk("l5_avg")
        n = len(per)
        res = {p: {"season_avg": round(v["season_avg"], 1), "season_rank": rs[p], "l5_avg": round(v["l5_avg"], 1),
                   "l5_rank": rl[p], "of": n, "games": v["games"]} for p, v in per.items()}
        cache_pr[key] = res
        return res

    cache_dvt = {}

    def def_vs_tiers(pos, stat):
        key = (pos, stat)
        if key in cache_dvt:
            return cache_dvt[key]
        prk = player_ranks(pos, stat)
        out = {}
        for _, r in df[df["position"] == pos].iterrows():
            if not floor_ok(r, pos):
                continue
            pk = prk.get(r["player_id"])
            if not pk:
                continue
            v = float(r.get(stat, 0) or 0)
            for t in (B.tier_rel(pk["season_rank"], pk["of"]), B.tier_rel_fine(pk["season_rank"], pk["of"])):
                if t:
                    out.setdefault(r["opponent_team"], {}).setdefault(t, []).append(v)
        cache_dvt[key] = out
        return out

    result, skipped = {}, []
    for p in picks:
        mk = p["market_key"]
        stat, label, _ = SPEC[mk]
        info = ident.get(B.norm(p["player"]))
        if not info:
            skipped.append((p["player"], "not found in nflverse stats"))
            continue
        pos, team, pid = info["pos"], info["team"], info["id"]
        if pos == "FB":
            pos = "RB"
        if pos not in ("QB", "RB", "WR", "TE") or SPEC[mk][2].get(pos, "x") == "x":
            skipped.append((p["player"], "%s %s not supported" % (pos, stat)))
            continue
        opp = (threats.get("teams", {}).get(team) or {}).get("opp")
        home = None
        if p.get("eid") in events:
            a, h = events[p["eid"]]
            if team in (a, h):
                opp, home = (h if team == a else a), (team == h)
        if not opp:
            skipped.append((p["player"], "no opponent found this week"))
            continue
        vals, ranks = site_defense(pos, mk, stat)
        r_opp = ranks.get(opp)
        if r_opp is None:
            skipped.append((p["player"], "no matchup rank for %s" % opp))
            continue
        tb = defense_tables(pos, stat)
        # the player's games (this season, before this week)
        rows = df[(df["player_id"] == pid)].sort_values("week")
        games = [{"week": int(r["week"]), "opp": r["opponent_team"], "v": float(r.get(stat, 0) or 0)}
                 for _, r in rows.iterrows() if floor_ok(r, pos)]
        series = [g["v"] for g in games]
        prk = player_ranks(pos, stat).get(pid)
        ptier = B.tier_rel(prk["season_rank"], prk["of"]) if prk else None
        pfine = B.tier_rel_fine(prk["season_rank"], prk["of"]) if prk else None
        tbd, tfd = B.tier_broad(r_opp), B.tier_fine(r_opp)
        prow = {"key": "a", "name": label, "season": B._avg(series), "last3": B._avg(series[-3:]), "last5": B._avg(series[-5:]),
                "opp_rank": r_opp, "opp_tier": tbd, "opp_tier_label": B.TIER_LABEL[tbd],
                "vs_tier": B._avg([g["v"] for g in games if ranks.get(g["opp"]) and B.tier_broad(ranks[g["opp"]]) == tbd]),
                "vs_fine": None}
        if tfd:
            prow["vs_fine"] = {"label": B.TIER_LABEL[tfd],
                               **B._avg([g["v"] for g in games if ranks.get(g["opp"]) and B.tier_fine(ranks[g["opp"]]) == tfd])}
        dvt = def_vs_tiers(pos, stat).get(opp, {})

        def tier_avg(t):
            return B._avg(dvt.get(t) or []) if t else None

        def rec(tag, rk):
            e = tb[tag].get(opp)
            return {"pg": round(e["pg"], 1), "games": e["games"], "rank": tb[rk].get(opp)} if e else None
        drow = {"key": "a", "name": label, "rank": r_opp,
                "season_pg": round(vals[opp], 1) if vals.get(opp) is not None else None,
                "last3": rec("last3", "r3"), "last5": rec("last5", "r5"),
                "vs_tier": tier_avg(ptier), "vs_fine": tier_avg(pfine)}
        bd = {"names": {"a": label}, "pos": pos, "season_games": len(games),
              "player_tier": ({"tier": ptier, "label": B.player_tier_label(ptier, prk["of"], pos) if ptier else None,
                               "fine": pfine, "fine_label": B.player_tier_label(pfine, prk["of"], pos) if pfine else None,
                               "rank": prk["season_rank"], "of": prk["of"]} if prk else None),
              "player": [prow], "defense": [drow]}
        key = "%s|%s" % (B.norm(p["player"]), mk)
        result[key] = {"player": info["name"], "team": team, "opp": opp, "home": home, "pos": pos, "market_key": mk,
                       "label": label, "headshot": heads.get(B.norm(p["player"]), ""),
                       "player_rank": prk, "breakdown": bd,
                       "log": [{"week": g["week"], "opp": g["opp"], "v": g["v"]} for g in games]}

    out = {"generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
           "season": season, "week": week, "through_week": through, "picks": result}
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as f:
        json.dump(out, f, separators=(",", ":"))
    print("Wrote %s - %d breakdowns (%d skipped)." % (os.path.relpath(OUT, ROOT), len(result), len(skipped)))
    for n, why in skipped:
        print("  skipped %s: %s" % (n, why))


if __name__ == "__main__":
    build()
