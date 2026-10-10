import os
from datetime import datetime
from zoneinfo import ZoneInfo

import requests
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
SHEET_ENDPOINT = os.environ.get("SHEET_ENDPOINT")

# OPTIONALS FIELDS (for more accurate calorie calculations):
WHEIGHT = 60
HEIGHT = 1.77
AGE = 13
GENDER = "male"

# MAIN CODE:
base_url = "https://app.100daysofpython.dev"
completed_workouts = input("Tell me which exercises you did: ")

# Get with the API the duration, time, exercise, and burned calories with human language:
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_params = {
    "query": completed_workouts,
    "weight_kg": WHEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
    "gender": GENDER,
}

response = requests.post(url=f"{base_url}/v1/nutrition/natural/exercise", headers=headers, json=exercise_params)
response.raise_for_status()
exercise_data = response.json()

# Getting the today actual time:
spain_zone = ZoneInfo("Europe/Madrid")
today_date = datetime.now(tz=spain_zone).strftime("%d/%m/%Y")
now_time = datetime.now(tz=spain_zone).strftime("%H:%M:%S")

for exercise in exercise_data["exercises"]:
    sheet_inputs = {
        "workout": {
            "Date": today_date,
            "Time": now_time,
            "Exercise": exercise["name"].title(),
            "Duration": exercise["duration_min"],
            "Calories": exercise["nf_calories"],
        }
    }
    response = requests.post(url=SHEET_ENDPOINT, json=sheet_inputs)
    print("Status Code:", response.status_code)
