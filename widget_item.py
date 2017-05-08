from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QListWidget, QListWidgetItem


class MyListWidgetItem(QListWidgetItem):
    # << Custom Main Widget >> #
    def __init__(self, text):
        super(MyListWidgetItem, self).__init__()
        self.path = " "
        self.ext = ""
        self.setPath(text)
        self.setExtension(text)

    def setExtension(self, text):
        self.ext = text
        self.ext = self.ext.split('.')
        self.ext = self.ext[-1]

    def setPath(self, text):
        self.path = text

    def showPath(self):
        return self.path

    def showExtension(self):
        return self.ext
