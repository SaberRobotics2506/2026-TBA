from apiClass import api
import pandas as pd

event_key = "2016nytr"

tba = api()
response = tba.get_response(f'/event/{event_key}/awards')

df = pd.DataFrame(response)
df.to_csv("awards.csv")
