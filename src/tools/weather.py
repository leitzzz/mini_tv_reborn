import urequests as requests

from screen.st7735 import TFT
from screen.sysfont import sysfont


def show_weather(tft, data=None):
    if data is None:
        tft.text((0, 10), "No weather data", TFT.RED,
                 sysfont, 1, nowrap=True)
        return

    location = data.get("location")
    temperature = data.get("temperature")
    humidity = data.get("humidity")
    wind_speed = data.get("wind_speed")
    precipitation_probability = data.get("precipitation_probability")
    precipitation_probability_value = int(
        precipitation_probability.replace("%", ""))
    precipitation_probability_color = TFT.GREEN if precipitation_probability_value < 60 else TFT.RED

    tft.text((0, 10), f"{location}", TFT.GREEN,
             sysfont, 2, nowrap=True)
    tft.text((0, 40), f"Precipitacion: {precipitation_probability}", precipitation_probability_color,
             sysfont, 1, nowrap=True)
    tft.text((0, 60), f"Temperature: {temperature}", TFT.GREEN,
             sysfont, 1, nowrap=True)
    tft.text((0, 80), f"Humidity: {humidity}", TFT.GREEN,
             sysfont, 1, nowrap=True)
    tft.text((0, 100), f"Wind speed: {wind_speed}", TFT.GREEN,
             sysfont, 1, nowrap=True)


def fetch_weather_data(city_coords=None):

    latitude, longitude = city_coords

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"}

    # TODO: must check https:// is given some memory error, maybe we can use http:// instead, but the api seems to require https://, so we need to check if there is a way to make it work with https:// in micropython without running out of memory.
    response = requests.get(
        f"http://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m%2Cwind_speed_10m%2Crelative_humidity_2m%2Cprecipitation_probability%2Crain", timeout=5, headers=headers)
    data = response.json()

    return {
        "temperature": f"{data["current"]["temperature_2m"]} {data["current_units"]["temperature_2m"]}",
        "humidity": f"{data["current"]["relative_humidity_2m"]} {data["current_units"]["relative_humidity_2m"]}",
        "wind_speed": f"{data["current"]["wind_speed_10m"]} {data["current_units"]["wind_speed_10m"]}",
        "precipitation_probability": f"{data["current"]["relative_humidity_2m"]} {data["current_units"]["relative_humidity_2m"]}"
    }
