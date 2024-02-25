from flask import Blueprint

auth = Blueprint("auth", __name__)


@auth.route('/login')
def login():
    return "Login"


@auth.route('/signup')
def signup():
    return "sign up"


@auth.route('/logout')
def logout():
    return "Log out"
