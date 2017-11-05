import os
import sys
import configparser
import settings_dialog

import PyQt5
from PyQt5 import QtGui

from PyQt5.QtGui import QFont

"""
 Settings with global variables
"""

pathsOfDocuments = []
listPaths = []
selectedRecipe = ""
loadedRecipe = ""
defaultRecipe = ""
zipsFolder = ""
tempFolder = ""
localPath = ""
sets = ""
font = ""



def getValue(form_field):
    value = form_field
    print("GET defalut Value: ", value)
    return value

def getDefaultRecipe(form_field): # settings_dialog.settings_ui.combo_box_1.currentText()
    defaultRecipe = form_field
    print(defaultRecipe)
    return defaultRecipe

"""
def getDefaultFontName():
    return defaultFontName


def getDefaultFontSize():
    return defaultFontSize


def getDefaultOutputName():
    return defaultOutputName
    """

"""
def buildConfiguration():
    confWriter = configparser.ConfigParser()
    recipe = str(getValue(settings_dialog.settings_ui.combo_box_1.currentText()))
    size = int(getValue(settings_dialog.settings_ui.spin_box_1.currentText()))

    recipe = str(getValue(settings_dialog.settings_ui.combo_box_1.currentText()))
    size = int(getValue(settings_dialog.settings_ui.spin_box_1.value()))
    font = size = int(getValue(settings_dialog.settings_ui.spin_box_1.currentText()))

    size = getDefaultValue()
    font = getDefaultFontName()
    outputName = getDefaultOutputName()
    confWriter['user'] = {
        'default-recipe': recipe,
        'font-name': font,
        'font-size': size,
        'default-book-name': outputName
    }
    return confWriter
"""

def saveConfiguration(defaultRecipe, fontName, fontSize, bookName):
        config = configparser.ConfigParser()
        config['user'] = {'default-recipe': str(defaultRecipe),
                          'font-name': str(fontName),
                          'font-size': int(fontSize),
                          'default-book-name': str(bookName)}
        with open('configuration.ini', 'w') as configfile:
            config.write(configfile)


def loadConfiguration(configfile='configuration.ini'):
    confReader = configparser.ConfigParser()
    confReader.read(configfile)
    return confReader


def prepareGlobalVariables():
    global localPath
    localPath = os.path.dirname(__file__)
    global sets
    sets = loadConfiguration()
    global pathsOfDocuments
    pathsOfDocuments = []
    global zipsFolder
    zipsFolder = "/zips/"
    global tempFolder
    tempFolder = "/temp/"
    global listPaths
    listPaths = []
    global selectedRecipe
    selectedRecipe = str(localPath + zipsFolder
                         + sets['user']['default-recipe'])
    global defaultRecipe
    defaultRecipe = str(sets['user']['default-recipe'])
    global font
    font = QFont(sets['user']['font-name'],
                 int(sets['user']['font-size']))


prepareGlobalVariables()
sets = configparser.ConfigParser()
sets = loadConfiguration()
