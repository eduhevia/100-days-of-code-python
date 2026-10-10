import os

import requests

SERPAPI_ENDPOINT = "https://serpapi.com/search"


class FlightSearch:
    """This class is responsible for talking to the Flight Search API."""

    def __init__(self):
        self._api_key = os.environ["SERPAPI_API_KEY"]

    def check_flights(
        self, origin_city_code, destination_city_code, from_time, to_time, is_direct=True, is_fallback=False
    ) -> dict | None:
        query_params = {
            "engine": "google_flights",
            "gl": "es",
            "hl": "es",
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": from_time,
            "return_date": to_time,
            "type": "1",
            "adults": "1",
            "currency": "EUR",
            "api_key": self._api_key,
        }

        if is_direct:
            query_params["stops"] = "1"
        else:
            query_params["stops"] = "2"

        response = requests.get(url=SERPAPI_ENDPOINT, params=query_params)

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            return None

        data = response.json()
        if "error" in data:
            if is_fallback:
                print(f"API error: {data['error']}")
            return None
        return data
