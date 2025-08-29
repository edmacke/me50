import pytest

from jar import Jar


def test_init():
    jar = Jar()
    assert 12 == jar.capacity
    assert 0 == jar.size


def test_str():
    jar = Jar(6)
    jar.deposit(6)

    assert '🍪🍪🍪🍪🍪🍪' == jar.__str__()
    assert '🍪🍪🍪🍪🍪🍪' == str(jar)


def test_init_negative():
    with pytest.raises(ValueError):
        Jar(-1)


def test_init_zero():
    jar = Jar(0)
    assert 0 == jar.capacity
    assert 0 == jar.size


def test_init_one():
    jar = Jar(1)
    assert 1 == jar.capacity
    assert 0 == jar.size


def test_deposit():
    jar = Jar()

    jar.deposit(3)
    assert 3 == jar.size

    jar.deposit(6)
    assert 9 == jar.size

    with pytest.raises(ValueError):
        jar.deposit(4)
    assert 9 == jar.size

    jar.deposit(3)
    assert 12 == jar.size


def test_withdraw():
    jar = Jar()

    jar.deposit(12)
    with pytest.raises(ValueError):
        jar.withdraw(13)
    assert 12 == jar.size

    jar.withdraw(3)
    jar.withdraw(3)
    jar.withdraw(3)
    jar.withdraw(2)
    assert 1 == jar.size

    jar.withdraw(1)
    assert 0 == jar.size

    with pytest.raises(ValueError):
        jar.withdraw(1)


def test_size():
    jar = Jar(20)
    jar.deposit(20)

    assert 20 == jar.size
