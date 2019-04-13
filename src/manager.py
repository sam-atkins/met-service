from manageconf import get_config
import requests


DARKSKY_API_KEY = get_config("DARKSKY_API_KEY", "")


def get_weather_from_provider(lat: str, lon: str):
    """
    Makes request to DarkSky API to get weather forecast for location based on
    latitude and longitude

    Args:
        lat (str): latitude of the location
        lon (str): longitude of the location

    Returns:
        JSON response object: weather forecast of the location
    """
    url = f"https://api.darksky.net/forecast/{DARKSKY_API_KEY}/{lat},{lon}?units=ca"
    darksky_exclude_list = get_config("darksky_exclude", [])
    if darksky_exclude_list:
        exclude_str = ",".join(darksky_exclude_list)
        url = f"{url}&exclude={exclude_str}"
    response = requests.get(url)
    status_code = response.status_code
    if 200 <= status_code < 300:
        return response.text
    else:
        response.raise_for_status()
