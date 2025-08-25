import plates


def test_starts_with_two_alphas():
    assert plates.is_valid('AA123')


def test_not_start_with_two_alphas():
    assert not plates.is_valid('')
    assert not plates.is_valid('A')
    assert not plates.is_valid('A1')
    assert not plates.is_valid('1A')
    assert not plates.is_valid('1A')


def test_correct_length():
    assert plates.is_valid('AA')
    assert plates.is_valid('AA1')
    assert plates.is_valid('AA12')
    assert plates.is_valid('AA123')
    assert plates.is_valid('AA1234')


def test_invalid_length():
    assert not plates.is_valid('A')
    assert not plates.is_valid('AA123456')


def test_valid():
    assert plates.is_valid('AAA222')
    assert plates.is_valid('AAA220')


def test_numbers_in_middle():
    assert not plates.is_valid('AAA22A')
    assert not plates.is_valid('AAA02A')
    assert not plates.is_valid('AAA022')


def test_valid_punctuation():
    assert plates.is_valid('AAA222')


def test_invalid_punctuation():
    assert not plates.is_valid('HELLO,WORLD')
    assert not plates.is_valid('HELLO WORLD')
    assert not plates.is_valid('PI3.14')
