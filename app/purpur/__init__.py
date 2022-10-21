from flask import Blueprint

purpur = Blueprint("purpur",__name__,url_prefix='/purpur')


from app.purpur import view