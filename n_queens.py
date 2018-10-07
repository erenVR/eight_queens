import Board as b
import helpers as h
import time
from database import DataAccessBoard


def n_queens(board, n, col, dao):
    if col >= n:
        board.increment_solutions_counter()
        h.print_board(board)
        h.save_board(board, dao)
        return True
    for row in range(n):
        if board.is_safe_box(row, col):
            board.set_queen_on_board(row, col)
            n_queens(board, n, col + 1, dao)
            board.remove_queen_on_board(row, col)
    return False


def n_queens_main(n):
    dao = DataAccessBoard.DataAccessBoard()
    try:
        solutions = n_queen_with_time(n, dao)
    except:
        dao.rollback()
        raise
    finally:
        dao.finish_session()
    return solutions


def n_queen_with_time(n, dao):
    start_time = time.clock()
    board = b.Board(n)
    n_queens(board, n, 0, dao)
    print('----------------------------------------')
    print(f'Solutions for N {n}: {board.solutions}')
    time_elapsed = (time.clock() - start_time) / 1000
    print(f'Time elapsed {time_elapsed} for N equals to {n}\n Board:\n ')
    return board.solutions
