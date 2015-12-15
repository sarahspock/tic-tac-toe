from flask import Flask
from api.board.controllers import board
from api.controls.controllers import controls
from api.games.controllers import games
from api.players.controllers import players
import traceback
import sys

app = Flask(__name__)

app.register_blueprint(board)
app.register_blueprint(controls)
app.register_blueprint(games)
app.register_blueprint(players)


if __name__ == '__main__':
    try:
        app.run(threaded=True)
    except:
        traceback.print_exc(file=sys.stdout)

