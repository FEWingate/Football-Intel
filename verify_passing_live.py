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
print(f"HTTP {resp.status_code}, x-requests-used: {resp.headers.get('x-requests-used')}")
data = resp.json()

fd_count = 0
for event in data:
    fd = next((bk for bk in event.get("bookmakers", []) if bk.get("key") == "fanduel"), None)
    py = next((m for m in (fd.get("markets", []) if fd else []) if m.get("key") == "player_passing_yards"), None)
    if py and py.get("outcomes"):
        fd_count += 1
        names = sorted(set(o.get("description") for o in py["outcomes"]))
        print(f"  {event.get('away_team')} @ {event.get('home_team')}: {names}")

print(f"\nReal events with FanDuel player_passing_yards right now: {fd_count} of {len(data)}")
