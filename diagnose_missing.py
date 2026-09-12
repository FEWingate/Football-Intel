import json
d = json.load(open("fanduel_props/latest.json"))
print(f"Total games: {len(d['games'])}")
print()

total_pass = sum(len(g["player_props"].get("passing_yards", {})) for g in d["games"])
print(f"Total real passing_yards entries across all games: {total_pass}")
print()

chi_car = next((g for g in d["games"] if g["away_code"] == "CHI" and g["home_code"] == "CAR"), None)
if chi_car:
    print("CHI@CAR passing_yards entries:", list(chi_car["player_props"].get("passing_yards", {}).keys()))
    for name, p in chi_car["player_props"].get("passing_yards", {}).items():
        print(f"  {name}: line={p['line']}, {len(p['alts'])} alt(s)")
else:
    print("CHI@CAR not found in this data at all.")
