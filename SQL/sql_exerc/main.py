import os
from flask import Flask, render_template, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import AddForm, DeleteForm, AddProjectForm


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
    project = db.relationship("Project", backref="tech", lazy="dynamic")


    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.project.count() > 0:
            project_names = ", ".join([pr.name for pr in self.project if pr.name])
            return f"Item Name: {self.name}\n Project Names: {project_names}"
        else:
            return f"Item Name: {self.name}"


class Project(db.Model):
    __tablename__ = "project"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    tech_id = db.Column(db.Integer, db.ForeignKey("tech.id"))

    def __init__(self, name, tech_id):
        self.project_name = name
        self.tech_id = tech_id

    def __repr__(self):
        return f"{self.project_name}"


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


@app.route("/add_project", methods=["GET", "POST"])
def add_project():
    form = AddProjectForm()

    if form.validate_on_submit():
        project_name = form.project_name.data
        tech_id = form.tech_id.data
        new_project = Project(project_name, tech_id)
        db.session.add(new_project)
        db.session.commit()

        return redirect(url_for("view_tech"))

    return render_template("add_project.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
