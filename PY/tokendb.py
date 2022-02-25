from flask_login import UserMixin
from . import db

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(250))
    username = db.Column(db.String(32))