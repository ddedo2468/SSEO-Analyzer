from sqlalchemy import JSON
from app import db
from datetime import datetime
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(length=20), nullable=False, unique=True)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    password = db.Column(db.String(length=255), nullable=False)
    urls = db.relationship('URL', backref='owner')


class URL(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now())
    url = db.Column(db.String(length=255), nullable=False)
    title = db.Column(db.Boolean, default=False, nullable=False)
    title_length = db.Column(db.Integer)
    description = db.Column(db.Boolean)
    h1 = db.Column(db.Boolean)
    h_tags_order = db.Column(db.Boolean)
    h1_count = db.Column(db.Integer) 
    img_alt = db.Column(db.Boolean)
    keywords = db.Column(JSON)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"URL(id={self.id})"
