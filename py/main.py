import sys
from mainwindow_ui import*
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
window = Ui_MainWindow()

sys.exit(app.exec_())
