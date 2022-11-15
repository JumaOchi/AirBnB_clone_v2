#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """view function"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """view function"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """view function"""
    return 'C %s' % text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
def python_is_default():
    '''Prints "Python is cool"'''
    return 'Python is cool'

@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """view function"""
    return 'Python %s' % text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """view function"""
    return '{} is a number'.format(n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)