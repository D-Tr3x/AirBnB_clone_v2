#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """ Displays a HTML page with a list of all States, sorted by name """
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """
    Displays a HTML page with info about <id>, if it exists
    """
    found_state = None
    for s in storage.all("State").values():
        if s.id == id:
            found_state = s
            break
    return render_template("9-states.html", state=found_state)


@app.teardown_appcontext
def teardown(exception):
    """ Removes the current SQLAlchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
