from manageconf import get_config
import requests


def get_weather_from_provider(lat: str, lon: str) -> str:
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
    darksky_api_key = get_config("DARKSKY_API_KEY", None)
    if darksky_api_key is None:
        raise Exception("Config error, missing darksky_api_key")
    url = f"https://api.darksky.net/forecast/{darksky_api_key}/{lat},{lon}?units=ca"
    darksky_exclude_str = get_config("darksky_exclude", "")
    if darksky_exclude_str:
        url = f"{url}&exclude={darksky_exclude_str}"
    return url
