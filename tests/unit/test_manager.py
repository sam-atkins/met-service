import json

import pytest
from requests.exceptions import HTTPError

from src.manager import get_weather_from_provider, _build_url
from tests.datasets.darksky_api_response import DARKSKY_RESPONSE


@pytest.mark.parametrize("status_code", [200, 201])
def test_get_weather_from_provider_returns_payload_on_2xx(status_code, requests_mock):
    url = (
        "https://api.darksky.net/forecast/fake-api-key/"
        "51.50853,-0.12574?units=ca&exclude=minutely,hourly,flags"
    )
    mock_response = json.dumps(DARKSKY_RESPONSE)
    requests_mock.get(url, text=mock_response, status_code=status_code)
    lat = "51.50853"
    lon = "-0.12574"
    response = get_weather_from_provider(lat=lat, lon=lon)
    assert response == mock_response


def test_get_weather_from_provider_raises_on_400(requests_mock):
    url = (
        "https://api.darksky.net/forecast/fake-api-key/"
        "51.50853,-0.12574?units=ca&exclude=minutely,hourly,flags"
    )
    requests_mock.get(url, text="{}", status_code=400)
    lat = "51.50853"
    lon = "-0.12574"
    with pytest.raises(HTTPError):
        get_weather_from_provider(lat=lat, lon=lon)


def test__build_url_returns_url_with_exclude_str():
    lat = "51.50853"
    lon = "-0.12574"
    url = _build_url(lat=lat, lon=lon)
    assert url == (
        "https://api.darksky.net/forecast/fake-api-key/"
        "51.50853,-0.12574?units=ca&exclude=minutely,hourly,flags"
    )
