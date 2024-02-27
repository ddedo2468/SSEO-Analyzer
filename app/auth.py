from flask import Blueprint, render_template, url_for, request, flash, redirect
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from .models import User

auth = Blueprint("auth", __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in!", category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
               flash('Password is incorrect.', category='error')
        else:
            flash('Email does not exist.', category='error')


    return render_template('login.html', title='login')


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        email_in_use = User.query.filter_by(email=email).first()
        username_in_use = User.query.filter_by(user_name=username).first()
        
        if email_in_use:
            flash('Email is already in use.', category='error')
        elif username_in_use:
            flash('Username is already in use.', category='error')
        elif password1 != password2:
            flash('Password don\'t match!', category='error')
        elif len(username) < 2:
            flash('Username is too short.', category='error')
        elif len(password1) < 6:
            flash('Password is too short.', category='error')
        elif len(email) < 4:
            flash("Email is invalid.", category='error')
        else:
            new_user = User(email=email, user_name=username, password=generate_password_hash(password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('user created')
            return redirect(url_for('views.home_page'))

    return render_template('signup.html', title='signup')

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('views.home_page'))
