from flask import Flask, redirect, url_for, request, render_template
from flask_login import login_manager, login_url, login_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'AAHAHAH'
app.debug = True


if __name__ == '__main__':
    app.run()