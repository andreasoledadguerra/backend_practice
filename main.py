import uvicorn
import requests

from fastapi import FastAPI, Query
from requests import Response

# Create FastAPI instance
app = FastAPI()

# Open-Meteo API endpoint for weather forecast
url_forecast = "https://api.open-meteo.com/v1/forecast"

@app.get("/temperature")
def get_temperature_by_dates(lat: float, lon: float, date_i: str, date_f: str) -> Response:
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m",
        "start_date": date_i,
        "end_date": date_f,
        "timezone": "UTC"
    }
    response: Response = requests.get(url_forecast, params=params)
    return response

# @app.get("/ping")
# def ping():
#     result = {"Eve": "Vieja"}
#     return result

# @app.get("/dummy_endpoint")
# def dummy_endpoint(param_1: str = Query(...), param_2: int = Query(...)):
#    print(f"param_1={param_1} - param_2={param_2}")
#    return {"content": "dummy"}
#
# def my_complex_function(a: int, b: int):
#    return a + b
#
# @app.get("/some_new_endpoint")
# def some_new_endpoint(a: int, b: int):
#    result = my_complex_function(a, b)
#    return {"content": result}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)