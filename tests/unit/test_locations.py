import pytest

from met_service.locations import (
    get_location_info_by_short_name,
    get_location_coords_by_short_name,
)


def test_get_location_info_by_short_name_returns_location_dict():
    location_name = "ldn"
    get_location = get_location_info_by_short_name(location_name)
    assert get_location == {
        "name": "London",
        "country": "GB",
        "coord": {"lon": -0.12574, "lat": 51.50853},
    }


@pytest.mark.parametrize("location_name", ["abc", "zzz", "where?", 123])
def test_get_location_info_by_short_name_returns_empty_dict_if_bad_name(location_name):
    get_location = get_location_info_by_short_name(location_name)
    assert get_location == {}


def test_get_location_coords_by_short_name_returns_location_dict():
    location_name = "ldn"
    get_location = get_location_coords_by_short_name(location_name)
    assert get_location == {"lon": -0.12574, "lat": 51.50853}


@pytest.mark.parametrize("location_name", ["abc", "zzz", "where?", 123])
def test_get_location_coords_by_short_name_returns_empty_dict_if_bad_name(
    location_name
):
    get_location = get_location_coords_by_short_name(location_name)
    assert get_location == {}
