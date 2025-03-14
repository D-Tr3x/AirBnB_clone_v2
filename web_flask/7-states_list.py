#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from operator import attrgetter


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """
    Displays a HTML page with the list of all State objects sorted by name
    """
    states = storage.all(State)
    print("DEBUG: Retrieved {} states".format(len(states)))
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exception):
    """ Removes the current SQLAlchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
