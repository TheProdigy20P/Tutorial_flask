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
