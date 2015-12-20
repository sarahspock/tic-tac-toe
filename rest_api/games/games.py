import rest_api.constants as constants
import abc
import rest_api.players.players as players
import models


class Game(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """
        :return:  Game state of a particular game.
        """
        self._x_player = players.Player()
        self._o_player = players.Player()
        models.games_list.append(self)

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

    @property
    def current_turn(self):
        """
        :return: The player whose turn it is.
        """
        if self._o_player.turn:
            return "O"
        else:
            return "X"