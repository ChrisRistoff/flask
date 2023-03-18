from flask import Flask, render_template, request
from test import latin

app = Flask(__name__, template_folder="")


@app.route("/")
def index():
    user_logged_in = True
    some_variable = "Kra kra"
    letters = list(some_variable)
    dicto = {"a": 1, "b": 2, "c": 3}
    mylist = [1, 2, 3, 4, 5]
    return render_template(
        "basic.html",
        variable=some_variable,
        letters=letters,
        dicto=dicto,
        listo=mylist,
        user_logged_in=user_logged_in,
    )


@app.route("/gg")
def gg():
    return render_template("basic2.html")


@app.route("/form")
def form():
    return render_template("forms.html")


@app.route("/thank_you")
def thank_you():
    first = request.args.get("first")
    last = request.args.get("last")
    email = request.args.get("email")

    lower = False
    upper = False
    number = False
    length = False
    report = False

    password = request.args.get("password")

    for char in password:
        if char.islower():
            lower = True
        if char.isupper():
            upper = True
        if char.isdigit():
            number = True

    if len(password) >= 8:
        length = True

    if lower and upper and number and length:
        report = True

    return render_template(
        "thank_you.html",
        first=first,
        last=last,
        email=email,
        report=report,
        lower=lower,
        upper=upper,
        number=number,
        length=length,
    )


@app.route("/test/<name>")
def test(name):
    return "hello {}".format(latin(name))


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
