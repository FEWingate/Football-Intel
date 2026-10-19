#!/usr/bin/env python3
"""
pff_coverage.py - LOCAL, PRIVATE: builds private/pff/coverage_context.json from the PFF facet pulls.

Run after pff_facets.py (it reads private/pff/facet_*.json):
  python3 pff_facets.py && python3 pff_coverage.py

Per team (FI team codes) it writes:
  defense.man_zone      - how the defense splits coverage snaps man vs zone, and what it allows vs each
                          (yards/target, catch %, TDs, INTs) with league ranks (1 = best defense)
  defense.defenders     - the team's top coverage defenders (CB/S/LB) with PFF coverage grade, targets,
                          catch rate, yards/coverage snap, QB rating against, and each defender's man vs zone line
  offense.receivers     - the team's receivers' man vs zone lines (targets, catches, yards, yprr, EPA, route grade)
  offense.passing_proxy - TEAM passing production vs man and vs zone, summed from every receiver's charted man/zone
                          line (targets stand in for attempts). NOT QB-specific: it leaves out sacks, scrambles and
                          throwaways, and mixes QBs if a team used more than one (flagged via multi_qb).
Private data: never committed (private/pff/ is gitignored). Merged into the model input only, via pff_context.py.
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
PRIV = os.path.join(ROOT, "private", "pff")
PFF_TO_FI = {"ARZ": "ARI", "BLT": "BAL", "CLV": "CLE", "HST": "HOU", "JAC": "JAX", "WSH": "WAS", "LA": "LAR"}
DB_POS = {"CB", "S", "FS", "SS", "LB", "SLOT"}
MIN_COV_SNAPS = 15


def current_season():
    """PFF's facet files carry no season field, so take it from matchup/current.json (the site's own week pointer)."""
    try:
        return int(json.load(open(os.path.join(ROOT, "matchup", "current.json"))).get("season"))
    except (OSError, ValueError, TypeError):
        return None


def load(name):
    try:
        return json.load(open(os.path.join(PRIV, name)))
    except (OSError, ValueError):
        return None


def rows_of(d, key):
    return (d or {}).get(key) or []


def code(t):
    return PFF_TO_FI.get(t, t)


def n(x):
    return x if isinstance(x, (int, float)) else 0


def rate(a, b, dec=2):
    return round(a / b, dec) if b else None


def pct(a, b):
    return round(100 * a / b, 1) if b else None


META = {"draft_season", "eligible_season", "franchise_id", "jersey_number", "player", "player_id", "player_game_count",
        "position", "status", "team", "team_name", "base_snap_counts_coverage", "base_targets", "declined_penalties", "penalties"}


def side(r, p):
    """Every column PFF gave for one scheme ('man' or 'zone'), prefix stripped."""
    pre = p + "_"
    return {k[len(pre):]: v for k, v in r.items() if k.startswith(pre)}


def season_line(b):
    return {k: v for k, v in b.items() if k not in META}


def rank_dict(vals, reverse=False):
    ordered = sorted([k for k in vals if vals[k] is not None], key=lambda k: vals[k], reverse=reverse)
    return {k: i + 1 for i, k in enumerate(ordered)}


SUM_KEYS = ("targets", "receptions", "yards", "touchdowns", "interceptions", "drops")


def passer_rating(att, comp, yds, td, ints):
    """NFL passer rating from attempts/completions/yards/TD/INT (targets stand in for attempts)."""
    if not att:
        return None
    a = min(max((comp / att - 0.3) * 5, 0), 2.375)
    b = min(max((yds / att - 3) * 0.25, 0), 2.375)
    c = min(max(td / att * 20, 0), 2.375)
    d = min(max(2.375 - ints / att * 25, 0), 2.375)
    return round((a + b + c + d) / 6 * 100, 1)


def passing_proxy(rcv_rows, qb_rows):
    """Team passing production vs man/zone, summed from receivers. Returns {team: block}."""
    agg = {}
    have_int = False
    for r in rcv_rows:
        t = code(r.get("team"))
        if not t:
            continue
        a = agg.setdefault(t, {p: dict.fromkeys(SUM_KEYS, 0) for p in ("man", "zone")})
        for p in ("man", "zone"):
            for k in SUM_KEYS:
                v = r.get(p + "_" + k)
                if isinstance(v, (int, float)):
                    a[p][k] += v
                    if k == "interceptions":
                        have_int = True
    qbs = {}
    for r in qb_rows:
        t = code(r.get("team"))
        att = n(r.get("attempts")) or n(r.get("passing_snaps")) or n(r.get("dropbacks"))
        if t and att:
            qbs.setdefault(t, []).append({"player": r.get("player"), "attempts": int(att)})
    out = {}
    for t, a in agg.items():
        block = {}
        for p in ("man", "zone"):
            q = a[p]
            tg = q["targets"]
            line = {k: (int(q[k]) if float(q[k]).is_integer() else q[k]) for k in SUM_KEYS}
            line.update({"catch_pct": pct(q["receptions"], tg), "yards_per_target": rate(q["yards"], tg),
                         "td_pct": pct(q["touchdowns"], tg),
                         "passer_rating": passer_rating(tg, q["receptions"], q["yards"], q["touchdowns"], q["interceptions"])
                         if have_int else None})
            block[p] = line
        tot = block["man"]["targets"] + block["zone"]["targets"]
        block["man_share_pct"] = pct(block["man"]["targets"], tot)
        lst = sorted(qbs.get(t, []), key=lambda x: -x["attempts"])
        total_att = sum(x["attempts"] for x in lst)
        for x in lst:
            x["share_pct"] = pct(x["attempts"], total_att)
        block["qbs"] = lst[:3]
        block["multi_qb"] = len(lst) > 1 and lst[1]["attempts"] >= 0.15 * total_att
        out[t] = block
    for p in ("man", "zone"):
        ranks = rank_dict({t: b[p]["yards_per_target"] for t, b in out.items()}, reverse=True)  # 1 = best offense
        for t, b in out.items():
            b[p]["yards_per_target_rank"] = ranks.get(t)
    for t, b in out.items():
        b["note"] = ("Summed from receivers' PFF man/zone charting (targets stand in for attempts). Not QB-specific: "
                     "excludes sacks, scrambles and throwaways, and mixes QBs when a team used more than one. "
                     "Rank 1 = best offense (most yards per target).")
    return out


def main():
    cov = load("facet_defense_coverage.json")
    sch = load("facet_defense_coverage_scheme.json")
    rcv = load("facet_receiving_scheme.json")
    if not (cov or sch or rcv):
        sys.exit("No facet files found - run pff_facets.py first.")
    cov_rows = rows_of(cov, "coverage_summary")
    sch_rows = rows_of(sch, "coverage_scheme")
    rcv_rows = rows_of(rcv, "receiving_scheme")
    pos_seen = {}
    for r in sch_rows + cov_rows:
        pos_seen[r.get("position")] = pos_seen.get(r.get("position"), 0) + 1
    print("defender positions seen:", dict(sorted(pos_seen.items(), key=lambda kv: -kv[1])))

    teams = {}

    def T(t):
        return teams.setdefault(t, {"defense": {}, "offense": {}})

    # ---- team man/zone totals from every defender's scheme split ----
    tot = {}
    for r in sch_rows:
        t = code(r.get("team"))
        if not t:
            continue
        a = tot.setdefault(t, {"man": dict.fromkeys(("snaps", "targets", "rec", "yards", "td", "int"), 0),
                               "zone": dict.fromkeys(("snaps", "targets", "rec", "yards", "td", "int"), 0)})
        for p in ("man", "zone"):
            a[p]["snaps"] += n(r.get(p + "_snap_counts_coverage"))
            a[p]["targets"] += n(r.get(p + "_targets"))
            a[p]["rec"] += n(r.get(p + "_receptions"))
            a[p]["yards"] += n(r.get(p + "_yards"))
            a[p]["td"] += n(r.get(p + "_touchdowns"))
            a[p]["int"] += n(r.get(p + "_interceptions"))
    man_pct, ypt_man, ypt_zone = {}, {}, {}
    for t, a in tot.items():
        s = a["man"]["snaps"] + a["zone"]["snaps"]
        man_pct[t] = pct(a["man"]["snaps"], s)
        ypt_man[t] = rate(a["man"]["yards"], a["man"]["targets"])
        ypt_zone[t] = rate(a["zone"]["yards"], a["zone"]["targets"])
    r_man_rate = rank_dict(man_pct, reverse=True)          # 1 = plays the most man
    r_man_ypt = rank_dict(ypt_man)                         # 1 = allows fewest yards/target vs man
    r_zone_ypt = rank_dict(ypt_zone)
    for t, a in tot.items():
        s = a["man"]["snaps"] + a["zone"]["snaps"]
        out = {"man_pct": man_pct[t], "zone_pct": round(100 - man_pct[t], 1) if man_pct[t] is not None else None,
               "man_rate_rank_most_man_is_1": r_man_rate.get(t),
               "rank_note": "rank 1 = best defense (fewest yards per target allowed). Counts only plays PFF charted as man or zone; other plays are not in these totals."}
        for p in ("man", "zone"):
            q = a[p]
            out["vs_" + p] = {"targets": q["targets"], "receptions": q["rec"], "yards": q["yards"],
                              "tds": q["td"], "ints": q["int"],
                              "yards_per_target": rate(q["yards"], q["targets"]),
                              "catch_rate": pct(q["rec"], q["targets"])}
        out["vs_man"]["yards_per_target_rank"] = r_man_ypt.get(t)
        out["vs_zone"]["yards_per_target_rank"] = r_zone_ypt.get(t)
        T(t)["defense"]["man_zone"] = out

    # ---- individual defenders: season line + man/zone lines ----
    base = {(r.get("player_id")): r for r in cov_rows}
    per_team = {}
    for r in sch_rows:
        if r.get("position") not in DB_POS:
            continue
        b = base.get(r.get("player_id"), {})
        snaps = n(b.get("snap_counts_coverage")) or (n(r.get("man_snap_counts_coverage")) + n(r.get("zone_snap_counts_coverage")))
        if snaps < MIN_COV_SNAPS:
            continue
        d = {"player": r.get("player"), "pos": r.get("position"), "games": r.get("player_game_count"),
             "coverage_snaps": snaps, "all_coverage_snaps": r.get("base_snap_counts_coverage"), "season": season_line(b),
             "man": side(r, "man"), "zone": side(r, "zone")}
        per_team.setdefault(code(r.get("team")), []).append(d)
    for t, lst in per_team.items():
        lst.sort(key=lambda d: -n(d["coverage_snaps"]))
        T(t)["defense"]["defenders"] = lst[:16]

    # ---- receivers: man vs zone ----
    rec_team = {}
    for r in rcv_rows:
        tm = n(r.get("man_targets")) + n(r.get("zone_targets"))
        if tm < 3:
            continue
        rec_team.setdefault(code(r.get("team")), []).append(
            {"player": r.get("player"), "pos": r.get("position"), "games": r.get("player_game_count"),
             "total_targets": tm, "all_targets": r.get("base_targets"),
             "uncharted_targets": (r.get("base_targets") - tm) if isinstance(r.get("base_targets"), (int, float)) else None,
             "vs_man": side(r, "man"), "vs_zone": side(r, "zone")})
    for t, lst in rec_team.items():
        lst.sort(key=lambda d: -d["total_targets"])
        T(t)["offense"]["receivers"] = lst[:20]

    # ---- team passing production vs man/zone, summed from receivers ----
    psum = load("facet_passing_summary.json")
    qb_rows = []
    if psum:
        pk = next((k for k, v in psum.items() if isinstance(v, list) and v and isinstance(v[0], dict)), None)
        qb_rows = psum.get(pk, []) if pk else []
    for t, blk in passing_proxy(rcv_rows, qb_rows).items():
        T(t)["offense"]["passing_proxy"] = blk
    print("passing_proxy: %d teams (QB rows: %d)" % (sum(1 for v in teams.values() if "passing_proxy" in v["offense"]), len(qb_rows)))

    out = {"source": "PFF (private) facet leaderboards, season-to-date",
           "season": (cov or sch or rcv or {}).get("season") or current_season(), "teams": teams}
    json.dump(out, open(os.path.join(PRIV, "coverage_context.json"), "w"))
    print("Wrote private/pff/coverage_context.json - %d teams (defenders: %d teams, receivers: %d teams)"
          % (len(teams), len(per_team), len(rec_team)))


if __name__ == "__main__":
    main()
