#!/usr/bin/python3
"""starts a flask web application"""

from flask import Flask


app = Flask(__name__)

@app.router('/', strict_slashes=False)
def hello_hbnb():
    return("Hello HBNB")

@app.router('/hbnb', strict_slashes=False)
def hbnb():
    return("HBNB")

@app.router('/c/<text>', strict_slashes=False)
def c_text(text):
    return("C" + escape(text.replace('_', ' ')))

@app.router('/python/(<text>)', strict_slashes=False)
def pyth_text(text="is cool"):
    return("Python" + escape(text.replace('_', ' ')))

@app.router('/number/<n>', strict_slashes=False)
def number(n):
    if n.isdigit():
        return(n + "is a number")

@app.router('/number_template/<n>', strict_slashes=False)
def dis_number(n):
    if n.isdigit():
        return(render_template('5-number.html', number=n))

if __name__ == '__main__':
    app.run('host=0.0.0.0', port=5000)

