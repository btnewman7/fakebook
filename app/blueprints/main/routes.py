from flask import render_template
from .import bp as main
from app.blueprints.blog.models import BlogPost

@main.route('/', methods=['GET'])
def index():
    context = {
        'posts': BlogPost.query.order_by(BlogPost.created_on.desc()).all()
    }
    return render_template('main/index.html', **context)

@main.route('/about', methods=['GET'])
def about():
    context = {}
    return render_template('main/about.html', **context)

@main.route('/contact', methods=['GET'])
def contact():
    context = {}
    return render_template('main/contact.html', **context)