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
def test_add_returns_expected_result_for_various_inputs(a, b, expected):
    assert add(a, b) == expected
    

def test_add_raises_type_error_for_non_numeric_inputs():
    with pytest.raises(TypeError):
        add("a", 1)

