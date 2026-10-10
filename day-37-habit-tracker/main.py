from datetime import datetime
from zoneinfo import ZoneInfo

import requests

USERNAME = "eduhevia"
TOKEN = "alkj3jflkja3lkjawja89dfuaf29"
GRAPH_ID = "reading-graph"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

spain_zone = ZoneInfo("Europe/Madrid")
today = datetime.now(tz=spain_zone).strftime("%Y%m%d")
pages_read = str(int(float(input("How many pages have you read?: "))))


# Creating a new profile in Pixela
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Creating a new graph
graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Reading Graph",
    "unit": "pages",
    "type": "int",
    "color": "shibafu",
}

# Creating a new pixel
pixel_creation_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_data = {
    "date": today,
    "quantity": pages_read,
}

# Updating an existing pixel
update_pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
update_pixel_data = {
    "quantity": pages_read,
}

headers = {"X-USER-TOKEN": TOKEN}
response = requests.post(url=update_pixel_endpoint, json=pixel_data, headers=headers)
print(response.text)
