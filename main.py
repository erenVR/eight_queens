import sys
import helpers as h
import n_queens


def main(argv):
    n = int(argv)
    print(f'Number of queens {n}')
    if not h.validate_queen_number(n):
        sys.exit(1)
    n_queens.iterate_n_n_queen(n)


if __name__ == "__main__":
    main(sys.argv[1])
