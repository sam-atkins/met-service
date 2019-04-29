import json

from requests.exceptions import HTTPError
from unittest.mock import patch

from met_service.service import get_weather
from tests.datasets.darksky_api_response import DARKSKY_RESPONSE


@patch(
    "met_service.service.get_weather_from_provider",
    return_value=json.dumps(DARKSKY_RESPONSE),
)
def test_get_weather_with_name_returns_200(
    mock_get_weather, apigw_full_event_with_name, mocker
):
    response = get_weather(apigw_full_event_with_name, "")
    assert response["statusCode"] == 200
    data = json.loads(response["body"])
    assert "daily" in data


@patch(
    "met_service.service.get_weather_from_provider",
    return_value=json.dumps(DARKSKY_RESPONSE),
)
def test_get_weather_with_coords_returns_200(
    mock_get_weather, apigw_event_with_coords, mocker
):
    response = get_weather(apigw_event_with_coords, "")
    assert response["statusCode"] == 200
    data = json.loads(response["body"])
    assert "daily" in data


@patch(
    "met_service.service.get_weather_from_provider",
    return_value=json.dumps(DARKSKY_RESPONSE),
)
def test_get_weather_with_empty_request_body_returns_400(
    mock_get_weather, apigw_event_empty_body, mocker
):
    response = get_weather(apigw_event_empty_body, "")
    assert response["statusCode"] == 400
    data = json.loads(response["body"])
    assert data == {"message": "Provide the location name or lat and lon"}


@patch(
    "met_service.service.get_weather_from_provider",
    return_value=json.dumps(DARKSKY_RESPONSE),
)
def test_get_weather_with_incomplete_request_body_returns_400(
    mock_get_weather, apigw_event_with_incomplete_coords, mocker
):
    response = get_weather(apigw_event_with_incomplete_coords, "")
    assert response["statusCode"] == 400
    data = json.loads(response["body"])
    assert data == {"message": "Provide the location name or lat and lon"}


@patch(
    "met_service.service.get_weather_from_provider",
    return_value=json.dumps(DARKSKY_RESPONSE),
)
def test_get_weather_with_name_not_config_returns_400(
    mock_get_weather, apigw_event_with_name_not_in_config, mocker
):
    response = get_weather(apigw_event_with_name_not_in_config, "")
    assert response["statusCode"] == 400
    data = json.loads(response["body"])
    assert data == {"message": "Missing config for provided location name"}


@patch("met_service.service.get_weather_from_provider", side_effect=HTTPError)
def test_get_weather_with_name_returns_500_if_httperror(
    mock_get_weather, apigw_full_event_with_name, mocker
):
    response = get_weather(apigw_full_event_with_name, "")
    assert response["statusCode"] == 500
