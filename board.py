from constants import *
import pygame
from button import Button
from ai import AI
from blank import PieceColor, Blank

pygame.init()






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
        # pygame.draw.circle(WIN, [(255, 255, 255), (0, 0, 0)][self.color.value], (x, y), 20)


class King(Piece):
    def __init__(self, y):
        super(King, self).__init__(y)

    def draw(self, x, y):
        super().draw(x, y)

    def __repr__(self):
        super().__repr__()


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = [LCOLOR, RCOLOR][(x + y) % 2]

    def draw(self):
        pygame.draw.rect(WIN, self.color, [self.x * CLENGTH, self.y * CLENGTH, CLENGTH, CLENGTH])

    def __repr__(self):
        return f"({self.x}, {self.y})"


class Board:
    def __init__(self):
        self.cells = [[Cell(col, row) for col in range(8)] for row in range(8)]
        self.pieces = [
            [Piece(0) if i % 2 else Blank() for i in range(8)],
            [Piece(1) if i % 2 == 0 else Blank() for i in range(8)],
            [Piece(2) if i % 2 else Blank() for i in range(8)],
            [Blank() for _ in range(8)],
            [Blank() for _ in range(8)],
            [Piece(5) if i % 2 == 0 else Blank() for i in range(8)],
            [Piece(6) if i % 2 else Blank() for i in range(8)],
            [Piece(7) if i % 2 == 0 else Blank() for i in range(8)],
        ]

        self.source_coord = (-1, -1)
        self.turn = 1
        self.highlighted_cells = []
        self.buttons = []
        self.ai = AI()

    def click(self, xpos, ypos):
        xc = xpos // CLENGTH
        yc = ypos // CLENGTH
        # if the click is outside the board, reset the pieces
        if not (0 <= xc <= 7 and 0 <= yc <= 7):  # de morgans law moment
            self.reset_source()
            return

        if self.source_coord == (-1, -1):  # if there isn't a source cell
            if self.pieces[yc][xc] != Blank():  # if a cell with a piece is clicked
                if self.turn == self.pieces[yc][xc].color.value:  # if the turn matches the color of the piece
                    self.source_coord = (xc, yc)  # set the clicked piece as the source piece
                    self.highlight_cells(xc, yc)
                else:
                    self.reset_source()
            else:
                self.reset_source()
        else:
            if self.source_coord == (xc, yc):  # if the clicked piece is the same as the source piece
                self.reset_source()  # reset
            else:
                # add checking if piece move is valid
                if (xc, yc) in self.highlighted_cells:
                    if abs(yc - self.source_coord[1]) == 2:  # if the piece moves 2 (jumps)
                        self.pieces[(yc + self.source_coord[1]) // 2][(xc + self.source_coord[0]) // 2] = Blank()
                    self.move_piece(xc, yc)
                    self.ai.move(self)

    def move_piece(self, x, y):
        if y == 7 and self.turn == 0 or y == 0 and self.turn == 1:
            self.buttons.append(Button(0, TLENGTH))
            self.pieces[y][x] = King(7 - y)
        else:
            self.pieces[y][x] = self.pieces[self.source_coord[1]][
                self.source_coord[0]]  # move source piece to the new piece
        self.pieces[self.source_coord[1]][self.source_coord[0]] = Blank()  # set the source piece to 0
        self.turn = int(not self.turn)  # unselect the source piece
        self.reset_source()  # change the turn

    def draw(self, mousex, mousey):

        # draw the coloured squares of the board
        for row in self.cells:
            for cell in row:
                cell.draw()

        # draw highlighted squares
        for coord in self.highlighted_cells:
            pygame.draw.rect(WIN, HCOLOR, [coord[0] * CLENGTH, coord[1] * CLENGTH, CLENGTH, CLENGTH])

        # draw pieces
        for row_num in range(NUM_ROWS):
            for col_num in range(NUM_ROWS):
                if self.source_coord == (col_num, row_num):
                    pygame.draw.rect(WIN, SCOLOR, [col_num * CLENGTH, row_num * CLENGTH, CLENGTH, CLENGTH])
                self.pieces[row_num][col_num].draw(col_num, row_num)

        for button in self.buttons:
            button.check_hover(mousex, mousey)
            button.draw()

    def reset_source(self):
        self.source_coord = (-1, -1)
        self.highlighted_cells = []

    def highlight_cells(self, x, y):
        direction: int
        if self.turn:
            direction = -1
        else:
            direction = 1

        '''
        If the piece top left is opposite color and piece 2 top left is blank, add to highlighted
        otherwise, if the piece top left is empty, add to highlighted
        
        Same for top right
        '''

        self.check_direction(x, y, direction, -1)
        self.check_direction(x, y, direction, 1)
        if isinstance(self.pieces[y][x], King):
            self.check_direction(x, y, -direction, -1)
            self.check_direction(x, y, -direction, 1)

    def check_direction(self, x, y, ydirection, xdirection):
        try:
            if self.pieces[y + ydirection][x + xdirection].color.value == -1:
                self.highlighted_cells.append((x + xdirection, y + ydirection))
                return
        except IndexError:
            pass
        try:
            if self.pieces[y + ydirection][x + xdirection].color.value == int(not self.turn) and \
                    self.pieces[y + 2 * ydirection][x + 2 * xdirection].color.value == -1:
                self.highlighted_cells.append((x + 2 * xdirection, y + 2 * ydirection))
        except IndexError:
            pass

    def quit(self):
        white = 0
        black = 0
        for row in self.pieces:
            for piece in row:
                if piece.color.value == 0:
                    black += 1
                elif piece.color.value == 1:
                    white += 1
        return not all([white, black])

    def evaluate(self):
        count = 0
        for row in self.pieces:
            for piece in row:
                if piece.color.value == 0:
                    count -= 1
                elif piece.color.value == 1:
                    count += 1
        return count
