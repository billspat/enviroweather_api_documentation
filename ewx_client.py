"""Shared helpers for the Enviroweather API example notebooks and tests.

Every "Step N" notebook in this package needs the same setup: pick an
environment (production/staging/development), fetch a fresh anonymous site
token, and build the Authorization header. Centralizing that here keeps each
notebook focused on the endpoints it's documenting.
"""

import requests

ENVIRONMENTS = {
    "production": {
        "api_url": "https://api.enviroweather.msu.edu/ewx-api/api",
        "rm_api_url": "https://api.enviroweather.msu.edu/rm-api/api",
    },
    "staging": {
        "api_url": "https://mcrp-dev.geo.msu.edu/ewx/ewx-api/api",
        "rm_api_url": "https://mcrp-dev.geo.msu.edu/ewx/rm-api/api",
    },
    "development": {
        "api_url": "https://mcrp-dev.geo.msu.edu/tma/ewx/ewx-api/api",
        "rm_api_url": "https://mcrp-dev.geo.msu.edu/tma/ewx/rm-api/api",
    },
}

DEFAULT_ENVIRONMENT = "production"

# "msu" (East Lansing) is the station used throughout Enviroweather's own
# request examples, so the example notebooks/tests use it as a safe default.
DEFAULT_STATION_CODE = "msu"


def get_environment_urls(environment: str = DEFAULT_ENVIRONMENT) -> tuple[str, str]:
    """Return (api_url, rm_api_url) for the named environment."""
    env = ENVIRONMENTS[environment]
    return env["api_url"], env["rm_api_url"]


def get_site_token(api_url: str) -> str:
    """Request a fresh anonymous site token from the API.

    Tokens expire after about a day, so request a new one per session rather
    than hard-coding one (see temporary_site_token.txt in the repo root for a
    scratch copy you can use without even making this request).
    """
    response = requests.get(f"{api_url}/db2/siteToken", timeout=30)
    response.raise_for_status()
    body = response.json()
    if body["error"]:
        raise RuntimeError(f"siteToken request failed: {body['message']}")
    return body["data"]["token"]


def get_auth_header(token: str) -> dict[str, str]:
    """Build the Authorization header required by all api/rm-api requests."""
    return {"Authorization": f"Bearer {token}"}
