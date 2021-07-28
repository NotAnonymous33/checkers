from constants import *
from enum import Enum
import pygame

pygame.init()

class PieceColor(Enum):
    WHITE = 1
    BLACK = 0


class Piece:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = None
        if y >= 3:
            self.color = PieceColor.WHITE
        else:
            self.color = PieceColor.BLACK
        self.image = IMAGES[self.color.value]



    def draw(self):
        WIN.blit(self.image, (self.x * CLENGTH, self.y * CLENGTH))


class Cell:
    def __init__(self, x, y, piece=None):
        self.x = x
        self.y = y
        self.color = [LCOLOR, RCOLOR][(x + y) % 2]
        self.piece = piece
        self.selected = False

    def __repr__(self):
        return f"({self.x},{self.y})"

    def draw(self):
        color = self.color
        if self.selected:
            color = SCOLOR
        pygame.draw.rect(WIN, color, [self.x * CLENGTH, self.y * CLENGTH, CLENGTH, CLENGTH])
        if self.piece is not None:
            self.piece.draw()




class Board:
    def __init__(self):
        self.cells = []
        self.source_cell = None
        self.target_cell = None
        self.turn = 1
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
            self.cells.append(temp)

        # Add bottom 3 rows
        for row in range(5, 8):
            temp = []
            for col in range(8):
                temp.append(Cell(col, row))
                if (row + col) % 2:
                    temp[-1].piece = Piece(col, row)
            self.cells.append(temp)

    def click(self, xpos, ypos):
        xc = xpos // CLENGTH
        yc = ypos // CLENGTH
        if not (0 <= xc < NUM_ROWS) or not (0 <= yc < NUM_ROWS):
            self.reset_source_cell()
            return
        clicked_cell = self.cells[yc][xc]
        if self.source_cell is None:
            if clicked_cell.piece is not None:
                if (clicked_cell.piece.color.value + self.turn) % 2 == 0:
                    self.source_cell = clicked_cell
                    self.source_cell.selected = True
        else:
            # there is a source cell
            # Check if the clicked cell is valid position
            # if valid position, move cell, set turn to opposite, clear source and target cell
            if abs(clicked_cell.x - self.source_cell.x) == 1:
                if (clicked_cell.y - self.source_cell.y == -1 and self.turn) or (clicked_cell.y - self.source_cell.y == 1 and not self.turn):
                    # move piece
                    self.source_cell.piece.x = xc
                    self.source_cell.piece.y = yc
                    clicked_cell.piece = self.source_cell.piece
                    self.source_cell.piece = None
                    self.reset_source_cell()

                    self.turn = int(not self.turn)
                    print(self.turn)
                else:
                    self.reset_source_cell()
            else:
                self.reset_source_cell()

    def reset_source_cell(self):
        self.source_cell.selected = False
        self.source_cell = None




    def evaluate(self) -> int:
        ev = 0
        for row in self.cells:
            for cell in row:
                if cell.piece is not None:
                    if cell.piece.value == 1:
                        ev += 1
                    else:
                        ev -= 1
        return ev




    def draw(self):
        for row in self.cells:
            for cell in row:
                cell.draw()

