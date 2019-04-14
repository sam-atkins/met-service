from src.manager import _build_url


def test__build_url_returns_url_with_exclude_str():
    lat = "51.50853"
    lon = "-0.12574"
    url = _build_url(lat=lat, lon=lon)
    assert url == (
        "https://api.darksky.net/forecast/fake-api-key/"
        "51.50853,-0.12574?units=ca&exclude=minutely,hourly,flags"
    )
