
import settings

from ui import about_ui

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon,QPixmap,QRegExpValidator, QFont, QFontDatabase
from PyQt5.QtCore import qDebug, Qt, QEvent,QRegExp, QCoreApplication
from PyQt5.QtWidgets import QApplication, QFontDialog, QMainWindow,  QFileDialog, QSlider, QTextEdit, QDialog, QDialogButtonBox, \
                            QPushButton, QListWidget, QListWidgetItem, QAbstractItemView,QMouseEventTransition, QSizePolicy, \
                            QSpacerItem, QAction, QDialog, QComboBox, QListView, QMessageBox

sets = settings.loadConfiguration()

class AboutDialog(QtWidgets.QDialog, about_ui.Ui_Dialog):
    def __init__(self):
        super(AboutDialog, self).__init__()
        self.dialog = QtWidgets.QDialog()
        about_ui.Ui_Dialog.setupUi(self, self)
        self.dialog.ui = about_ui.Ui_Dialog()
        self.dialog.ui.setupUi(self.dialog)
        self.buttonBox.accepted.connect(self.accept)
        self.dialog.ui.label_4.setOpenExternalLinks(True);
        global sets
        self.setFont(QFont(sets['user']['font-name'],int(sets['user']['font-size'])))
        self.show()

    def accept(self):
        super(AboutDialog, self).accept()
