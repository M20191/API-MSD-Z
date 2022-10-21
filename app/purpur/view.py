# Import modules
from typing import Any
from flask import jsonify
from . import purpur
import requests


# Variable used in the index page to list versions
resp = requests.get("https://api.purpurmc.org/v2/purpur")
vpurpur = resp.json()["versions"]

@purpur.route('/')
def latest_version() -> dict[str, Any]:
    """Return the latest version and build from purpur

    Returns:
        (json dict[str, Any]): json with link for download
    """
    return jsonify(
        {"link":f"https://api.purpurmc.org/v2/purpur/{vpurpur[-1]}/latest/download"}
        )

@purpur.route('/<version_jar>')
def download_purpur(version_jar) -> dict[str, Any]:
    """Return the latest build from purpur select version

    Returns:
        (json dict[str, Any]): json with link for download
    """
    return jsonify(
        {"link":f"https://api.purpurmc.org/v2/purpur/{version_jar}/latest/download"}
        )

@purpur.route('/<version_jar>/<build>')
def download_build_purpur(version_jar,build) -> dict[str, Any]:
    """Return the select build and version from purpur

    Returns:
        (json dict[str, Any]): json with link for download
    """
    return jsonify(
        {"link":f"https://api.purpurmc.org/v2/purpur/{version_jar}/{build}/download"}
        )


    