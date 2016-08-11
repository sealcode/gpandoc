# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recipe.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!
import sys

sys.path.insert(0, 'yaml_files/')

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QAction
import zipfile

class Ui_Dialog(QDialog):
    def __init__(self, parent):
        super(Ui_Dialog,self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(349, 400)
        self.vertical_layout_1 = QtWidgets.QVBoxLayout()
        self.vertical_layout_1.setObjectName("vertical_layout_1")

        self.vertical_layout_2 = QtWidgets.QVBoxLayout()
        self.vertical_layout_2.setObjectName("vertical_layout_2")

        self.vertical_layout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.vertical_layout_3.setObjectName("vertical_layout_3")

        self.label_1 = QtWidgets.QLabel(Dialog)
        self.label_1.setObjectName("label_1")

        self.combo_box_1 = QtWidgets.QComboBox(Dialog)
        self.combo_box_1.setObjectName("combo_box_1")

        self.scroll_area_1 = QtWidgets.QScrollArea(Dialog)
        self.scroll_area_1.setObjectName("scroll_area_1")

        self.button_box_1 = QtWidgets.QDialogButtonBox(Dialog)
        self.button_box_1.setObjectName("button_box_1")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.vertical_layout_1.addWidget(self.label_1)
        self.vertical_layout_1.addWidget(self.combo_box_1)
        self.vertical_layout_2.addWidget(self.scroll_area_1)
        self.vertical_layout_2.addWidget(self.button_box_1)
        self.vertical_layout_3.addLayout(self.vertical_layout_1)
        self.vertical_layout_3.addLayout(self.vertical_layout_2)

        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 314, 407))

        self.scroll_area_1.setWidgetResizable(True)
        self.scroll_area_1.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll_area_1.setWidget(self.scrollAreaWidgetContents)


        self.button_box_1.setOrientation(QtCore.Qt.Horizontal)
        self.button_box_1.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)

        self.retranslateUi(Dialog)
        self.button_box_1.accepted.connect(Dialog.accept)
        self.button_box_1.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle("GPANDOC ~ Przepisy")
        self.label_1.setText(_translate("Dialog", "Wybór przepisu:"))
