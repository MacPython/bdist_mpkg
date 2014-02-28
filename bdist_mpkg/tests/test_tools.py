""" Test some tools
"""
from __future__ import with_statement

import os
from os.path import abspath, split as psplit, isfile, join as pjoin
from subprocess import check_call, Popen, PIPE

from ..tools import pax, unpax, ugrp_path, find_program, run_setup

from ..tmpdirs import InTemporaryDirectory

from nose import SkipTest
from nose.tools import assert_true, assert_equal

HERE, SELF = psplit(abspath(__file__))

def test_pax_unpax():
    with InTemporaryDirectory() as tmpdir:
        pax(HERE, tmpdir)
        pax_file = pjoin(tmpdir, 'Contents', 'Archive.pax.gz')
        assert_true(isfile(pax_file))
        os.mkdir('pax_contents')
        unpax(pax_file, 'pax_contents')
        assert_equal(set(os.listdir('pax_contents')),
                     set(os.listdir(HERE)))


def test_user_group():
    with InTemporaryDirectory() as tmpdir:
        open('test_file', 'wt').write('hello')
        assert_equal(ugrp_path(tmpdir), ugrp_path('test_file'))


def test_find_program():
    # Test utility to find programs on the path
    try:
        check_call(['which', 'which'])
    except OSError:
        raise SkipTest('Cannot find `which` on system')
    proc = Popen(['which', 'which'], stdout=PIPE, stderr=PIPE)
    out, err = proc.communicate()
    assert_equal(out.strip(), find_program('which'))
    assert_equal(find_program('no-reasonable-likelihood'), None)
    assert_equal(find_program('no-reasonable-likelihood', 'foo'), 'foo')


setup1 = """
from distutils.core import setup

setup(name = 'myname')
"""

setup2 = """
from distutils.core import setup

if __name__ == '__main__':
    setup(name = 'myname')
"""

setup2 = """# Setup called in ifmain block
from distutils.core import setup

if __name__ == '__main__':
    setup(name = 'myname')
"""

setup3 = """# Functions using custom classes
from distutils.core import setup

class MyClass(object):
    pass

def get_name():
    c = MyClass()
    return 'myname'

setup(name = get_name())
"""

def test_run_setup():
    # Test run_setup function
    # Test fixes for cases in http://bugs.python.org/issue18970
    for fname, contents in (('setup1.py', setup1),
                            ('setup2.py', setup2),
                            ('setup3.py', setup3)):
        with InTemporaryDirectory():
            with open(fname, 'wt') as fobj:
                fobj.write(contents)
            res = run_setup(fname)
            assert_equal(res.get_name(), 'myname')
