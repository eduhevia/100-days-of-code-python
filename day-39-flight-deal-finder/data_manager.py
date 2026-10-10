import os

import requests
from dotenv import load_dotenv

load_dotenv()


class DataManager:
    """This class is responsible for talking to the Google Sheet."""

    def __init__(self):
        self.credentials = (os.environ.get("SHEETY_USER"), os.environ.get("SHEETY_PASS"))
        self.prices_endpoint = os.environ.get("SHEETY_PRICES_ENDPOINT")
        self.users_endpoint = os.environ.get("SHEETY_USERS_ENDPOINT")
        self.destination_data = {}

    def get_destination_data(self) -> list:
        """Get the destination data like the city, IATA code, ID, and lowest price."""
        response = requests.get(url=self.prices_endpoint, auth=self.credentials)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_lowest_price(self, row_id, new_price):
        url_row = f"{self.prices_endpoint}/{row_id}"
        new_data = {
            "price": {
                "lowestPrice": new_price,
            }
        }
        response = requests.put(url=url_row, json=new_data, auth=self.credentials)
        response.raise_for_status()

    def get_customer_emails(self) -> list:
        response = requests.get(url=self.users_endpoint, auth=self.credentials)
        response.raise_for_status()
        self.customer_data = response.json()["users"]
        return self.customer_data
