import sys
import yaml
from ui import recipes_ui
from ui import mainwindow_ui

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,  QFileDialog, QTextEdit, \
                            QPushButton, QListWidget, QListWidgetItem, QAbstractItemView, QMouseEventTransition, QAction,QDialog
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

        ### Actions for mouse right click ###
        quit_action_1 = QAction("Zamknij", self, shortcut="Ctrl+Q", triggered=QApplication.instance().quit)
        quit_action_2 = QAction("Czyść", self, triggered=self.clearAllItems)
        quit_action_3 = QAction("Zaznacz wszystko", self, shortcut="Ctrl+A", triggered=self.selectItems)
        quit_action_4 = QAction("Usuń zaznaczone", self, shortcut="Del",triggered=self.clearSelectedItems)
        self.addAction(quit_action_4)
        self.addAction(quit_action_3)
        self.addAction(quit_action_2)
        self.addAction(quit_action_1)

        # Info for users how to add files
        self.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.setToolTip("Aby dodać pliki skorzystaj z przycisku wybierz, lub przeciągnij je i upuść na liście")


    # clear current selected item
    def clearSelectedItems(self):
        for selected_item in self.selectedItems():
            self.takeItem(self.row(selected_item))

    # clear all files on the list
    def clearAllItems(self):
        self.clear()

    # select all files on the list
    def selectItems(self):
        self.selectAll();

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            super(mListWidget, self).dragEnterEvent(event)

    # event
    def dragMoveEvent(self, event):
            super(mListWidget, self).dragMoveEvent(event)
    # event
    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                self.addItem(url.path())
            event.acceptProposedAction()
        else:
            super(mListWidget, self).dropEvent(event)



class mMainWindow(UI_MainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

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

    def select_recipe(self):
        dialog = QDialog()
        dialog.ui = recipes_ui.Ui_Dialog(self)
        dialog.ui.setupUi(dialog)
        dialog.exec_()

