from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import login_required, current_user
from .utlis import analyze_url
from app import db
from .models import URL, User
import json

views = Blueprint("views", __name__)

@views.route("/home")
@login_required
def home_page():
    return render_template('home.html', user=current_user)

@views.route("/history")
@login_required
def histosy():
    return "Search History"



@views.route("/analyzer", methods=['GET', 'POST'])
@login_required
def analyzer():
    
    if request.method == 'POST':
        url = request.form.get('url')
        url_data = analyze_url(url)
        new_url = URL(**url_data)
        new_url.user_id = current_user.id
        db.session.add(new_url)
        db.session.commit()

        return render_template('results.html', url_data=url_data, user=current_user)


    return render_template('seo_analyzer.html', user=current_user)

@views.route("/counter")
@login_required
def counter():
    return "comming soon"

@views.route("/crawler")
@login_required
def crawler():
    return "comming soon"
