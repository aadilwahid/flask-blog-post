from flask import render_template, url_for, flash, redirect, request
from flaskblogpost import app, db, bcrypt
from flaskblogpost.forms import RegistrationForm, LoginForm
from flaskblogpost.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

posts = [
    {
        "author": 'John',
        'title': 'blog post 1',
        'content': 'first content of blog post',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane',
        'title': 'blog post 2',
        'content': 'second content of blog post',
        'date_posted': 'April 23, 2018'
    }]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if not user:
            flash('User with this email does not exist.', 'danger')
            return render_template('login.html', title='Login', form=form)
        
        if not bcrypt.check_password_hash(user.password, form.password.data):
            flash('Incorrect password.', 'danger')
            return render_template('login.html', title='Login', form=form)
            
        login_user(user, remember=form.remember.data)
        next_page = request.args.get('next')
        flash('You have been logged in!', 'success')
        return redirect(next_page) if next_page else redirect(url_for('home'))

    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')