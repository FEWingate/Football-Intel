import os, sys, json
import requests

PARLAY_API_KEY = os.environ.get("PARLAY_API_KEY")
if not PARLAY_API_KEY:
    sys.exit("FATAL: PARLAY_API_KEY not set.")

url = "https://parlay-api.com/v1/sports/americanfootball_nfl/odds"
params = {
    "regions": "us",
    "markets": "player_receiving_yards,player_passing_yards,player_rushing_yards,player_receptions,player_anytime_touchdown_scorer",
}
resp = requests.get(url, headers={"X-API-Key": PARLAY_API_KEY}, params=params, timeout=30)
print(f"HTTP {resp.status_code}")
print(f"x-requests-used: {resp.headers.get('x-requests-used')}")
print(f"x-requests-remaining: {resp.headers.get('x-requests-remaining')}")
if resp.status_code != 200:
    print(resp.text[:1000])
    sys.exit(1)

data = resp.json()
print(f"Total events returned: {len(data)}")

fd_events = 0
sample_printed = False
for event in data:
    fd = next((bk for bk in event.get("bookmakers", []) if bk.get("key") == "fanduel"), None)
    if fd and fd.get("markets"):
        fd_events += 1
        if not sample_printed:
            print()
            print(f"Sample event: {event.get('away_team')} @ {event.get('home_team')}")
            print(json.dumps(fd, indent=2)[:2000])
            sample_printed = True
print()
print(f"Events with real FanDuel player-prop data: {fd_events} of {len(data)}")
