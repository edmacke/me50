import pytest

from working import convert


def test_valid():
    assert '9:00 to 17:00' == convert('9:00 AM to 5:00 PM')
    assert '9:00 to 17:00' == convert('9 AM to 5 PM')
    assert '9:00 to 17:00' == convert('9:00 AM to 5 PM')
    assert '9:00 to 17:00' == convert('9 AM to 5:00 PM')


def test_invalid_from():
    with pytest.raises(ValueError):
        convert('12:60 AM to 5:00 PM')

    with pytest.raises(ValueError):
        convert('13:00 AM to 5:00 PM')

def test_invalid_to():
    with pytest.raises(ValueError):
        convert('9:00 AM to 12:60 PM')

    with pytest.raises(ValueError):
        convert('9:00 AM to 13:00 PM')
