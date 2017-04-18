#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
['] logic_ui2.py is a script joined
all functions and methods in one app

import all
"""
import io
import os
import sys
import glob
import shutil
import recipe
import zipfile
import pypandoc
import datetime
import configparser

import subprocess
from os import path
from zipfile import ZipFile
from subprocess import check_call
from PIL import Image, ImageQt


import widget_item
import table_widget
import about_dialog
import recipe_dialog
import settings_dialog
import variables_dialog
import instruction_dialog


def isFolderExist(name):
    isFolderExist = (os.path.isdir(name))
    return isFolderExist

def crateFolderAboutName(name):
    try:
        print("Create " + name + " dir")
        os.mkdir(name)
    except FileExistsError as error:
        print("Dir" + name + " exist yet")
        print(error)


crateFolderAboutName("temp")
crateFolderAboutName("outputs")

localPath = os.path.dirname(__file__)
zipsFolder="/zips/" #-- U.W.A.G.A
defaultRecipe=""
pathsOfDocuments=[]

def prepareGlobalVariables(localPath,):
    localPath= os.path.dirname(__file__)
    sets = configparser.ConfigParser()
    sets = settings.loadConf()
    zipsFolder="/zips/"
    defaultRecipe=""
    listPaths=[]
