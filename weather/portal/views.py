import logging
from datetime import date, timedelta

from django.shortcuts import render
from weather.portal.utils import FakeWeatherAPI 

logger = logging.getLogger(__name__)
fake_api = FakeWeatherAPI()


def home(request):
    """
    Home view using the fake weather API
    """
    lat, lon = 37.7749, -122.4194
    data = fake_api.get_forecast(lat, lon)
    current = data.get('current', {})

    weather_data = {
        'current': {
            'temp_c': f"{current.get('temperature', 'N/A')}°C",
            'condition': {
                'text': current.get('weather_description', 'Unknown'),
                'icon': current.get('weather_icon', '')
            },
            'humidity': f"{current.get('humidity', 'N/A')}%",
            'wind_kph': f"{current.get('wind_speed', 'N/A')} km/h"
        }
    }

    return render(request, 'home.html', {'weather': weather_data})


def city_weather(request, city):
    """
    Combined current, forecast, and historical weather using the fake weather API.
    """
    city_coords = {
        'beijing': (39.9042, 116.4074),
        'new-york': (40.7128, -74.0060),
        'london': (51.5074, -0.1278),
        'tokyo': (35.6762, 139.6503),
        'paris': (48.8566, 2.3522),
        'sydney': (-33.8688, 151.2093),
        'san-francisco': (37.7749, -122.4194),
    }

    lat, lon = city_coords.get(city.lower(), (37.7749, -122.4194))

    # Current Weather
    current_data = fake_api.get_forecast(lat, lon)
    current = current_data.get('current', {})

    weather_data = {
        'city': city.replace('-', ' ').title(),
        'current': {
            'temp_c': f"{current.get('temperature', 'N/A')}°C",
            'condition': {
                'text': current.get('weather_description', 'Unknown'),
                'icon': current.get('weather_icon', '')
            },
            'humidity': f"{current.get('humidity', 'N/A')}%",
            'wind_kph': current.get('wind_speed', 'N/A'),
            'wind_direction': current.get('wind_compass', 'N/A'),
        }
    }

    # 10-day forecast
    forecast_response = fake_api.get_daily_forecast(lat, lon, days=10)
    forecast_data = [
        {
            'date': day['date'],
            'weather_description': day['weather_description'],
            'temp_max': day['temperature_max'],
            'temp_min': day['temperature_min'],
            'precipitation': day['precipitation_sum'],
            'wind_speed': day['wind_speed_max'],
            'uv_index': day.get('uv_index_max', 0),
        }
        for day in forecast_response['daily']
    ]

    # 7-day historical data
    end_date = date.today() - timedelta(days=1)
    start_date = end_date - timedelta(days=6)
    historical_response = fake_api.get_historical_weather(lat, lon, start_date, end_date)
    historical_data = [
        {
            'date': day['date'],
            'weather_description': day['weather_description'],
            'temp_max': day['temperature_max'],
            'temp_min': day['temperature_min'],
            'precipitation': day['precipitation_sum'],
            'wind_speed': day['wind_speed_max'],
        }
        for day in historical_response['historical']
    ]

    context = {
        'weather': weather_data,
        'forecast_data': forecast_data,
        'historical_data': historical_data,
        'city': city.replace('-', ' ').title(),
        'popular_cities': list(city_coords.keys()),
    }

    return render(request, 'city.html', context)
