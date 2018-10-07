import pytest
from Board import Board
from database.DataAccessBoard import DataAccessBoard
import database.mapper as mapper


@pytest.mark.parametrize("n,board_sol", [
    (4, [[0, 0, 1, 0],
         [1, 0, 0, 0],
         [0, 0, 0, 1],
         [0, 1, 0, 0]])
])
def test_database_connection(n, board_sol):
    board = Board(n)
    board.board = board_sol
    board_db = mapper.map_data_base_board(board)
    dao = DataAccessBoard()
    dao.save_board(board_db)
