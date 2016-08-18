
import sys

import logic_ui

from ui import mainwindow_ui

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QListWidget

app = QtWidgets.QApplication(sys.argv)
window = logic_ui.MainWindow(app)
window.show()


sys.exit(app.exec_())
