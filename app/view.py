from app import app
from flask import render_template


@app.route('/')
def index():
    n = 'Ivan'
    return render_template('index.html', name=n)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
