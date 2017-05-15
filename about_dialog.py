import settings

from ui.about import Ui_About

from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont

sets = settings.loadConfiguration()


class AboutDialog(QtWidgets.QDialog, Ui_About):
    def __init__(self):
        super(AboutDialog, self).__init__()
        self.dialog = QtWidgets.QDialog()
        Ui_About.setupUi(self, self)
        self.dialog.ui = Ui_About()
        self.dialog.ui.setupUi(self.dialog)
        self.buttonBox.accepted.connect(self.accept)
        self.dialog.ui.label_4.setOpenExternalLinks(True)
        global sets
        self.setFont(QFont(
            sets['user']['font-name'],
            int(sets['user']['font-size'])))
        self.show()

    def accept(self):
        super(AboutDialog, self).accept()
