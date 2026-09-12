import os, sys, json
import requests

PARLAY_API_KEY = os.environ.get("PARLAY_API_KEY")
if not PARLAY_API_KEY:
    sys.exit("FATAL: PARLAY_API_KEY not set.")

markets = ["player_passing_yards"] + [f"player_passing_yards_milestones_{n}_or_more"
    for n in (150, 175, 200, 225, 250, 275, 300, 325, 350, 400)]

url = "https://parlay-api.com/v1/sports/americanfootball_nfl/odds"
params = {"regions": "us", "markets": ",".join(markets)}
resp = requests.get(url, headers={"X-API-Key": PARLAY_API_KEY}, params=params, timeout=30)
print(f"HTTP {resp.status_code}")
print(f"x-requests-used: {resp.headers.get('x-requests-used')}")
if resp.status_code != 200:
    print(resp.text[:500])
    sys.exit(1)

data = resp.json()
found = 0
for event in data:
    fd = next((bk for bk in event.get("bookmakers", []) if bk.get("key") == "fanduel"), None)
    if not fd:
        continue
    py_markets = [m for m in fd.get("markets", []) if m.get("key", "").startswith("player_passing_yards")]
    if py_markets:
        found += 1
        if found == 1:
            print(f"\nSample: {event.get('away_team')} @ {event.get('home_team')}")
            print(json.dumps(py_markets, indent=2)[:1500])

print(f"\nEvents with real passing_yards data when queried ALONE: {found} of {len(data)}")
