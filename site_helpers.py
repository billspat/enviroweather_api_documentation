""" site_helpers.py: module with functions to help with creating aspects of the html static site inside the interactive website
"""
# imports
from yaml import load, Loader # yaml files are small, use python loaders
from os import path, getenv
import marimo as mo


# constants/config
TOC_FILE = "doclist.yaml"
MARIMO_FILE_TYPE = getenv("marimo_file_type", "PY") # Set this to HTML 



# helpers
def load_toc(toc_file:str = TOC_FILE)->dict: 
    """read in a YAML file to convert into a list of links.  The "links" do NOT have file extensionson them
    in an attempt to work both in the exported HTML and native marimo editors"""
    if not path.exists(toc_file):
        Warning(f"can't find toc file {toc_file}, return empty  toc, carry on...")
        toc ={}
    with open(toc_file, 'r') as file: 
        toc = load(file, Loader=Loader)

    return toc

def py_link(filename:str, urlbase ="")->str:
    return f"{urlbase}/?file={filename}.py"

def html_link(filename:str, urlbase="")->str:
    return f"{filename}.html"  


# this was designed to know if it was to create notebook py links or 
# html links based on thee script running it, but in the html 
# export process, it's not really dectectble, so this is not that useful 
def toc_md_links(script_type = MARIMO_FILE_TYPE)->str:
    """convert dictionary of links into simple markdown bulleted list"""

    script_type = script_type.upper()
    nav_links = load_toc()
    md_list = """\n"""
    for link_text, filename in nav_links.items():
        if script_type == "PY":
            file_url =  py_link(filename)
        elif script_type == "HTML":
            file_url = html_link(filename)
        else:
            file_url = html_link(filename)
        md_list = md_list + f"""  - [{link_text}]({file_url})\n"""
    md_list = md_list
    return md_list


def toc_md(nav_links:dict, filetype = "html")->str:
    """convert dictionary of links into simple markdown bulleted list"""
    md_list = """\n"""
    for key, value in nav_links.items():
        if filetype == "py":
            file_url = f"/?file={value}.{filetype}"
        elif filetype == "html":
            file_url = f"{value}.{filetype}"    
        else:
            file_url = f"{value}.{filetype}"
        md_list = md_list + f"""  - [{key}]({file_url})\n"""
    md_list = md_list
    return md_list


def toc_html(nav_links,filetype = "html"):
    # Generate the HTML links
    links_html = "<ul style='list-style-type: none; padding-left: 0;'>"
    for key, value in nav_links.items():
        links_html += f'<li style="margin-bottom: 8px;"><a href="{value}.{filetype}" style="text-decoration: none; color: #007bff;">{key}</a></li>'
    links_html += "</ul>"
    return(links_html)

def nav_sidebar(links_html):
    # Wrap everything in a collapsible section and place it in the sidebar
    return mo.sidebar(
        mo.md(f"""
        ## TOC
        <details open>
            <summary style="cursor: pointer; font-weight: bold; margin-bottom: 10px;">
                Navigation
            </summary>
            {links_html}
        </details>
        """)
    )

def add_nav():
    toc_links = load_toc()
    toc_html = (toc_links)
    return(nav_sidebar(toc_html))
