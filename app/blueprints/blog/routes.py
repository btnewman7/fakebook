from flask import render_template
from .import bp as blog

@blog.route('/', methods=['GET'])
def index():
    context = {
        'posts': []
    }
    return render_template('blog/index.html', **context)