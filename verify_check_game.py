import json
data = json.load(open("parlay_props_sample.json"))
fd = [r for r in data if r.get("bookmaker") == "fanduel"]
buf_hou = [r for r in fd if "Buffalo" in (r.get("home_team","")+r.get("away_team","")) or "Houston" in (r.get("home_team","")+r.get("away_team",""))]
print(f"Total real FanDuel rows for this specific game: {len(buf_hou)}")
keys = sorted(set(r["market_key"] for r in buf_hou))
print("Every real market_key present for THIS game:")
for k in keys:
    print(" ", k)
print()
names = ["Stroud", "Allen", "Cook", "Montgomery"]
matches = [r for r in buf_hou if r.get("player") and any(n in r["player"] for n in names)]
print(f"Rows specifically naming Stroud/Allen/Cook/Montgomery: {len(matches)}")
for r in matches:
    print(f'  {r["player"]} | {r["market_key"]} | line={r.get("line")}')
