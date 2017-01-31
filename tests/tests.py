import unittest
import os
import sys
from os.path import isfile

sys.path.append('..')

class TemplateTest(unittest.TestCase):
    '''Test Pandoc templates'''

    import converter

    def test_variables(self):
        IN_FILE = 'variables.md'
        OUT = 'value1 value2 value3\n'
        with open(IN_FILE) as test_file:
            IN = test_file.read()
        result = self.converter.convert(IN, 'markdown', 'markdown',
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
        result = self.converter.convert(IN, 'markdown', 'markdown',
                                        variables={
                                            'var1': ['value1', 'value2', 'value3']
                                        }, extra_args=['--template=%s' % (IN_FILE),
                                                       '--standalone'])
        OUT.sort()
        result = result.rstrip().split(',')
        result.sort()
        self.assertEqual(OUT, result)

class RecipeTest(unittest.TestCase):
    '''Test recipe interpratating'''

    import recipe

    def setUp(self):
        self.in_recipe = self.recipe.Recipe('recipe.zip')

    def test_parser(self):
        self.assertEqual(self.in_recipe['Document']['type'], 'poetry')

    def test_lists(self):
        self.assertEqual(self.in_recipe.lists, ['authors'])

    def test_strings(self):
        self.assertEqual(self.in_recipe.strings, ['title'])
    
    def test_texts(self):
        self.assertEqual(self.in_recipe.texts, ['preamble'])

    
if __name__ == '__main__':
    unittest.main()
