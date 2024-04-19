import requests
from twilio.rest import Client

API_URL = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "365a4a387b5b975d837542823db00e93"
LAT = 39.52
LON = -75.72
RECORDS_TO_FETCH = 4

weather_params = {
    "appid": API_KEY,
    "lat": LAT,
    "lon": LON,
    "cnt": RECORDS_TO_FETCH
}

response = requests.get(API_URL, weather_params)
response.raise_for_status()
weather_data = response.json()
will_it_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_it_rain = True

if will_it_rain:
    print("Bring an umbrella.")

    18773569744