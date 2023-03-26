import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__, template_folder="templates")
app.config['SECRET_KEY'] = 'mysecret'

# sql
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
+ os.path.join(basedir, 'data.sqlite')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app.db)


class Users(db):
    login = db.Column(db.String(20), primary_key=True)
    password = db.Column(db.String(20))
    salt = db.Column(db.String(32))

