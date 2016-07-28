import sys
sys.path.insert(0, 'ui/')
import mainwindow_ui

from PyQt5 import QtWidgets

def load_resources():
    pass

def add_files():
    pass


app = QtWidgets.QApplication(sys.argv)
window = mainwindow_ui.UI_MainWindow()


sys.exit(app.exec_())
