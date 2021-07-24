from constants import *
from enum import Enum
import pygame

pygame.init()

class PieceColor(Enum):
    WHITE = 0
    BLACK = 1


class Piece:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = IMAGES[y >= 3]


    def draw(self):
        WIN.blit(self.image, (self.x * CLENGTH, self.y * CLENGTH))


class Cell:
    def __init__(self, x, y, piece=None):
        self.x = x
        self.y = y
        self.color = [LCOLOR, RCOLOR][(x + y) % 2]
        self.piece = piece

    def __repr__(self):
        return f"({self.x},{self.y})"

    def draw(self):
        pygame.draw.rect(WIN, self.color, [self.x * CLENGTH, self.y * CLENGTH, CLENGTH, CLENGTH])
        if self.piece is not None:
            self.piece.draw()




class Board:
    def __init__(self):
        self.cells = []
        # Add top 3 rows
        for row in range(3):
            temp = []
            for col in range(8):
                temp.append(Cell(col, row))
                if (row + col) % 2:
                    temp[-1].piece = Piece(col, row)
            self.cells.append(temp)

        # Add next 2 empty rows
        for row in range(3, 5):
            temp = []
            for col in range(8):
                temp.append(Cell(col, row))
            self.cells.append((temp))

        for row in range(5, 8):
            temp = []
            for col in range(8):
                temp.append(Cell(col, row))
                if (row + col) % 2:
                    temp[-1].piece = Piece(col, row)
            self.cells.append(temp)

        # Add bottom 3 rows






    def draw(self):
        for row in self.cells:
            for cell in row:
                cell.draw()
