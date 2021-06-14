#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, abort, redirect, url_for
from model import db
import os


app = Flask(__name__)


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


@app.route('/cards')
def cards():
    cards = db
    return render_template(
        'cards.html',
        cards=cards)

@app.route('/card/<int:index>')
def card(index):
    try:
        card = db[index]
        max_index = len(db) - 1 
        return render_template(
            'card.html',
            card=card,
            index=index,
            max_index=max_index)
    except IndexError:
        abort(404)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)