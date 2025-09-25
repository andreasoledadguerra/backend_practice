"""
Este script haría la lógica de enviar una solicitud HTTP a un endpoint FastAPI.
"""

import requests


if __name__ == "__main__":
    params = {
        "lat": 40.7128,
        "lon": -74.0060,
        "date_i": "2025-06-01",
        "date_f": "2025-06-07"
    }
    response = requests.get("http://localhost:8000/temperature", params=params)
    print(response.status_code)
    print(response.json())

    #params = {"param_1": "test", "param_2": 123}
    #response = requests.get("http://localhost:8000/dummy_endpoint", params=params)
    #print(response.status_code)
    #print(response.json())
#
    #response = requests.get("http://localhost:8000/some_new_endpoint", params={"a": 5, "b": 10})
    #print(response.status_code)
    #print(response.json())