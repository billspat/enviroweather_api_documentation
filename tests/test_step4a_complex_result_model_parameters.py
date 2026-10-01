"""Tests for Step 4a: More Complex Result Model Parameters (calculated defaults)."""

import requests


def test_applescab_inputs_has_default_resource_key(api_url: str, auth_headers: dict[str, str]) -> None:
    response = requests.get(
        f"{api_url}/db2/resources/applescab/inputs?show=rmInputs", headers=auth_headers, timeout=30
    )
    assert response.status_code == 200
    body = response.json()
    assert body["error"] is False
    assert body["data"][0]["defaultResourceKey"] == "mcintoshgreentip"


def test_orientalfruitmoth_inputs_has_default_resource_key(
    api_url: str, auth_headers: dict[str, str]
) -> None:
    response = requests.get(
        f"{api_url}/db2/resources/orientalfruitmoth/inputs?show=rmInputs", headers=auth_headers, timeout=30
    )
    assert response.status_code == 200
    body = response.json()
    assert body["error"] is False
    assert body["data"][0]["defaultResourceKey"] == "orientalfruitmothadultemergence"


def test_tomcast_inputs_has_default_resource_key(api_url: str, auth_headers: dict[str, str]) -> None:
    response = requests.get(
        f"{api_url}/db2/resources/tomcast/inputs?show=rmInputs", headers=auth_headers, timeout=30
    )
    assert response.status_code == 200
    body = response.json()
    assert body["error"] is False
    assert body["data"][0]["defaultResourceKey"] == "tomcastdefaults"


def test_mcintoshgreentip_default_calculation(
    rm_api_url: str, auth_headers: dict[str, str], station_code: str, recent_date: str
) -> None:
    url = (
        f"{rm_api_url}/db2/run?stationCode={station_code}&stationType=1"
        f"&selectDate={recent_date}&resultModelCode=mcintoshgreentip"
    )
    response = requests.get(url, headers=auth_headers, timeout=30)
    assert response.status_code == 200
    body = response.json()
    assert body["error"] is False
    assert "gtStart_estimated" in body["data"]


def test_orientalfruitmothadultemergence_default_calculation(
    rm_api_url: str, auth_headers: dict[str, str], station_code: str, recent_date: str
) -> None:
    url = (
        f"{rm_api_url}/db2/run?stationCode={station_code}&stationType=1"
        f"&selectDate={recent_date}&resultModelCode=orientalfruitmothadultemergence"
    )
    response = requests.get(url, headers=auth_headers, timeout=30)
    assert response.status_code == 200
    body = response.json()
    assert body["error"] is False
    assert "biofix1_estimated" in body["data"]
