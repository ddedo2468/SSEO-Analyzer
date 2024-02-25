from flask import Blueprint


views = Blueprint("views", __name__)

@views.route("/home")
def home_page():
    return "Home Page"

@views.route("/history")
def histosy():
    return "Search History"

@views.route("/analyzer")
def analyzer():
    return "analyzer Page"

@views.route("/counter")
def counter():
    return "comming soon"

@views.route("/crawler")
def crawler():
    return "comming soon"
