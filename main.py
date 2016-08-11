
import sys

from ui import mainwindow_ui

from PyQt5 import QtWidgets


app = QtWidgets.QApplication(sys.argv)
window = mainwindow_ui.Ui_MainWindow()

sys.exit(app.exec_())
