from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
    BooleanField,
    DateTimeField,
    RadioField,
    SelectField,
    TextField,
    TextAreaField,
)
from wtforms.validators import DataRequired


app = Flask(__name__, template_folder="")

app.config["SECRET_KEY"] = "mysecretkey"


class Form(FlaskForm):
    name = StringField("Enter your name")
    submit = SubmitField("Submit")


@app.route("/", methods=["GET", "POST"])
def index():
    name = False
    form = Form()

    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ""

    return render_template("forms.html", form=form, name=name)


class Form2(FlaskForm):
    username = StringField("Enter your username", validators=[DataRequired()])
    best = BooleanField("Are you the best")
    mood = RadioField(
        "What is your mood", choices=[("happy", "Happy"), ("sad", "Angry")]
    )
    food = SelectField(
        "Pick your favorite food",
        choices=[("chicken", "Chicken"), ("beef", "Beef"), ("fish", "Fish")],
    )
    feedback = TextAreaField()
    date = DateTimeField()
    submit = SubmitField("Submit")


@app.route("/forms2", methods=["GET", "POST"])
def form2():
    form = Form2()

    if form.validate_on_submit():
        session["username"] = form.username.data
        session["best"] = form.best.data
        session["mood"] = form.mood.data
        session["food"] = form.food.data
        session["feedback"] = form.feedback.data
        session["date"] = form.date.data

        return redirect(url_for("thanks"))

    return render_template("forms2.html", form=form)


@app.route("/thanks")
def thanks():
    return render_template("thanks.html")


if __name__ == "__main__":
    app.run(debug=True)
