import requests
from datetime import datetime
import os

os.environ["nutri_api_key"] = '3ea794043eef5e9b9c639f00a01df1cf'
os.environ["sheety_authorization"] = "Basic cm9oaXQyMTAzOk12dHJhZGVyczEy"

NOW = datetime.now()
DATE = NOW.strftime('%d/%m/%Y')
TIME = NOW.strftime('%X')
print(TIME)
print(DATE)

GENDER = 'Male'
WEIGHT_KG = '64'
HEIGHT_CM = '170'
AGE = '20'

APP_ID = '997f9cad'
API_KEY = os.environ.get("nutri_api_key")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
results = response.json()
exercise = []
time = []
calories_burned = []

sheety_api = "https://api.sheety.co/8d0fc4d0741f0b93e77ad7bed25abb6f/myworkouts/workouts"

for result in results["exercises"]:
    body = {
    "workout": {
     'date': DATE,
     'time': TIME,
     'exercise': result["user_input"],
     'duration': result["duration_min"],
     'calories': result["nf_calories"],
        }
    }

    #authentication centre

    sheety_header = {
        "Username": "rohit2103",
        "Password": "Mvtraders12",
        "Authorization": os.environ.get("sheety_authorization")
    }
    sheet_update = requests.post(sheety_api, json=body, headers=sheety_header)
    print(sheet_update.text)


