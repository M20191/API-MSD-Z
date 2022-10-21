from flask import Blueprint

paper = Blueprint("paper",__name__,url_prefix='/paper')

from . import view