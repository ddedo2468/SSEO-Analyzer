from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_login import LoginManager

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'w5xP3K6r8u9xZ2A4d7g9j5n8q1t4w6z9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/seo-analyzer'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['STATIC_FOLDER'] = 'static'

db = SQLAlchemy(app)

from .auth import auth
from .views import views

app.register_blueprint(auth, url_prefix='/')
app.register_blueprint(views, url_prefix='/')

from app.models import User, URL


login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.init_app(app)


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
