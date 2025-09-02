import pytest

from working import convert


def test_check50():
    assert '00:00 to 12:00' == convert('12 AM to 12 PM')
    assert '09:00 to 17:00' == convert('9 AM to 5 PM')
    assert '09:00 to 17:00' == convert('9:00 AM to 5:00 PM')
    assert '20:00 to 08:00' == convert('8 PM to 8 AM')
    assert '20:00 to 08:00' == convert('8 PM to 8:00 AM')


def test_valid():
    assert '09:00 to 17:00' == convert('9 AM to 5 PM')
    assert '09:00 to 17:00' == convert('9:00 AM to 5 PM')
    assert '09:00 to 17:00' == convert('9 AM to 5:00 PM')


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


def test_missing_to():
    with pytest.raises(ValueError):
        assert '00:00 to 12:00' == convert('12 AM 12 PM')
