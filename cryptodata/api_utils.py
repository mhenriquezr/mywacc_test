from django.conf import settings
import requests
import pytz
from datetime import datetime
from .models import MarketData, Price


def fetch_and_store_bitcoin_data(days='7', vs_currency='usd'):
    url = f"https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency={vs_currency}&days={days}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        prices = data["prices"]

        for price_data in prices:
            timestamp, price = price_data
            date = datetime.fromtimestamp(timestamp / 1000.0)
            aware_date = pytz.timezone(settings.TIME_ZONE).localize(date)

            Price.objects.update_or_create(
                date=aware_date, currency=vs_currency,
                defaults={'price': price, 'currency': vs_currency}
            )


def fetch_and_store_market_data(days='7', vs_currency='usd'):
    url = f"https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency={vs_currency}&days={days}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        market_data = data["market_caps"]
        total_volumes = data["total_volumes"]

        for i in range(len(market_data)):
            timestamp, market_cap = market_data[i]
            _, total_volume = total_volumes[i]

            date = datetime.fromtimestamp(timestamp / 1000.0)
            aware_date = pytz.timezone(settings.TIME_ZONE).localize(date)

            MarketData.objects.update_or_create(
                date=aware_date, currency=vs_currency,
                defaults={'total_volume': total_volume,
                          'market_cap': market_cap, 'currency': vs_currency}
            )
