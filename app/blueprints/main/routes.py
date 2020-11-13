from flask import render_template
from .import bp as main

@main.route('/', methods=['GET'])
def index():
    context = {}
    return render_template('main/index.html', **context)

@main.route('/about', methods=['GET'])
def about():
    context = {}
    return render_template('main/about.html', **context)

@main.route('/contact', methods=['GET'])
def contact():
    context = {}
    return render_template('main/contact.html', **context)