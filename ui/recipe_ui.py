# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recipe.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(355, 478)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.vertical_layout_1 = QtWidgets.QVBoxLayout()
        self.vertical_layout_1.setObjectName("vertical_layout_1")
        self.label_1 = QtWidgets.QLabel(Dialog)
        self.label_1.setObjectName("label_1")
        self.vertical_layout_1.addWidget(self.label_1)
        self.combo_box_1 = QtWidgets.QComboBox(Dialog)
        self.combo_box_1.setObjectName("combo_box_1")
        self.vertical_layout_1.addWidget(self.combo_box_1)
        self.verticalLayout.addLayout(self.vertical_layout_1)
        self.vertical_layout_2 = QtWidgets.QVBoxLayout()
        self.vertical_layout_2.setObjectName("vertical_layout_2")
        self.scroll_1 = QtWidgets.QScrollArea(Dialog)
        self.scroll_1.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll_1.setWidgetResizable(True)
        self.scroll_1.setObjectName("scroll_1")
        self.content_1 = QtWidgets.QWidget()
        self.content_1.setGeometry(QtCore.QRect(0, 0, 300, 378))
        self.content_1.setMaximumSize(QtCore.QSize(300, 600))
        self.content_1.setObjectName("content_1")
        self.label_2 = QtWidgets.QLabel(self.content_1)
        self.label_2.setGeometry(QtCore.QRect(8, 3, 301, 421))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.scroll_1.setWidget(self.content_1)
        self.vertical_layout_2.addWidget(self.scroll_1)
        self.button_box_1 = QtWidgets.QDialogButtonBox(Dialog)
        self.button_box_1.setOrientation(QtCore.Qt.Horizontal)
        self.button_box_1.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box_1.setObjectName("button_box_1")
        self.vertical_layout_2.addWidget(self.button_box_1)
        self.verticalLayout.addLayout(self.vertical_layout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Wybór przepisu"))
        self.label_1.setText(_translate("Dialog", "Lista przepisów:"))
        self.label_2.setText(_translate("Dialog", "TextLabel"))

