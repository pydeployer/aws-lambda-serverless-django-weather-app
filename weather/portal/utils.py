from faker import Faker
import random
import datetime

class FakeWeatherAPI:
    def __init__(self, timezone="auto"):
        self.fake = Faker()
        self.timezone = timezone

    def get_forecast(self, latitude: float, longitude: float):
        now = datetime.datetime.now().isoformat(timespec='seconds')

        temperature = round(self.fake.pyfloat(min_value=-10, max_value=35, right_digits=1), 1)
        humidity = self.fake.pyint(min_value=20, max_value=100)
        wind_speed = round(self.fake.pyfloat(min_value=0.0, max_value=15.0, right_digits=1), 1)
        wind_deg = round(self.fake.pyfloat(min_value=0, max_value=360), 1)
        weather_code = random.choice(self.get_all_weather_codes())

        return {
            "latitude": latitude,
            "longitude": longitude,
            "generationtime_ms": round(self.fake.pyfloat(min_value=0.1, max_value=1.5), 2),
            "utc_offset_seconds": 0,
            "timezone": self.timezone,
            "timezone_abbreviation": "PDT",
            "elevation": round(self.fake.pyfloat(min_value=0, max_value=500), 1),
            "current_units": {
                "time": "iso8601",
                "temperature": "°C",
                "humidity": "%",
                "wind_speed": "m/s",
                "wind_direction": "°",
                "weather_code": "wmo"
            },
            "current": {
                "time": now,
                "temperature": temperature,
                "humidity": humidity,
                "wind_speed": wind_speed,
                "wind_direction": wind_deg,
                "wind_compass": self.get_wind_direction(wind_deg),
                "weather_code": weather_code,
                "weather_description": self.get_weather_description(weather_code),
                "weather_icon": self.get_weather_icon(weather_code)
            }
        }

    def get_daily_forecast(self, latitude: float, longitude: float, days: int = 7):
        today = datetime.date.today()
        return self._generate_daily_data(latitude, longitude, today, days, label="daily")

    def get_historical_weather(self, latitude: float, longitude: float, start_date: datetime.date, end_date: datetime.date):
        days = (end_date - start_date).days + 1
        return self._generate_daily_data(latitude, longitude, start_date, days, label="historical")

    def _generate_daily_data(self, latitude, longitude, start_date, days, label="daily"):
        daily_data = []
        for i in range(days):
            date = start_date + datetime.timedelta(days=i)
            temperature_max = round(random.uniform(15, 35), 1)
            temperature_min = round(random.uniform(5, temperature_max - 5), 1)
            precipitation_sum = round(random.uniform(0.0, 20.0), 1)
            wind_speed_max = round(random.uniform(2.0, 15.0), 1)
            uv_index_max = round(random.uniform(1, 11), 1)
            weather_code = random.choice(self.get_all_weather_codes())

            item = {
                "date": date.isoformat(),
                "temperature_max": temperature_max,
                "temperature_min": temperature_min,
                "precipitation_sum": precipitation_sum,
                "wind_speed_max": wind_speed_max,
                "weather_code": weather_code,
                "weather_description": self.get_weather_description(weather_code),
                "weather_icon": self.get_weather_icon(weather_code)
            }

            if label == "daily":
                item["uv_index_max"] = uv_index_max  # only forecast includes UV index

            daily_data.append(item)

        return {
            "latitude": latitude,
            "longitude": longitude,
            "timezone": self.timezone,
            f"{label}_units": {
                "date": "iso8601",
                "temperature_max": "°C",
                "temperature_min": "°C",
                "precipitation_sum": "mm",
                "wind_speed_max": "m/s",
                "uv_index_max": "index" if label == "daily" else None,
                "weather_code": "wmo"
            },
            label: daily_data
        }

    # --- Helpers ---
    def get_weather_description(self, weather_code):
        descriptions = {
            0: "Clear sky", 1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
            45: "Fog", 48: "Depositing rime fog",
            51: "Light drizzle", 53: "Moderate drizzle", 55: "Dense drizzle",
            61: "Slight rain", 63: "Moderate rain", 65: "Heavy rain",
            71: "Slight snow fall", 73: "Moderate snow fall", 75: "Heavy snow fall",
            77: "Snow grains", 80: "Slight rain showers", 81: "Moderate rain showers",
            82: "Violent rain showers", 85: "Slight snow showers", 86: "Heavy snow showers",
            95: "Thunderstorm", 96: "Thunderstorm with slight hail", 99: "Thunderstorm with heavy hail",
        }
        return descriptions.get(weather_code, "Unknown")

    def get_weather_icon(self, weather_code):
        icons = {
            0: "☀️", 1: "🌤️", 2: "⛅", 3: "☁️", 45: "🌫️", 48: "🌫️",
            51: "🌦️", 53: "🌦️", 55: "🌧️", 61: "🌧️", 63: "🌧️", 65: "⛈️",
            71: "🌨️", 73: "🌨️", 75: "❄️", 77: "❄️", 80: "🌦️", 81: "🌧️",
            82: "⛈️", 85: "🌨️", 86: "❄️", 95: "⛈️", 96: "⛈️", 99: "⛈️"
        }
        return icons.get(weather_code, "❓")

    def get_wind_direction(self, degrees):
        if degrees is None:
            return "N/A"
        try:
            degrees = float(degrees)
        except (TypeError, ValueError):
            return "N/A"
        directions = [
            "N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
            "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"
        ]
        index = round(degrees / 22.5) % 16
        return directions[index]

    def get_all_weather_codes(self):
        return [
            0, 1, 2, 3, 45, 48,
            51, 53, 55, 61, 63, 65,
            71, 73, 75, 77,
            80, 81, 82, 85, 86,
            95, 96, 99
        ]
