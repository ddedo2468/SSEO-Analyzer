from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, current_user
from sqlalchemy.orm.attributes import set_attribute
from .utlis import analyze_url
from app import db
from app import app
from .models import URL, User
from datetime import datetime
from urllib.parse import unquote

views = Blueprint("views", __name__)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', user=current_user), 404

@views.route("/home")
@login_required
def home_page():
    return render_template('home.html', user=current_user)

@views.route("/history", methods=['GET'])
@login_required
def history():
    user_urls = URL.query.filter_by(user_id=current_user.id).all()
    return render_template('history.html', user=current_user, user_urls=user_urls)


@views.route("/results/<path:url>", methods=['GET', 'POST'])
@login_required
def show_result(url):
    decoded_url = unquote(url)
    url_data = URL.query.filter_by(url=decoded_url).first()
    return render_template('results.html', url_data=url_data, user=current_user)

@views.route("/analyzer", methods=['GET', 'POST'])
@login_required
def analyzer():
    
    if request.method == 'POST':
        url = request.form.get('url')

        url_exists = URL.query.filter_by(url=url, user_id=current_user.id).first()

        if url_exists:
            url_data = analyze_url(url)
            for key, value in url_data.items():
                set_attribute(url_exists, key, value)
            url_exists.update()
            db.session.commit()
            flash("url updated", "success")
        else:
            url_data = analyze_url(url)
            new_url = URL(**url_data)
            new_url.user_id = current_user.id
            new_url.update()
            db.session.add(new_url)
            db.session.commit()
            flash("url created", "success")


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
