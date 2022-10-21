# Import modules
from flask import jsonify
from . import velocity
import requests
from typing import Any

# Functions
def get_versions() -> list[int, Any]:
    """Return json file with all velocity versions

    Returns:
        (json dict[int, Any]): json velocity versions
    """
    # Requests json with versions
    url = "https://papermc.io/api/v2/projects/velocity/"
    resp = requests.get(url)

    return resp.json()["versions"]


def get_builds(version: str) -> list[int, Any]:
    """Return json file with all velocity builds
    Args:
        version (str): version of velocity download

    Returns:
        (json dict[int, Any]): json velocity builds
    """
    # Requests 
    url = f"https://papermc.io/api/v2/projects/velocity/versions/{version}"
    resp = requests.get(url)

    return resp.json()["builds"]


def get_name(version: str, build: int) -> str:
    """Get link to download (MSD-Z)

    Args:
        version (str): Version of velocity download
        build (int): Build of velocity downlaod

    Returns:
        (str): name of velocity jar
    """
    # Requests
    url = f"https://papermc.io/api/v2/projects/velocity/versions/{version}/builds/{build}"
    resp = requests.get(url)

    return resp.json()["downloads"]["application"]["name"]


# Variable used in the index page to list versions
vvelocity = get_versions()

@velocity.route("/")
def download_velocity() -> dict[str, Any]:
    """Return latest build and version from velocity

    Returns:
        (json  dict[str: Any]): json with link for download
    """
    # Get latest version
    version = get_versions()[-1]

    # Get latest build
    build = get_builds(version)[-1]

    # Get name download
    name = get_name(version,build)

    # Download
    return jsonify(
        {"link":f"https://papermc.io/api/v2/projects/velocity/versions/{version}/builds/{build}/downloads/{name}"}
        )
