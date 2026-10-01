# MSU Enviroweather: API Documentation

## Important note

### *This documentation is a first cut based on notes from 2024 and not completely up to date, but will be updated to the most recent version*

## Background

MSU Enviroweather is many things: a network of weather stations across the state of Michigan, a database that collects these data, weather, crop and pest models that combine our network data with other weather data, **web APIs** for computers to access all of that, and website and mobile application on top of those web APIs for humans. 

This documentation website is for those who want to access our web APIs to build new applications or integrate the results of our models with an application.  

If you just want to use the models, go to [https://enviroweather.msu.edu](https://enviroweather.msu.edu) or use the mobile app created by Michigan Ag Bio Research on the app storesn the [Apple App Store](https://enviroweather.msu.edu/#:~:text=on%20the%20Apple%20App%20Store%20or%20Google%20Play) or [Google Play](https://play.google.com/store/apps/details?id=edu.msu.abr.enviroweather&pcampaignid=web_share)

## About these files

We document our API using "Python Notebooks" which are a way to combine word and code, in a tutorial form.  This repository contains python code in notebook from.  From those notebooks we generate HTML and publish a website so you don't need python to read them (but can still see the Python) 

If you want to use the Python notebooks interactively, this is the place to be, otherwise go (*website TBD*)


There are two forms of these notebooks: 

1. [Marimo](https://marimo.io): an open-source reactive Python notebook system, built from the ground up to solve well-known problems associated with traditional notebooks.  Marimo notebooks are not widely used (yet) but we find the HTML outputs to be superior for making documentation websites.  The Marimo-formatted files are in the main folder and have a "*.py" extension as they are python scripts.  

2. [Jupyter Notebooks](https://jupyter.org/) are a more commonly used form of notebook.   You can install Jupyter and [run a notebook](https://docs.jupyter.org/en/latest/running.html#running) or open them directly in [VS Code's notebook interface](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)

## Getting Started with Notebook Documentation

### Easy

Go to our documentation website


## Developing/Contributing to this documentation

*very rough draft with details to be added*

0. Pre-requisites

**Requires Python**

You must have a recent python to work with this. Tested with Python 3.13 and 3.14, but older version may also work.  As part of python you may need `pip` or `uv` (see below)

**Command line helps**
We use VS code and a terminal interface for much our work and these instructions are geared for that over other systems. 

1. Clone me

clone this repo onto your computer

2. Install requirements

This folder is python package format but not exactly a package.  This way things can be installed easily, and scripts can be accessed from the command line.  You can install requirements pip or [uv](https://docs.astral.sh/uv/).  If you haven't used uv, it's worth a try. 

We really really suggest you use a python environment.  Use Pyenv, Conda, or use `uv` which handles the environment for you

option a.  install with PIP: `pip install .`
option b.  [install uv](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer); then run `uv sync`  (`pipx install uv` also good but requires [pipx](https://pipx.pypa.io/latest/how-to/install-pipx.html))

**This should install marimo**  If it doesn't see https://docs.marimo.io/getting_started/installation/   

Note we currently don't use any marimo extensions, so don't need to install ` "marimo[recommended]"`, only `marimo`

3. edit with marimo

in the terminal window of this folder, start marimo which is browser-based editing: 
 
`marimo edit`

You could edit with Jupyter in vs code but the goal now is to maintain marimo files

4. add tests 

there are python tests here.  They don't test the notebooks directly, but are included repeates of much of the code used in the notebooks to ensure our python is using the APIs correctly.  This is some work to maintain:  edit notebook with new model URLs, examples etc, then add similar tests to ensure the URLs are working as expected. 

Note we already have a test suite for the PHP api servers, these tests are mostly to ensure our notebooks will run.  Again, with the uv

`uv run pytest tests/`

5. Make a copy in Jupyter

While we get used to Marimo, and until we get feedback on the best format, we are maintaing jupyter versions since jupyter is so widely used and works directly in VS code. 
All the Jupyter notebook files are in the 'juypter' folder to make it easy to find. 

To make a Jupyter version of any marimo notebook file `notebookfile` in the `/jupyter` folder, run the following command: 

`uv run marimo export ipynb <file>.py --sort top-down -o jupyter/<file>.ipynb -f`

*TODO/TBD: write a script to convert all marimo files at once*

6. Build the website



