from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': "Ruy"}
    return render_template('index.html', title='Home', user=user)
<<<<<<< HEAD
=======
    
>>>>>>> 317006031c64c16c028c7890fdc2fba58bb449ab
