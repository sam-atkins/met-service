import json

from manageconf import Config, get_config  # noqa F401
from requests.exceptions import HTTPError

from .locations import get_location_coords_by_short_name
from .manager import get_weather_from_provider


def get_weather(event, context):
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
    body = event.get("body", {})
    if body is None:
        return error_response

    payload = json.loads(body)
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
        return {"statusCode": 200, "body": json.dumps(response)}
    except HTTPError as ex:
        error_message = f"Server error: {ex}"
        return {"statusCode": 500, "body": json.dumps(error_message)}
