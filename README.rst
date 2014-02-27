==========
bdist_mpkg
==========

bdist_mpkg is a distutils plugin that implements the ``bdist_mpkg`` command.
The command builds a Mac OS X metapackage for use by Installer.app for easy GUI
installation of Python modules, much like ``bdist_wininst``.

It also comes with a ``bdist_mpkg`` script, which is a setup.py front-end that
will allow you to easy build an installer metapackage from nearly any existing
package that uses distutils.

Please email the `Python-Mag SIG mailing list
<http://www.python.org/community/sigs/current/pythonmac-sig/>`_ with questions,
and let us know of bugs via `github issues
<https://github.com/MacPython/bdist_mpkg/issues>`_

Code
====

The code started life at:

http://undefined.org/python/#bdist_mpkg

Bob Ippolito wrote most of the code.

The `current repository`_ is on Github.

.. _current repository: http://github.com/MacPython/bdist_mpkg

Install
=======

Via pip::

    pip install bdist_mpkg

From source::

    python setup.py install

Usage
=====

From your projects base directory (containing ``setup.py``)::

    python setup.py bdist_mpkg

You can also run directly via the command line::

    bdist_mpkg setup.py

This will run the built installer by default.

Try ``python setup.py --help bdist_mpkg`` for some options.

License
=======

MIT license.  See the ``LICENSE`` file in the source archive.

Compatibility
=============

The code should be compatible with Pythons 2.5 through 3.3
