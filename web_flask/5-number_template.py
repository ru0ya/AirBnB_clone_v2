#!/usr/bin/python3
"""starts a flask web application"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!."""
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'"""
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """Displays 'C' followed by value of <text>

    Replacing any underscores in <text> with spaces"""
    return ("C".format(text.replace("_", " ")))


@app.route("/python/<text>", strict_slashes=False)
def pyth_text(text="is cool"):
    """Displays 'Python' followed by value of <text>

    Replacing any underscores in <text> with spaces"""
    return ("Python".format(text.replace("_", " ")))


@app.route("/number/<n>", strict_slashes=False)
def number(n):
    """checks if 'n' is a digit and
    displays {n} is a number"""
    if n.isdigit():
        return (n + "is a number")


@app.route("/number_template/<n>", strict_slashes=False)
def dis_number(n):
    """Checks if 'n' is a digit and
    renders the output to a html page if true
    with output 'n' is a number"""
    if n.isdigit():
        return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
