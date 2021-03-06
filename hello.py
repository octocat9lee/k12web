#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'zhoulee'

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello Flask!</h1>'


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1> ' % name


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
