import json
data = json.load(open("parlay_props_sample.json"))
fd = [r for r in data if r.get("bookmaker") == "fanduel"]
games = sorted(set((r.get("away_team"), r.get("home_team")) for r in fd if r.get("away_team") or r.get("home_team")))
print(f"Total real FanDuel rows in this sample: {len(fd)}")
print(f"Distinct games represented for FanDuel in this sample: {len(games)}")
for g in games:
    print(" ", g)
print()
all_games = sorted(set((r.get("away_team"), r.get("home_team")) for r in data if r.get("away_team") or r.get("home_team")))
print(f"Distinct games represented across ALL books combined: {len(all_games)}")
