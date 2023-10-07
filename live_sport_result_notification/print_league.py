import json
from api_handler import data
from top_leagues import print_top_leagues


def print_league_result(league_name):
    # print("To print all leagues enter 'all' or choose from the following:")
    # print_top_leagues()

    if league_name.lower() == 'all':
        for game in data['events']:
            league = game['tournament']['name']
            home_team = game['homeTeam']['name']
            away_team = game['awayTeam']['name']
            home_score = game['homeScore']['current']
            away_score = game['awayScore']['current']
            result = f"{league}| {home_team} {home_score} - {away_score} {away_team}"
            print(result)
    else:
        for game in data['events']:
            league = game['tournament']['name']
            home_team = game['homeTeam']['name']
            away_team = game['awayTeam']['name']
            home_score = game['homeScore']['current']
            away_score = game['awayScore']['current']

            if league == league_name:
                result = f"{league}| {home_team} {home_score} - {away_score} {away_team}"
                print(result)

