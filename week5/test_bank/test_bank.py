import bank


def test_bank_hello_leading_space():
    assert 0 == bank.value('   Hello')


def test_bank_hello_trailing_space():
    assert 0 == bank.value('Hello ')


def test_bank_hello():
    assert 0 == bank.value('hello')


def test_bank_capitals():
    assert 0 == bank.value('HELLO')


def test_bank_hello_newman():
    assert 0 == bank.value('Hello, Newman')


def test_bank_incomplete():
    assert 20 == bank.value('HELL')


def test_bank_hey_leading_spaces():
    assert 20 == bank.value('   Hey')


def test_bank_hey_trailing_spaces():
    assert 20 == bank.value('Hey  ')


def test_bank_hey():
    assert 20 == bank.value('hey')


def test_bank_hey_caps():
    assert 20 == bank.value('HEY')


def test_bank_valid():
    assert 100 == bank.value('   What''s up')


def test_bank_incorrect_values():
    assert 100 == bank.value('invalid')


def test_bank_empty_string():
    assert 100 == bank.value('')
