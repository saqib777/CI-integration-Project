import pytest
from src.calculator import add

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (0, 0, 0),
        (-1, 1, 0),
        (10, 5, 15),
    ]
)
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected
