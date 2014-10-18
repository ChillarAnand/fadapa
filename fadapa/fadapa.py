""" 
Python module to parse FastQC output data.
"""


from __future__ import print_function


class Fadapa(object):
    """
    Returns a parsed data object for given fastqc data file

    :arg file_name: name of fastqc_data text file
    :type file_name: str
    """
    def __init__(self, file_name, **kwargs):
        self.file_name = file_name
        self._content = open(file_name, **kwargs).read().splitlines()
        self._m_mark = '>>'
        self._m_end = '>>END_MODULE'
        
    def summary(self):
        """
        Returns a list of all modules present in the content.
        Module begins  with  '>>Module Name',  ends with '>>END_MODULE'
        """
        try:
            data = []
            for line in self._content:
                if self._m_mark in line and not self._m_end in line:
                    module_name, status = line.split('\t')
                    data.append([status, module_name[2:]])
            data.insert(0, ['Status', 'Module Name'])
            return data
        except:
            raise "It is not a valid FastQC file. \
                   Please specify a correct file."

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
        try:
            con = self._content
            s_pos = next(con.index(x) for x in con if module in x)
            e_pos = con[s_pos:].index(self._m_end)
            raw_data = con[s_pos:s_pos+e_pos+1]
            return raw_data
        except:
            raise "Please specify correct module name as mentioned \
                    in summary method."

    def clean_data(self, module):
        """
        Returns a list of data for the given module.

        :arg module: name of module
        :type module: str
        """
        try:
            filtered_data = self.raw_data(module)[1:-1]
            data_list = [filter(None, x.split('\t'))  \
                         for x in filtered_data]
            data_list[0][0] = data_list[0][0][1:] 
            return data_list
        except:
            raise "Please specify correct module name as mentioned \
                   in summary method."
