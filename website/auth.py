from flask_login import current_user, login_user, logout_user
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import db,  User


auth = Blueprint('auth', __name__)

# signup route
@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        phone = request.form.get('phone')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            flash('User already exists.', 'danger')
        else:
            new_user = User(email=email, first_name=first_name, last_name=last_name, phone=phone, password=password)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('auth.login'))
    return render_template('auth/signup.html', user=current_user)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if user.password == password:
                login_user(user)
                return redirect(url_for('blog.writterboard'))
            else:
                flash('Incorrect password, please try again.', 'danger')
        else:
            flash('User does not exist.', 'danger')
    return render_template('auth/login.html', user=current_user)