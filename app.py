#!/usr/bin/env python
from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    #return '<h1>Hello!</h1>'
    return render_template('index.html')


if __name__ == '__main__':
  port = int(os.environ.get('PORT', 8000))   # Use PORT if it's there.
  #app.debug = True
  app.run(host = '0.0.0.0', port = port)
