""" This file contains defines parameters for bdist_mpkg that we use to fill
settings in setup.py, the bdist_mpkg top-level docstring, and for building the
docs.  In setup.py in particular, we exec this file, so it cannot import
bdist_mpkg """

# bdist_mpkg version information.  An empty _version_extra corresponds to a
# full release.  '.dev' as a _version_extra string means this is a development
# version
_version_major = 0
_version_minor = 4
_version_micro = 5
_version_extra = 'dev'
#_version_extra = ''

# Format expected by setup.py and doc/source/conf.py: string of form "X.Y.Z"
__version__ = "%s.%s.%s%s" % (_version_major,
                              _version_minor,
                              _version_micro,
                              _version_extra)

DESCRIPTION = "Builds Mac OS X installer packages from distutils"
LONG_DESCRIPTION = """
bdist_mpkg is a distutils plugin that implements the bdist_mpkg command, which
builds a Mac OS X metapackage for use by Installer.app for easy GUI installation
of Python modules, much like bdist_wininst.

It also comes with a bdist_mpkg script, which is a setup.py front-end that will
allow you to easy build an installer metapackage from nearly any existing
package that uses distutils.
"""

CLASSIFIERS = filter(None, map(str.strip,
"""
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Programming Language :: Python
Operating System :: MacOS :: MacOS X
Topic :: Software Development :: Libraries :: Python Modules
Topic :: Software Development :: Build Tools
""".splitlines()))
