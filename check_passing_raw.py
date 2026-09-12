import json
d = json.load(open("fanduel_props/latest.json"))

week1_teams = {"Chicago Bears", "Carolina Panthers", "Tampa Bay Buccaneers", "Cincinnati Bengals",
               "Buffalo Bills", "Houston Texans", "Denver Broncos", "Kansas City Chiefs"}
for g in d["games"]:
    if g["away_team"] in week1_teams or g["home_team"] in week1_teams:
        py = g["player_props"].get("passing_yards", {})
        print(f'{g["away_team"]} @ {g["home_team"]}: passing_yards has {len(py)} real player(s): {list(py.keys())}')
