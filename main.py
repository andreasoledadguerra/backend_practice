import uvicorn
import requests

from fastapi import FastAPI
from pydantic import BaseModel
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




if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)