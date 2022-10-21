# Import modules
from flask import jsonify
from . import waterfall
import requests
from typing import Any

# Functions
def get_versions() -> list[int, Any]:
    """Return json file with all waterfall versions

    Returns:
        (json dict[int, Any]): json waterfall versions
    """
    # Requests json with versions
    url = "https://papermc.io/api/v2/projects/waterfall/"
    resp = requests.get(url)

    return resp.json()["versions"]


def get_builds(version: str) -> list[int, Any]:
    """Return json file with all waterfall builds
    Args:
        version (str): version of waterfall download

    Returns:
        (json dict[int, Any]): json waterfall builds
    """
    # Requests 
    url = f"https://papermc.io/api/v2/projects/waterfall/versions/{version}"
    resp = requests.get(url)

    return resp.json()["builds"]


def get_name(version: str, build: int) -> str:
    """Get link to download (MSD-Z)

    Args:
        version (str): Version of waterfall download
        build (int): Build of waterfall downlaod

    Returns:
        (str): name of waterfall jar
    """
    # Requests
    url = f"https://papermc.io/api/v2/projects/waterfall/versions/{version}/builds/{build}"
    resp = requests.get(url)

    return resp.json()["downloads"]["application"]["name"]


# Variable used in the index page to list versions
vwaterfall = get_versions()


@waterfall.route('/')
def latest_version() -> dict[str, Any]:
    """Return the latest version and build of waterfall in JSON format.

    Returns:
        (json dict[str, Any]): json with link for download
    """
    # Get latest version
    version = get_versions()[-1]

    # Get latest build
    build = get_builds(version)[-1]

    # Get name download
    name = get_name(version,build)

    # Download
    return jsonify(
        {"link":f"https://papermc.io/api/v2/projects/waterfall/versions/{version}/builds/{build}/downloads/{name}"}
        )


@waterfall.route("/<version_jar>")
def download_waterfall(version_jar) -> dict[str, Any]:
    """Return the select version and latest build of waterfall in JSON format.

    Returns:
        (json dict[str, Any]): json with link for download
    """
    # Get a build
    build = get_builds(version_jar)[-1]

    # Get a name
    name = get_name(version_jar,build)

    # Download
    return jsonify(
        {"link":f"https://papermc.io/api/v2/projects/waterfall/versions/{version_jar}/builds/{build}/downloads/{name}"}
        )


@waterfall.route("/<version_jar>/<build>" )
def download_build_waterfall(version_jar,build) -> dict[str, Any]:
    """Return the selection version and selection build of waterfall in JSON format.

    Returns:
        (json dict[str, Any]): json with link for download
    """
    # Get a name
    name = get_name(version_jar,build)

    # Download
    return jsonify(
        {"link":f"https://papermc.io/api/v2/projects/waterfall/versions/{version_jar}/builds/{build}/downloads/{name}"}
        )
