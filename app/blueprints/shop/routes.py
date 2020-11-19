from .import bp as shop
from flask import render_template, redirect, url_for


@shop.route('/', methods=['GET'])
def index():
    return render_template('shop/index.html')