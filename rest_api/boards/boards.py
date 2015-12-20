import rest_api.constants as constants
import abc
import models


class Board(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self, game=None):
        self._bitmap = 0x0
        models.boards_list.append(self)
        self._game = game

    @property
    def bitmap(self):
        if self._is_valid():
            return self._bitmap
        return False

    def _is_valid(self):
        """
        :return: Boolean value, returns true if the bitboard appears to be legal.
        """
        if self._bitmap & constants.VALID_SPACES == self._bitmap:
            return True
        return False

    @property
    def game(self):
        """
        :return: The game associated with this boards.
        """
        return self._game

