# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(401, 526)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.saveBtn = QtWidgets.QPushButton(MainWindow)
        self.saveBtn.setGeometry(QtCore.QRect(300, 490, 92, 28))
        self.saveBtn.setObjectName("saveBtn")
        self.files_Lst = QtWidgets.QListWidget(MainWindow)
        self.files_Lst.setGeometry(QtCore.QRect(10, 70, 381, 341))
        self.files_Lst.setObjectName("files_Lst")
        self.joinDocsCBox = QtWidgets.QCheckBox(MainWindow)
        self.joinDocsCBox.setGeometry(QtCore.QRect(10, 420, 141, 25))
        self.joinDocsCBox.setObjectName("joinDocsCBox")
        self.addFileBtn = QtWidgets.QPushButton(MainWindow)
        self.addFileBtn.setGeometry(QtCore.QRect(300, 420, 92, 28))
        self.addFileBtn.setObjectName("addFileBtn")
        self.comboBox = QtWidgets.QComboBox(MainWindow)
        self.comboBox.setGeometry(QtCore.QRect(70, 10, 321, 30))
        self.comboBox.setObjectName("comboBox")
        self.recipeLbl = QtWidgets.QLabel(MainWindow)
        self.recipeLbl.setGeometry(QtCore.QRect(10, 10, 66, 20))
        self.recipeLbl.setObjectName("recipeLbl")
        self.pushButton = QtWidgets.QPushButton(MainWindow)
        self.pushButton.setGeometry(QtCore.QRect(200, 420, 92, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "gPandoc"))
        self.saveBtn.setText(_translate("MainWindow", "Zapisz"))
        self.joinDocsCBox.setText(_translate("MainWindow", "Łącz dokumenty"))
        self.addFileBtn.setText(_translate("MainWindow", "Dodaj"))
        self.recipeLbl.setText(_translate("MainWindow", "Przepis:"))
        self.pushButton.setText(_translate("MainWindow", "Usuń"))

