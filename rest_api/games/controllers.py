from flask import Blueprint, session
import models
import rest_api.controllers as controllers
import games as game_object
import sys
import traceback
from flask_restful import Api, Resource, marshal_with, reqparse

games = Blueprint('games', __name__, url_prefix='/v1.0/games')
api_object = Api(games)

parser = reqparse.RequestParser()
parser.add_argument('bitboard')
parser.add_argument('game_id')


class GameList(controllers.BaseList):
    """
    :return:  JSON representing all of the games
    """

    def model_list(self):
        """
        :return: List of models representing all of the games
        """
        return models.games_list

    def name(self):
        return "Current Games"

    def post(self):
        # Create a new game.
        try:
            new_game = game_object.Game()
            self.model_list().append(new_game)
            return self._friendly_list_display(len(self.model_list())-1)
        except:
            traceback.print_exc(file=sys.stdout)

    def get(self):
        return self._friendly_list_display()

    def _friendly_list_display(self, id=None):
        if id is None:
            friendly_dict_display = {}
            counter = 0
            for game in self.model_list():
                friendly_dict_display["Game " + str(counter)] = {
                    "Current Turn" : game.current_turn,
                    "X Bitboard": game.x_player.board.bitmap,
                    "O Bitboard": game.o_player.board.bitmap
                }
            return friendly_dict_display
        else:
            game_to_print = self.model_list()[id]
            return {
                "Current Turn" : game_to_print.current_turn,
                "X Bitboard": game_to_print.x_player.board.bitmap,
                "O Bitboard": game_to_print.o_player.board.bitmap
            }

class Game(Resource):
    """
    You can also post a new boards state after a move has been completed.
    :return:  JSON representing the boards state for each players
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
            # the players's boards information exists and can be changed.
            if len(models.boards) > board_id:
                models.boards[board_id] = args['bitboard']
                return models.boards[board_id]
            else:
                return {'message': "Board doesn't exist"}
        except ValueError:
            return {'message': 'Board should be an integer'}

    def model_list(self):
        """
        :return: List of models representing all of the games
        """
        return models.games_list


api_object.add_resource(GameList, "/")
api_object.add_resource(Game, "/<int:game_id>")
