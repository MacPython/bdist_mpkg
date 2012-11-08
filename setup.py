#!/usr/bin/env python

from setuptools import setup

import os

# Get version and release info, which is all stored in bdist_mpkg/info.py
ver_file = os.path.join('bdist_mpkg', 'info.py')
exec(open(ver_file).read())

setup(
    name="bdist_mpkg",
    version=__version__,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=CLASSIFIERS,
    author="Bob Ippolito",
    author_email="pythonmac-sig@python.org",
    url="http://undefined.org/python/#bdist_mpkg",
    license="MIT License",
    packages=['bdist_mpkg'],
    platforms=['any'],
    zip_safe=True,
    entry_points={
        'distutils.commands': [
            'bdist_mpkg = bdist_mpkg.cmd_bdist_mpkg:bdist_mpkg',
        ],
        'console_scripts': [
            'bdist_mpkg = bdist_mpkg.script_bdist_mpkg:main',
        ],
    },
)
