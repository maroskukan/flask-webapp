#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, abort, redirect, url_for
from model import db
import os


app = Flask(__name__)
views = 0

content = {
    "header": "Learning Flask",
    "message": "This the content message"
    }

@app.errorhandler(404)

def not_found(e):
    return render_template(
        '404.html'
    )

@app.route('/')
def home():
    return render_template(
        'home.html'
    )


@app.route('/card')
def card():
    card = db[0]
    return render_template(
        'card.html',
        content=card)

@app.route('/card/<int:index>')
def card_view(index):
    try:
        card = db[index]
        return render_template(
            'card.html',
            content=card)
    except IndexError:
        abort(404)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)