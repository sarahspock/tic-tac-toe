import api.constants as constants
import abc
import api.players.players as players


class Game(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """
        :return:  Game state of a particular game.
        """
        self._x_player = players.Player()
        self._o_player = players.Player()

    @property
    def x_player(self):
        return self._x_player

    @property
    def o_player(self):
        return self._o_player

    def set_current_player(self):
        if self.x_player.turn:
            self.x_player.turn = False
            self.o_player.turn = True
        else:
            self.o_player.turn = False
            self.x_player.turn = True
