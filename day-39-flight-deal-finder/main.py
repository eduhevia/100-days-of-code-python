from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

import requests_cache
from data_manager import DataManager
from flight_data import find_cheapest_flight
from flight_search import FlightSearch
from notification_manager import NotificationManager


def main():
    # ==================== Conserve requests and preserve your free plan ====================
    requests_cache.install_cache(
        "flight_deal_cache",
        expire_after=3600,
        allowable_methods=["GET"],
    )

    # ==================== Talk to Sheety ====================
    data_manager = DataManager()
    sheet_data = data_manager.get_destination_data()

    # ==================== Set the Dates ====================
    spain_zone = ZoneInfo("Europe/Madrid")

    # Guardamos las fechas base
    tomorrow = (datetime.now(tz=spain_zone) + timedelta(days=1)).strftime("%Y-%m-%d")
    six_month_from_today = (datetime.now(tz=spain_zone) + timedelta(days=180)).strftime("%Y-%m-%d")

    # ==================== Inicializar Managers (¡FUERA DEL BUCLE!) ====================
    flight_search = FlightSearch()
    # Creamos el manager de notificaciones una sola vez al inicio
    notification_manager = NotificationManager(sender_email="familiaheviasanchez@gmail.com")

    # ==================== Retrieve your customer emails ====================
    customer_data = data_manager.get_customer_emails()
    customer_email_list = [row["whatIsYourEmail?"] for row in customer_data]
    print(f"Your email list includes {customer_email_list}")

    # ==================== Do a Flight Search ====================
    ORIGIN_CITY_IATA = "ALC"

    for destination in sheet_data:
        print(f"\nGetting flights for {destination['city']}...")

        # Plan A: Direct Flight
        flight_response = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=six_month_from_today,
            is_direct=True,
            is_fallback=False,
        )
        cheapest_flight = find_cheapest_flight(flight_response, six_month_from_today)

        # Plan B: Indirect Flight
        if cheapest_flight.price == "N/A":
            print(f"No direct flight found to {destination['city']}. Checking indirect flights...")
            flight_response = flight_search.check_flights(
                ORIGIN_CITY_IATA,
                destination["iataCode"],
                from_time=tomorrow,
                to_time=six_month_from_today,
                is_direct=False,
                is_fallback=True,
            )
            cheapest_flight = find_cheapest_flight(flight_response, six_month_from_today)

        print(f"{destination['city']}: {cheapest_flight.price}€")

        # Lower price verification
        if (
            cheapest_flight
            and cheapest_flight.price != "N/A"
            and int(cheapest_flight.price) < int(destination["lowestPrice"])
        ):
            print(f"Lower price flight found to {destination['city']}!")
            data_manager.update_lowest_price(row_id=destination["id"], new_price=cheapest_flight.price)

            # Prepare the email body
            subject = f"✈️ ¡Chollo detectado a {destination['city']}!"
            body = (
                f"Ruta: {cheapest_flight.origin_airport} → {destination['city']}\n"
                f"Precio: {cheapest_flight.price}€\n"
                f"Fechas: {cheapest_flight.out_date} / {cheapest_flight.return_date}"
            )

            # Send the whole client list
            for customer in customer_email_list:
                notification_manager.send_email(
                    recipient=customer,
                    subject=subject,
                    body=body,
                )
        else:
            print("No lower price found!")


if __name__ == "__main__":
    main()
