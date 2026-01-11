from src.calculator import add

def test_add(numbers):
    a, b = numbers
    assert add(a, b) == 5
