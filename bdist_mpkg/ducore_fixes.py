"""
As github user Vickor pointed out --
https://github.com/MacPython/bdist_mpkg/issues/1 -- bdist_mpkg calls
``run_setup`` from ``distutils.core`` - but this doesn't give the expected
result in some cases: http://bugs.python.org/issue18970

In this module:

* Copy ``run_setup`` functon from ``distutils.core``
* Add patch from the bug report above
* Modify to deal with ``distutils.core`` global variables
"""

import sys
import distutils.core as dic
from distutils.core import setup


def run_setup (script_name, script_args=None, stop_after="run"):
    """Run a setup script in a somewhat controlled environment, and
    return the Distribution instance that drives things.  This is useful
    if you need to find out the distribution meta-data (passed as
    keyword args from 'script' to 'setup()', or the contents of the
    config files or command-line.

    'script_name' is a file that will be read and run with 'exec()';
    'sys.argv[0]' will be replaced with 'script' for the duration of the
    call.  'script_args' is a list of strings; if supplied,
    'sys.argv[1:]' will be replaced by 'script_args' for the duration of
    the call.

    'stop_after' tells 'setup()' when to stop processing; possible
    values:
      init
        stop after the Distribution instance has been created and
        populated with the keyword arguments to 'setup()'
      config
        stop after config files have been parsed (and their data
        stored in the Distribution instance)
      commandline
        stop after the command-line ('sys.argv[1:]' or 'script_args')
        have been parsed (and the data stored in the Distribution)
      run [default]
        stop after all commands have been run (the same as if 'setup()'
        had been called in the usual way

    Returns the Distribution instance, which provides all information
    used to drive the Distutils.
    """
    if stop_after not in ('init', 'config', 'commandline', 'run'):
        raise ValueError("invalid value for 'stop_after': %r" % (stop_after,))

    dic._setup_stop_after = stop_after

    save_argv = sys.argv
    g = {'__file__': script_name, '__name__': '__main__'}
    try:
        try:
            sys.argv[0] = script_name
            if script_args is not None:
                sys.argv[1:] = script_args
            with open(script_name, 'rb') as f:
                exec(f.read(), g)
        finally:
            sys.argv = save_argv
            dic._setup_stop_after = None
    except SystemExit:
        # Hmm, should we do something if exiting with a non-zero code
        # (ie. error)?
        pass
    except:
        raise

    if dic._setup_distribution is None:
        raise RuntimeError(("'distutils.core.setup()' was never called -- "
               "perhaps '%s' is not a Distutils setup script?") % \
              script_name)

    # I wonder if the setup script's namespace -- g -- would be of
    # any interest to callers?
    #print "_setup_distribution:", _setup_distribution
    return dic._setup_distribution
