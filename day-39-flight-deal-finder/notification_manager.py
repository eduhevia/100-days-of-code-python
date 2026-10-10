import os
import smtplib
from email.message import EmailMessage

import requests
from dotenv import load_dotenv

load_dotenv()


class NotificationManager:
    """This class is responsible for sending notifications with the deal flight details."""

    def __init__(self, sender_email):
        self.token = os.environ.get("TELEGRAM_BOT_TOKEN")
        self.chat_id = os.environ.get("TELEGRAM_CHAT_ID")
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587
        self.sender_email = sender_email
        self.sender_password = os.environ.get("PASSWORD_APP")

    def send_email(self, recipient, subject, body):
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = self.sender_email
        msg["To"] = recipient
        msg.set_content(body, charset="utf-8")

        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)
            print(f"Email sent successfully to {recipient}!")
            return True

        except smtplib.SMTPAuthenticationError as auth_err:
            print(f"Authentication failed: Check your email or App Password. Details: {auth_err}")
            return False

        except smtplib.SMTPConnectError as connect_err:
            print(f"Could not connect to the server: {connect_err}")
            return False

        except smtplib.SMTPException as smtp_err:
            print(f"SMTP protocol error occurred: {smtp_err}")
            return False

    def send_telegram_message(self, message):
        url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        payload = {
            "chat_id": self.chat_id,
            "text": message,
            "parse_mode": "HTML",
        }
        response = requests.post(url, json=payload)
        response.raise_for_status()
        print("Notification has been send to Telegram succesfully!")
