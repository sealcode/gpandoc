# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recipe.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow


class Recipes_Ui(QDialog):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        dialog = QDialog()
        dialog.setObjectName("Dialog")

        self.vertical_layout_1 = QtWidgets.QVBoxLayout()
        self.vertical_layout_1.setObjectName("vertical_layout_1")
        self.vertical_layout_2 = QtWidgets.QVBoxLayout()
        self.vertical_layout_2.setObjectName("vertical_layout_2")
        self.vertical_layout_3 = QtWidgets.QVBoxLayout(dialog)
        self.vertical_layout_3.setObjectName("vertical_layout_3")

        self.label_1 = QtWidgets.QLabel(dialog)
        self.label_1.setObjectName("label_1")

        self.button_box_1 = QtWidgets.QDialogButtonBox(dialog)
        self.button_box_1.setObjectName("button_box_1")

        self.combo_box_1 = QtWidgets.QComboBox(dialog)
        self.combo_box_1.setObjectName("combo_box_1")

        self.scroll_area_1 = QtWidgets.QScrollArea(dialog)
        self.scroll_area_1.setObjectName("scroll_area_1")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.vertical_layout_1.addWidget(self.label_1)
        self.vertical_layout_1.addWidget(self.combo_box_1)
        self.vertical_layout_2.addWidget(self.button_box_1)
        self.vertical_layout_2.addWidget(self.scroll_area_1)
        self.vertical_layout_3.addLayout(self.vertical_layout_1)

        self.scroll_area_1.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll_area_1.setWidgetResizable(True)

        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 314, 407))

        self.scroll_area_1.setWidget(self.scrollAreaWidgetContents)

        self.button_box_1.setOrientation(QtCore.Qt.Horizontal)
        self.button_box_1.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)

        self.vertical_layout_3.addLayout(self.vertical_layout_2)

        self.button_box_1.accepted.connect(dialog.accept)
        self.button_box_1.rejected.connect(dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(dialog)

        self.setWindowTitle("GPadnoc ~ Przepisy")
        self.retranslateUi(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_1.setText(_translate("Dialog", "Wybór przepisu:"))
        self.show()

