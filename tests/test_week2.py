from week2.camel import camel
from week2.twttr import twttr
from week2.plates import plates
from week2.nutrition import nutrition

def test_camel1():
    assert 'first_name' == camel.answer('firstName')


def test_camel2():
    assert 'preferred_first_name' == camel.answer('preferredFirstName')


def test_vowels():
    assert twttr.is_vowel('A')
    assert twttr.is_vowel('E')
    assert twttr.is_vowel('I')
    assert twttr.is_vowel('O')
    assert twttr.is_vowel('U')
    assert twttr.is_vowel('a')
    assert twttr.is_vowel('e')
    assert twttr.is_vowel('i')
    assert twttr.is_vowel('o')
    assert twttr.is_vowel('u')


def test_twitter1():
    assert 'Twttr' == twttr.answer('Twitter')

def test_twitter2():
    assert "Wht's yr nm?" == twttr.answer("What's your name?")

def test_twitter3():
    assert 'CS50' == twttr.answer('CS50')

def test_alpha2():
    assert plates.start_with_two_letters('AA')

    assert not plates.start_with_two_letters('')
    assert not plates.start_with_two_letters('A')
    assert not plates.start_with_two_letters('A1')
    assert not plates.start_with_two_letters('1A')

def test_length():
    assert plates.valid_length('12')
    assert plates.valid_length('123')
    assert plates.valid_length('1234')
    assert plates.valid_length('12345')
    assert plates.valid_length('123456')

    assert not plates.valid_length('1')
    assert not plates.valid_length('1234567')

def test_valid_numbers():
    assert plates.valid_numbers('AAA222')
    assert plates.valid_numbers('AAA220')

    assert not plates.valid_numbers('AAA22A')
    assert not plates.valid_numbers('AAA02A')
    assert not plates.valid_numbers('AAA022')

def test_valid_punctuation():
    assert plates.valid_punctuation('AAA222')

    assert not plates.valid_punctuation('HELLO,WORLD')
    assert not plates.valid_punctuation('HELLO WORLD')
    assert not plates.valid_punctuation('PI3.14')

def test_calories():
    assert 130 == nutrition.calories("APPLE")
    assert 50 == nutrition.calories("Avocado")
    assert 100 == nutrition.calories("Sweet Cherries")
    assert None == nutrition.calories("Tomato")