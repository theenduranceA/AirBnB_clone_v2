#!/usr/bin/python3
"""Script that starts a flask web application."""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """Removes current SQLAlchemy Session"""
    storage.close()


@app.route("/states", strict_slashes=False)
def states():
    """Displays HTML page"""
    my_list = storage.all("State")
    return render_template("9-states.html", state=my_list)


@app.route("/states/<id>", strict_slashes=False)
def get_state(id):
    """Displays HTML page"""
    my_list = storage.all("State")
    for state in my_list.values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
