# mywacc_test/cryptodata/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'api/prices', views.PriceViewSet)
router.register(r'api/marketdata', views.MarketDataViewSet)

urlpatterns = [
    path('', views.home, name='home'),  # Se asegura de que la vista 'home' esté definida
    path('update-bitcoin-data/', views.update_bitcoin_data, name='update_bitcoin_data'),
    path('bitcoin-market-data-chart/', views.bitcoin_market_data_chart, name='bitcoin_market_data_chart'),
    path('api/', include(router.urls)),  # API URLs
]