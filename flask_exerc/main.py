from flask import Flask, render_template, session, request, redirect, url_for, flash
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
    IntegerField,
)
from wtforms.validators import DataRequired

app = Flask(__name__, template_folder="")

app.config["SECRET_KEY"] = "supersecretkey"


@app.route("/")
def index():
    return render_template("index.html")


class Calculator(FlaskForm):
    num1 = IntegerField("Enter your first number")
    num2 = IntegerField("Enter your second number")
    submit = SubmitField("Submit")


@app.route("/calculator", methods=["GET", "POST"])
def calculator():
    num1 = False
    num2 = False
    form = Calculator()

    if form.validate_on_submit():
        session["num1"] = form.num1.data
        session["num2"] = form.num2.data
        num1 = int(session["num1"])
        num2 = int(session["num2"])
        num3 = num1 + num2
        flash(f"Your answer is {num3}!")

    return render_template("calculator.html", form=form, num1=num1, num2=num2)


class Feedback(FlaskForm):
    name = StringField("Enter your name", validators=[DataRequired()])
    feedback = TextAreaField(validators=[DataRequired()])
    score = RadioField(
        "What would you rate your experience with the app?",
        choices=[("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")],
        validators=[DataRequired()],
    )
    agree = BooleanField(
        "I agree to not send messages that will waste people's time.",
        validators=[DataRequired()],
    )
    submit = SubmitField("Submit")


@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    name = False
    feedback = False
    score = False
    agree = False
    form = Feedback()

    if form.validate_on_submit():
        session["name"] = form.name.data
        session["feedback"] = form.feedback.data
        session["score"] = form.score.data
        session["agree"] = form.agree.data
        name = session["name"]
        feedback = session["feedback"]
        score = session["score"]
        agree = session["agree"]
        flash(f"Thank you for your feedback, {name}!")
        return redirect(url_for("feedback"))

    return render_template(
        "feedback.html",
        form=form,
        name=name,
        feedback=feedback,
        score=score,
        agree=agree,
    )


class Hello(FlaskForm):
    name = StringField("Enter your name")
    submit = SubmitField("Submit")


@app.route("/hello", methods=["GET", "POST"])
def hello():
    name = False
    form = Hello()

    if form.validate_on_submit():
        session["name"] = form.name.data
        name = session["name"]

    return render_template("hello.html", form=form, name=name)


if __name__ == "__main__":
    app.run(debug=True)
