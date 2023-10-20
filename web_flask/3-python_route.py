#!/usr/bin/python3
"""Script that starts a flask web application."""

from flask import Flask
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
