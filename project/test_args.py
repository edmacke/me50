import sys

import pytest

from args import get_args


def test_no_args():
    with pytest.raises(SystemExit):
        get_args()

    with pytest.raises(SystemExit):
        sys.argv = ['test_args']
        get_args()


def test_valid_args_short():
    sys.argv = ['test_args', '-i', 'id', '-s', 'secret', '-u', 'userid']
    args = get_args()

    assert 'id' == args['id']
    assert 'secret' == args['secret']
    assert 'userid' == args['user']


def test_valid_args_long():
    sys.argv = ['test_args', '--id', 'id', '--secret', 'secret', '--user', 'userid']
    args = get_args()

    assert 'id' == args['id']
    assert 'secret' == args['secret']
    assert 'userid' == args['user']


def test_arg_missing_id():
    with pytest.raises(SystemExit):
        sys.argv = ['test_args', '--secret', 'secret', '--user', 'userid']
        get_args()


def test_arg_missing_secret():
    with pytest.raises(SystemExit):
        sys.argv = ['test_args', '--id', 'id', '--user', 'userid']
        get_args()


def test_arg_missing_user():
    with pytest.raises(SystemExit):
        sys.argv = ['test_args', '--id', 'id', '--secret', 'secret']
        get_args()
