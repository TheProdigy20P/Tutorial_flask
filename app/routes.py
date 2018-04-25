from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Ruy'}
    print(render_template('index.html', title='Home', user=user))
    return render_template('index.html', title='Home', user=user)
