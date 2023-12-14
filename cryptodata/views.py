from django.utils import timezone
from rest_framework.decorators import api_view
from .api_utils import fetch_and_store_bitcoin_data, fetch_and_store_market_data
from rest_framework.response import Response
import plotly.express as px
from django.shortcuts import render
from .models import Price
from datetime import datetime, timedelta

from rest_framework import viewsets
from .models import Price, MarketData
from .serializers import PriceSerializer, MarketDataSerializer

import logging
logger = logging.getLogger(__name__)

class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


class MarketDataViewSet(viewsets.ModelViewSet):
    queryset = MarketData.objects.all()
    serializer_class = MarketDataSerializer

# mywacc_test/cryptodata/views.py


def home(request):
    # Aquí puedes agregar lógica adicional si es necesario
    return render(request, 'cryptodata/home.html')


def bitcoin_price_chart(request):
    # Obtener el rango de fechas y la moneda de los parámetros de la solicitud o usar valores predeterminados
    days = request.GET.get('days', 7)
    vs_currency = request.GET.get('currency', 'usd')
    logger.info(f"Bitcoin price chart: days={days}, currency={vs_currency}")

    try:
        days = int(days)
    except ValueError:
        days = 7  # Si el valor de 'days' no es un entero, usa el predeterminado

    end_date = timezone.now()
    start_date = end_date - timedelta(days=days)

    # Filtrar los precios por el rango de fechas y la moneda
    prices = Price.objects.filter(
        date__range=[start_date, end_date],
        currency=vs_currency
    ).order_by('date')

    # Asegúrate de que tienes datos antes de intentar crear el gráfico
    if prices.exists():
        # Extract date and price values from the queryset
        dates = [price.date for price in prices]
        prices_values = [price.price for price in prices]

        # Crear el gráfico
        fig = px.line(
            x=dates,
            y=prices_values,
            title=f'Precio de Bitcoin en los últimos {days} días en {vs_currency.upper()}'
        )

        # Convertir el gráfico a HTML
        plot_div = fig.to_html(full_html=False)
    else:
        plot_div = "No hay datos disponibles para el rango de fechas seleccionado."

    context = {
        'plot_div': plot_div,
        'currency': vs_currency.upper(),
        'days': days
    }
    return render(request, 'cryptodata/bitcoin_chart.html', context)


def bitcoin_market_data_chart(request):
    # Asignaciones similares a las usadas en `bitcoin_price_chart`
    days = request.GET.get('days', 7)
    vs_currency = request.GET.get('currency', 'usd')
    try:
        days = int(days)
    except ValueError:
        days = 7  # Si el valor de 'days' no es un entero, usa el predeterminado

    end_date = timezone.now()
    start_date = end_date - timedelta(days=days)

    # Filtrar los datos de mercado por el rango de fechas y la moneda
    market_data = MarketData.objects.filter(
        date__range=[start_date, end_date],
        currency=vs_currency
    ).order_by('date')

    # Asegúrate de que tienes datos antes de intentar crear el gráfico
    if market_data.exists():
        # Extract date, market_cap and total_volume values from the queryset
        dates = [data.date for data in market_data]
        market_caps = [data.market_cap for data in market_data]
        total_volumes = [data.total_volume for data in market_data]

        # Crear el gráfico de capitalización de mercado
        market_cap_fig = px.line(
            x=dates,
            y=market_caps,
            title=f'Capitalización de Mercado de Bitcoin en los últimos {days} días en {vs_currency.upper()}'
        )
        market_cap_plot_div = market_cap_fig.to_html(full_html=False)

        # Crear el gráfico de volumen total
        volume_fig = px.line(
            x=dates,
            y=total_volumes,
            title=f'Volumen Total de Bitcoin en los últimos {days} días en {vs_currency.upper()}'
        )
        volume_plot_div = volume_fig.to_html(full_html=False)

    else:
        market_cap_plot_div = "No hay datos de capitalización de mercado disponibles para el rango de fechas seleccionado."
        volume_plot_div = "No hay datos de volumen total disponibles para el rango de fechas seleccionado."

    context = {
        'market_cap_plot_div': market_cap_plot_div,
        'volume_plot_div': volume_plot_div,
        'currency': vs_currency.upper(),
        'days': days
    }
    return render(request, 'cryptodata/bitcoin_market_data_chart.html', context)


@api_view(['GET'])
def update_bitcoin_data(request):
    # Captura los parámetros de la solicitud
    days = request.query_params.get('days', '7')
    vs_currency = request.query_params.get('vs_currency', 'usd')

    fetch_and_store_bitcoin_data(days=days, vs_currency=vs_currency)
    fetch_and_store_market_data(days=days, vs_currency=vs_currency)

    return Response({"status": f"Datos de Bitcoin actualizados para {days} días en {vs_currency}"})
