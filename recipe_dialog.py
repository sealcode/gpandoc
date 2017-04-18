#!/usr/bin/python3
# -*- coding: utf-8 -*-

import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QDialog

import recipe
from ui import recipe_ui

class RecipeDialog(QtWidgets.QDialog, recipe_ui.Ui_Dialog):
    def __init__(self,app,selectedRecipe,zipsFolder):
        super(RecipeDialog, self).__init__()
        recipe_ui.Ui_Dialog.setupUi(self, self)

        self.zipPackages =[]
        self.loadedRecipe = selectedRecipe
        self.path = os.path.dirname(__file__)
        self.label_1.setScaledContents(True);

        self.zipPackages  = [os.path.basename(x) for x in glob.glob(self.path+zipsFolder+'*.zip')]

        self.combo_box_1.addItems(self.zipPackages)
        self.combo_box_1.currentIndexChanged[str].connect(self.changeRecipe)
        self.button_box_1.accepted.connect(self.accept)
        self.button_box_1.rejected.connect(self.reject)
        global sets
        self.setFont(QFont(sets['user']['font-name'],int(sets['user']['font-size'])))
        self.showPreviewOfRecipe()

    def accept(self):
        self.loadedRecipe = str(self.path+ zipsFolder+ str(self.combo_box_1.currentText()))
        print("Current loaded recipe: "+ self.loadedRecipe)   # for debugging
        self.retRecipe()
        super(RecipeDialog, self).accept()

    def reject(self):
        super(RecipeDialog, self).reject()

    def retRecipe(self):
        return (self.loadedRecipe)

    def setRecipe(self):
        self.ui.combo_box_1.setCurrentText(str(self.loadedRecipe))

    def showPreviewOfRecipe(self):
        zippedImgs = ZipFile(self.path+zipsFolder+str(self.combo_box_1.currentText()))

        self.label_2.setText("Brak podglądu")
        self.label_2.setScaledContents(True)

        for file_in_zip in zippedImgs.namelist():
            if ("preview" in file_in_zip):
                print ("Found image: ", file_in_zip, " -- ")  # for debugging
                data = zippedImgs.read(file_in_zip)       # read bits to variable
                dataEnc = io.BytesIO(data)                # save bytes like io
                dataImgEnc = Image.open(dataEnc)          # convert bytes on Image file
                qimage = ImageQt.ImageQt(dataImgEnc)      # create QtImage from Image
                pixmap = QtGui.QPixmap.fromImage(qimage)  # convert QtImage to QPixmap
                print(pixmap)     # for debugging

                self.label_2.setPixmap(pixmap)

    def changeRecipe(self):
        print(self.combo_box_1.currentText())
        self.showPreviewOfRecipe()
