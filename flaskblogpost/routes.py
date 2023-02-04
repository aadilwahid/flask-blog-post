from flask import render_template, url_for, flash, redirect
from flaskblogpost import app
from flaskblogpost.forms import RegistrationForm, LoginForm
from flaskblogpost.models import User, Post

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
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))

    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'asdf':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))

        flash('Login Unsuccessful. Please check username and password', 'danger')

    return render_template('login.html', title='Login', form=form)
