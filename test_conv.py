import pytest
import conv


@pytest.mark.parametrize("a, expected", [(2, 10), (14, 1110), (53, 110101)])
def test_conv(a, expected):
    result = conv.convert(a)
    assert result == expected
