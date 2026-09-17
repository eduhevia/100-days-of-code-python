import os

import requests

TOKEN_TELEGRAM = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID_TELEGRAM = os.environ.get("TELEGRAM_CHAT_ID")
api_key = os.environ.get("OWM_API_KEY")

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
weather_params = {"lat": 37.366667, "lon": 143.700000, "appid": api_key, "cnt": 4}

response = requests.get(url=OWM_Endpoint, params=weather_params)
response.raise_for_status()

print("State Code:", response.status_code, "\n")
wheather_data = response.json()["list"]


def is_raining():
    for i in range(4):
        weather_id = wheather_data[i]["weather"][0]["id"]
        if weather_id < 700:
            return True
    return False


def send_message_telegram(text):
    url = f"https://api.telegram.org/bot{TOKEN_TELEGRAM}/sendMessage"
    payload = {"chat_id": CHAT_ID_TELEGRAM, "text": text, "parse_mode": "Markdown"}
    response_tg = requests.post(url, json=payload)
    response_tg.raise_for_status()


if is_raining():
    print("It's going to rain! Sending notification...")
    send_message_telegram(
        "⚠️ *ALERTA METEOROLÓGICA* ⚠️\n\n"
        "Se detecta probabilidad de lluvia para las próximas horas en tu ubicación.\n"
        "Por favor, recuerda llevar un paraguas (☂️) al salir."
    )
else:
    print("No rain is expected in the next 12 hours.")
