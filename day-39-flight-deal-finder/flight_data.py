class FlightData:
    """This class is responsible for structuring the flight data."""

    def __init__(self, price, origin, destination, out_date, return_date, stops):
        self.price = price
        self.origin_airport = origin
        self.destination_airport = destination
        self.out_date = out_date.split(" ")[0] if out_date != "N/A" else "N/A"
        self.return_date = return_date.split(" ")[0] if return_date != "N/A" else "N/A"
        self.stops = stops


def find_cheapest_flight(data, return_date) -> FlightData:
    empty_flight = FlightData(
        price="N/A",
        origin="N/A",
        destination="N/A",
        out_date="N/A",
        return_date="N/A",
        stops="N/A",
    )

    if data is None:
        return empty_flight

    all_flights = data.get("best_flights", []) + data.get("other_flights", [])

    cheapest_flight: FlightData | None = None

    if not all_flights:
        return empty_flight

    for flight in all_flights:
        if "price" not in flight or "flights" not in flight or not flight["flights"]:
            continue

        try:
            price = flight["price"]
            origin_airport = flight["flights"][0]["departure_airport"]["id"]
            destination_airport = flight["flights"][-1]["arrival_airport"]["id"]
            out_date = flight["flights"][0]["departure_airport"]["time"]
            nr_stops = len(flight["flights"]) - 1
            actual_flight = FlightData(price, origin_airport, destination_airport, out_date, return_date, nr_stops)

            if cheapest_flight is None or int(actual_flight.price) < int(cheapest_flight.price):
                cheapest_flight = actual_flight
        except (KeyError, IndexError, ValueError):
            print("--- No price available for flight. ---")
            continue

    return cheapest_flight if cheapest_flight is not None else empty_flight
