"""Tests for Step 1: Tokens (siteToken endpoint)."""

import requests


def test_site_token_is_nonempty_string(site_token: str) -> None:
    assert isinstance(site_token, str)
    assert len(site_token) > 0


def test_site_token_request_shape(api_url: str) -> None:
    response = requests.get(f"{api_url}/db2/siteToken", timeout=30)
    assert response.status_code == 200
    body = response.json()
    assert body["error"] is False
    assert isinstance(body["data"]["token"], str)


def test_auth_header_format(auth_headers: dict[str, str]) -> None:
    assert auth_headers["Authorization"].startswith("Bearer ")
