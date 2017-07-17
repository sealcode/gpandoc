#!/usr/bin/python3
# -*- coding: utf-8 -*-

import PyQt5
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets

from PyQt5.QtCore import QFile

from PyQt5.QtGui import QFont

from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QListWidget
from PyQt5.QtWidgets import QListWidgetItem

from ui import recipe_ui

import io
import os
from os import path

import sys
import glob
import zips
import recipe
import settings
import main_dialog

import zipfile
from zipfile import ZipFile

import subprocess
from subprocess import check_call

from PIL import Image
from PIL import ImageQt


settings.loadConfiguration()


class RecipeDialog(QtWidgets.QDialog, recipe_ui.Ui_Dialog):
    def __init__(self, app, selectedRecipe):
        super(RecipeDialog, self).__init__()
        recipe_ui.Ui_Dialog.setupUi(self, self)

        self.zipPackages = []
        self.loadedRecipe = selectedRecipe
        self.label_1.setScaledContents(True)

        self.zipPackages = [os.path.basename(x)
                            for x in glob.glob(settings.localPath
                            + settings.zipsFolder + '*.zip')]

        self.combo_box_1.addItems(self.zipPackages)
        self.combo_box_1.currentIndexChanged[str].connect(self.changeRecipe)
        self.button_box_1.accepted.connect(self.accept)
        self.button_box_1.rejected.connect(self.reject)
        self.setFont(QFont(settings.sets['user']['font-name'],
                     int(settings.sets['user']['font-size'])))

        self.showPreviewOfRecipe()

    def accept(self):
        self.loadedRecipe = str(settings.localPath + settings.zipsFolder
                                + str(self.combo_box_1.currentText()))
        print("Current loaded recipe: " + self.loadedRecipe)   # for debugging
        super(RecipeDialog, self).accept()

    def reject(self):
        super(RecipeDialog, self).reject()

    def getRecipe(self):
        return self.loadedRecipe

    def setRecipe(self):
        self.ui.combo_box_1.setCurrentText(str(self.loadedRecipe))

    def showPreviewOfRecipe(self):
        self.path = os.path.dirname(__file__)
        print(self.path + settings.zipsFolder
              + str(self.combo_box_1.currentText()))

        zippedImgs = ZipFile(self.path + settings.zipsFolder
                             + str(self.combo_box_1.currentText()))

        self.label_2.setText("Brak podglądu")
        self.label_2.setScaledContents(True)

        for file_in_zip in zippedImgs.namelist():
            if ("preview" in file_in_zip):
                print("Found image: ", file_in_zip, " -- ")
                # for debugging
                data = zippedImgs.read(file_in_zip)
                # read bits to variable
                dataEnc = io.BytesIO(data)
                # save bytes like io
                dataImgEnc = Image.open(dataEnc)
                # convert bytes on Image file
                qimage = ImageQt.ImageQt(dataImgEnc)
                # create QtImage from Image
                pixmap = QtGui.QPixmap.fromImage(qimage)
                # convert QtImage to QPixmap
                print(pixmap)     # for debugging

                self.label_2.setPixmap(pixmap)

    def changeRecipe(self):
        print(self.combo_box_1.currentText())
        loadedRecipe = self.combo_box_1.currentText()
        self.showPreviewOfRecipe()
