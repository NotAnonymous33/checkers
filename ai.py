from copy import copy, deepcopy
from constants import *
from blank import Blank

class AI:
    def __init__(self, depth=0):
        self.depth = depth

    def move(self, board):
        # find the best move and move it
        best_source_coord = (0, 0)
        best_dest_coord = (0, 0)
        lowest_eval = 50
        '''
        ________________________________________
        |Actual stuff which is meant to happen 
        ---------------------------------------
        | 1. For each piece
        | 2. For each move the piece can make
        | 3. Evaluate this position
        | 4. If the position is higher than the current valued position
        | 5. Set the source coord as the best source coord
        | 6. Set the dest coord as the best dest coord
        | 7. After evaluating all moves, move the piece from src to dest
        ------------------------------------------
        Loop through pieces using x y range
        If black set this as temp coord
        Check highlighted cells
        For each highlighted cell, create new board copy and move cell from temp coord to highlighted cell
        Evaluate position
        If evaluated position is higher than current evaluation, set best coords
        Move the piece
        
        '''
        for row in range(NUM_ROWS):
            for col in range(NUM_ROWS):

                if board.pieces[row][col].color.value == 0:
                    board.source_coord = (col, row)
                    board.highlight_cells(col, row)
                    for move in board.highlighted_cells:
                        temp_board = copy(board)
                        temp_board.pieces = [row[:] for row in board.pieces]
                        temp_board.move_piece(*move)  # may need to be *move
                        evaluation = temp_board.evaluate()
                        # [print(temp_board.pieces[i]) for i in range(len(temp_board.pieces))]
                        if evaluation < lowest_eval:
                            lowest_eval = evaluation
                            best_source_coord = (col, row)
                            best_dest_coord = move

        board.source_coord = best_source_coord
        print(best_source_coord)
        print(best_dest_coord)
        board.move_piece(*best_dest_coord)
        if abs(best_source_coord[0] - best_dest_coord[0]) == 2:
            board.pieces[(best_dest_coord[1] + best_source_coord[1]) // 2][(best_dest_coord[0] + best_source_coord[0]) // 2] = Blank()





    def minimax(self):
        pass
