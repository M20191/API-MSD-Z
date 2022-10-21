from flask import Blueprint

velocity = Blueprint("velocity",__name__,url_prefix='/velocity')

from . import view