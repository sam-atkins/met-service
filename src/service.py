from flask import Flask, jsonify, request
from manageconf import Config, get_config  # noqa F401

from locations import get_location_coords_by_short_name
from manager import get_weather_from_provider


app = Flask(__name__)


API_VERSION = "v1.0"
DEBUG = get_config("DEBUG", True)


@app.route(f"/{API_VERSION}/weather", methods=["GET", "POST"])
def get_weather():
    """
    Gets weather for a provided location via querystrings.

    Query string options:
        lon, lat | name

    Returns:
        JSON response object
    """
    lat = request.args.get("lat", None)
    lon = request.args.get("lon", None)
    if not any((lat, lon)):
        location_name = request.args.get("name", None)
        if location_name is None:
            return (
                jsonify(
                    {"message": "Provide the location name or latitude and longitude"}
                ),
                400,
            )
        location_coords = get_location_coords_by_short_name(location_name=location_name)
        lon = location_coords.get("lon", None)
        lat = location_coords.get("lat", None)
        if not any((lat, lon)):
            return (
                jsonify({"message": "Missing config for provided location name."}),
                400,
            )
    try:
        response = get_weather_from_provider(lat=lat, lon=lon)
        return jsonify({"payload": response}), 200
    except Exception as ex:
        error_message = f"Server error: {ex}"
        return jsonify({"message": error_message}), 500


if __name__ == "__main__":
    app.run(debug=DEBUG, host="0.0.0.0")
