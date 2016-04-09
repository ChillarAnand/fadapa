Welcome to Fadapa
-----------------

FAstqc DAta PArser - The Easiest way to parse FastQC results.

|Build| |Coverage|


Demo
----
Check out this `iPython Notebook <http://nbviewer.ipython.org/github/fadapa/fadapa/blob/master/demo/Parsing%20FastQC%20Output%20Data%20With%20Fadapa!.ipynb/>`_ for demo.


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
    print(f.raw_data('module name'))

    #get cleaned data of any module
    print(f.clean_data('module name'))


.. |Build| image:: https://api.travis-ci.org/fadapa/fadapa.png?branch=master
   :target: http://travis-ci.org/fadapa/fadapa/
.. |Coverage| image:: https://coveralls.io/repos/fadapa/fadapa/badge.png?branch=master
   :target: https://coveralls.io/r/fadapa/fadapa?branch=master
