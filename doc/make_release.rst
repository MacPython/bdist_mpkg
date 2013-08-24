################
Making a release
################

* Review the open list of `bdist_mpkg issues
  <https://github.com/matthew-brett/bdist_mpkg/issues>`_.  Check whether there
  are outstanding issues that can be closed, and whether there are any issues
  that should delay the release.  Label them !

* Review and update the :file:`Changelog` file.  Get a partial list of
  contributors with something like::

      git shortlog -n v0.5.0..

  where ``v0.5.0`` was the last release tag name.

  Then manually go over ``git shortlog v0.5.0..`` to make sure the release notes
  are as complete as possible and that every contributor was recognized.

* Consider any updates to the ``AUTHOR`` file.

* Update the date in the ``LICENSE`` file.

* Use the opportunity to update the ``.mailmap`` file if there are any duplicate
  authors listed from ``git shortlog -nse``.

* Check the ``long_description`` in ``bdist_mpkg/info.py``.  Check it matches
  the ``README`` in the root directory.  Check the output of::

    rst2html.py README.rst > ~/tmp/readme.html

  because this will be the output used by pypi_

* Clean::

    git clean -fxd

* Make sure the tests pass (from the ``bdist_mpkg`` root directory; you need
  administrator account permissions)::

    nosetests bdist_mpkg

* Check everything compiles without syntax errors::

    python -m compileall .

* Edit :file:`bdist_mpkg/info.py` to set ``_version_extra`` to ``''``; commit.
  Then::

    python -m compileall .
    git clean -fxd
    python setup.py sdist --formats=gztar,zip

* Check this installs and tests correctly with something like::

    virtualenv venv
    cd venv
    . bin/activate
    tar zxvf ../dist/bdist_mpkg-0.4.5dev.tar.gz
    cd bdist_mpkg-0.4.5dev/
    python setup.py install
    nosetests bdist_mpkg
    cd ../..
    rm -rf venv
    git clean -fxd

* Once everything looks good, you are ready to upload the source release to
  PyPi.  See `setuptools intro`_.  Make sure you have a file ``\$HOME/.pypirc``,
  of form::

    [distutils]
    index-servers =
        pypi

    [pypi]
    username:your.pypi.username
    password:your-password

    [server-login]
    username:your.pypi.username
    password:your-password

* When ready::

    python setup.py register
    python setup.py sdist --formats=gztar,zip upload

* Tag the release with tag of form ``v0.5.0``::

    git tag -am 'Second main release' v0.5.0

* Push the tag and any other changes to trunk with::

    git push --tags

* Set up maintenance / development branches

  If this is this is a full release you need to set up two branches, one for
  further substantial development (often called 'trunk') and another for
  maintenance releases.

  * Branch to maintenance::

      git co -b maint/0.5.x

    Set ``_version_extra`` back to ``.dev`` and bump ``_version_micro`` by 1.
    Thus the maintenance series will have version numbers like - say -
    '0.5.1.dev' until the next maintenance release - say '0.5.1'.  Commit. Don't
    forget to push upstream with something like::

      git push upstream maint/0.5.x --set-upstream

  * Start next development series::

      git co main-master

    then restore ``.dev`` to ``_version_extra``, and bump ``_version_minor`` by
    1.

    Thus the development series ('trunk') will have a version number here of
    '0.6.0.dev' and the next full release will be '0.6.0'.

    Next merge the maintenance branch with the "ours" strategy.  This just
    labels the maintenance `info.py` edits as seen but discarded, so we can
    merge from maintenance in future without getting spurious merge conflicts::

       git merge -s ours maint/0.5.x

  If this is just a maintenance release from ``maint/0.5.x`` or similar, just
  tag and set the version number to - say - ``0.5.2.dev``.

* Push the main branch::

    git push main-master

* Announce to the mailing lists.
