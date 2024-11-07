import requests
from datetime import datetime
from .config import OPENWEATHERMAP_API_KEY

def get_historical_weather(latitude: float, longitude: float, date: str):
    # Convert date to UNIX timestamp for API request
    timestamp = int(datetime.strptime(date, "%Y-%m-%d").timestamp())

    url = f"http://api.openweathermap.org/data/2.5/onecall/timemachine"
    params = {
        "lat": latitude,
        "lon": longitude,
        "dt": timestamp,
        "appid": OPENWEATHERMAP_API_KEY,
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch weather data: {response.text}")

def check_adverse_weather_conditions(weather_data):
    # Check for adverse weather conditions
    adverse_conditions = ["rain", "snow", "thunderstorm"]
    for hour_data in weather_data.get("hourly", []):
        weather_conditions = [w.get("main").lower() for w in hour_data.get("weather", [])]
        if any(condition in adverse_conditions for condition in weather_conditions):
            return True
    return False
