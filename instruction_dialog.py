
import settings

from ui import howToUse_ui

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon,QPixmap,QRegExpValidator, QFont, QFontDatabase
from PyQt5.QtCore import qDebug, Qt, QEvent,QRegExp, QCoreApplication
from PyQt5.QtWidgets import QApplication, QFontDialog, QMainWindow,  QFileDialog, QSlider, QTextEdit, QDialog, QDialogButtonBox, \
                            QPushButton, QListWidget, QListWidgetItem, QAbstractItemView,QMouseEventTransition, QSizePolicy, \
                            QSpacerItem, QAction, QDialog, QComboBox, QListView, QMessageBox

sets = settings.loadConfiguration()


class InstructionDialog(QtWidgets.QDialog, howToUse_ui.Ui_Dialog):
    def __init__(self):
        super(InstructionDialog, self).__init__()
        self.dialog = QtWidgets.QDialog()
        howToUse_ui.Ui_Dialog.setupUi(self, self)
        self.dialog.ui = howToUse_ui.Ui_Dialog()
        self.dialog.ui.setupUi(self.dialog)
        self.buttonBox.accepted.connect(self.accept)
        self.show()

    def accept(self):
        super(InstructionDialog, self).accept()
