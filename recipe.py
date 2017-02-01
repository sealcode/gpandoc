import logging
import configparser
#import numpy as np
from zipfile import ZipFile
from PIL import Image


class Recipe(configparser.ConfigParser):
    '''Hold and interpret INI style configuration'''

    def __init__(self, in_file):
        self.log = logging.getLogger(self.__class__.__name__)
        super(Recipe, self).__init__()
        with ZipFile(in_file) as zip_recipe:
            with zip_recipe.open('recipe.ini') as ini:
                self.read_string(ini.read().decode('utf-8'))  
       
    
    def __getattr__(self, name):
        '''Extract values from INI with simple accessors'''
        if name == 'list':
            return [k for k,v in self['Variables'].items() if v == 'list']
        elif name == 'string':
            return [k for k,v in self['Variables'].items() if v == 'string']
        elif name == 'text':
            return [k for k,v in self['Variables'].items() if v == 'text']
        elif name == 'image':
            return [k for k,v in self['Document'].items() if v == 'image']
        elif name == 'outputFormat':
            return [k for k,v in self['Document'].items() if v == 'output_format']
        elif name == 'template':
            return [k for k,v in self['Document'].items() if v == 'template']
        else:
            raise AttributeError("'%s' object has no attribute '%s'" %
                                 (self.__class__.__name__, name))
    
         
