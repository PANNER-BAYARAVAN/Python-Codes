import requests
import pandas as pd

url = "https://covid-19-data.p.rapidapi.com/help/countries"

querystring = {"format":"json"}

headers = {
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
    'x-rapidapi-key': "4cf8458d4emshe8499a26868f54ep1e13e6jsn82952d193069"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

data = response.text
df = pd.DataFrame([x.split(',') for x in data.split('\n')])
print(df)

a_json = json.loads(response.text)
print(a_json)

dataframe = pd.DataFrame.from_dict(a_json)
print(dataframe)

