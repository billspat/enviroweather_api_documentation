# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo>=0.23.16",
# ]
# ///

import marimo

__generated_with = "0.25.0"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Enviroweather API documentation (v1)

    ## Preview: in development / active only

    This collection is reserved for requests that are not yet released to the development-stable or production environments. It currently has no requests in it.

    Once new preview endpoints are added to the source Postman collection, convert them here following the same pattern as the other `ewx_api_v1_stepN_*.py` notebooks (see [`ewx_api_v1_step1_tokens.py`](./ewx_api_v1_step1_tokens.py) for the environment/token boilerplate, and reuse `ewx_client.py`).
    """)
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
