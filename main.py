import sys
import helpers as h
import Board as b
import n_queens


def main(argv):
    n = int(argv)
    print(f'Number of queens {n}')
    if not h.validate_queen_number(n):
        sys.exit(1)
    board = b.Board(n)
    if not n_queens.n_queens(board, n, 0):
        print(f"There is no solution")
        sys.exit(1)
    print(board)


if __name__ == "__main__":
    main(sys.argv[1])
