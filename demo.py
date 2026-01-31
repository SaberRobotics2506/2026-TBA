import requests
import os
from dotenv import load_dotenv
import pandas as pd
from tabulate import tabulate

load_dotenv()
api_key = os.getenv('API_KEY_DEMO')
api_url = "https://www.thebluealliance.com/api/v3"
keepGoing = False

global data
data = {
    "Team Number": [],
    "Name": [],
    "Nickname": [],
    "City": [],
    "State": [],
    "Website": [],
    "Rookie Year": []
}

def get_team_info(team_number, api_key=api_key):
    try:
        response = requests.get(f'{api_url}/team/frc{team_number}', headers={'X-TBA-Auth-Key': api_key}, timeout=5)
        response_json = response.json()
        return response_json
    except Exception as e:
        return None

def add_team(team_number):
    team_info = get_team_info(team_number)
    if team_info is None:
        print(f"Failed to retrieve data for team {team_number}")
        return
    
    data["Team Number"].append(team_info.get("team_number"))
    data["Name"].append(team_info.get("name"))
    data["Nickname"].append(team_info.get("nickname"))
    data["City"].append(team_info.get("city"))
    data["State"].append(team_info.get("state_prov"))
    data["Website"].append(team_info.get("website"))
    data["Rookie Year"].append(team_info.get("rookie_year"))

print("Enter all the team numbers you would like info for. Press enter when you are done")
team_numbers = []
while not keepGoing:
    try:
        userIn = input()
        if userIn == "":
            break
        else:
            team_numbers.append(int(userIn))
    except ValueError:
        print("Please enter a valid number")
print("Please wait...")
for i in range(len(team_numbers)):
    add_team(team_numbers[i])

df = pd.DataFrame(data)
print(tabulate(df, headers='keys', tablefmt='psql')) # type: ignore