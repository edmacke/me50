import faces.faces as faces
import indoor.indoor as indoor
import playback.playback as playback


def test_indoor1():
    assert 'hello' == indoor.fix_msg('HELLO')


def test_indoor2():
    assert 'this is cs50' == indoor.fix_msg('THIS IS CS50')


def test_indoor3():
    assert '50' == indoor.fix_msg('50')


def test_playback1():
    assert 'This...is...CS50' == playback.fix_msg('This is CS50')


def test_playback2():
    assert 'This...is...our...week...on...functions' == playback.fix_msg('This is our week on functions')


def test_playback3():
    assert "Let's...implement...a...function...called...hello" == playback.fix_msg("Let's implement a function called hello")


def test_smile1():
    assert 'Hello 🙂' == faces.fix_msg('Hello :)')


def test_smile2():
    assert 'Goodbye 🙁' == faces.fix_msg('Goodbye :(')


def test_smile3():
    assert 'Hello 🙂 Goodbye 🙁' == faces.fix_msg('Hello :) Goodbye :(')
