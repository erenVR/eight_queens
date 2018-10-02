import Board as b
import helpers as h
import time


def n_queens(board, n,  col):
    if col >= n:
        board.increment_solutions_counter()
        h.print_board(board)
        return True
    for row in range(n):
        if board.is_safe_box(row, col):
            board.set_queen_on_board(row, col)
            n_queens(board, n, col + 1)
            board.remove_queen_on_board(row, col)
    return False


def n_queens_with_time(n):
    board = b.Board(n)
    start_time = time.clock()
    n_queens(board, n, 0)
    print('----------------------------------------')
    print(f'Solutions for N {n}: {board.solutions}')
    time_elapsed = (time.clock() - start_time)/1000
    print(f'Time elapsed {time_elapsed} for N equals to {n}\n Board:\n ')
    return True


def iterate_n_n_queen(n):
    for number in range(4, n + 1):
        n_queens_with_time(number)
