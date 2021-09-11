#!/usr/bin/python3
"""
flask model
"""
from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_world():
  """ hello hbnb """
    return 'Hello HBNB!'
