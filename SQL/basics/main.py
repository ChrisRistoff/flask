import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))
# __file__ -> main.py -> krsnhrstv/flask/SQL/main.py

app = Flask(__name__)
app.config["SECRET_KEY"] = "supersecretkey"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "data.sqlite"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

database = SQLAlchemy(app)
migrate = Migrate(app, database)

############################################


class UserDetails(database.Model):
    __tablename__ = "main"
    # create columns
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.Text)
    email = database.Column(database.Text)
    age = database.Column(database.Integer)

    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def __repr__(self):
        return f"Name: {self.name} Email: {self.email}"
