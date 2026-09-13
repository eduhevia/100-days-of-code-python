import datetime as dt
import os
import random
import smtplib
from email.message import EmailMessage
from zoneinfo import ZoneInfo

import pandas as pd

MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("MY_MAIL_PASSWORD")

zone_spain = ZoneInfo("Europe/Madrid")

# Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now(tz=zone_spain)

data = pd.read_csv("birthdays.csv")

today_birthday = (data["month"] == now.month) & (data["day"] == now.day)
birthday_matches = data[today_birthday]

for index, row in birthday_matches.iterrows():
    name = row["name"]
    email = row["email"]

    msg = EmailMessage()
    msg["Subject"] = "¡Feliz Cumpleaños!"
    msg["From"] = MY_EMAIL
    msg["To"] = email

    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as message_file:
        # Replace [NAME] with the person whose birthday it's today
        text_file = message_file.read()
        text_file = text_file.replace("[NAME]", name)
        msg.set_content(text_file)

    # Send the email content (msg)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.send_message(msg)
