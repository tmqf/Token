from flask import Flask, redirect, url_for, request, render_template
from flask_login import login_manager, login_required, login_url, login_user, logout_user, LoginManager
from flask_socketio import SocketIO
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
import psycopg2
db = SQLAlchemy()

def tokenApp():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config['SECRET_KEY'] = 'SECRET KEY'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'SQL URL'
    app.debug = True
    db.init_app(app)

    from .nonauth import noauth
    from .auth import auth
    from .tokendb import Users

    app.register_blueprint(noauth, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    logged = LoginManager()
    logged.login_view = 'auth.login'
    logged.init_app(app)

    @logged.user_loader
    def checkUser(id):
        return Users.query.get(int(id))

    return app