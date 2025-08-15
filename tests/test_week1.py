import bank.bank as bank
import deep.deep as deep


def test_42():
    assert 'Yes' == deep.answer('42')


def test_42():
    assert 'Yes' == deep.answer(' 42 ')


def test_42_words_hyphen():
    assert 'Yes' == deep.answer('forty-two')


def test_42_words_space():
    assert 'Yes' == deep.answer('forty two')


def test_42_words_case():
    assert 'Yes' == deep.answer('FORTY TWO')
    assert 'Yes' == deep.answer('FORTY-TWO')


def test_43_words_case():
    assert 'No' == deep.answer('43')


def test_bank_hello_leading_space():
    assert '$0' == bank.answer('   Hello')


def test_bank_hello_trailing_space():
    assert '$0' == bank.answer('Hello ')

def test_bank_hello_newman():
    assert '$0' == bank.answer('Hello, Newman')

def test_bank_hey():
    assert '$20' == bank.answer('   Hey')


def test_bank_bingo():
    assert '$100' == bank.answer('   What''s up')
