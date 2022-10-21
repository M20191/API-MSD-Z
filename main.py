# Import modules and blueprints
from typing import Any
from flask import Flask, render_template, jsonify
from app import velocity, waterfall
from app.paper import paper
from app.purpur import purpur
from app.spigot import spigot
from app.velocity import velocity
from app.waterfall import waterfall
from app.sponge import sponge

# Imports Versions-jars to list 
from app.spigot.view import vspigot
from app.purpur.view import vpurpur
from app.paper.view import vpaper
from app.velocity.view import vvelocity
from app.waterfall.view import vwaterfall
from app.sponge.view import vsponge

# Import random for random image in the index page background
import random

app = Flask(__name__)

# Register blueprints
app.register_blueprint(paper)
app.register_blueprint(purpur)
app.register_blueprint(spigot)
app.register_blueprint(velocity)
app.register_blueprint(sponge)

app.register_blueprint(waterfall)

@app.route('/')
def index():
    # Images for the index background
    images_back = ["https://images7.alphacoders.com/333/333369.jpg","https://images7.alphacoders.com/556/556718.jpg","https://images2.alphacoders.com/126/1263621.png"]
    image = random.choice(images_back)
    
    # List versions of jars/forks
    context = {
        "purpur":vpurpur,
        "paper":vpaper,
        "spigot":vspigot,
        "velocity":vvelocity,
        "waterfall":vwaterfall,
        "versions_header":["purpur","paper","spigot","sponge","velocity","waterfall"],
        "versions_header_vars":[vpurpur,vpaper,vspigot,vsponge,vvelocity,vwaterfall]
    }

    return render_template('index.html',image=image,zip=zip,context=context,**context)


@app.route('/versions')
def versions() -> dict[str, Any]:
    # versions spigot
    tmp = []
    for key in vspigot.keys():
        tmp.append(key)
    return jsonify(
        {"spigot":tmp,"paper":vpaper,"purpur":vpurpur,"waterfall":vwaterfall,"velocity":vvelocity,"sponge":vsponge}
        )
# Core
if __name__ == "__main__":
    # Main
    app.run(host="0.0.0.0")