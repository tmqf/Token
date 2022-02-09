from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
import string, random

db = SQLAlchemy()
DB_NAME = "database.db"

def createApp():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '1'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User

    createDB(app)

    loginManager = LoginManager()
    loginManager.login_view = 'auth.login'
    loginManager.init_app(app)

    @loginManager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def createDB(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('DB has been created')
