#!/usr/bin/env python

NAME = 'pydnstable'
VERSION = '0.2'

from distutils.core import setup
from distutils.extension import Extension

try:
    from Cython.Distutils import build_ext
    setup(
        name = NAME,
        version = VERSION,
        ext_modules = [ Extension('dnstable', ['dnstable.pyx'], libraries = ['dnstable']) ],
        cmdclass = {'build_ext': build_ext},
    )
except ImportError:
    setup(
        name = NAME,
        version = VERSION,
        ext_modules = [ Extension('dnstable', ['dnstable.c'], libraries = ['dnstable']) ],
    )
