#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys
import logging
import configparser
import settings
import main_dialog
import table_widget
from ui import mainwindow_ui

import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication

settings.crateFolderAboutName("temp")
settings.crateFolderAboutName("outputs")
settings.prepareGlobalVariables()
print("settings zipsFolder:", settings.zipsFolder)


def main():
    app = QApplication(sys.argv)
    window = main_dialog.MainWindow(app)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
