from flask import Flask, render_template, url_for

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(debug=True)
