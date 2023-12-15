# MyWacc Cryptodata

## Descripción
MyWacc Cryptodata es una aplicación web desarrollada en Django, diseñada para visualizar datos del mercado de criptomonedas, específicamente Bitcoin. Esta aplicación recoge datos históricos de precios y datos de mercado, permitiendo al usuario visualizar gráficos interactivos para diferentes periodos y monedas.

## Características
- Visualización de datos históricos de precios de Bitcoin.
- Visualización de datos de mercado como capitalización de mercado y volumen total.
- Actualización diaria de datos utilizando Celery y Redis.
- Filtros dinámicos para la selección de rangos de fechas y monedas.
- API RESTful para acceder a los datos de precios y de mercado.

## Tecnologías Utilizadas
- Django
- Django REST framework
- Celery
- Redis
- Plotly
- Docker

## Instalación y Configuración
1. Clona el repositorio:
   
```git clone https://github.com/mhenriquez/mywacc-test.git```

2. Navega al directorio del proyecto:

```cd mywacc-cryptodata```

3. Construye y ejecuta el proyecto con Docker:

```docker-compose up --build```

## Uso
Una vez que la aplicación esté en ejecución, puedes acceder a ella a través de tu navegador web en http://localhost:8000. La interfaz te permitirá:

- Ver gráficos interactivos de precios y datos de mercado de Bitcoin.
- Seleccionar rangos de fechas y monedas diferentes para los gráficos.
- Acceder a la API REST para obtener datos crudos.

  
## URLs
- `/cryptodata/`: URL principal de la aplicación MyWacc Cryptodata.
- `/bitcoin-chart/`: URL para ver gráficos interactivos de precios de Bitcoin.
- `/bitcoin-market-data-chart/`: URL para ver gráficos de datos de mercado de Bitcoin.
- `/update-bitcoin-data/`: URL para actualizar los datos de Bitcoin.
- `/api/prices/`: URL de la API REST para acceder a datos de precios de criptomonedas.
- `/api/marketdata/`: URL de la API REST para acceder a datos de mercado de criptomonedas.


## Creación del Service App en Azure
Para implementar MyWacc Cryptodata en Azure, se siguió un proceso que incluyó:

1. Creación de una cuenta de Azure y configuración de un grupo de recursos.
2. Configuración de un servicio de base de datos, como Azure Database for PostgreSQL, para almacenar los datos de la aplicación.
3. Implementación de la aplicación Django en Azure App Service, configurando el entorno de producción y asegurando la integración con la base de datos.
4. Configuración de las variables de entorno para el manejo de claves secretas y otros parámetros de configuración.
5. Configuración de Azure Scheduler o Azure Functions para la actualización automática de los datos.

## Resumen de Funciones Básicas en Views y API Utils
- **Views (Vistas):**
  - `home`: Renderiza la página de inicio con gráficos interactivos y opciones de filtro.
  - `api_home`: Renderiza una página para la interfaz de la API, mostrando información sobre las rutas disponibles.
  
- **API Utils (Utilidades de la API):**
  - `get_crypto_data`: Obtiene datos de precios de criptomonedas a partir de una fuente de datos externa, como una API de criptomonedas.
  - `calculate_market_data`: Calcula datos de mercado como capitalización y volumen total a partir de los datos de precios.
  - `update_data_daily`: Actualiza los datos de la base de datos diariamente utilizando Celery y Redis.

