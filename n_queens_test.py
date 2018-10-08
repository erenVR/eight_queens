import pytest
import n_queens


@pytest.mark.parametrize("n, n_solutions", [
    (4, 2),
    (8, 92),
    (9, 352),
    #(11, 2680),
    #(13, 73712)
])
def test_n_queens(n, n_solutions):
    result = n_queens.n_queens_main(n)
    assert result == n_solutions
