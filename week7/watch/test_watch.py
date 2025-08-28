from watch import parse


def test_valid():
    assert 'https://youtu.be/xvFZjo5PgG0' == parse('<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')


def test_valid1():
    assert 'https://youtu.be/xvFZjo5PgG0' == parse('<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>')


def test_valid2():
    assert 'https://youtu.be/xvFZjo5PgG0' == parse('<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')


def test_missing_src():
    assert parse('<iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>') is None


def test_missing_typo():
    assert parse('<iframe src="https://www.youtube?com/embed/xvFZjo5PgG0"></iframe>') is None
