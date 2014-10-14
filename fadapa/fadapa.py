""" 
Python module to parse FastQC output data.
"""

from __future__ import print_function


class Parser(object):
    """
    Returns a parsed data object for given fastqc data file

    :arg file_name: name of fastqc_data text file
    :type file_name: str
    """
    def __init__(self, file_name, **kwargs):
        self.file_name = file_name
        self._content = open(file_name, **kwargs).read().splitlines()
        
    def summary(self):
        """
        Returns a list of all modules present in the content.
        Module begins  with  '>>Module Name',  ends with '>>END_MODULE'
        """
        data = []
        m_mark = '>>'
        m_end = '>>END_MODULE'
        for line in self._content:
            if m_mark in line and not m_end in line:
               module_name, status = line.split('\t')
               data.append([status, module_name[2:]])
        data.insert(0, ['STATUS', 'Module Name'])
        return data

    def content(self):
        """
        Print the contents of the given file.
        """
        for line in self._content:
            print(line)
            
    def raw_data(self, module):
        """
        Returns raw data lines for a given module name.

        :arg module: name of module as returned by _moduels function.
        :type module: str
        """
        stop_mark = '>>END_MODULE'
        con = self._content
        s_pos = next(con.index(x) for x in con if module in x)
        e_pos = con[s_pos:].index(stop_mark)
        raw_data = con[s_pos:s_pos+e_pos+1]
        return raw_data

    def clean_data(self, module):
        """
        Returns a list of data for the given module.

        :arg module: name of module
        :type module: str
        """
        filtered_data = self.raw_data(module)[1:-1]
        data_list = [filter(None, x.split('\t')) for x in filtered_data]
        return data_list
