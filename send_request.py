"""
Este script haría la lógica de enviar una solicitud HTTP a un endpoint FastAPI.
"""

import requests

headers = {"Authorization": "mi_token_super_secreto_1711"}

if __name__ == "__main__":

    # Ejemplo de llamada al endpoint FastAPI para obtener temperatura por fechas
    params = {
        "lat": 40.7128,
        "lon": -74.0060,
        "date_i": "2025-08-09",
        "date_f": "2025-08-15"
    }
    response = requests.get("http://localhost:8000/temperature", params=params, headers=headers)
    print(response.status_code)
    print(response.json())

    # Ejemplo de llamada al endpoint FastAPI para obtener el clima por ciudad
    params = {
        "city": "New York",
        "lat": 40.7128,
        "lon": -74.0060,
        "current_weather": True,
        "timezone": "UTC"
    }  
    response = requests.get("http://localhost:8000/temperature/city", params=params,headers=headers)
    print(response.status_code)
    print(response.json())



    # Ejemplo de llamada al endpoint FastAPI para obtener el historial de temperatura
    params = {
        "lat": 40.7128,
        "lon": -74.0060,
        "start_date": "2025-08-09",
        "end_date": "2025-08-15",
        "current_weather": True,
        "timezone": "UTC"
    }
    response = requests.get("http://localhost:8000/temperature/history", params=params, headers=headers)
    print(response.status_code)
    print(response.json()) 



    # Ejemplo de llamada al endpoint FastAPI para obtener estadísticas de temperatura
    params = {    
        "lat": 40.7128,
        "lon": -74.0060,
        "start_date": "2025-08-09",
        "end_date": "2025-08-15",
        "mean_temperature": True,
        "min_temperature": True,
        "max_temperature": True,
        "timezone":"UTC"
    }
    response = requests.get("http://localhost:8000/temperature/stats", params=params, headers=headers)
    print(response.status_code)
    print(response.json())





