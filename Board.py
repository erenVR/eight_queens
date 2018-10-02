import helpers as h
import numpy as np


class Board:
    def __init__(self, n):
        self.board = h.initialize_board(n)
        self.occupied_column = np.zeros(n)
        self.occupied_row = np.zeros(n)
        self.occupied_left_right_diagonal = np.zeros(2 * n)
        self.occupied_right_left_diagonal = np.zeros(2 * n)
        self.size = n
        self.solutions = 0

    def queen_share_col(self, col):
        return self.occupied_column[col] > 0

    def queen_share_row(self, row):
        return self.occupied_row[row] > 0

    #Diagonal \
    def queen_share_left_right_diagonal(self, row, col):
        id_diagonal = row + col
        return self.occupied_left_right_diagonal[id_diagonal] > 0

    #Diagonal /
    def queen_share_right_left_diagonal(self, row, col):
        id_diagonal = row - col + self.size - 1
        return self.occupied_right_left_diagonal[id_diagonal] > 0

    def is_safe_box(self, row, col):
        share_any_boxes = self.queen_share_row(row) or \
                          self.queen_share_col(col) or \
                          self.queen_share_left_right_diagonal(row, col) or \
                          self.queen_share_right_left_diagonal(row, col)
        return not share_any_boxes

    def set_queen_on_board(self, row, col):
        self.set_value_on_board(row, col, 1)

    def remove_queen_on_board(self, row, col):
        self.set_value_on_board(row, col, 0)

    def set_value_on_board(self, row, col, value):
        self.occupied_row[row] = value
        self.occupied_column[col] = value
        self.board[row][col] = value
        self.occupied_left_right_diagonal[row + col] = value
        self.occupied_right_left_diagonal[row - col + self.size - 1] = value

    def increment_solutions_counter(self):
        self.solutions += 1

    def __str__(self):
        h.print_board(self.board)
