"""Tests for Step 5: Result Models."""

import requests


def test_weathersummary_run(
    rm_api_url: str, auth_headers: dict[str, str], station_code: str, recent_date: str
) -> None:
    url = (
        f"{rm_api_url}/db2/run?stationCode={station_code}&stationType=1"
        f"&selectDate={recent_date}&resultModelCode=weathersummary"
    )
    response = requests.get(url, headers=auth_headers, timeout=30)
    assert response.status_code == 200
    body = response.json()
    assert body["error"] is False
    assert isinstance(body["data"]["Table"], list)


def test_rainfallregional_run(
    rm_api_url: str, auth_headers: dict[str, str], station_code: str, recent_date: str
) -> None:
    url = (
        f"{rm_api_url}/db2/run?stationCode={station_code}&stationType=1"
        f"&selectDate={recent_date}&resultModelCode=rainfallregional"
        "&selector=network&mdStartAccumulation=March 12th"
    )
    response = requests.get(url, headers=auth_headers, timeout=30)
    assert response.status_code == 200
    body = response.json()
    assert body["error"] is False
    assert isinstance(body["data"]["Table"], list)
    assert len(body["data"]["Table"]) > 0


def test_meteogram_run(
    rm_api_url: str, auth_headers: dict[str, str], station_code: str, recent_date: str
) -> None:
    url = (
        f"{rm_api_url}/db2/run?stationCode={station_code}&stationType=1"
        f"&selectDate={recent_date}&resultModelCode=meteogram&units=metric&duration=72"
    )
    response = requests.get(url, headers=auth_headers, timeout=30)
    assert response.status_code == 200
    body = response.json()
    assert body["error"] is False
    assert isinstance(body["data"]["Table"], list)


def test_latestobstable_run_returns_well_formed_response(
    rm_api_url: str, auth_headers: dict[str, str], station_code: str
) -> None:
    """latestobstable is marked "in testing" and currently returns an
    application-level error in production. Assert the response is at least
    well-formed (has the standard error/message/status/data envelope) rather
    than asserting success, since availability is outside our control.
    """
    url = f"{rm_api_url}/db2/run?stationCode={station_code}&stationType=1&resultModelCode=latestobstable"
    response = requests.get(url, headers=auth_headers, timeout=30)
    assert response.status_code == 200
    body = response.json()
    assert isinstance(body["error"], bool)
    assert isinstance(body["message"], str)
