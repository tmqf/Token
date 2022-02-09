from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        

        if password == '':
            flash('Password field is required', category='error')
        elif email and password == '':
            flash('Email and password field is required', category='error')

        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again', category='error')
        else:
            flash('Email doesn\'t exist', category='error')

    return render_template('login.html', user=current_user)

@auth.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        username = request.form.get('username')

        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email already exists', category='error')
        elif len(email) < 4:
            flash("Email must be greater than 4 characters", category='error')
        elif password1 != password2:
            flash("Passwords don\'t match", category='error')
        elif len(password1) < 7:
            flash("Password must be 7 or more characters", category='error')
        elif len(username) < 2:
            flash("Username must be more than 2 characters", category='error')
        elif len(username) > 32:
            flash("Username cannot be more than 32 characters", category='error')
        else:
            newUser = User(email=email, username=username, password=generate_password_hash(password1, method=('sha256')))
            db.session.add(newUser)
            db.session.commit()
            login_user(newUser, remember=True)
            flash("Account has been created!", category='success')
            return redirect(url_for('views.home'))
    
    return render_template('register.html', user=current_user)