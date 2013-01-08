""" Extraordinarily crude run-oneself test

You'll need ``nose`` installed to run this.

Run all tests with ``nosetests bdist_mpkg`` from the root directory (containing
the ``setup.py`` file).
"""
from __future__ import with_statement

import sys
import os
from os.path import dirname, join as pjoin, isfile, isdir
from subprocess import check_call

from ..tmpdirs import TemporaryDirectory

from nose import SkipTest
from nose.tools import assert_true, assert_equal

MY_PATH = dirname(__file__)
MY_PYTHON = sys.executable

def test_myself():
    # Build myself into a temporary directory
    os.chdir(pjoin(MY_PATH, '..', '..'))
    if not isfile('setup.py'):
        raise SkipTest('Not running from development directory')
    with TemporaryDirectory() as tmpdir:
        cmd = '%s setup.py bdist_mpkg --dist-dir=%s' % (MY_PYTHON, tmpdir)
        check_call(cmd, shell=True)
        tmpls = os.listdir(tmpdir)
        assert_equal(len(tmpls), 1)
        assert_true(tmpls[0].endswith('.mpkg'))
        assert_true(isdir(pjoin(tmpdir, tmpls[0])))
        # Check zipping
        cmd += ' -z'
        check_call(cmd, shell=True)
        tmpls = sorted(os.listdir(tmpdir))
        assert_equal(len(tmpls), 2)
        assert_true(tmpls[0].endswith('.mpkg'))
        assert_true(tmpls[1].endswith('.zip'))
        assert_true(isfile(pjoin(tmpdir, tmpls[1])))
