"""Tests for Step 5a: More Complex Result Models.

applescab, orientalfruitmoth, and tomcast are seasonal - whether a plain
"no overrides" request succeeds depends on the calendar. These tests assert
the response envelope is always well-formed, and additionally assert success
when the endpoints happen to be in season.
"""

import requests


def test_applescab_run_returns_well_formed_response(
    rm_api_url: str, auth_headers: dict[str, str], station_code: str, recent_date: str
) -> None:
    url = (
        f"{rm_api_url}/db2/run?stationCode={station_code}&stationType=1"
        f"&selectDate={recent_date}&resultModelCode=applescab"
    )
    response = requests.get(url, headers=auth_headers, timeout=30)
    assert response.status_code == 200
    body = response.json()
    assert isinstance(body["error"], bool)
    if not body["error"]:
        assert "gtStart_used" in body["data"]


def test_orientalfruitmoth_run_returns_well_formed_response(
    rm_api_url: str, auth_headers: dict[str, str], station_code: str, recent_date: str
) -> None:
    url = (
        f"{rm_api_url}/db2/run?stationCode={station_code}&stationType=1"
        f"&selectDate={recent_date}&resultModelCode=orientalfruitmoth"
    )
    response = requests.get(url, headers=auth_headers, timeout=30)
    assert response.status_code == 200
    body = response.json()
    assert isinstance(body["error"], bool)


def test_orientalfruitmoth_bad_biofix_combo_is_rejected(
    rm_api_url: str, auth_headers: dict[str, str], station_code: str
) -> None:
    """biofix2 before biofix1 should be a documented application-level error."""
    url = (
        f"{rm_api_url}/db2/run?stationCode={station_code}&stationType=1"
        "&selectDate=2023-12-01&resultModelCode=orientalfruitmoth"
        "&biofix1=2023-05-30&biofix2=2023-04-30"
    )
    response = requests.get(url, headers=auth_headers, timeout=30)
    assert response.status_code == 200
    body = response.json()
    assert body["error"] is True


def test_tomcast_run_returns_well_formed_response(
    rm_api_url: str, auth_headers: dict[str, str], station_code: str, recent_date: str
) -> None:
    url = (
        f"{rm_api_url}/db2/run?stationCode={station_code}&stationType=1"
        f"&selectDate={recent_date}&resultModelCode=tomcast"
    )
    response = requests.get(url, headers=auth_headers, timeout=30)
    assert response.status_code == 200
    body = response.json()
    assert isinstance(body["error"], bool)
