import rest_api.constants as constants
import abc
import rest_api.boards.boards as board


class Player(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """
        :return: a Player object (represents the state of the player).
        """
        self._board = board.Board()
        self._turn = False

    @property
    def turn(self):
        """
        :return: whether it is currently this player's turn.
        """
        return self._turn

    @turn.setter
    def turn(self, new_turn):
        self._turn = new_turn

    @property
    def board(self):
        return self._board
