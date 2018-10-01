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
