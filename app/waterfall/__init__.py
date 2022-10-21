from flask import Blueprint

waterfall = Blueprint("waterfall",__name__,url_prefix="/waterfall")

from . import view