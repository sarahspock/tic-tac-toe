import api.constants as constants
import abc


class Move(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self, proposed_move, boards):
        """
        :param proposed_move; A bitboard representing a move submitted by the players.
        :return a bitboard representing a valid move or false if there is no valid move.
        """
        self._proposed_move = proposed_move
        self._boards = boards

    @property
    def proposed_move(self):
        return self._proposed_move

    @property
    def boards(self):
        return self._boards

    @property
    def move(self):
        """
        :return: A legal move or false if the proposed move isn't legal.
        """
        if self._is_a_move() and self._is_legal():
            return self.proposed_move
        return False

    def _is_legal(self):
        """
        Checks every board in the list to see if this move has been made already
        :return: True if the move is a legal move. False otherwise.
        """
        for board in self.boards:
            # Note: This is a bitwise OR
            if board & self.proposed_move != 0:
                return False
        return True

    def _is_a_move(self):
        """
        :return: True if the propsed move actually represents a move / is valid data.
        """
        for move in constants.LEGAL_MOVES:
            if self.proposed_move == move:
                return True
        return False
