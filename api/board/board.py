import api.constants as constants
import abc


class Board(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self._bitmap = 0x0

    @property
    def bitmap(self):
        return self._bitmap

    def is_valid(self):
        """

        :return: Boolean value, returns true if the bitboard appears to be legal.
        """