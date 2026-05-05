import pytest
import utils


@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (2, 3, 5), (5, 2, 7)])
def test_add(a, b, expected):
    result = utils.add(a, b)
    assert result == expected


@pytest.mark.parametrize("a, b, expected", [(1, 2, -1), (2, 3, -1), (5, 2, 3)])
def test_subtract(a, b, expected):
    result = utils.subtract(a, b)
    assert result == expected


@pytest.mark.parametrize("a, b, expected", [(1, 2, 2), (2, 3, 6), (5, 2, 10)])
def test_multiply(a, b, expected):
    result = utils.multiply(a, b)
    assert result == expected


@pytest.mark.parametrize("a, b, expected", [(1, 2, 0.5), (6, 4, 1.5), (5, 2, 2.5)])
def test_divide(a, b, expected):
    result = utils.divide(a, b)
    assert result == expected

