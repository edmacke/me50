from io import StringIO

import pytest

from week3.fuel import fuel
from week3.grocery import grocery
from week3.outdated import outdated
from week3.taqueria import taqueria


def test_input(monkeypatch, capsys):
    value = StringIO('3/4')
    monkeypatch.setattr('sys.stdin', value)
    fuel.main()

    assert 'Fraction: 75%\n' == capsys.readouterr().out


def test_percentage():
    assert 75 == fuel.percentage('3/4')
    assert 25 == fuel.percentage('1/4')
    assert 1 == fuel.percentage('1/100')
    assert 99 == fuel.percentage('99/100')


def test_answer():
    assert '75%' == fuel.answer('3/4')
    assert '25%' == fuel.answer('1/4')
    assert 'F' == fuel.answer('4/4')
    assert 'E' == fuel.answer('0/4')
    assert '33%' == fuel.answer('1/3')
    assert '67%' == fuel.answer('2/3')


def test_divide_by_zero():
    with pytest.raises(ValueError):
        fuel.answer('4/0')


def test_words():
    with pytest.raises(ValueError):
        fuel.answer('three/four')


def test_float():
    with pytest.raises(ValueError):
        fuel.answer('1.5/3')


def test_negative():
    with pytest.raises(ValueError):
        fuel.answer('-3/4')


def test_over_100():
    with pytest.raises(ValueError):
        fuel.answer('5/4')


def test_taco():
    assert 3.0 == taqueria.price('taco')


def test_baja_taco():
    assert 4.25 == taqueria.price('Baja taco')


def test_baja_burger():
    with pytest.raises(KeyError):
        taqueria.price('BURGER')


def test_add_item():
    items = {}
    grocery.add_item('apple', items)
    grocery.add_item('apple', items)
    grocery.add_item('banana', items)
    grocery.add_item('sweet potato', items)

    assert 2 == items['apple']
    assert 1 == items['banana']
    assert 1 == items['sweet potato']


def test_dates():
    assert '1900-01-03' == outdated.iso8601('1/3/1900')
    assert '1636-09-08' == outdated.iso8601('9/8/1636')
    assert '1636-09-08' == outdated.iso8601('September 8, 1636')

    with pytest.raises(ValueError):
        outdated.iso8601('September 8 1636')

    with pytest.raises(ValueError):
        outdated.iso8601('23/6/1912')

    with pytest.raises(ValueError):
        outdated.iso8601('December 80, 1980')
