import Board as b
import helpers as h
import time


def n_queens(board, n,  col):
    if col >= n:
        return True
    for row in range(n):
        if board.is_safe_box(row, col):
            board.set_queen_on_board(row, col)
            if n_queens(board, n, col + 1):
                return True
            board.remove_queen_on_board(row, col)
    return False


def n_queens_with_time(n):
    board = b.Board(n)
    start_time = time.clock()
    if not n_queens(board, n, 0):
        print(f"There is no solution")
        return False
    time_elapsed = time.clock() - start_time
    print(f'Time elapsed {time_elapsed} for N equals to {n}\n Board:\n ')
    h.print_board(board.board)
    return True


def iterate_n_n_queen(n):
    for number in range(4, n + 1):
        n_queens_with_time(n)
