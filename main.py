import sys
from ui import main_window

from PyQt5 import QtWidgets

def main():
    app = QtWidgets.QApplication(sys.argv)

    window = QtWidgets.QWidget()
    main_window.Ui_MainWindow().setupUi(window)
    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
