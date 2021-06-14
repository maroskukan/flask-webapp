#!/usr/bin/env python
# -*- coding: utf-8 -*-

from types import MethodType
from flask import Flask, render_template, abort, redirect, url_for, jsonify, request, flash
from model import db, save_db
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = "secretkey"

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

@app.route('/add_card', methods=["GET", "POST"])
def add_card():
    if request.method == "POST":
        card = {
            "question": request.form['question'],
            "answer": request.form['answer']
        }
        db.append(card)
        save_db()
        flash("Question {} has been successfully submitted".format(
            request.form.get("question")), "success")
        return redirect(url_for('cards'))
    else:
        return render_template('add_card.html')

@app.route('/api/cards')
def api_cards():
    return jsonify(db)

@app.route('/api/card/<int:index>')
def api_card(index):
    try:
        return jsonify(db[index])
    except IndexError:
        abort(404)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)