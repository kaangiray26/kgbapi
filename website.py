#!/usr/bin/python
# -*- encoding:utf-8 -*-

from flask import Flask, send_file
from ratelimit import limits
from imops import Icon

app = Flask(__name__)
ops = Icon()

_CALLS = 100
_PERIOD = 60

@app.route("/square")
@limits(calls=_CALLS, period=_PERIOD)
def square_img():
    return send_file(ops.generate(), mimetype='image/png')

@app.errorhandler(404)
@limits(calls=_CALLS, period=_PERIOD)
def not_found(error):
    return {"status": "not found"}, 404