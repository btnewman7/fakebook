from flask import render_template, redirect, url_for, request
from .import bp as blog
from .models import BlogPost
from flask_login import current_user, login_required

@blog.route('/', methods=['GET'])
@login_required
def index():
    context = {
        'posts': []
    }
    return render_template('blog/index.html', **context)

    
@blog.route('/create', methods=['POST'])
@login_required
def create():
    data = {
        'body': request.form.get('post'),
        'user_id': current_user.id
    }
    post = BlogPost()
    post.from_dict(data)
    post.save()
    return redirect(url_for('main.index'))