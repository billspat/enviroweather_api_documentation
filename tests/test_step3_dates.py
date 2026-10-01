"""Tests for Step 3: Dates."""

import requests


def test_get_generic_date_pickers(api_url: str, auth_headers: dict[str, str]) -> None:
    response = requests.get(f"{api_url}/db2/datePickers", headers=auth_headers, timeout=30)
    assert response.status_code == 200
    body = response.json()
    assert body["error"] is False
    assert body["data"][0]["key"] == "selectDate"


def test_get_date_pickers_with_station_code(
    api_url: str, auth_headers: dict[str, str], station_code: str
) -> None:
    response = requests.get(
        f"{api_url}/db2/datePickers?stationCode={station_code}", headers=auth_headers, timeout=30
    )
    assert response.status_code == 200
    body = response.json()
    assert body["error"] is False
    date_input = body["data"][0]["dateInputs"][0]
    assert date_input["stationCode"] == station_code
    assert "dateStart" in date_input
    assert "dateEnd" in date_input


def test_get_date_pickers_for_result_model(
    api_url: str, auth_headers: dict[str, str], station_code: str
) -> None:
    response = requests.get(
        f"{api_url}/db2/resources/weathersummary/datePickers?stationCode={station_code}",
        headers=auth_headers,
        timeout=30,
    )
    assert response.status_code == 200
    body = response.json()
    assert body["error"] is False
    assert body["data"][0]["key"] == "selectDate"


def test_latestobstable_datepickers_is_forbidden(api_url: str, auth_headers: dict[str, str]) -> None:
    """latestobstable has been withdrawn from production; this route now fails
    with a plain 401 and a non-standard body (``{"error": "Forbidden"}``,
    where ``error`` is a string, not the usual envelope). See
    ewx_api_v1_resource_common_errors.py for why this matters.
    """
    response = requests.get(
        f"{api_url}/db2/resources/latestobstable/datePickers", headers=auth_headers, timeout=30
    )
    assert response.status_code == 401
    assert response.json()["error"] == "Forbidden"
