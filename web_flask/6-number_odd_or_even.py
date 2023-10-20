#!/usr/bin/python3
"""Script that starts a flask web application."""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """String to be returned"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Sub-string to display."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displays C and its text."""
    return "C %s" % text.replace("_", " ")


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Displays Python and its text"""
    return "Python %s" % text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Displays n is a number, only if n is an integer"""
    return "%s is a number" % n


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Display a HTML page only if n is an integer"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<n>", strict_slashes=False)
def number_odd_or_even(n):
    """Displays a HTML page only if n is an integer"""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
