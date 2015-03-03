"""
Tests for Fadapa.
"""

import sys
import unittest
try:
    from StringIO import StringIO
except:
    from io import StringIO


from fadapa import Fadapa


class TestFadapa(unittest.TestCase):

    def setUp(self):
        self.p_data = Fadapa('tests/fastqc_data.txt')
        self.z_data = Fadapa('tests/fastqc.zip')

    def test_summary(self):
        summary = self.p_data.summary()
        self.assertEqual(summary[0], ['Module Name', 'Status'])
        self.assertEqual(self.p_data.summary(), self.z_data.summary())

    def test_content(self):
        sys.stdout = StringIO()
        self.p_data.content()
        self.assertEqual(sys.stdout.getvalue()[:8], '##FastQC')

    def test_raw_data(self):
        data = self.p_data.raw_data('Basic Statistics')
        self.assertEqual(data[-1], '>>END_MODULE')

    def test_cleaned_data(self):
        data = self.p_data.clean_data('Basic Statistics')
        self.assertEqual(data[0][0], 'Measure')

