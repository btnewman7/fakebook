from .blueprints.shop.models import Category
from flask import current_app as app

@app.context_processor
def get_product_categories():
    return { 'product_categories': [c for c in Category.query.order_by(Category.name).all()] }