Welcome to Fadapa
-----------------

FAstqc DAta PArser - The Easiest way to parse FastQC results.

 |Status| |Build| |Coverage| |Latest Version| |Supported Python versions|

Installation
------------
1. Recomended way to install is using ``pip``
::

    pip install fadapa

2. Alternatively you can install with ``esay_install``
::

   easy_install fadapa

3. You can also install from Github source code.
::

   cd 
   git clone https://github.com/fadapa/fadapa.git 
   cd fadapa
   python setup.py install

Usage
-----

::

    # import fadapa
    from fadapa import Fadapa

    #load file
    f = Fadapa('/path/to/fastqc_output_file.txt')

    #get file name
    print(f.file_name)

    #get entire content
    print(f.content())

    #get all module names and their status
    print(f.summary())

    #get raw data of any module
    print(f.raw_module('module name'))

    #get cleaned data of any module
    print(f.clean_data('module name'))

Author
------

`Anand Reddy Pandikunta`_

.. _Anand Reddy Pandikunta: http://www.avilpage.com

.. |Status| image:: https://pypip.in/status/fadapa/badge.svg
    :target: https://pypi.python.org/pypi/fadapa/
.. |Build| image:: https://api.travis-ci.org/fadapa/fadapa.png?branch=master
   :target: http://travis-ci.org/fadapa/fadapa/
.. |Coverage| image:: https://coveralls.io/repos/fadapa/fadapa/badge.png?branch=master
   :target: https://coveralls.io/r/fadapa/fadapa?branch=master
.. |Latest Version| image:: https://pypip.in/version/fadapa/badge.svg?text=version
   :target: https://pypi.python.org/pypi/fadapa/
.. |Supported Python versions| image:: https://pypip.in/py_versions/fadapa/badge.svg
   :target: https://pypi.python.org/pypi/fadapa/
