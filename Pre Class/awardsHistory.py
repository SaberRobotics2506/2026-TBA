import requests
import pandas as pd
import os

API_URL = "https://www.thebluealliance.com/api/v3"
API_KEY = os.getenv("API_KEY_TEAMS")

event_key = input("Enter your team ID here: ")

print(API_KEY)

try:
    response = requests.get(f"{API_URL}/event/{event_key}/awards", headers={'X-TBA-Auth-Key': API_KEY}, timeout=5)
    if not (response.status_code == 200 or 304):
        print(f"Request failed. Please do one of the following: \n 1) Enter a valid team ID \n 2) Check your internet connection (can you access https://www.thebluealliance.com/api/v3) \n 3) Check your API Key\n\n{response.status_code}")
    response = response.json()
    df = pd.json_normalize(response)
    df.to_csv(f"{event_key}_awards.csv", index=False)
    
except Exception as e:
    print(f"Error: {e}")