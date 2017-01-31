#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import logging
import configparser
import settings
import subprocess
from subprocess import check_call


import ui
import logic_ui
from ui import mainwindow_ui

try:
    import outputs
except ImportError:
    print ("Create outputs folder")
    check_call(['mkdir','outputs'])

try:
    import temp
except ImportError:
    print ("Create temp folder")
    check_call(['mkdir','temp'])


from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QListWidget

logging.basicConfig(level=logging.DEBUG)

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.log = logging.getLogger(self.__class__.__name__)
        self.main_window = Ui_MainWindow()
        self.main_window.setupUi(self)
        self._connect_signals()
        sets = configparser.ConfigParser()
        sets = settings.loadConf()
        self.setFont(QFont(sets['user']['font-name'],int(sets['user']['font-size'])))

        self.show()

    def _connect_signals(self):
        self.main_window.saveBtn.clicked[bool].connect(self.on_save)

    def on_save(self, check):
      self.log.debug('on_save STUB')


def main():
    app = QtWidgets.QApplication(sys.argv)

    window = logic_ui.MainWindow(app)

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
