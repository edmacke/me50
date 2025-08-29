from datetime import date, timedelta

import pytest

from seasons import calculate_delta, delta_words


def test_365_days():
    test_date = date.today() - timedelta(days=365)
    assert timedelta(days=365) == calculate_delta(test_date.strftime('%Y-%m-%d'))


def test_366_days():
    test_date = date.today() - timedelta(days=366)
    assert timedelta(days=366) == calculate_delta(test_date.strftime('%Y-%m-%d'))


def test_words_365_days():
    assert 'Five hundred twenty-five thousand, six hundred minutes' == delta_words(timedelta(days=365))


def test_words_2_years():
    assert 'One million, fifty-one thousand, two hundred minutes' == delta_words(timedelta(days=730))


def test_words_2_years_leap():
    assert 'One million, fifty-two thousand, six hundred forty minutes' == delta_words(timedelta(days=731))


def test_words_1_day():
    assert 'One thousand, four hundred forty minutes' == delta_words(timedelta(days=1))


def test_words_1_minute():
    assert 'One minute' == delta_words(timedelta(minutes=1))


def test_invalid_dates():
    with pytest.raises(SystemExit):
        calculate_delta('')

    with pytest.raises(SystemExit):
        calculate_delta('2024')

    with pytest.raises(SystemExit):
        calculate_delta('2024-02')

    with pytest.raises(SystemExit):
        calculate_delta('2024-02-30')

    with pytest.raises(SystemExit):
        calculate_delta('abc-01-30')

    with pytest.raises(SystemExit):
        calculate_delta('2024-aa-30')

    with pytest.raises(SystemExit):
        calculate_delta('2024-01-aa')

    with pytest.raises(SystemExit):
        calculate_delta('2024-1-30')
