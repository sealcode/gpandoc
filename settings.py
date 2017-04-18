import configparser
"""

"""
font=""

def getDefaultRecipe():
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
    size =  getDefaultFontSize()
    font =  getDefaultFontName()
    outputName = getDefaultOutputName()
    confWriter['user'] = {
        'default-recipe': recip,
        'font-name': font,
        'font-size': size,
        'default-book-name': outputName
    }
    return confWriter

def saveConfiguration(configfile = 'configuration.ini'):
    #confWriter = configparser.ConfigParser()
    confWriter = buildConfiguration()
    with open('configuration.ini', 'w') as sets:
        confWriter.write(sets)

def loadConfiguration(configfile='configuration.ini'):
    confReader = configparser.ConfigParser()
    loadConf=confReader.read(configfile)
    return loadConf

currentConfiguration = loadConfiguration()
