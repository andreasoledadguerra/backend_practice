# Backend Practice

A FastAPI-based backend application that provides weather temperature data using the Open-Meteo API.

## Features

- **Weather API Endpoint**: Retrieve hourly temperature data for a specified location and date range.
- **FastAPI Framework**: Built with FastAPI for high-performance async web APIs.
- **Open-Meteo Integration**: Fetches data from the free Open-Meteo weather API.

## Prerequisites

- Python 3.7+
- FastAPI
- Requests
- Uvicorn

## Installation

1. Clone the repository:
   ```bash
   git clone git@github.com:andreasoledadguerra/backend_practice.git
   cd backend_practice
   ```

2. Install dependencies:
   ```bash
   pip install fastapi requests uvicorn
   ```

## Usage

### Running the Application

Start the FastAPI server using uvicorn:

```bash
python main.py
```

Or directly with uvicorn:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`.

### API Endpoints

#### GET /temperature

Retrieves hourly temperature data for a given location and date range.

**Query Parameters:**
- `lat` (float): Latitude of the location
- `lon` (float): Longitude of the location
- `date_i` (string): Start date in YYYY-MM-DD format
- `date_f` (string): End date in YYYY-MM-DD format

**Example Request:**
```
GET http://localhost:8000/temperature?lat=40.7128&lon=-74.0060&date_i=2025-08-01&date_f=2025-08-07
```

**Response:**
```json
{
  "data": {
    "latitude": 40.7128,
    "longitude": -74.0060,
    "generationtime_ms": 0.123,
    "utc_offset_seconds": 0,
    "timezone": "UTC",
    "timezone_abbreviation": "UTC",
    "elevation": 10.0,
    "hourly_units": {
      "time": "iso8601",
      "temperature_2m": "°C"
    },
    "hourly": {
      "time": ["2025-08-01T00:00:00", ...],
      "temperature_2m": [22.5, 23.1, ...]
    }
  },
  "status_code": 200,
  "success": true
}
```

### Testing the API

Run the included test script to make a sample request:

```bash
python send_request.py
```

This will send a request for New York City's temperature data from August 1-7, 2025, and print the response.

## Project Structure

- `main.py`: Main FastAPI application with the temperature endpoint
- `send_request.py`: Test script to demonstrate API usage
- `open_meteo.py`: (Additional Open-Meteo related code, if any)
- `README.md`: This file
- `LICENSE`: Project license

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
