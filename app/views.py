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

@views.route("/history", methods=['GET'])
@login_required
def histosy():
    user_urls = URL.query.filter_by(user_id=current_user.id).all()
    return render_template('history.html', user=current_user, user_urls=user_urls)


@views.route("/results/<string:url>", methods=['GET', 'POST'])
@login_required
def show_result(url):
    url_data = URL.query.filter_by(url=url).first()
    print(url_data)
    return render_template('results.html', url_data=url_data, user=current_user)

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
