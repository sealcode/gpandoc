import os
import configparser
import settings_dialog

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


def isFolderExist(name):
    isFolderExist = (os.path.isdir(name))
    return isFolderExist


def crateFolderAboutName(name):
    try:
        os.mkdir(name)
    except FileExistsError as error:
        print("Directory \"" + name + "\" exist")
        return True
    print("Create \"" + name + "\" directory")


def getDefaultRecipe():
    defaultRecipe = settings_dialog.settings_ui.combo_box_1.currentText()
    print(defaultRecipe)
    return defaultRecipe


def getDefaultFontName():
    return defaultFontName


def getDefaultFontSize():
    return defaultFontSize


def getDefaultOutputName():
    return defaultOutputName


def buildConfiguration():
    confWriter = configparser.ConfigParser()

    recipe = getDefaultRecipe()
    size = getDefaultFontSize()
    font = getDefaultFontName()
    outputName = getDefaultOutputName()
    confWriter['user'] = {
        'default-recipe': recipe,
        'font-name': font,
        'font-size': size,
        'default-book-name': outputName
    }
    return confWriter


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
    global sets
    sets = confReader
    return confReader


def prepareGlobalVariables():
    global localPath
    localPath = os.path.dirname(__file__)

    global sets
    sets = configparser.ConfigParser()
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
