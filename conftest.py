"""Shared pytest fixtures for the Enviroweather API integration tests.

These tests hit the real, public production API - no mocking. Network access
is required. Living here at the package root (next to ewx_client.py) means
pytest adds this directory to sys.path automatically, so tests can simply
``from ewx_client import ...``.
"""

from datetime import date, timedelta

import pytest

from ewx_client import DEFAULT_STATION_CODE, get_auth_header, get_environment_urls, get_site_token


@pytest.fixture(scope="session")
def api_url() -> str:
    return get_environment_urls()[0]


@pytest.fixture(scope="session")
def rm_api_url() -> str:
    return get_environment_urls()[1]


@pytest.fixture(scope="session")
def site_token(api_url: str) -> str:
    return get_site_token(api_url)


@pytest.fixture(scope="session")
def auth_headers(site_token: str) -> dict[str, str]:
    return get_auth_header(site_token)


@pytest.fixture(scope="session")
def station_code() -> str:
    return DEFAULT_STATION_CODE


@pytest.fixture(scope="session")
def recent_date() -> str:
    """A date a couple of days in the past, so weather data is finalized."""
    return (date.today() - timedelta(days=2)).isoformat()
