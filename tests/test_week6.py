import os
import sys

import pytest

from week6.lines import lines
from week6.shirt import shirt


def test_no_args():
    sys.argv = [__name__]
    with pytest.raises(SystemExit):
        lines.main()


def test_too_many_args():
    sys.argv = [__name__, 'foo', 'bar']
    with pytest.raises(SystemExit):
        lines.main()


def test_not_python_file():
    sys.argv = [__name__, 'foo']
    with pytest.raises(SystemExit):
        lines.main()


def test_python_file_not_found():
    sys.argv = [__name__, 'not_found.py']

    with pytest.raises(SystemExit):
        lines.main()


def test_python_file_found():
    os.chdir('D:\\Documents\\Python\\me50\\week6\\lines')
    sys.argv = [__name__, 'sample.py']

    lines.main()


def test_loc():
    os.chdir('D:\\Documents\\Python\\me50\\week6\\lines')
    sys.argv = [__name__, 'sample.py']
    assert lines.get_count(sys.argv[1]) > 0


def test_shirt():
    os.chdir('D:\\Documents\\Python\\me50\\week6\\shirt')
    sys.argv = [__name__, 'before1.jpg', 'after1.jpg']

    shirt.main()
