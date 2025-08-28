from response import valid

def test_valid():
    assert valid('malan@harvard.edu')
    assert valid('ed.macke@lfg.com')

def test_not_valid():
    assert not valid('ed.macke')
    assert not valid('ed.macke@')
    assert not valid('@lfg.com')
    assert not valid('lfg.com')
    assert not valid('malan@@harvard.edu')
    assert not valid('ed.macke@lfg..com')