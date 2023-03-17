from flask import Flask
from test import latin

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World!"


@app.route("/gg")
def gg():
    return "gg"


@app.route("/test/<name>")
def test(name):
    return "hello {}".format(latin(name))


if __name__ == "__main__":
    app.run(debug=True)
