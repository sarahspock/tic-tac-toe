from flask import Blueprint, session
from flask_restful import Api, Resource, marshal_with, reqparse
import models

board = Blueprint('boards', __name__, url_prefix='/v1.0')
api = Api(board)

parser = reqparse.RequestParser()
parser.add_argument('bitboard')
parser.add_argument('board_id')


class Board(Resource):
    """
    You can also post a new board state after a move has been completed.
    :return:  JSON representing the board state for each players
    """

    def get(self, board_id):
        """
        :param board_id: the id of the board. There should be one for each player.
        :return: a bitboard representing the move state of the players board.
        The 9th bit (most significant) is the top leftmost square, and the least
        significant bit is the bottom rightmost square.
        """
        if len(models.boards) > board_id:
            return models.boards[board_id]
        else:
            return {'message': 'Invalid board ID'}

    def post(self):
        """
        :return: The bitboard value that was posted.
        """

        args = parser.parse_args()
        if 'board_id' not in args or 'bitboard' not in args:
            return {'message': 'Required POST fields missing'}
        try:
            board_id = int(args['board_id'])
            # the player's board information exists and can be changed.
            if len(models.boards) > board_id:
                models.boards[board_id] = args['bitboard']
                return models.boards[board_id]
            else:
                return {'message': "Board doesn't exist"}
        except ValueError:
            return {'message': 'Board should be an integer'}


class BoardList(Resource):
    """
    :return:  JSON representing the board state for both players
    """

    def get(self):
        """
        :return: all board states
        """
        return models.boards

    def post(self):
        """
        :return: just added bitboard
        """
        models.boards.append(0x0)
        return models.boards[-1]

api.add_resource(BoardList, "/")
api.add_resource(Board, "/<int:board_id>")
