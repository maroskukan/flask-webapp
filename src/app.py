#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
import os


app = Flask(__name__)
views = 0

content = {
    "header": "Learning Flask",
    "message": "This the content message"
    }

@app.route('/')
def home():
    return render_template('home.html', content=content)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)