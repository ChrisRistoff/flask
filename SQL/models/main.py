import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))
# __file__ -> main.py -> krsnhrstv/flask/SQL/main.py

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "data.sqlite"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
Migrate(app, db)

############################################


class Users(db.Model):
    __tablename__ = "users"
    # create columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    # One to many relationship
    # one user can have many techs
    tech = db.relationship("Tech", backref="user", lazy="dynamic")
    # one to one
    # one user can have one fav Brand
    brand = db.relationship("Brand", backref="user", uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.tech:
            return f"Name: {self.name} Tech: {self.tech} 
                    Fav brand: {self.brand}"
        else:
            return f"Name: {self.name} Tech: None Fav brand: {self.brand} "

    def report_tech(self):
        print("Here is my tech Tech")
        for tech in self.tech:
            print(tech.item_name)


class Tech(db.Model):
    __tablename__ = "tech"
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.Text)
    users_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def __init__(self, item_name, users_id):
        self.item_name = item_name
        self.users_id = users_id


class Brand(db.Model):
    __tablename__ = "brand"
    id = db.Column(db.Integer, primary_key=True)
    brand_name = db.Column(db.Text)

    users_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def __init__(self, brand_name, users_id):
        self.brand_name = brand_name
        self.users_id = users_id


if __name__ == "__main__":
    app.run(debug=True)
