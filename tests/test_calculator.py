import math
import pytest
from src.calculator import add

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (0, 0, 0),                    # zero boundary
        (-1, 1, 0),                   # negative ↔ positive boundary
        (1_000_000, 1_000_000, 2_000_000),  # large number boundary
        (0.1, 0.2, 0.3),               # floating-point boundary
    ]
)
def test_add_handles_boundary_values(a, b, expected):
    if isinstance(expected, float):
        assert math.isclose(add(a, b), expected)
    else:
        assert add(a, b) == expected
