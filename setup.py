#!/usr/bin/env python

from distutils.core import setup

setup(name='vsmpy',
      version = '0.1',
      description = 'Bare bones Vector Space Model',
      author = 'Alexandre Trilla',
      author_email = 'alex@atrilla.net',
      license='MIT/X11',
      maintainer = 'Alexandre Trilla',
      maintainer_email = 'alex@atrilla.net',
      url='http://atrilla.net/',
      download_url = 'https://github.com/atrilla/vsmpy',
      packages=['vsmpy'],
      py_modules = ['vsmpy.vsm'],
     )
