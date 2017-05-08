#!/usr/bin/python3
# -*- coding: utf-8 -*-
import PyQt5

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets

from PyQt5.QtCore import QFile
from PyQt5.QtCore import QFileDevice
from PyQt5.QtCore import QFileSelector
from PyQt5.QtCore import QFileInfo
from PyQt5.QtCore import QDirIterator
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QEvent
from PyQt5.QtCore import QRegExp
from PyQt5.QtCore import QCoreApplication

from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QFontDatabase

from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QSlider
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QListView
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QListWidget
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QSpacerItem
from PyQt5.QtWidgets import QFontDialog
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QListWidget
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtWidgets import QDialogButtonBox
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtWidgets import QMouseEventTransition


import os
import sys
import glob
import shutil
import recipe
import pypandoc
import datetime
import settings
import configparser

import widget_item
import table_widget
import about_dialog
import recipe_dialog
import settings_dialog
import variables_dialog
import instruction_dialog

from zipfile import ZipFile

from about_dialog import AboutDialog
from recipe_dialog import RecipeDialog
from widget_item import MyListWidgetItem
from settings_dialog import SettingsDialog
from variables_dialog import VariablesDialog
from instruction_dialog import InstructionDialog


import ui
from ui import mainwindow_ui
from ui.mainwindow_ui import Ui_MainWindow

settings.sets = configparser.ConfigParser()
settings.sets = settings.loadConfiguration()
fixNameOfFile = QRegExp("(([\w\d])+([ ]||[-]||[_]))*")


class MainWindow(QMainWindow, Ui_MainWindow):
    # << Custom Main Widget >> #
    def __init__(self, app):
        super(MainWindow, self).__init__()
        Ui_MainWindow.setupUi(self, self)
        self.setWindowIcon(QIcon("ui/sealcode-logo.ico"))
        self.actionUstawienia.triggered.connect(self.settings)
        self.actionO_GPandoc.triggered.connect(self.aboutGPadnoc)
        self.actionInstrukcja_uzycia.triggered.connect(self.instruction)
        self.setFont(QFont(settings.sets['user']['font-name'],
                           int(settings.sets['user']['font-size'])))

        self.reg = QRegExpValidator(fixNameOfFile)
        self.line_edit_1.setValidator(self.reg)
        self.line_edit_1.setText(settings.sets['user']['default-book-name'])
        self.line_edit_1.setToolTip(
            "Wynik konwersji zostanie zapisany w folderze\"/outputs\". "
            + "Przy odznaczonej opcji \"łącz dokumenty\",\n" + "do nazw plików"
            + "wynikowych dopisywany jest numer porządkowy według listy.")

        self.push_button_1.clicked.connect(self.load_files)
        self.push_button_2.clicked.connect(self.select_recipe)
        self.push_button_3.clicked.connect(self.conf_variables)
        self.push_button_4.clicked.connect(self.clear_selected_items)
        self.push_button_5.clicked.connect(self.clear_all_items)
        self.show()

        self.list_widget_1.setAcceptDrops(True)
        self.list_widget_1.setMouseTracking(True)
        self.list_widget_1.verticalScrollBar()
        self.list_widget_1.horizontalScrollBar()
        self.list_widget_1.setDragDropMode(QAbstractItemView.InternalMove)
        self.list_widget_1.setSelectionMode(
             QAbstractItemView.ExtendedSelection)

        self.list_widget_1.currentItemChanged.connect(self.items_changed)

    # Actions for mouse right click #
        quit_action_1 = QAction("Zamknij", self, shortcut="Ctrl+Q",
                                triggered=QApplication.instance().quit)
        quit_action_2 = QAction("Czyść", self, triggered=self.clear_all_items)
        quit_action_3 = QAction("Zaznacz wszystko", self, shortcut="Ctrl+A",
                                triggered=self.select_items)
        quit_action_4 = QAction("Usuń zaznaczone", self, shortcut="Del",
                                triggered=self.clear_selected_items)
        self.list_widget_1.addAction(quit_action_4)
        self.list_widget_1.addAction(quit_action_3)
        self.list_widget_1.addAction(quit_action_2)
        self.list_widget_1.addAction(quit_action_1)

    # Info for users how to add files
        self.list_widget_1.setContextMenuPolicy(Qt.ActionsContextMenu)

        self.push_button_1.setToolTip("Kliknij, aby dodać pliki do listy")
        self.push_button_2.setToolTip("Kliknij, aby wybrać przepis")
        self.push_button_3.setToolTip(
            "Kliknij, aby przejść do generowania dokumentu")
        self.push_button_4.setToolTip(
            "Kliknij, aby usunać zaznaczone elementy")

        self.push_button_5.setToolTip("Kliknij, aby wyczyścić liste")
        settings.localPath
        settings.zipsFolder

        self.returnedFiles = []
        self.boxIsChecked = False
        self.selectedRecipe = str(settings.localPath + settings.zipsFolder +
                                  settings.sets['user']['default-recipe'])
        self.items_changed()


