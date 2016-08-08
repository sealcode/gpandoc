# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,  QFileDialog, QTextEdit, \
                            QPushButton, QListWidget, QListWidgetItem, QAbstractItemView, QMouseEventTransition, QAction
from PyQt5.QtCore import QFile, QFileDevice, QFileSelector, QFileInfo, QDirIterator, pyqtWrapperType, qDebug, Qt
from PyQt5.QtGui import QIcon

class mListWidget(QListWidget):
    def __init__(self, parent):
        super(mListWidget, self).__init__(parent)
        self.setAcceptDrops(True)
        self.setMouseTracking(True)
        self.setDragDropMode(QAbstractItemView.InternalMove)
        self.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        quit_action = QAction("E&xit", self, shortcut="Ctrl+Q", triggered=QApplication.instance().quit)
        self.addAction(quit_action)
        self.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.setToolTip("Aby dodać pliki skorzystaj z przycisku wybierz, lub przeciągnij je i upuść na liście")


    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            super(mListWidget, self).dragEnterEvent(event)

    #def dragLeaveEvent(self, event):
        #if():
         #   for selected_item in self.selectedItems():
          #      self.takeItem(self.row(selected_item))


    def dragMoveEvent(self, event):
            super(mListWidget, self).dragMoveEvent(event)

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                self.addItem(url.path())
            event.acceptProposedAction()
        else:
            super(mListWidget, self).dropEvent(event)


class UI_MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setMouseTracking(True)
        main_window = QtWidgets.QWidget()
        main_window.setObjectName("main_window")
        main_window.setMinimumSize(QtCore.QSize(400, 380))

        # create elements
        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName("central_widget")
        self.setCentralWidget(self.central_widget)

        self.vertical_layout_1 = QtWidgets.QVBoxLayout()
        self.vertical_layout_1.setObjectName("vertical_layout_1")
        self.vertical_layout_2 = QtWidgets.QVBoxLayout(self.central_widget)
        self.vertical_layout_2.setObjectName("vertical_layout_2")

        self.horizontal_layout_1 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_1.setObjectName("horizontal_layout_1")
        self.horizontal_layout_2 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_2.setObjectName("horizontal_layout_2")
        self.horizontal_layout_3 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_3.setObjectName("horizontal_layout_3")
        self.horizontal_layout_4 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_4.setObjectName("horizontal_layout_4")
        self.horizontal_layout_5 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_5.setObjectName("horizontal_layout_5")

        self.check_box_1 = QtWidgets.QCheckBox(self.central_widget)
        self.check_box_1.setObjectName("check_box_1")

        self.label_1 = QtWidgets.QLabel(self.central_widget)
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.central_widget)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.central_widget)
        self.label_4.setObjectName("label_4")

        self.push_button_1 = QtWidgets.QPushButton(self.central_widget)
        self.push_button_1.setObjectName("push_button_1")
        self.push_button_2 = QtWidgets.QPushButton(self.central_widget)
        self.push_button_2.setObjectName("push_button_2")
        self.push_button_3 = QtWidgets.QPushButton(self.central_widget)
        self.push_button_3.setObjectName("push_button_3")

        self.menu_bar = QtWidgets.QMenuBar(main_window)
        self.menu_bar.setObjectName("menu_bar")

        self.status_bar = QtWidgets.QStatusBar(main_window)
        self.status_bar.setObjectName("status_bar")

        self.list_widget = mListWidget(self.central_widget)
        self.list_widget.setObjectName("list_widget")

        # create fonts
        font_1 = QtGui.QFont()
        font_1.setPointSize(14)

        # set fonts
        main_window.setFont(font_1)

        font_1.setPointSize(10)

        self.label_1.setFont(font_1)
        self.label_2.setFont(font_1)
        self.label_4.setFont(font_1)

        self.check_box_1.setFont(font_1)

        self.push_button_1.setFont(font_1)
        self.push_button_2.setFont(font_1)

        font_1.setPointSize(12)
        self.push_button_3.setFont(font_1)

        self.horizontal_layout_1.addWidget(self.label_1)
        self.horizontal_layout_1.addWidget(self.push_button_1)
        self.horizontal_layout_2.addWidget(self.label_2)
        self.horizontal_layout_2.addWidget(self.check_box_1)
        self.horizontal_layout_3.addWidget(self.label_4)
        self.horizontal_layout_3.addWidget(self.push_button_2)
        self.horizontal_layout_5.addWidget(self.push_button_3)

        self.vertical_layout_1.addLayout(self.horizontal_layout_1)
        self.vertical_layout_1.addLayout(self.horizontal_layout_2)

        self.vertical_layout_1.addWidget(self.list_widget)

        self.vertical_layout_1.addLayout(self.horizontal_layout_3)
        self.vertical_layout_1.addLayout(self.horizontal_layout_4)
        self.vertical_layout_1.addLayout(self.horizontal_layout_5)
        self.vertical_layout_2.addLayout(self.vertical_layout_1)



        # item = QtWidgets.QListWidgetItem()
        # item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        # self.list_widget.addItem(item)

        self.setWindowTitle("GPANDOC")
        self.show()
        self.retranslate_ui(main_window)

        QtCore.QMetaObject.connectSlotsByName(main_window)


    def retranslate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate

        self.label_1.setText(_translate("main_window", "1. Wybierz pliki do zaimportowania:"))
        self.label_2.setText(_translate("main_window", "Lista wybranych plików:"))
        self.label_4.setText(_translate("main_window", "2. Przepis (format, czcionka, marginesy itp):"))

        self.push_button_1.setText(_translate("main_window", "Wybierz pliki"))
        self.push_button_2.setText(_translate("main_window", "Wybierz przepis"))
        self.push_button_3.setText(_translate("main_window", "Zapisz"))

        self.push_button_1.clicked.connect(self.load_files)
        self.check_box_1.setText(_translate("main_window", "Łącz dokumenty"))
        self.show()


    def add_to_list(self, list_of_files):
        while list_of_files:
            self.list_widget.addItem(list_of_files.pop())


    def load_files(self):
        list_of_files = []
        file_names, _ = QFileDialog.getOpenFileNames(self, "Wybierz pliki", '', "Files (*.txt *.cpp, *.py *.doc *.pdf);;Folders(*/);;All Files (*)")

        for file_name in file_names:
            list_of_files.append(file_name)
        print(list_of_files)
        self.add_to_list(list_of_files)




