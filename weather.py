import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass

load_dotenv()


@dataclass
class WeatherData:
    main: str
    description: str
    icon: str
    temperature: int

def get_lat_lon(city_name, state_code, country_code):
    api_key = os.getenv('API_KEY')
    resp = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={api_key}').json()
    data = resp[0]
    lat, lon = data.get('lat'), data.get('lon')
    return lat, lon

def get_current_weather(lat, lon):
    api_key = os.getenv('API_KEY')
    resp = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric').json()

    data = WeatherData(
        main=resp.get('weather')[0].get('main'),
        description=resp.get('weather')[0].get('description'),
        icon=resp.get('weather')[0].get('icon'),
        temperature=int(resp.get('main').get('temp'))
    )

    return data

def main():
    city_name = input("Enter the city name: ")
    state_code = input("Enter the state code: ")
    country_code = input("Enter the country code: ")

    lat, lon = get_lat_lon(city_name, state_code, country_code)
    weather_data = get_current_weather(lat, lon)

    print(f"Weather in {city_name}, {state_code}, {country_code}:")
    print(f"Main: {weather_data.main}")
    print(f"Description: {weather_data.description}")
    print(f"Icon: {weather_data.icon}")
    print(f"Temperature: {weather_data.temperature}°C")

if __name__ == "__main__":
    main()
