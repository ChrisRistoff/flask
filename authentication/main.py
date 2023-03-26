from flask_bcrypt import Bcrypt
import os
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from hash_check import hashpw, checkpw
from forms import RegistrationForm, LoginForm

app = Flask(__name__, template_folder="templates")
app.config['SECRET_KEY'] = 'mysecret'

# sql
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(
        basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app, db)


class Users(db.Model):
    __tablename__ = "users"
    login = db.Column(db.String(20), primary_key=True)
    hashed = db.Column(db.String(32))

    def __init__(self, login, hashed):
        self.login = login
        self.hashed = hashed

    def __repr__(self):
        return f"User {self.login}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed, salt = hashpw(form.password.data)
        user = Users(login=form.username.data, hashed=hashed)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(login=form.username.data).first()
        if user:
            if checkpw(form.password.data, user.hashed, user.salt):
                return redirect(url_for('user_page'))
    return render_template('login.html', form=form)

@app.route('/user_page')
def user_page():
    return render_template('user_page.html')

if __name__ == '__main__':
    app.run(debug=True)










