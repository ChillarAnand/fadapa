#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import find_packages, setup
import fadapa.release as rl

setup(name='fadapa',
      version=rl.VERSION,
      description=rl.DESCRIPTION,
      long_description=rl.LONG_DESCRIPTION,
      author=rl.AUTHOR,
      author_email=rl.EMAIL,
      maintainer='Anand Reddy Pandikunta',
      maintainer_email='anand21nanda@gmail.com',
      license=rl.LICENSE,
      url=rl.URL,
      classifiers=[
          'Development Status :: 4 - Beta',
          
          'Topic :: Software Development :: Libraries',
          'License :: OSI Approved :: MIT License',
          'Topic :: Scientific/Engineering :: Bio-Informatics',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.2'
          ],
      packages=find_packages(),
      data_files=[],
)

