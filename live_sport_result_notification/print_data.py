import json
from api_handler import data
from get_question import get_user_input
from get_league import get_league
from get_team import get_team
from print_team import print_team_result
from print_league import print_league_result

with open('data.json', 'w') as f:
    json.dump(data, f)


def send_info():
    user_input = get_user_input()

    if user_input == 'l':
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


