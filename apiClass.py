import requests
import os

class api():
    def __init__(self, apiUrl="https://www.thebluealliance.com/api/v3") -> None:
        self.API_URL = apiUrl
    def get_response(self, path_to_response):
        try:
            response = requests.get(f'{self.API_URL}{path_to_response}', headers={'X-TBA-Auth-Key': os.getenv("API_KEY_TEAMS")}, timeout=5)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error from api.get_response(): {e}")
            exit(0)
    # def parse_to_json(self):
