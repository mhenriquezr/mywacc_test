from celery import shared_task
from .api_utils import fetch_and_store_bitcoin_data, fetch_and_store_market_data

@shared_task
def update_bitcoin_data():
    fetch_and_store_bitcoin_data()

@shared_task
def update_market_data():
    fetch_and_store_market_data()
