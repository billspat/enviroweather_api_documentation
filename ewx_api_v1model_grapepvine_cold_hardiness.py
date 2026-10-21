# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo>=0.23.16",
#     "requests>=2.32.3",
# ]
# ///

import marimo

__generated_with = "0.25.0"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    # this is a Marimo document, not a jupyter notebook.  Import marimo to use it
    import marimo as mo
    import site_helpers as site
    toc_md = site.toc_md_links()
    mo.sidebar(mo.md("""## Pages""" + toc_md))
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Enviroweather API documentation (v1)

    # Model: Grapevine Cold Hardiness

    This model is different from all the others in 2 ways:

    1. It has a complex parameter for sending multiple grape varieties in one request
    2. On the back-end, this model is actually run by the NEWA network on a cloud server that we don't control.  It is quite slow

    If you don't send the date-ish input (`gtStart`, `biofix1`/`biofix2`, `dateStartAccumulation`), RM-API estimates it for you from the station's weather data - which only works once the model is "in season". Outside the season, or with a bad combination of inputs, you'll get an application-level error (`error: true`) back with HTTP 200, so always check the `error` field.

    **Since it's a winter model, it only runs with dates after October 1 and until Late Spring.  If it is not currently in that time period, you may have to set the start/end dates to the previous season.**
    """)
    return


@app.cell
def _():
    import requests
    from datetime import date, timedelta
    from ewx_client import DEFAULT_STATION_CODE, ENVIRONMENTS, get_auth_header, get_environment_urls, get_site_token

    return (
        date,
        get_auth_header,
        get_environment_urls,
        get_site_token,
        requests,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Setup: set environment and get a token

    We manually set the environment (to production by default) and use helpder functions to get a token. See ewx_api_v1_step1_tokens.py for full wallk through.
    """)
    return


@app.cell
def _(get_auth_header, get_environment_urls, get_site_token):
    ewx_env = "production"
    api_url, rm_api_url = get_environment_urls(ewx_env)
    anonymous_token = get_site_token(api_url)
    token_header = get_auth_header(anonymous_token)
    return api_url, ewx_env, rm_api_url, token_header


@app.cell(hide_code=True)
def _(api_url, ewx_env, mo, rm_api_url):
    mo.md(rf"""
    working with **{ewx_env}** environment for this session with base URLs

    * **api**: {api_url}
    * **rm api**: {rm_api_url}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Set Station code and Date

    We set a station code in the northern part of the state to find colder temperatures.  See Step 2 Weather Stations for how to get othere stations.  Set the date to today but default.
    """)
    return


@app.cell
def _(date):
    ## Set Station 
    station_code = "cth"

    select_date = date.today().isoformat()

    # alternatively manually set a date near the end of last season.  This works as of 10/2026
    # select_date = "2026-03-31"
    print(select_date)
    return select_date, station_code


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Important: set long timeout

    This model takes a long time to run. As described about, the Enviroweather API is actually calling an external API from NEWA to run the model, and the speed of that is outside of our control. In our experience, it can easily go longer than the default "timeout" setting.  When calling this request from your own program, set a timeout.

    In Python, you set the timeout in the request 'get' method, for example: `requests.get(url, timeout = 120)`

    The code block below sets this to 2 minutes.  Adjust this if you need it to be longer.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Grapevine Cold Hardiness model:defaults

    When called with no varieties selected, RM-API has a default selection it will use.  Let's try that, but again it won't run if it's not between October 1 and May 1.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
 
    """)
    return


@app.cell
def _(
    graoevine_data,
    requests,
    rm_api_url,
    select_date,
    station_code,
    token_header,
):
    # assemble the model URL and send request

    extended_timeout_seconds = 120  # set timeout for 2 minutes
    model_code = "grapevinecoldhardiness"
    grapevine_url = (
        f"{rm_api_url}/db2/run?stationCode={station_code}&stationType=1&selectDate={select_date}&resultModelCode={model_code}"
    )
    print(grapevine_url)
    grapevine_response = requests.get(grapevine_url, headers=token_header, timeout=extended_timeout_seconds)
    print(grapevine_response)
    grapevine_data = grapevine_response.json()
    if grapevine_data["error"]:
        print("error in response:", graoevine_data["message"])
    grapevine_data
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Request with Varieties

    An example request URL with select varieties encoded

    ```
    https://api.enviroweather.msu.edu/rm-api/api/run?
    selectedStation=cth&cultivars[]=Cabernet_Franc&cultivars[]=Chardonnay&cultivars[]=Frontenac&cultivars[]=Marquette&cultivars[]=Riesling&
    selectDate=10%2F19%2F2026&resultModelId=256&resultModelCode=grapevinecoldhardiness&stationType=1&stationId=6&stationCode=cth
    ```
    """)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
