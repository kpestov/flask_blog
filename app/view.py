from app import app
from flask import render_template


@app.route('/')
def index():
    n = 'Ivan'
    return render_template('index.html', name=n)