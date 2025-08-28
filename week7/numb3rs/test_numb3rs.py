from numb3rs import validate


def test_valid():
    assert validate('0.0.0.0')
    assert validate('255.255.255.255')
    assert validate('192.168.0.0')
    assert validate('127.0.0.1')


def test_incorrect_parts():
    assert not validate('192')
    assert not validate('192.168')
    assert not validate('192.168.0')
    assert not validate('192.168.0.0.0')


def test_cat():
    assert not validate('cat.0.0.0')
    assert not validate('0.cat.0.0')
    assert not validate('0.0.cat.0')
    assert not validate('0.0.0.cat')
    assert not validate('cat.cat.cat.cat')


def test_512():
    assert not validate('512.0.0.0')
    assert not validate('0.512.0.0')
    assert not validate('0.0.512.0')
    assert not validate('0.0.0.512')
    assert not validate('512.512.512.512')


def test_1000():
    assert not validate('1000.1.2.3')
    assert not validate('1.1000.2.3')
    assert not validate('1.2.1000.3')
    assert not validate('1.2.3.1000')
    assert not validate('1000.1000.1000.1000')

    # work around bug #312
    assert not validate('999.1.2.3')
    assert not validate('1.999.2.3')
    assert not validate('1.2.999.3')
    assert not validate('1.2.3.999')
    assert not validate('999.999.999.999')


def test_padded_zero():
    assert not validate('001.168.1.1')
    assert not validate('192.001.1.1')
    assert not validate('192.168.001.1')
    assert not validate('192.168.1.001')
    assert not validate('001.002.003.004')
