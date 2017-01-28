import configparser
"""
 #LOAD SETTINGS
    sets = loadConf()
    sets['user']['default-recipe']
 #SAVE SETTINGS
default
"""
font=""
def saveConf(defaultRecipe,fontName,fontSize,bookName):
    config = configparser.ConfigParser()
    config['user'] = {'default-recipe': str(defaultRecipe),'font-name': str(fontName),'font-size': int(fontSize), 'default-book-name': str(bookName)}
    with open('configuration.ini', 'w') as configfile:
        config.write(configfile)

def loadConf():
    config = configparser.ConfigParser()
    config.read('configuration.ini')
    return config
