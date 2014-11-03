# -*- encoding: utf-8 -*-

import sys
import unittest

from fadapa import Fadapa


class TestFadapa(unittest.TestCase):

    def setUp(self):
        self.p_data = Fadapa('fastqc_data.txt')

    def test_summary(self):
        summary = self.p_data.summary()
        self.assertEqual(summary[0], ['Status', 'Module Name'])

    def test_content(self):
        self.p_data.content()
        self.assertEqual(sys.stdout.getvalue()[:8],'##FastQC')

    def test_raw_data(self):
        data = self.p_data.raw_data('Basic Statistics')
        self.assertEqual(data[-1], '>>END_MODULE')

    def test_cleaned_data(self):
        data = self.p_data.clean_data('Basic Statistics')
        self.assertEqual(data[0][0], 'Measure')



