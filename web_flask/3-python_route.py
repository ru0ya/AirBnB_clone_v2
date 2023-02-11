#!/usr/bin/python3
"""
Flask web application
listening on 0.0.0.0, port=5000
"""


from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'."""
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'"""
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """Displays 'C' followed by the value of <text>
    Replacing any underscores in <text> with space
    """
    return ("C {}".format(text.replace("_", " ")))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pyth_text(text="is cool"):
    """Displays 'Python' followed by value of <text>
    Replacing any underscores in <text> with spaces
    """
    return ("Python {}".format(text.replace("_", " ")))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
