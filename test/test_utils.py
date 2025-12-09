import pytest

from src.utils import adder



@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0)
])
def test_add_ok(a, b, expected):
    assert adder(a, b) == expected