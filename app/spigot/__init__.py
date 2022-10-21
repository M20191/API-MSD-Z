from flask import Blueprint

spigot = Blueprint("spigot",__name__,url_prefix='/spigot')

from app.spigot import view