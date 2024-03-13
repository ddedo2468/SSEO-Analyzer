from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_login import LoginManager

""" Initialize the app,db with configrations """

# Create a Flask application instance
app = Flask(__name__)

# Enable CORS for cross-origin requests
CORS(app)

# Configure application settings
app.config['SECRET_KEY'] = 'w5xP3K6r8u9xZ2A4d7g9j5n8q1t4w6z9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/seo-analyzer'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['STATIC_FOLDER'] = 'static'

# Initialize SQLAlchemy for database interactions
db = SQLAlchemy(app)

# Import blueprint modules for authentication and views
from .auth import auth
from .views import views

# Register blueprints to define route structures within the application
app.register_blueprint(auth, url_prefix='/')
app.register_blueprint(views, url_prefix='/')

# Import User and URL models for user authentication and URL data management
from app.models import User, URL

# Initialize LoginManager for user authentication
login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.init_app(app)

# Define a function to retrieve a user based on their ID
@login_manager.user_loader
def load_user(id):
    # Load the user model with the specified ID
    return User.query.get(int(id))
