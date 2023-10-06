import json
from api_handler import data

with open('data.json', 'w') as f:
    json.dump(data, f)


def send_info():
    for game in data['events']:
        league = game['tournament']['name']
        home_team = game['homeTeam']['name']
        away_team = game['awayTeam']['name']
        home_score = game['homeScore']['current']
        away_score = game['awayScore']['current']

        result = f"{league}| {home_team} {home_score} - {away_score} {away_team}"
        print(result)
