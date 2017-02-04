# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'variables.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.vertical_layout = QtWidgets.QVBoxLayout()
        self.vertical_layout.setObjectName("vertical_layout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.vertical_layout.addWidget(self.label)
        self.form_layout = QtWidgets.QFormLayout()
        self.form_layout.setObjectName("form_layout")
        self.vertical_layout.addLayout(self.form_layout)
        self.button_box = QtWidgets.QDialogButtonBox(Dialog)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.vertical_layout.addWidget(self.button_box)
        self.verticalLayout_2.addLayout(self.vertical_layout)

        self.retranslateUi(Dialog)
        self.button_box.accepted.connect(Dialog.accept)
        self.button_box.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Zmienne"))
        self.label.setText(_translate("Dialog", "Konfiguracja "))

