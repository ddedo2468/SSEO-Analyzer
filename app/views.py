from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint("views", __name__)

@views.route("/home")
@login_required
def home_page():
    return render_template('home.html')

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
