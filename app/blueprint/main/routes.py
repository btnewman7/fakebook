from flask import render_template
from .import bp as main

@main.route('/', methods=['GET'])
def index():
    context = {}
    return render_template('main/index.html', **context)