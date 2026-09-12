import json
d = json.load(open("fanduel_props/latest.json"))
print(f"Total games: {len(d['games'])}")
print()
print("Every real game, with commence_time:")
for g in sorted(d["games"], key=lambda x: x["commence_time"] or ""):
    print(f"  {g['away_team']} @ {g['home_team']}  |  {g['commence_time']}")
print()
print("Per-stat real entry counts:")
for stat in ("passing_yards", "rushing_yards", "receiving_yards", "receptions"):
    total = sum(len(g["player_props"].get(stat, {})) for g in d["games"])
    print(f"  {stat}: {total}")
print(f"  anytime_td: {sum(len(g['anytime_td']) for g in d['games'])}")
