from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/seo-analyzer'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from .auth import auth
from .views import views

app.register_blueprint(auth, url_prefix='/')
app.register_blueprint(views, url_prefix='/')

from app.models import User, URL
