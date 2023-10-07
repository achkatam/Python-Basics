import json
from api_handler import data
from get_question import get_user_input
from print_team import print_team_result
from print_league import print_league_result
from top_leagues import print_top_leagues

with open('data.json', 'w') as f:
    json.dump(data, f)


def send_info():
    user_input = get_user_input()

    if user_input == 'l':
        print_top_leagues()
        league_name = input("Enter league name: ")
        result = print_league_result(league_name)
        return result
    elif user_input == 't':
        team_name = input("Enter team name: ")
        result = print_team_result(team_name)
        return result
    else:
        print("Invalid input")
        return None


