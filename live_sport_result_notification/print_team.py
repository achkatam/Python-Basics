import json
from api_handler import data


def print_team_result(team):
    team_name = team
    for game in data['events']:
        league = game['tournament']['name']
        home_team = game['homeTeam']['name']
        away_team = game['awayTeam']['name']
        home_score = game['homeScore']['current']
        away_score = game['awayScore']['current']

        if team_name == home_team or team_name == away_team:
            result = f"{league}| {home_team} {home_score} - {away_score} {away_team}"
            print(result)
            break

