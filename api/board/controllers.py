from flask import Blueprint
from flask_restful import Api, Resource, marshal_with

board = Blueprint('boards', __name__, url_prefix='/v1.0')
api = Api(board)


class Board(Resource):
    """
    You can also post a new board state after a move has been completed.
    :return:  JSON representing the board state for each players
    """