# << END of: Custom Main Widget >> #
    def aboutGPadnoc(self):
        dialog = AboutDialog()
        dialog.exec_()

    def instruction(self):
        dialog = InstructionDialog()
        dialog.exec_()

    def settings(self, loadedRecipe):
        dialog = SettingsDialog(loadedRecipe)
        self.setFont(QFont(settings.sets['user']['font-name'],
                           int(settings.sets['user']['font-size'])))
        dialog.exec_()


# << Listwidget handling >> #

    # clear current selected item
    def clear_selected_items(self):
        for select in self.list_widget_1.selectedItems():
            self.list_widget_1.takeItem(self.list_widget_1.row(select))
        self.items_changed()

    def check_extensions(self):
        if (self.list_widget_1.count()):
            ext = self.list_widget_1.item(0).showExtension()
            for x in range(self.list_widget_1.count()):
                if(str(ext) != str(
                   self.list_widget_1.item(x).showExtension())):

                    # print ("check_extension return: \nFalse, because list
                    # included different extensions.\nDisable checkBox")
                    # for debugging
                    self.check_box_1.setChecked(False)
                    self.check_box_1.setEnabled(False)
                    return False
            # print ("check_extension return: \nTrue, because list included the
            # same extensions.\nEnable checkBox")   # for debugging

            self.check_box_1.setEnabled(True)
        self.check_box_1.setEnabled(True)
        return True

    def items_changed(self):
        if(self.selectedRecipe is None and defaultRecipe is None or
           self.list_widget_1.count() == 0):

            self.push_button_3.setEnabled(False)
            self.check_extensions()
        else:
            self.push_button_3.setEnabled(True)
            self.check_extensions()


# clear all files on the list
    def clear_all_items(self):
        self.list_widget_1.clear()
        self.items_changed()

    # select all files on the list
    def select_items(self):
        self.list_widget_1.selectAll()
        # print("\n" + str(listPaths)) # chcek list values: listPaths
        for x in range(self.list_widget_1.count()):
            print(self.list_widget_1.item(x).showPath())

    def print_extensions(self):
        for x in range(self.list_widget_1.count()):
            print(self.list_widget_1.item(x).showExtension())

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        self.items_changed()

# << ADD paths on list_widget_1 from listPaths used pop()  >> #
    def add_to_list_widget(self, listPaths):
        for path in listPaths:
            fileName = str(path).split("/")
            item = MyListWidgetItem(path)
            item.setText(fileName[-1])
            item.setPath(str(path))
            self.list_widget_1.addItem(item)
        # for debugging
        self.print_extensions()
        self.check_extensions()

# << Load files on >> #

    def load_files(self):
        listPaths = []
        files, _ = QFileDialog.getOpenFileNames(
                self, "Wybierz pliki", '',
                "wszystkie (*);; " + "commonmark (*.commonmark);;" +
                "docbook (*.docbook);;" + "docx (*.docx);;" +
                "epub (*.epub);;" + "haddock (*.haddock);;" +
                "html (*.html);;" + "json (*.json);;" + "latex (*.latex);;" +
                "markdown (*.markdown *.md);;" +
                "markdown_github (*.markdown_github);;" +
                "markdown_mmd(*.markdown_mmd);;" +
                "markdown_phpextra (*.markdown_phpextra);;" +
                "markdown_strict (*.markdown_strict);;" +
                "mediawiki (*.mediawiki);;" + "native (*.native);;" +
                "odt (*.odt);;" + "opml (*.opml);;" + "org (*.org);;" +
                "rst (*.rst);;" + "t2t (*.t2t);;" + "textile (*.textile);;" +
                "twiki (*.twiki)")

        for file in files:
            listPaths.append(file)
        print(listPaths)  # for debugging
        self.add_to_list_widget(listPaths)
        self.items_changed()
# << END of: Load files on >> #

    def return_boxIsChecked(self):
        self.isChecked = self.check_box_1.checkState()
        return self.isChecked

    def return_files(self):
        self.returnedFiles = []
        for x in range(self.list_widget_1.count()):
            self.returnedFiles.append(self.list_widget_1.item(x).showPath())
        return self.returnedFiles
# << >>

    # << Select recipe - handling >> #
    def select_recipe(self):
        recipeDialog = None
        recipeDialog = RecipeDialog(recipeDialog, self.selectedRecipe)
        recipeDialog.exec_()
        self.selectedRecipe = recipeDialog.retRecipe()
        self.items_changed()
        print(self.selectedRecipe)
        # for debugging

    # << END of: Select recipe - handling >>
    # with ZipFile('spam.zip') as myzip:

    def conf_variables(self):
        bookName = str(self.line_edit_1.text())
        variablesDialog = VariablesDialog(self.selectedRecipe,
                                          self.return_files(),
                                          self.return_boxIsChecked(),
                                          bookName)
        variablesDialog.exec_()
        self.shellCommand()

    def shellCommand(self):
        command = None


# <<< END OF MAINWINDOW >>> #
