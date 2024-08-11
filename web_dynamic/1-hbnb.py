#!/usr/bin/python3
"""
Starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from uuid import uuid4

app = Flask(name)

@app.route('/1-hbnb/', strict_slashes=False)
def hbnb():
    """
    Renders the main HBnB filters page
    """
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    places = storage.all("Place").values()
    cache_id = uuid4()
    return render_template('1-hbnb.html', 
                           states=states, 
                           amenities=amenities, 
                           places=places, 
                           cache_id=cache_id)

@app.teardown_appcontext
def teardown_db(*args, **kwargs):
    """
    Closes the database session after each request
    """
    storage.close()

if name == "main":
    app.run(host='0.0.0.0', port=5000)
