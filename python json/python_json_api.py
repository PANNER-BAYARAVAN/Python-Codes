import requests

url = "https://covid-19-data.p.rapidapi.com/help/countries"

querystring = {"format":"json"}

headers = {
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
    'x-rapidapi-key': "4cf8458d4emshe8499a26868f54ep1e13e6jsn82952d193069"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
