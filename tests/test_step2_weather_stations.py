"""Tests for Step 2: Weather Stations."""

import requests


def test_get_station_list(api_url: str, auth_headers: dict[str, str]) -> None:
    response = requests.get(f"{api_url}/db2/places?show=ewxstation", headers=auth_headers, timeout=30)
    assert response.status_code == 200
    body = response.json()
    assert body["error"] is False
    stations = body["data"][0]["placeInputs"][0]["options"]
    assert len(stations) > 0
    assert all("value" in s and "display" in s for s in stations)


def test_default_station_is_in_station_list(
    api_url: str, auth_headers: dict[str, str], station_code: str
) -> None:
    response = requests.get(f"{api_url}/db2/places?show=ewxstation", headers=auth_headers, timeout=30)
    stations = response.json()["data"][0]["placeInputs"][0]["options"]
    codes = {s["value"] for s in stations}
    assert station_code in codes


def test_get_station_closest_to_lat_lon(api_url: str, auth_headers: dict[str, str]) -> None:
    url = f"{api_url}/db2/stationnear?lat=42.75313740994824&lon=-84.4907810027659"
    response = requests.get(url, headers=auth_headers, timeout=30)
    assert response.status_code == 200
    body = response.json()
    assert body["error"] is False
    assert isinstance(body["data"][0]["station_id"], str)


def test_get_stations_in_bounding_box(api_url: str, auth_headers: dict[str, str]) -> None:
    url = (
        f"{api_url}/db2/stationin"
        "?sw_lat=42.75313740994824&sw_lon=-84.4907810027659"
        "&ne_lat=43.75313740994824&ne_lon=-82.4907810027659"
    )
    response = requests.get(url, headers=auth_headers, timeout=30)
    assert response.status_code == 200
    body = response.json()
    assert body["error"] is False
