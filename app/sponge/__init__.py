from flask import Blueprint

sponge = Blueprint("sponge",__name__,url_prefix='/sponge')

from app.sponge import view