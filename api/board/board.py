import api.constants as constants
import abc
import models


class Board(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self._bitmap = 0x0
        models.boards.append(self)

    @property
    def bitmap(self):
        if self._is_valid():
            return self._bitmap
        return False

    def _is_valid(self):
        """
        :return: Boolean value, returns true if the bitboard appears to be legal.
        """
        if self.bitmap & constants.VALID_SPACES == self.bitmap:
            return True
        return False
