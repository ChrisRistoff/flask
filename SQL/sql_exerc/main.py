import os
from flask import Flask, render_template, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import AddForm, DeleteForm


app = Flask(__name__, template_folder="templates")
app.config["SECRET_KEY"] = "mysecret"


# sql
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "data.sqlite"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
Migrate(app, db)


# model
class Tech(db.Model):
    __tablename__ = "tech"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Item Name: {self.name}"


# views
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/view")
def view_tech():
    tech = Tech.query.all()

    return render_template("view_tech.html", tech=tech)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        new_item = Tech(name)
        db.session.add(new_item)
        db.session.commit()

        return redirect(url_for("view_tech"))

    return render_template("add_tech.html", form=form)


@app.route("/delete", methods=["GET", "POST"])
def delete():
    form = DeleteForm()

    if form.validate_on_submit():
        id = form.id.data
        item_to_delete = Tech.query.get(id)
        db.session.delete(item_to_delete)
        db.session.commit()

        return redirect(url_for("view_tech"))

    return render_template("remove_tech.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
