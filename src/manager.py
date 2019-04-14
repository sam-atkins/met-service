from manageconf import get_config
import requests


DARKSKY_API_KEY = get_config("DARKSKY_API_KEY", "")


def get_weather_from_provider(lat: str, lon: str):
    """
    HTTP request to DarkSky API to get weather forecast for the given location based
    on the latitude and longitude args

    Args:
        lat (str): latitude of the location
        lon (str): longitude of the location

    Returns:
        JSON response object: weather forecast of the location
    """
    url = _build_url(lat=lat, lon=lon)
    response = requests.get(url)
    status_code = response.status_code
    if 200 <= status_code < 300:
        return response.text
    else:
        response.raise_for_status()


def _build_url(lat: str, lon: str) -> str:
    """
    Builds the request url, with exclude params to remove forecast data (based on
    the config param `darksky_exclude`)

    Args:
        lat (str): latitude of the location
        lon (str): longitude of the location

    Returns:
        str: request url
    """
    url = f"https://api.darksky.net/forecast/{DARKSKY_API_KEY}/{lat},{lon}?units=ca"
    darksky_exclude_str = get_config("darksky_exclude", "")
    if darksky_exclude_str:
        url = f"{url}&exclude={darksky_exclude_str}"
    return url
