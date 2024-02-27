from flask import Blueprint, render_template, request
from flask_login import login_required, current_user

views = Blueprint("views", __name__)

@views.route("/home")
@login_required
def home_page():
    return render_template('home.html')

@views.route("/history")
@login_required
def histosy():
    return "Search History"

@views.route("/analyzer")
@login_required
def analyzer():
    
    if request.method == 'POST':
        url = request.form.get('url')

    return render_template('seo_analyzer.html')

@views.route("/counter")
@login_required
def counter():
    return "comming soon"

@views.route("/crawler")
@login_required
def crawler():
    return "comming soon"
