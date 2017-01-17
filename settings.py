import configparser

def saveConf():
    config = configparser.ConfigParser()
    config['DEFAULT'] = {'DeflautZips': '', 'BookName': 'book'}

    with open('conf.ini', 'w') as configfile:
        config.write(configfile)


def loadConf():

    with open('conf.ini', 'r') as configfile:
        config.read(configfile)

    config = configparser.ConfigParser()
    config['DEFAULT'] = {'SavedZips': '', 'BookName': 'book'}


