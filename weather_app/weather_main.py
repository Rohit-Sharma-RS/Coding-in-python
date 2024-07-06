import os
import requests
from twilio_autosms import Msg
api_key = os.environ.get('API_KEY')
my_lat = '22.572645'
my_long = '88.363892'

parameters = {
    'lat': 22.572645,
    'lon': 88.363892,
    'appid': api_key,
}

para = {
    'lat': -18.797520,
    'lon': 47.517410,
    'appid': api_key
}

request = requests.get('https://api.openweathermap.org/data/2.5/weather',params=parameters)
data = request.json()
print(data)
is_it_raining = data['weather'[0]]
print(is_it_raining)
rain_id = data['weather'][0]['id']
description = data['weather'][0]['description']
print(rain_id)
print(description)
if rain_id < 700:
    Msg()
else:
    print('nothing')

