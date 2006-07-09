import sys
import distutils.command
from bdist_mpkg import cmd_bdist_mpkg
distutils.command.__all__.append('bdist_mpkg')
sys.modules['distutils.command.bdist_mpkg'] = cmd_bdist_mpkg
setattr(distutils.command, 'bdist_mpkg', cmd_bdist_mpkg)
