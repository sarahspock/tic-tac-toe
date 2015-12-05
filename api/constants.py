# These are useful constants used to make the program readable, presenting useful
# information like spaces on the board.
# The Board:
# 123
# 456
# 789
# Represented by a bitboard that is 9 lengths long:
# 0x1FF or Binary: b'1 1111 1111
SPACE_ONE = 0x100
SPACE_TWO = 0x80
SPACE_THREE = 0x40
SPACE_FOUR = 0x20
SPACE_FIVE = 0x10
SPACE_SIX = 0x08
SPACE_SEVEN = 0x04
SPACE_EIGHT = 0x02
SPACE_NINE = 0x01

LEGAL_MOVES = [SPACE_ONE, SPACE_TWO, SPACE_THREE, SPACE_FOUR,
               SPACE_FIVE, SPACE_SIX, SPACE_SEVEN, SPACE_EIGHT,
               SPACE_NINE]