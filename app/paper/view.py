# Import modules
from flask import jsonify
from . import paper
from typing import Any
import requests

# Functions
def get_versions() -> list[int, Any]:
    """Return json file with all paper versions

    Returns:
        (json dict[int, Any]): json paper versions
    """
    # Requests json with versions
    url = "https://papermc.io/api/v2/projects/paper/"
    resp = requests.get(url)

    return resp.json()["versions"]


def get_builds(version: str) -> list[int, Any]:
    """Return json file with all paper builds
    Args:
        version (str): version of paper download

    Returns:
        (json dict[int, Any]): json paper builds
    """
    # Requests 
    url = f"https://papermc.io/api/v2/projects/paper/versions/{version}"
    resp = requests.get(url)

    return resp.json()["builds"]


def get_name(version: str, build: int) -> str:
    """Get link to download (MSD-Z)

    Args:
        version (str): Version of paper download
        build (int): Build of paper downlaod

    Returns:
        (str): name of paper jar
    """
    # Requests
    url = f"https://papermc.io/api/v2/projects/paper/versions/{version}/builds/{build}"
    resp = requests.get(url)

    return resp.json()["downloads"]["application"]["name"]


# Variable used in the index page to list versions
vpaper = get_versions()


@paper.route("/")
def latest_version() -> dict[str, Any]:
    """Return the latest version and build of paper in JSON format.

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
        {"link":f"https://papermc.io/api/v2/projects/paper/versions/{version}/builds/{build}/downloads/{name}"}
        )


@paper.route('/<version_jar>')
def download_paper(version_jar) -> dict[str, Any]:
    """Return the select version and latest build of paper in JSON format.

    Returns:
        (json dict[str, Any]): json with link for download
    """
    # Get Build
    build = get_builds(version_jar)[-1]
        
    # Get Version
    version = get_name(version_jar,build)
        
    # Download
    return jsonify(
        {"link":f"https://papermc.io/api/v2/projects/paper/versions/{version_jar}/builds/{build}/downloads/{version}"}
        )


@paper.route('/<version_jar>/<build>')
def download_build_paper(version_jar,build) -> dict[str, Any]:
    """Return the selection version and selection build of paper in JSON format.

    Returns:
        (json dict[str, Any]): json with link for download
    """
    # Get name
    name = get_name(version_jar,build)
    return jsonify(
        {"link":f"https://papermc.io/api/v2/projects/paper/versions/{version_jar}/builds/{build}/downloads/{name}"}
        )

