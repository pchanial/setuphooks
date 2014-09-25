#!/usr/bin/env python
from numpy.distutils.core import setup

# we use the module test_hooks (not in git) instead of hooks (in git)
# to make it possible to change HEAD and still be able to run the command
# 'python setup.py --version' with the same module
from test_hooks import get_cmdclass, get_version

VERSION = '0.1'
name = 'setuphooks'

setup(name=name,
      version=get_version(name, VERSION),
      author='Pierre Chanial',
      author_email='pierre.chanial@gmail.com',
      packages=[name],
      cmdclass=get_cmdclass())
