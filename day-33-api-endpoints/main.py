import smtplib
import time
from datetime import datetime
from email.message import EmailMessage
from zoneinfo import ZoneInfo

import requests

MY_EMAIL = "familiaheviasanchez@gmail.com"
PASSWORD = ""

MY_LAT = 38.427418
MY_LONG = -0.398368


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    return iss_latitude in [MY_LAT - 5, MY_LAT + 5] and iss_longitude in [
        MY_LONG - 5,
        MY_LONG + 5,
    ]


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    return time_now <= sunset and time_now >= sunrise


time_now = datetime.now(tz=ZoneInfo("Europe/Madrid")).hour

msg = EmailMessage()
msg["Subject"] = "ISS Up You!"
msg["From"] = MY_EMAIL
msg["To"] = "eduhevia12@gmail.com"


while True:
    if is_iss_overhead() == True and is_night() == True:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            msg.set_content(
                "The ISS should be visible if you look at the sky.\nIf the sky is clear, go and watch it!"
            )
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.send_message(msg)
            time.sleep(60)
