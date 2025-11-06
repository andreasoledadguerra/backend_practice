import uvicorn
import requests

from fastapi import FastAPI
from pydantic import BaseModel, Optional
from typing import Dict, Any


# Create FastAPI instance
app = FastAPI()

# Base URL for Open-Meteo API
BASE_URL_OPEN_METEO = "https://api.open-meteo.com"

# Open-Meteo API endpoint for weather forecast
url_forecast = f"{BASE_URL_OPEN_METEO}/v1/forecast"

# Modelo de respuesta (validación) para FastAPI
class WeatherResponse(BaseModel):
    data: Dict[str, Any]
    status_code: int
    success: bool

class WeatherHistoryResponse(BaseModel):
    latitude: float
    longitude: float
    timezone: str
    data: Dict[str, Any]
    status_code: int
    success: bool

#class WeatherStatsResponse(BaseModel):
#    latitude: float
#    longitude: float
#    timezone: str
#    mean_temperature: Optional[float] = None
#    min_temperature: Optional[float] = None
#    max_temperature: Optional[float] = None
#    status_code: int
#    success: bool

# Decorador para definir un endpoint GET en FastAPI para obtener temperatura por fechas
@app.get("/temperature")
def get_temperature_by_dates(lat: float, lon: float, date_i: str, date_f: str) -> WeatherResponse:
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m",
        "start_date": date_i,
        "end_date": date_f,
        "timezone": "UTC"
    }

    # Hace una petición a Open-Meteo
    response = requests.get(url_forecast, params=params)
    
    return WeatherResponse(
        data=response.json(),           # Extrae los datos JSON
        status_code=response.status_code,  # Copia el status code
        success=response.status_code == 200  # Marca si fue exitosa
    )

@app.get("/temperature/{city}")
def get_weather_by_city(city: str, lat: float, lon: float) -> WeatherResponse:
    # en este ejemplo asumimos que el cliente puede pasar lat/lon directo
    # o pasar solo city y resolver lat/lon aquí — el decorador usará lat/lon si están presentes.
    params = {
        "city": city,
        "latitude": lat,
        "longitude": lon,
        "current_weather": True,
        "timezone": "UTC"
    }

    #Hace la petición a Open-Meteo
    response = requests.get(url_forecast, params=params)

    return WeatherResponse(
        data=response.json(),           # Extrae los datos JSON
        status_code=response.status_code,  # Copia el status code
        success=response.status_code == 200  # Marca si fue exitosa
    )

@app.get("temperature/{history}")
def get_temperature_history(lat: float, lon: float, start_date: str, end_date: str, timezone: str = "UTC") -> WeatherHistoryResponse:
    params = {
        "latitude": lat,
        "longitude": lon,
        "start_date": start_date,
        "end_date": end_date,
        "current_weather": True,
        "timezone": timezone
    }
    response = requests.get(url_forecast, params=params
                           )
    return WeatherHistoryResponse( 
        latitude=lat,
        longitude=lon,
        timezone="UTC",
        data=response.json(),           # Extrae los datos JSON
        status_code=response.status_code,  # Copia el status code
        success=response.status_code == 200  # Marca si fue exitosa
    )

@app.get("/temperature/{stats}")
def get_temperature_stats(lat: float, lon: float, start_date: str, end_date: str) -> WeatherResponse:
    params = {
        "latitude": lat,
        "longitude": lon,
        "start_date": start_date,
        "end_date": end_date,
        "temperature_statistics": True,
        "timezone": "UTC"
    }
    response = requests.get(url_forecast, params=params)

    return WeatherResponse(
        data=response.json(),           # Extrae los datos JSON
        status_code=response.status_code,  # Copia el status code
        success=response.status_code == 200  # Marca si fue exitosa
    )

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)

    