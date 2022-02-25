from flask import Blueprint, render_template, url_for, redirect, request
from flask_login import login_required, current_user

noauth = Blueprint('noauth', __name__)

@noauth.route('/')
def home():
    return render_template('home.html')