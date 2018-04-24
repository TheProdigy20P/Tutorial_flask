Create a directory where the project will run

cd into that directory.

then run

    python3 -m venv venv

The second venv is the name of the virtualenvironment

It did not work and I got this error


    The virtual environment was not created successfully because ensurepip is not available. On Debian/Ubuntu systems, you need to install the python3-venv package using the following command. apt-get install python3-venv You may need to use sudo with that command.  After installing the python3-venv package, recreate your virtual environment. Failing command: ['/home/benoit/Projects/python/Tutorial_flask/tutorial_flask/bin/python3', '-Im', 'ensurepip', '--upgrade', '--default-pip']

Running this command with SUDO fixed it.

    sudo apt install python3-venv

Next activate the virtual environment.

    venv/bin/activate

Next install flask in your new venv

    pip install flask




