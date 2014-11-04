#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

import fadapa.release as rl


with open('README.rst') as fh:
    long_description = fh.read()
    
setup(name='fadapa',
      version=rl.VERSION,
      description=rl.DESCRIPTION,
      long_description=long_description,
      keywords = 'bioinformatics fastqc parsing',
      author=rl.AUTHOR,
      author_email=rl.EMAIL,
      maintainer='Anand Reddy Pandikunta',
      maintainer_email='anand21nanda@gmail.com',
      url=rl.URL,
      packages=find_packages(),
      data_files=[],
      test_suite = 'discover_tests',
      classifiers=[
          'Development Status :: 5 - Production/Stable', 
          
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: OS Independent',
          'Operating System :: POSIX',
          
          'Programming Language :: Python', 
          'Programming Language :: Python :: 2.7', 
          'Programming Language :: Python :: 3', 
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',

          'Topic :: Scientific/Engineering :: Bio-Informatics',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Utilities'
          ],
)
