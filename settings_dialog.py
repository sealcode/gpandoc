#!/usr/bin/python3
# -*- coding: utf-8 -*-

import io
import os
import sys
import glob
import shutil
import recipe
import zipfile
import pypandoc
import datetime
import subprocess
import configparser


from os import path
from zipfile import ZipFile
from subprocess import check_call
from PIL import Image, ImageQt


import PyQt5
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore

from PyQt5.QtCore import QRegExp

from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QDialogButtonBox


from PyQt5.QtGui import QFont
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtGui import QRegExpValidator

import settings
from ui import settings_ui


# Settings Dialog
class SettingsDialog(QtWidgets.QDialog, settings_ui.Ui_Dialog):
    def __init__(self, loadedRecipe):
        super(SettingsDialog, self).__init__()
        self.dialog = QtWidgets.QDialog()
        settings_ui.Ui_Dialog.setupUi(self, self)
        self.dialog.ui = settings_ui.Ui_Dialog()
        self.dialog.ui.setupUi(self.dialog)
        self.spin_box_1.valueChanged.connect(self.setFontOnDialog)
        self.font_box_1.currentFontChanged.connect(self.setFontOnDialog)
        self.buttonBox.button(QDialogButtonBox.Apply).clicked.connect(
            self.accept)
        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(
            self.reject)
        QFontDatabase().Latin
        global defaultRecipe
        global path
        global zips

        path = os.path.dirname(__file__)
        self.zipPackages = [os.path.basename(x) for x in glob.glob(
            path + '/zips/' + '*.zip')]
        self.combo_box_1.addItems(self.zipPackages)

        # print(sets.sections()) # for debugging
        sets = settings.loadConfiguration()
        self.combo_box_1.setCurrentText(sets['user']['default-recipe'])
        self.font_box_1.setCurrentFont(QFont(sets['user']['font-name']))
        self.spin_box_1.setValue(int(sets['user']['font-size']))
        font = QFont.fromString(QFont(), sets['user']['font-name'])

        rx = QRegExp("(([\w\d])+([ ]||[-]||[_]))*")
        self.reg = QRegExpValidator(rx)
        self.line_edit_1.setValidator(self.reg)
        self.line_edit_1.setText(sets['user']['default-book-name'])
        self.show()

    def setFontOnDialog(self):
        self.setFont(QFont(self.font_box_1.currentText(),
                           int(self.spin_box_1.value())))

    def accept(self):
        settings.saveConfiguration(self.combo_box_1.currentText(),
                                   self.font_box_1.currentText(),
                                   self.spin_box_1.value(),
                                   self.line_edit_1.text())

        information = QMessageBox.information(
                      self, 'Uwaga', "Ustawienia zostaną wprowadzone \npo " +
                      "ponownym uruchomieniu aplikacji", QMessageBox.Ok)

        if information == QMessageBox.Ok:
            print('inforamtion - QMessageBox say Ok')  # for debugging

        defaultRecipe = str(settings.localPath + settings.zipsFolder +
                            self.combo_box_1.currentText())
        self.setFont(QFont(settings.sets['user']['font-name'],
                           int(settings.sets['user']['font-size'])))

        super(SettingsDialog, self).accept()

    def reject(self):
        settings.loadConfiguration()
        super(SettingsDialog, self).reject()
