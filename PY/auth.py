from flask import Flask, request, redirect, url_for, render_template, Blueprint, flash
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .tokendb import Users
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/dashboard')
@login_required
def channels():
    if login_user == None:
        flash("Please login to acces this page", category='error')
    return render_template('channels.html', user=current_user)

###############################################################

"""@auth.route('/logout')
def logout():
    logout_user()"""

###############################################################

@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        userEmail = request.form.get('email')
        userPW = request.form.get('password')

        checkUser = Users.query.filter_by(email=userEmail).first()

        if checkUser:
            if check_password_hash(checkUser.password, userPW):
                login_user(checkUser, remember=True)
                flash("Logged in successfully", category='success')
                return redirect(url_for('auth.channels'))
            else:
                flash("Incorrect password, please try again", category='error')
        else:
            flash("Password doesn't exist! please make an account", category='error')

    return render_template('login.html', user=current_user)

###############################################################

@auth.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        userEmail = request.form.get('email')
        userPW1 = request.form.get('password1')
        userPW2 = request.form.get('password2')
        userName = request.form.get('username')

        checkUser = Users.query.filter_by(email=userEmail).first()

        if checkUser:
            flash('Email already exists!', category='error')
        elif userPW1 != userPW2:
            flash('Passwords don\'t match!', category='error')
        elif len(userPW1) < 7:
            flash("Password must be greater than 7 characters", category='error')
        elif len(userName) > 32:
            flash("Username cannot be more than 32 characters", category='error')
        elif len(userName) < 2:
            flash("Username cannot be less than 2 characters", category='error')
        else:
            registerUser = Users(email=userEmail, username=userName, password=generate_password_hash(userPW1, method=('sha256'), salt_length=160))
            db.session.add(registerUser)
            db.session.commit()
            login_user(registerUser, remember=True)
            flash("Account has been created!", category='success')
            return redirect(url_for('auth.channels'))

    return render_template('register.html', user=current_user)