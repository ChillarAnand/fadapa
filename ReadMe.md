## Welcome to Fadapa
FAstqc DAta PArser - The Easiest way to parse FastQC results.


## PyPI status:

[![Latest Version](https://pypip.in/version/fadapa/badge.svg?text=version)](https://pypi.python.org/pypi/fadapa/)
[![Downloads](https://pypip.in/download/fadapa/badge.svg)](https://pypi.python.org/pypi/fadapa/)
[![Supported Python versions](https://pypip.in/py_versions/fadapa/badge.svg)](https://pypi.python.org/pypi/fadapa/)
[![License](https://pypip.in/license/fadapa/badge.svg)](https://pypi.python.org/pypi/fadapa/)


## Installation

Recomended way to install is using `pip`
   

    pip install fadapa

Alternatively you can install `esay_install`


    easy_install fadapa
    
You can also install from Github source code.

    cd 
    git clone https://github.com/fadapa/fadapa.git
    cd fadapa
    python setup.py install
    
## Usage
  
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


## Author

[Anand Reddy Pandikunta](http://www.avilpage.com)

