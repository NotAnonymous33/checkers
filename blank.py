from enum import Enum

class PieceColor(Enum):
    WHITE = 1
    BLACK = 0
    BLANK = -1


class Blank:
    def __init__(self):
        self.color = PieceColor.BLANK

    def __repr__(self):
        return "blank"

    def draw(self, *args, **kwargs):
        pass