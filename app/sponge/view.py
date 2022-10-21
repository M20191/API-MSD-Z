# Import modules
from typing import Any
from . import sponge
import requests
import json
from flask import jsonify


def get_versions(version="") -> list[str]:
	"""Return names versions select and latest verions if that has select

	Args:
		version (str): Version sponge
		latest (str, optional): Gets latest build from sponge version . Defaults to 'False'.

	Returns:
		list[str]: all builds
	"""
	# Version gets all builds
	if version:url = f"https://dl-api-new.spongepowered.org/api/v2/groups/org.spongepowered/artifacts/spongevanilla/versions?tags=,minecraft:{version}"
	else:url = "https://dl-api-new.spongepowered.org/api/v2/groups/org.spongepowered/artifacts/spongevanilla/versions"

	# Requests
	resp = requests.get(url)
	# All versions in one list
	versions = [keys for keys in resp.json()["artifacts"].keys()]
	
	return versions

def get_link(version:str) -> str:
	"""Gets link for download (MSD-Z)

	Args:
		version (str): Version sponge

	Returns:
		str: link to download
	"""
	url = f"https://dl-api-new.spongepowered.org/api/v2/groups/org.spongepowered/artifacts/spongevanilla/versions/{version}"
	resp = requests.get(url)
	return resp.json()["assets"][-1]["downloadUrl"]


# Variable used in the index page to list versions
resp = requests.get("https://dl-api-new.spongepowered.org/api/v2/groups/org.spongepowered/artifacts/spongevanilla")
vsponge = resp.json()["tags"]["minecraft"]


@sponge.route("/")
def latest_version() -> dict[str, Any]:
	"""Return latest version of sponge

	Returns:
		dict[str, Any]: return link to download
	"""

	# Get version - name
	version = get_versions()[0]
	# Get link
	link = get_link(version)
	
	# Download
	return jsonify(
        {"link":link}
        )

@sponge.route('/<version_jar>')
def get_sponge_version(version_jar: str) -> dict[str, Any]:
	"""Return jar selected from sponge

	Args:
		version_jar (str): selected version from sponge

	Returns:
		dict[str, Any]: _description_
	"""
	# Get version - name
	version = get_versions(version_jar)[0]
	# Get link
	link = get_link(version)
	
	# Download
	return jsonify(
        {"link":link}
        )



