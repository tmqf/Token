from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Person(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(250))
    username = db.Column(db.String(32))