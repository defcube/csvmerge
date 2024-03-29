#!/usr/bin/env python
from distutils.core import setup
import os
try:
    readme = open(os.path.dirname(os.path.realpath(__file__)) +\
            '/README.rst').read()
except IOError:
    readme = ""
setup(
    name='csvmerge',
    version='1.0.9',
    author_email='gattster@gmail.com',
    author='Philip Gatt',
    py_modules=['csvmergeutil'],
    scripts=['csvmerge'],
    description="Merges multiple csv files into a single file",
    long_description=readme,
    url='http://github.com/defcube/csvmerge')
