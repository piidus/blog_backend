from flask_login import current_user, login_user, logout_user
from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import random
from .models import db,  User, log
from .email_setup import Mailer


auth = Blueprint('auth', __name__)

# signup route
@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        print(request.json)
        email = request.json['email']
        first_name = request.json['firstName']
        last_name = request.json['lastName']
        phone = request.json['phone']
        password = request.json['password']
        print(email, first_name, last_name, phone, password) 
        # check valus are not empty
        if email == '' or first_name == '' or last_name == '' or phone == '' or password == '':
            return jsonify({'success': False, 'message': 'All fields are required!'}), 400
        else:
            user = User.query.filter_by(email=email).first()
            if user:
                return jsonify({'success': False, 'message': 'User already exists!'}), 400
            else:
                new_user = User(email=email, first_name=first_name, last_name=last_name, phone=phone, password=generate_password_hash(password, method='pbkdf2:sha1', salt_length=8))
                db.session.add(new_user)
                db.session.commit()
                # login_user(new_user)
                flash('Account created! Now LOGIN', 'success')
                return jsonify({'success': True, 'message': 'User created successfully!'}), 200
            
    return render_template('auth/signup.html', user=current_user)

# return a six digit code
@auth.route('/auth/authcode', methods=['POST'])
def authcode():
    email = request.json['email']
    authcode = random.randint(100000, 999999)
    try:
        mailer = Mailer()
        mailer.html_mail([email], 'Authentication Code', 'Your authentication code is: ' + '<b>' + str(authcode) + '</b>')
    except Exception as e:
        log.error(e)
        print(e)
    
    return jsonify ({'authcode': authcode})

# login route
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('blog.writterboard'))
            else:
                flash('Incorrect password, please try again.', 'danger')
        else:
            flash('User does not exist.', 'info')
    return render_template('auth/login.html', user=current_user)