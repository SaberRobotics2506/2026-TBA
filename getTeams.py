import requests
import pandas as pd

API_URL = "https://www.thebluealliance.com/api/v3"
API_KEY = "gAFGsJ0rhLBWsubSA9TWSdvAM6ECWFa8x2NdzFJ8kTPMFnH1GLwpwxaRzgMdujO3"
EVENT_CODE = "2026wimuk"

def getEventTeams(eventKey):
    try:
        response = requests.get(f"{API_URL}/event/{eventKey}/teams/keys", headers={'X-TBA-Auth-Key': API_KEY}, timeout=5)
        jsonResponse = response.json()
        return jsonResponse
    except Exception as e:
        print(f"Error: {e}")
        return "Error"

teamID = getEventTeams(EVENT_CODE)
teamNumbers = []
try:
    for i in range(len(teamID)):
        teamNumbers.append(f"<item>{(teamID[i])[3:]}</item>")
except KeyError:
    print("TBA Response Invalid. Check your event code or API key.")
df = pd.DataFrame(teamNumbers)
df.to_csv("teams.csv", index=False, header=False)
print("Done")