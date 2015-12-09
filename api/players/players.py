import api.constants as constants
import abc
import api.board.board as board


class Player(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """
        :return: a Player object (represents the state of the player).
        """
        self._board = board()