#!/usr/bin/python3
"""
script that starts a Flask web application:
    Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
"""

from flask import Flask


app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
    """returns string"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns string"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cText(text):
    """return C followed by given string"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pText(text='is cool'):
    """returns provided text or default"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """returns string of n is int"""
    if isinstance(n, int):
        return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)
