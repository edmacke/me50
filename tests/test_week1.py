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


