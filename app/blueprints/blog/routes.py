from app import db
from flask import render_template, redirect, url_for, request, flash
from .import bp as blog
from .models import BlogPost
from app.blueprints.authentication.models import User
from flask_login import current_user, login_required
from .forms import ProfileForm

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

@blog.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = ProfileForm()
    if form.validate_on_submit():
        try:
            data = {
                'first_name': form.first_name.data,
                'last_name': form.last_name.data,
                'email': form.email.data
            }
            u = User.query.get(current_user.id)
            u.from_dict(data)
            if form.password.data and form.confirm_password.data:
                u.hash_password(form.password.data)
            db.session.commit()
            flash('Profile updated successfully', 'success')
            return redirect(url_for('blog.profile'))
        except Exception:
            flash('Profile was not updated. Please try again.', 'danger')
            return redirect(url_for('blog.profile'))
    context = {
        'posts': current_user.posts,
        'form': form
    }
    return render_template('blog/profile.html', **context)


@blog.route('/network', methods=['GET'])
@login_required
def network():
    context = {
        'users': [u for u in User.query.all() if current_user.id != u.id]
    }
    return render_template('blog/network.html', **context)

@blog.route('/follow', methods=['GET'])
@login_required
def follow():
    user_id = request.args.get('user_id')
    u = User.query.get(user_id)
    current_user.follow(u)
    db.session.commit()
    flash(f'You have followed {u.first_name} {u.last_name}', 'success')
    return redirect(url_for('blog.network'))

@blog.route('/unfollow', methods=['GET'])
@login_required
def unfollow():
    user_id = request.args.get('user_id')
    u = User.query.get(user_id)
    current_user.unfollow(u)
    db.session.commit()
    flash(f'You have unfollowed {u.first_name} {u.last_name}', 'warning')
    return redirect(url_for('blog.network'))