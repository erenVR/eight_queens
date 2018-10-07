import database.models as model
import datetime


def map_data_base_queen_position(board):
    array = []
    for i in range(board.size):
        for j in range(board.size):
            if board.board[i][j] > 0:
                queen = model.QueenPosition()
                queen.row = i
                queen.column = j
                array.append(queen)
    return array


def map_data_base_board(board):
    board_data_base = model.BoardDatabase()
    board_data_base.size = board.size
    board_data_base.dt_created = datetime.datetime.now()
    board_data_base.queen_positions = map_data_base_queen_position(board)
    return board_data_base
