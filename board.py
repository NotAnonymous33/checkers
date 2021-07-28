from constants import *
from enum import Enum
import pygame

pygame.init()


class PieceColor(Enum):
    WHITE = 1
    BLACK = 0


class Piece:
    def __init__(self, y):
        self.color = None
        if y < 3:
            self.color = PieceColor.BLACK
        else:
            self.color = PieceColor.WHITE
        self.image = IMAGES[self.color.value]

    def __repr__(self):
        return f"{self.color}"

    def draw(self, x, y):
        WIN.blit(self.image, (x * CLENGTH, y * CLENGTH))


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = [LCOLOR, RCOLOR][(x + y) % 2]

    def draw(self):
        pygame.draw.rect(WIN, self.color, [self.x * CLENGTH, self.y * CLENGTH, CLENGTH, CLENGTH])


class Board:
    def __init__(self):
        self.cells = [[Cell(col, row) for col in range(8)] for row in range(8)]
        self.pieces = [
            [Piece(0) if i % 2 else 0 for i in range(8)],
            [Piece(1) if i % 2 == 0 else 0 for i in range(8)],
            [Piece(2) if i % 2 else 0 for i in range(8)],
            [0 for _ in range(8)],
            [0 for _ in range(8)],
            [Piece(5) if i % 2 == 0 else 0 for i in range(8)],
            [Piece(6) if i % 2 else 0 for i in range(8)],
            [Piece(7) if i % 2 == 0 else 0 for i in range(8)],
        ]

        self.source_piece = None
        self.source_coord = (-1, -1)
        self.turn = 1

    def click(self, xpos, ypos):
        xc = xpos // CLENGTH
        yc = ypos // CLENGTH
        if not (0 <= xc <= 7 and 0 <= yc <= 7):  # de morgans law moment
            self.reset_source()
        else:
            if self.source_coord == (-1, -1):  # if there isn't a source cell
                if self.pieces[yc][xc] != 0:  # if a cell with a piece is clicked
                    if self.turn == self.pieces[yc][xc].color.value:  # if the turn matches the color of the piece
                        self.source_coord = (xc, yc)  # set the clicked piece as the source piece
                    else:
                        self.reset_source()
                else:
                    self.reset_source()
            else:  # if a cell with a piece is clicked
                if self.source_coord == (xc, yc):  # if the clicked piece is the same as the source piece
                    self.reset_source()  # reset
                else:
                    # add checking if piece move is valid
                    self.pieces[yc][xc] = self.pieces[self.source_coord[1]][self.source_coord[0]]  # move source piece to the new piece
                    self.pieces[self.source_coord[1]][self.source_coord[0]] = 0  # set the source piece to 0
                    self.reset_source()  # unselect the source piece
                    self.turn = int(not self.turn)  # change the turn

    def draw(self):

        # draw the coloured squares of the board
        for row in self.cells:
            for cell in row:
                cell.draw()

        # draw highlighted squares

        # draw pieces
        for row_num in range(NUM_ROWS):
            for col_num in range(NUM_ROWS):
                if self.pieces[row_num][col_num] != 0:
                    if self.source_coord == (col_num, row_num):
                        pygame.draw.rect(WIN, SCOLOR, [col_num * CLENGTH, row_num * CLENGTH, CLENGTH, CLENGTH])
                    self.pieces[row_num][col_num].draw(col_num, row_num)

    def reset_source(self):
        self.source_coord = (-1, -1)