from .import bp as shop
from flask import render_template, redirect, url_for, request
from .models import Product, Category


@shop.route('/', methods=['GET'])
def index():
    context = {
        'products': Product.query.all()
    }
    return render_template('shop/index.html', **context)


@shop.route('/product', methods=['GET'])
def single():
    product_id = request.args.get('id')
    context = {
        'p': Product.query.get(product_id)
    }
    return render_template('shop/single.html', **context)

@shop.route('/category', methods=['GET'])
def category():
    category_id = request.args.get('id')
    print(request.args)
    context = {
        'category': Category.query.get(category_id),
        'products': Product.query.filter_by(category_id=category_id).all()
    }
    return render_template('shop/index.html', **context)