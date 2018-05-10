from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Ruy'}
    posts = [
        {
            'author':{'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author':{'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author':{'username': 'Benoit'},
            'body': 'Hey how cool is this!'
        }
    ]
###    throw
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
##DEBUG_LINE##    flash("hello")
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title= 'Sign In', form=form)
