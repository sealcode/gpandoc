import logging
import configparser
from zipfile import ZipFile


class Recipe(configparser.ConfigParser):
    '''Hold and interpret INI style configuration'''

    def __init__(self, in_file):
        self.log = logging.getLogger(self.__class__.__name__)
        super(Recipe, self).__init__()
        with ZipFile(in_file) as zip_recipe:
            with zip_recipe.open(in_file.split('.')[0] + '/recipe.ini') as ini:
                self.read_string(ini.read().decode('utf-8'))

    def __getattr__(self, name):
        '''Extract values from INI with simple accessors'''
        if name == 'lists':
            return [k for k,v in self['Variables'].items() if v == 'list']
        elif name == 'strings':
            return [k for k,v in self['Variables'].items() if v == 'string']
        elif name == 'texts':
            return [k for k,v in self['Variables'].items() if v == 'text']
        else:
            raise AttributeError("'%s' object has no attribute '%s'" %
                                 (self.__class__.__name__, name))