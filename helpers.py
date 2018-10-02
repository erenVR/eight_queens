import numpy as np


def validate_queen_number(number):
    valid = number > 3
    if not valid:
        print(f'Number of queens must be greater than 3 : {n}')
    return valid


def initialize_left_right_diagonal(n):
    matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            matrix[i][j] = i + j
    return matrix


def initialize_right_left_diagonal(n):
    matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            matrix[i][j] = i - j + n - 1
    return matrix


def initialize_board(n):
    return np.zeros((n, n))


def print_board(board):
    n = board.size
    for i in range(n):
        s = ''
        for j in range(n):
            s = s + str(board.board[i][j]) + ' '
        print(s + '\n')
    print('\n')
