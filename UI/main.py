import sys
from mainwindow_UI import*
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
a_window = Ui_MainWindow()

sys.exit(app.exec_())
