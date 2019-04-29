import json

from manageconf import Config, get_config  # noqa F401
from requests.exceptions import HTTPError

# NOTE due to different folder structure in build vs. dev, the try/except allows
# runtime and pytest to find the modules
try:
    from locations import get_location_coords_by_short_name
except ModuleNotFoundError:
    from met_service.locations import get_location_coords_by_short_name
try:
    from manager import get_weather_from_provider
except ModuleNotFoundError:
    from met_service.manager import get_weather_from_provider


def get_weather(event: dict, context: dict) -> dict:
    """
    Gets weather for a provided location.

    Args:
        event (dict): API Gateway Lambda Proxy Input Format
        context (dict): Lambda Context runtime methods and attributes

    Returns:
        JSON response object
    """
    error_response = {
        "statusCode": 400,
        "body": json.dumps({"message": "Provide the location name or lat and lon"}),
    }
    payload = event.get("body", {})
    if isinstance(payload, str):
        payload = json.loads(payload)
    if payload is None:
        return error_response
    lat = payload.get("lat", None)
    lon = payload.get("lon", None)
    if None in [lat, lon]:
        location_name = payload.get("name", None)
        if location_name is None:
            return error_response
        location_coords = get_location_coords_by_short_name(location_name=location_name)
        lon = location_coords.get("lon", None)
        lat = location_coords.get("lat", None)
        if None in [lat, lon]:
            return {
                "statusCode": 400,
                "body": json.dumps(
                    {"message": "Missing config for provided location name"}
                ),
            }
    try:
        response = get_weather_from_provider(lat=lat, lon=lon)
        return {"statusCode": 200, "body": response}
    except HTTPError as ex:
        error_message = f"Server error: {ex}"
        # log to Cloudwatch
        print(error_message)
        return {"statusCode": 500, "body": json.dumps(error_message)}
