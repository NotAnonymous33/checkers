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
        self.image = IMAGES[(x + y) % 2]

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
        self.cells = [[Cell(i, j) for j in range(8)] for i in range(8)]
        print(self.cells)

    def draw(self):
        for row in self.cells:
            for cell in row:
                cell.draw()
