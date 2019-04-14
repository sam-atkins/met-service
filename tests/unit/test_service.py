from unittest.mock import patch

import pytest
from requests.exceptions import HTTPError

from src.service import app

API_VERSION = "v1.0"


@pytest.fixture
def client():
    client = app.test_client()
    yield client


def test_get_weather_no_request_args_returns_400(client):
    api_url = f"/api/{API_VERSION}/weather"
    response = client.post(api_url)
    assert response.status_code == 400
    assert (
        response.data
        == b'{"message":"Provide the location name or latitude and longitude"}\n'
    )


def test_get_weather_only_lat_arg_returns_400(client):
    api_url = f"/api/{API_VERSION}/weather?lat=-0.12574"
    response = client.post(api_url)
    assert response.status_code == 400
    assert (
        response.data
        == b'{"message":"Provide the location name or latitude and longitude"}\n'
    )


def test_get_weather_only_lon_arg_returns_400(client):
    api_url = f"/api/{API_VERSION}/weather?lon=-0.12574"
    response = client.post(api_url)
    assert response.status_code == 400
    assert (
        response.data
        == b'{"message":"Provide the location name or latitude and longitude"}\n'
    )


@pytest.mark.parametrize("location_name", ["abc", "zzz", "where?", 123])
def test_get_weather_unknown_location_name_returns_400(location_name, client):
    api_url = f"/api/{API_VERSION}/weather?name={location_name}"
    response = client.post(api_url)
    assert response.status_code == 400
    assert response.data == b'{"message":"Missing config for provided location name"}\n'


@patch("src.service.get_weather_from_provider", return_value={})
def test_get_weather_returns_200(mock_get_weather, client):
    api_url = f"/api/{API_VERSION}/weather?name=ldn"
    response = client.post(api_url)
    assert response.status_code == 200


@patch("src.service.get_weather_from_provider", side_effect=HTTPError)
def test_get_weather_http_error_returns_500(mock_get_weather, client):
    api_url = f"/api/{API_VERSION}/weather?name=ldn"
    response = client.post(api_url)
    assert response.status_code == 500
