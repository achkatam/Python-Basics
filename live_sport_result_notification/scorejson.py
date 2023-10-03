import json

with open('response.json') as f:
    jsondata = json.load(f)

data = jsondata['events']

league = (jsondata['events'][0]['tournament']['name'])

hometeam = (jsondata['events'][0]['homeTeam']['name'])
awayteam = (jsondata['events'][0]['awayTeam']['name'])

home_score = (jsondata['events'][0]['homeScore']['current'])
away_score = (jsondata['events'][0]['awayScore']['current'])


# print(f"{hometeam} {home_score} - {away_score} {awayteam}")
def send_info():
    for game in data:
        league = game['tournament']['name']
        home_team = game['homeTeam']['name']
        away_team = game['awayTeam']['name']
        home_score = game['homeScore']['current']
        away_score = game['awayScore']['current']

        result = f"{league}| {home_team} {home_score} - {away_score} {away_team}"
        print(result)
