# Welcome to Fadapa
The Easiest way to parse FastQC results.

# Installation

    pip install fadapa

# Usage
  
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
