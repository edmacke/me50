import pytest

import fuel


def test_percentage_valid():
    assert 0 == fuel.convert('0/4')
    assert 75 == fuel.convert('3/4')
    assert 25 == fuel.convert('1/4')
    assert 1 == fuel.convert('1/100')
    assert 99 == fuel.convert('99/100')
    assert 100 == fuel.convert('100/100')


def test_percentage_valid_rounding():
    assert 33 == fuel.convert('1/3')
    assert 67 == fuel.convert('2/3')


def test_convert_alphas():
    with pytest.raises(ValueError):
        fuel.convert('three/four')


def test_convert_alpha_x():
    with pytest.raises(ValueError):
        fuel.convert('three/4')


def test_convert_alpha_y():
    with pytest.raises(ValueError):
        fuel.convert('3/four')


def test_larger_numerator():
    with pytest.raises(ValueError):
        fuel.convert('5/4')


def test_convert_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        fuel.convert('4/0')


def test_convert_float():
    with pytest.raises(ValueError):
        fuel.convert('1.5/3')


def test_convert_negative():
    with pytest.raises(ValueError):
        fuel.convert('-3/4')


def test_gauge_empty():
    assert 'E' == fuel.gauge(0)
    assert 'E' == fuel.gauge(1)


def test_gauge_full():
    assert 'F' == fuel.gauge(100)
    assert 'F' == fuel.gauge(99)


def test_gauge_other():
    assert '75%' == fuel.gauge(75)
    assert '25%' == fuel.gauge(25)
    assert '33%' == fuel.gauge(33)
    assert '67%' == fuel.gauge(67)
