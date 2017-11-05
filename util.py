import os

def dirExists(name):
    isFolderExist = (os.path.isdir(name))
    return isFolderExist


def createDir(name):
    try:
        os.mkdir(name)
    except FileExistsError as error:
        print("Directory \"" + name + "\" exist")
        return True
    print("Create \"" + name + "\" directory")