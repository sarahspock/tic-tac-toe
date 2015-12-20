# Overview
This is an implementation of tic-tac-toe using the Flask Python framework and Bootstrap for the front-end. The flask
implementation uses flask-restful, a flask library that provides resources to create an API using flask.

# Installation
Install all required libraries by typing:

pip install -r /path/to/requirements.txt

It is best to do this in a virtual machine, which can be created by typing the following in the project directory:

virtualenv venv

Type the following to activate the virtual environment:

source venv/bin/activate

# Running the Server
Type the following in the root project directory:

python run.py

This program launches a decoupled application containing both a backend (API) and frontend (sample).  Interact with the application by typing curl commands, as noted below;


# How to Use

### To See Currently Active Games
curl http://127.0.0.1:5000/api/v1.0/games/

### To Start a New Game
curl http://127.0.0.1:5000/api/v1.0/games/ -X POST

### To Delete a Game
Games are stored as a list in the system (since this is just a demo). Type the index from the list
of the game you wish to delete:
