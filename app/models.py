from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(length=20), nullable=False, unique=True)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    password = db.Column(db.String(length=60), nullable=False)
    urls = db.relationship('URL', backref='owner')


class URL(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Boolean, default=False, nullable=False)
    title_length = db.Column(db.Integer)
    description = db.Column(db.Boolean)
    h1 = db.Column(db.Boolean)
    h_tags_order = db.Column(db.Boolean)
    h1_count = db.Column(db.Integer) 
    img_alt = db.Column(db.Boolean)
    keywords = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
