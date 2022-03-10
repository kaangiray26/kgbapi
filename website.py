#!/usr/bin/python
# -*- encoding:utf-8 -*-

import secrets
from imops import Icon
from ratelimit import limits
from flask import Flask, send_file

app = Flask(__name__, template_folder='static')
ops = Icon()

_CALLS = 100
_PERIOD = 60

methods = {"Available Methods": [
    {
        "/splash": "Return a random splash text"
    },
    {
        "/square": "Generate random 5x5 bitmap"
    },
    {
        "/square/<hex>": "Generate random 5x5 bitmap with color <hex>"
    }
]}

with open("lines", "r") as f:
    lines = f.read().splitlines()


@app.route('/')
@limits(calls=_CALLS, period=_PERIOD)
def index():
    return methods


@app.route('/splash')
@limits(calls=_CALLS, period=_PERIOD)
def splash():
    return {"success": True, "line": lines[secrets.randbelow(len(lines))]}


@app.route("/square")
@limits(calls=_CALLS, period=_PERIOD)
def square():
    print("square")
    return send_file(ops.generate(), mimetype='image/png')


@app.route("/square/<hex>")
@limits(calls=_CALLS, period=_PERIOD)
def square_rgb(hex):
    print(hex)
    return send_file(ops.generate(hex), mimetype='image/png')


@app.errorhandler(404)
@limits(calls=_CALLS, period=_PERIOD)
def not_found(error):
    return {"status": "not found"}, 404
