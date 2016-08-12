
import sys

import logic_ui

from ui import mainwindow_ui

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow

app = QtWidgets.QApplication(sys.argv)
window = QMainWindow()
window.ui = logic_ui.MainWindow()
window.ui.setupUi(window)
window.show()

sys.exit(app.exec_())
