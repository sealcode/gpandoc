
import sys

sys.path.insert(0, 'ui/')
import ui.mainwindow_ui
import ui.recipes_ui
from PyQt5 import QtWidgets



app = QtWidgets.QApplication(sys.argv)
window = ui.mainwindow_ui.UI_MainWindow()

sys.exit(app.exec_())
