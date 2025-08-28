import pytest

from um import count


def test_one():
    assert 1 == count('um')


def test_punctuation():
    assert 1 == count('um?')
    assert 1 == count('um.')
    assert 1 == count('um...')
    assert 1 == count('?um')
    assert 1 == count('.um')
    assert 1 == count('...um')


def test_case():
    assert 1 == count('Um, thanks for the album.')


def test_2():
    assert 2 == count('Um, thanks, um...')


def test_yummy():
    assert 1 == count('Um, thanks, yummy...')


def test_none():
    assert 0 == count('Yummy!')


def test_world():
    assert 2 == count('Um, hello, um, world')


def test_at_end():
    assert 3 == count('Um, hello, um um')


def test_spaces():
    assert 1 == count(' Um ')


def test_hello_world():
    assert 1 == count('Hello, um, world')


def test_cs50():
    assert 1 == count('This is, um... CS50.')


def test_regex():
    assert 1 == count('Um... what are regular expressions?')


def test_regex2():
    assert 2 == count('Um, thanks, um, regular expressions make sense now.')


def test_multiple():
    assert 2 == count('Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?')


def test_trailing_space():
    assert 1 == count('Um ')
    assert 1 == count('Um   ')


def test_leading_space():
    assert 1 == count(' Um')
    assert 1 == count('  Um')


def test_leading_trailing_spaces():
    assert 1 == count('  Um  ')
    assert 1 == count(' Um ')
    assert 1 == count('Um')


def test_no_match():
    assert 0 == count('Umm')


def test_blank():
    assert 0 == count('')
    assert 0 == count(' ')
    with pytest.raises(TypeError):
        count(None)
