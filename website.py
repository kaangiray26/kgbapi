#!/usr/bin/python
# -*- encoding:utf-8 -*-

from flask import Flask, send_file
from ratelimit import limits
from imops import Icon

app = Flask(__name__)
ops = Icon()

_CALLS = 100
_PERIOD = 60

methods = {"Available Methods": {
    "/square": "Generate random 5x5 bitmap"
}}


@app.route('/')
@limits(calls=_CALLS, period=_PERIOD)
def index():
    return methods

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
