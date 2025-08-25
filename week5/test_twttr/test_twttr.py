import twttr


def test_twitter1_vowels():
    assert 'Twttr' == twttr.shorten('Twitter')


def test_twitter2_punctuation():
    assert "Wht's yr nm?" == twttr.shorten("What's your name?")


def test_twitter_all_caps():
    assert 'CS50' == twttr.shorten('CS50')


def test_twitter_capitals():
    assert 'TWTTR' == twttr.shorten('TWITTER')
