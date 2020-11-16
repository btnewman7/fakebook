from .import bp as auth
from flask import render_template, redirect, url_for, request
from .models import User
from flask_login import login_user, logout_user, current_user

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        form_data = request.form.to_dict()
        email = form_data.get('email')
        u = User.query.filter_by(email=email).first()
        if u is not None and u.check_hashed_password(form_data.get('password')):
            login_user(u)
            return redirect(url_for('main.index'))
        return redirect(url_for('authentication.login'))
    return render_template('auth/login.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        form_data = request.form.to_dict()
        data = {
            'first_name': form_data.get('first_name'),
            'last_name': form_data.get('last_name'),
            'email': form_data.get('email')
        }
        if form_data.get('password') == form_data.get('confirm_password'):
            u = User()
            u.from_dict(data)
            u.hash_password(form_data.get('password'))
            u.save()
            return redirect(url_for('authentication.login'))
        return redirect(url_for('authentication.register'))
    return render_template('auth/register.html')


@auth.route('/logout')
def logout():
    if current_user is not None:
        logout_user()
        return redirect(url_for('authentication.login'))