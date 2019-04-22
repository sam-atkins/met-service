"""
Favourite locations and helper functions. For now in order to keep things simple,
LOCATIONS is a hard coded dictionary.
"""


def get_location_info_by_short_name(location_name: str) -> dict:
    """Finds a location by the short location name

    Args:
        location_name (str): the short location name e.g. "ldn"

    Returns:
        dict: location info
    """
    try:
        return LOCATIONS[location_name]
    except KeyError:
        return {}


def get_location_coords_by_short_name(location_name: str) -> dict:
    """Finds a location by the short location name

    Args:
        location_name (str): the short location name e.g. "ldn"

    Returns:
        dict: location info
    """
    try:
        return LOCATIONS[location_name]["coord"]
    except KeyError:
        return {}


LOCATIONS = {
    "bar": {
        "name": "Barcelona",
        "country": "ES",
        "coord": {"lon": 2.12804, "lat": 41.399422},
    },
    "ips": {
        "name": "Ipswich",
        "country": "GB",
        "coord": {"lon": 1.16719, "lat": 52.056839},
    },
    "ldn": {
        "name": "London",
        "country": "GB",
        "coord": {"lon": -0.12574, "lat": 51.50853},
    },
    "muc": {
        "name": "Muenchen",
        "country": "DE",
        "coord": {"lon": 11.57549, "lat": 48.137428},
    },
    "sfo": {
        "name": "San Francisco",
        "country": "US",
        "coord": {"lon": -122.45108, "lat": 37.766602},
    },
    "wsz": {
        "name": "Warsaw",
        "country": "PL",
        "coord": {"lon": 21.01178, "lat": 52.229771},
    },
    "wic": {
        "id": 2634234,
        "name": "West Wickham",
        "country": "GB",
        "coord": {"lon": -0.01667, "lat": 51.366669},
    },
}
