from flask import Blueprint, session
from flask_restful import Api, Resource, marshal_with, reqparse
import models
import abc
import api.controllers as controllers

board = Blueprint('boards', __name__, url_prefix='/v1.0/boards')
api = Api(board)

parser = reqparse.RequestParser()
parser.add_argument('bitboard')
parser.add_argument('board_id')


class Board(controllers.Base):
    """
    You can also post a new board state after a move has been completed.
    :return:  JSON representing the board state for each players
    """

    def post(self):
        """
        :return: The bitboard value that was posted.
        """
        args = parser.parse_args()
        if 'board_id' not in args or 'bitboard' not in args:
            return {'message': 'Required POST fields missing'}
        try:
            board_id = int(args['board_id'])
            # the players's board information exists and can be changed.
            if len(models.boards) > board_id:
                models.boards[board_id] = args['bitboard']
                return models.boards[board_id]
            else:
                return {'message': "Board doesn't exist"}
        except ValueError:
            return {'message': 'Board should be an integer'}

    def model_list(self):
        """
        :return: List of models representing the boards in the game
        """
        if models.boards:
            return models.boards
        return []


class BoardList(controllers.BaseList):
    """
    :return:  JSON representing the board state for both players
    """

    def model_list(self):
        """
        :return: List of models representing the boards in the game
        """
        if models.boards:
            return models.boards
        return []

api.add_resource(BoardList, "/")
api.add_resource(Board, "/<int:board_id>")
