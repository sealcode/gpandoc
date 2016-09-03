import sys

from ui import recipe_ui
from ui.mainwindow_ui import Ui_MainWindow

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,  QFileDialog, QTextEdit, \
                            QPushButton, QListWidget, QListWidgetItem, QAbstractItemView, QMouseEventTransition, QAction,QDialog
from PyQt5.QtCore import QFile, QFileDevice, QFileSelector, QFileInfo, QDirIterator, pyqtWrapperType, qDebug, Qt
from PyQt5.QtGui import QIcon

###
class ListWidget(QListWidget):

    def __init__(self, parent=None):
        super(ListWidget, self).__init__(parent)
        self.setAcceptDrops(True)
        self.setMouseTracking(True)
        self.setDragDropMode(QAbstractItemView.InternalMove)
        self.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)

        # Actions for mouse right click
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
            super(ListWidget, self).dragEnterEvent(event)

    # event
    def dragMoveEvent(self, event):
            super(ListWidget, self).dragMoveEvent(event)
    # event
    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                self.addItem(url.path())
            event.acceptProposedAction()
        else:
            super(ListWidget, self).dropEvent(event)

###

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, app, parent=None):
        super(MainWindow, self).__init__(parent)
        
        Ui_MainWindow.setupUi(self, self)

        self.push_button_1.clicked.connect(self.load_files)
        self.push_button_2.clicked.connect(self.select_recipe)

        self.show()

        self.list_widget_1.setAcceptDrops(True)
        self.list_widget_1.setMouseTracking(True)
        self.list_widget_1.setDragDropMode(QAbstractItemView.InternalMove)
        self.list_widget_1.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.list_widget_1.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)

    # Actions for mouse right click #
        quit_action_1 = QAction("Zamknij", self, shortcut="Ctrl+Q", triggered=QApplication.instance().quit)
        quit_action_2 = QAction("Czyść", self, triggered=self.clearAllItems)
        quit_action_3 = QAction("Zaznacz wszystko", self, shortcut="Ctrl+A", triggered=self.selectItems)
        quit_action_4 = QAction("Usuń zaznaczone", self, shortcut="Del", triggered=self.clearSelectedItems)
        self.list_widget_1.addAction(quit_action_4)
        self.list_widget_1.addAction(quit_action_3)
        self.list_widget_1.addAction(quit_action_2)
        self.list_widget_1.addAction(quit_action_1)

    # Info for users how to add files
        self.list_widget_1.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.list_widget_1.setToolTip("Aby dodać pliki skorzystaj z przycisku wybierz. \nAby wyświetlić szybkie menu kliknij prawym przyciskiem. ")
	



    # <<< Listwidget handling >>> #

    # clear current selected item
    def clearSelectedItems(self):
        for selected_item in self.list_widget_1.selectedItems():
            self.list_widget_1.takeItem(self.list_widget_1.row(selected_item))

    # clear all files on the list
    def clearAllItems(self):
        self.list_widget_1.clear()

    # select all files on the list
    def selectItems(self):
        self.list_widget_1.selectAll();
    
    # EVENT: drag item on list
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            super(self.list_widget_1, self).dragEnterEvent(event)

    # EVENT: move item on list
    def dragMoveEvent(self, event):
        super(self.list_widget_1, self).dragMoveEvent(event)


    # EVENT: Put elements on the list 
    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                self.list_widget_1.addItem(url.path())
            event.acceptProposedAction()
        else:
            super(self.list_widget_1, self).dropEvent(event)

    # <<< END of: Listwidget handling >>> #


	
    # <<< Load files on >>> #
    def add_to_list(self, list_of_files):
        while list_of_files:
            self.list_widget_1.addItem(list_of_files.pop())


    def load_files(self):
        list_of_files = []
        file_names, _ = QFileDialog.getOpenFileNames(self, "Wybierz pliki", '', "Files (*.txt *.cpp, *.py *.doc *.pdf);;Folders(*/);;All Files (*)")

        for file_name in file_names:
            list_of_files.append(file_name)
        print(list_of_files)
        self.add_to_list(list_of_files)
   
    # <<< END of: Load files on >>> #



    # <<< RECIPE: Dialog handling >>> #
    def select_recipe(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = recipe_ui.Ui_Dialog()
        dialog.ui.setupUi(dialog)
        dialog.exec_()

