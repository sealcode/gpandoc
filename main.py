import sys

sys.path.insert(0, 'ui/')
import mainwindow_ui
import recipes_ui

from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
window = mainwindow_ui.UI_MainWindow()

sys.exit(app.exec_())
