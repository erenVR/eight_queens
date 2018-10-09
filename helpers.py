import numpy as np
import database.mapper as mapper


def validate_queen_number(number):
    valid = number > 3
    if not valid:
        print(f'Number of queens must be greater than 3 : {number}')
    return valid


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


def save_board(board, dao):
    board_db = mapper.map_data_base_board(board)
    return dao.save_board(board_db)
