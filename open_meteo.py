import requests
from requests import Response

# URL del endpoint de Open-Meteo para obtener el pronóstico del tiempo
url_forecast = "https://api.open-meteo.com/v1/forecast"

# Función para obtener la temperatura en un rango de fechas
#def get_temperature_by_dates(lat: float, lon: float, date_i: str, date_f: str) -> Response:
#    params = {
#        "latitude": lat,
#        "longitude": lon,
#        "hourly": "temperature_2m",
#        "start_date": date_i,
#        "end_date": date_f,
#        "timezone": "UTC"
#    }
#    response: Response = requests.get(url_forecast, params=params)
#    return response