"""Tests for Step 4: Result Model Parameters."""

import requests


def test_get_result_model_keys(api_url: str, auth_headers: dict[str, str]) -> None:
    response = requests.get(f"{api_url}/db2/resources?type=rm-api", headers=auth_headers, timeout=30)
    assert response.status_code == 200
    body = response.json()
    assert body["error"] is False
    keys = {item["key"] for item in body["data"]}
    assert "weathersummary" in keys
    assert "rainfallregional" in keys
    assert "meteogram" in keys
    assert "applescab" in keys


def test_weathersummary_has_no_extra_inputs(api_url: str, auth_headers: dict[str, str]) -> None:
    response = requests.get(
        f"{api_url}/db2/resources/weathersummary/inputs?show=rmInputs", headers=auth_headers, timeout=30
    )
    assert response.status_code == 200
    body = response.json()
    assert body["error"] is False
    assert body["data"] == []


def test_rainfallregional_inputs_has_selector(api_url: str, auth_headers: dict[str, str]) -> None:
    response = requests.get(
        f"{api_url}/db2/resources/rainfallregional/inputs?show=rmInputs", headers=auth_headers, timeout=30
    )
    assert response.status_code == 200
    body = response.json()
    assert body["error"] is False
    rm_inputs = body["data"][0]["resultModelInputs"]
    input_keys = {i["key"] for i in rm_inputs}
    assert "selector" in input_keys
    assert "mdStartAccumulation" in input_keys


def test_meteogram_inputs_has_duration(api_url: str, auth_headers: dict[str, str]) -> None:
    response = requests.get(
        f"{api_url}/db2/resources/meteogram/inputs?show=rmInputs", headers=auth_headers, timeout=30
    )
    assert response.status_code == 200
    body = response.json()
    assert body["error"] is False
    rm_inputs = body["data"][0]["resultModelInputs"]
    input_keys = {i["key"] for i in rm_inputs}
    assert "duration" in input_keys
