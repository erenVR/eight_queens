import pytest
import n_queens
import main as m


@pytest.mark.parametrize("n, n_solutions", [
    (4, 2),
    (8, 92),
    (9, 352),
    (11, 2680)
])
def test_n_queens(n, n_solutions):
    result = n_queens.n_queens_main(n)
    assert result == n_solutions


@pytest.mark.parametrize("n", ["4", "8"])
def test_main(n):
    m.main(n)
