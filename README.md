# Tutorial_flask

Following the Flask Mega-Tutorial. Can be found @ https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

Chapter 1: Hello World. Done!!!

2018-04-25

Decided to add a global gitignore to get ride of the __pycache__ folders.
I followed the instructions here
https://help.github.com/articles/ignoring-files/

CMD ran:

    git config --global core.excludesfile ~/.gitignore_global

Then I added the recommended rules for python found at https://github.com/github/gitignore/blob/master/Python.gitignore to the
~/gitignore_global file.

## Starting Chapter 2 Templates

Stopped @ Loops subheading

2018-05-03

Continuing chapter 2

Dont forget everytime you need to setup the venv and setup the FLASK_APP
environment variable.

    export FLASK_APP=microblog.py

Stopped @ Template Inheritance

Added this alias to my .bash_aliases

    alias venv="source venv/bin/activate;export FLASK_APP=microblog.py;flask run"

Chapter 2 Done!

## Starting Chapter 3 Web Forms

2018-05-10

Install the flask-wtf python packages that will be used to handle web Forms

in your venv setup run:

    pip install flask-wtf

Chapter 3 Done!

## starting Chapter 4 Database

2018-05-11

Flask makes no decision about which database to use. Instead you chose which
one you want and use Flask extension to use it.

We will use Flas-SQLAlchemy SQLAlchemy is a ORM Object Relational Mapper. Meaning
I can still use class and list in Python and they will be transformed into SQL
statement by the ORM. SQLAlchemy is an ORM for many Reltional databases.

Install Flas-SQLAlchemy in my venv.

    pip install flask-sqlalchemy

Part of this tutorial Miguel want us to also use is Flask-Migrate extension it
allow to easily migrate and manage data lets see if its any good.

    pip install flask-Migrate

Next add config items to the config file.

Stopped at: The Flask-SQLAlchemy extension takes the location of the application's database from the 
