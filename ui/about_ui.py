# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/about.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(407, 243)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_1 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Carlito")
        font.setPointSize(28)
        self.label_1.setFont(font)
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.verticalLayout.addWidget(self.label_1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Carlito")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Carlito")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Carlito")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_4.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.label_4.setText("<html><head/><body><p><a href=\"https://www.sealcode.org\"><span style=\" text-decoration: underline; color:#0000ff;\">Inicjatywa Naukowo Technologiczna Sealcode</span></a></p></body></html>")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.buttonBox.setFont(font)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox, 0, QtCore.Qt.AlignHCenter)
        self.label_3.setBuddy(self.label_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "o programie"))
        self.label_1.setText(_translate("Dialog", "gPandoc"))
        self.label_2.setText(_translate("Dialog", "~ Autorzy:"))
        self.label_3.setText(_translate("Dialog", "Jakub Pieńkowski\n"
"Jaroslaw Wieczorek\n"
"Kuba Orlik"))

