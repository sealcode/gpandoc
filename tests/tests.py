import unittest
import os
import sys
from os.path import isfile

sys.path.append('..')
import converter

class TemplateTest(unittest.TestCase):
    def test_variables(self):
        IN_FILE = 'variables.md'
        OUT = 'value1 value2 value3\n'
        with open(IN_FILE) as test_file:
            IN = test_file.read()
        result = converter.convert(IN, 'markdown', 'markdown',
                                   variables={
                                       'var1': 'value1',
                                       'var2': 'value2',
                                       'var3': 'value3'
                                   }, extra_args=['--template=%s' % (IN_FILE),
                                                  '--standalone'])
        self.assertEqual(OUT, result)

    def test_variable_lists(self):
        IN_FILE = 'variable_lists.md'
        OUT = ['value1', 'value2', 'value3']
        with open(IN_FILE) as test_file:
            IN = test_file.read()
        result = converter.convert(IN, 'markdown', 'markdown',
                                   variables={
                                       'var1': ['value1', 'value2', 'value3']
                                   }, extra_args=['--template=%s' % (IN_FILE),
                                                  '--standalone'])
        OUT.sort()
        result = result.rstrip().split(',')
        result.sort()
        self.assertEqual(OUT, result)

    
if __name__ == '__main__':
    unittest.main()
