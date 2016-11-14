# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recipe.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(349, 533)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.vertical_layout_1 = QtWidgets.QVBoxLayout()
        self.vertical_layout_1.setObjectName("vertical_layout_1")
        self.label_1 = QtWidgets.QLabel(Dialog)
        self.label_1.setObjectName("label_1")
        self.vertical_layout_1.addWidget(self.label_1)
        self.combo_box_1 = QtWidgets.QComboBox(Dialog)
        self.combo_box_1.setObjectName("combo_box_1")
        self.vertical_layout_1.addWidget(self.combo_box_1)
        self.verticalLayout_3.addLayout(self.vertical_layout_1)
        self.vertical_layout_2 = QtWidgets.QVBoxLayout()
        self.vertical_layout_2.setObjectName("vertical_layout_2")
        self.scroll = QtWidgets.QScrollArea(Dialog)
        self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll.setWidgetResizable(True)
        self.scroll.setObjectName("scroll")
        self.content = QtWidgets.QWidget()
        self.content.setGeometry(QtCore.QRect(0, 0, 300, 433))
        self.content.setMaximumSize(QtCore.QSize(300, 600))
        self.content.setObjectName("content")
        self.label_2 = QtWidgets.QLabel(self.content)
        self.label_2.setGeometry(QtCore.QRect(8, 3, 301, 421))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.scroll.setWidget(self.content)
        self.vertical_layout_2.addWidget(self.scroll)
        self.button_box_1 = QtWidgets.QDialogButtonBox(Dialog)
        self.button_box_1.setOrientation(QtCore.Qt.Horizontal)
        self.button_box_1.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box_1.setObjectName("button_box_1")
        self.vertical_layout_2.addWidget(self.button_box_1)
        self.verticalLayout_3.addLayout(self.vertical_layout_2)

        self.retranslateUi(Dialog)
        self.button_box_1.accepted.connect(Dialog.accept)
        self.button_box_1.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_1.setText(_translate("Dialog", "Wybór przepisu:"))
        self.label_2.setText(_translate("Dialog", "TextLabel"))

