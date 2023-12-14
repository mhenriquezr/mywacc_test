from django.contrib import admin
from django.urls import path, include
from cryptodata.views import bitcoin_price_chart, bitcoin_market_data_chart
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cryptodata/', include('cryptodata.urls')),  # Incluye las URLs de tu app 'cryptodata'
    path('bitcoin-chart/', bitcoin_price_chart, name='bitcoin_price_chart'),
    path('bitcoin-market-data-chart/', bitcoin_market_data_chart, name='bitcoin_market_data_chart'),  # Añade esta línea
    path('', RedirectView.as_view(pattern_name='bitcoin_price_chart', permanent=False)),
]