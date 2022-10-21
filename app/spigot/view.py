# Import modules
from flask import jsonify
from . import spigot

# List spigot versions
spigot_download = {
    "1.19.2":"https://download.getbukkit.org/spigot/spigot-1.19.2.jar",
    "1.18.2":"https://download.getbukkit.org/spigot/spigot-1.18.2.jar",
    "1.18.1": "https://download.getbukkit.org/spigot/spigot-1.18.1.jar",
    "1.17.1": "https://download.getbukkit.org/spigot/spigot-1.17.1.jar",
    "1.16.5": "https://cdn.getbukkit.org/spigot/spigot-1.16.5.jar",
    "1.15.2": "https://cdn.getbukkit.org/spigot/spigot-1.15.2.jar",
    "1.14.4": "https://cdn.getbukkit.org/spigot/spigot-1.14.4.jar",
    "1.12.2": "https://cdn.getbukkit.org/spigot/spigot-1.12.2.jar",
    "1.8.8": "https://cdn.getbukkit.org/spigot/spigot-1.8.8-R0.1-SNAPSHOT-latest.jar",
    }

# Variable used in the index page to list versions
vspigot = spigot_download

@spigot.route("/")
def latest():
    return jsonify({"link":spigot_download["1.19.2"]})


# spigot/version_jar
@spigot.route('/<version_jar>')
def download_spigot(version_jar):
    # Check if the requested version falls within the range of available versions.
    if version_jar not in spigot_download:
        tmp = [i for i in spigot_download.keys()]
        return f"Error version not found or it is not contemplated in our dictionary: \n{tmp}"
    # Return version else.
    return jsonify({'link': spigot_download[version_jar]})