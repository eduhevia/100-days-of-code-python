import os

import requests

# -------------------------------------------------------------------
# CONFIGURATION AND CONSTANTS
# -------------------------------------------------------------------
STOCK = os.environ.get("STOCK", "IBM")
COMPANY_NAME = "IBM"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

TOKEN_TELEGRAM = "8625349282:AAGVaVkv5z-jZzghhOiXyDTC3njHOjTiF2I"
CHAT_ID_TELEGRAM = os.environ.get("CHAT_ID_TELEGRAM")


# -------------------------------------------------------------------
# HELPER FUNCTIONS
# -------------------------------------------------------------------
def get_up_or_down_emoji(diff: float) -> str:
    """Returns a representative emoji based on price fluctuation."""
    if diff > 0:
        return "🔺"
    elif diff < 0:
        return "🔻"
    return "🟰"


def send_message_telegram(text: str) -> None:
    """Sends a Markdown formatted message through the Telegram Bot."""
    url = f"https://api.telegram.org/bot{TOKEN_TELEGRAM}/sendMessage"
    payload = {
        "chat_id": CHAT_ID_TELEGRAM,
        "text": text,
        "parse_mode": "Markdown"
        }  # fmt: skip
    response = requests.post(url, json=payload)
    response.raise_for_status()


# -------------------------------------------------------------------
# MAIN EXECUTION
# -------------------------------------------------------------------
def main():
    # 1. Fetch stock data
    stock_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": STOCK_API_KEY,
    }
    stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
    stock_response.raise_for_status()

    daily_data = stock_response.json()["Time Series (Daily)"]

    # Extract close prices for the two most recent recorded days
    recent_days = list(daily_data.values())[:2]
    today_close = float(recent_days[0]["4. close"])
    yesterday_close = float(recent_days[1]["4. close"])

    # Calculate price variation and percentage
    diff = today_close - yesterday_close
    percentage = (abs(diff) / yesterday_close) * 100
    emoji = get_up_or_down_emoji(diff)

    # 2. Fetch relevant news articles
    news_params = {"apiKey": NEWS_API_KEY, "q": COMPANY_NAME, "language": "en"}
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    top_three_articles = news_response.json()["articles"][:3]

    # 3. Build formatted message with your custom separators
    msg = f"*{STOCK}*: {emoji}{percentage:.2f}%\n"

    for article in top_three_articles:
        headline = article["title"]
        brief = article["description"]
        url = f"📰 [Read full article]({article['url']})"
        msg += (
            f"\n{'─' * 25}\n\n"
            f"*Headline:* _{headline}_\n\n"
            f"*Brief:* _{brief}_\n\n"
            f"{url}\n"
        )  # fmt: skip
    # 4. Send notification
    send_message_telegram(msg)


if __name__ == "__main__":
    main()
