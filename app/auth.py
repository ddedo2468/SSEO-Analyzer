from flask import Blueprint, render_template, url_for

auth = Blueprint("auth", __name__)


@auth.route('/login')
def login():
    return render_template('login.html', title='login')


@auth.route('/signup')
def signup():
    return render_template('signup.html', title='signup')

@auth.route('/logout')
def logout():
    return "Log out"
