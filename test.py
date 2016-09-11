import sys
import string
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Header(QHeaderView):

    def __init__(self, parent=None):
        super(Header, self).__init__(Qt.Horizontal, parent)

        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.ctxMenu)

        self.setup()

    @pyqtSlot(bool)
    def printID(self, i):
        print("id")
        if i == False:
            self.hideSection(0)
        else:
            self.showSection(0)

    @pyqtSlot(bool)        
    def printNAME(self, i):
        print("name")
        if i == False:
            self.hideSection(1)
        else:
            self.showSection(1)

    @pyqtSlot(bool)        
    def printUSERNAME(self, i):
        print("username")
        if i == False:
            self.hideSection(2)
        else:
            self.showSection(2)

    def setup(self):

        self.id = QAction("id",self)
        self.id.setCheckable(True)
        self.id.setChecked(True)
        self.connect(self.id, SIGNAL("triggered(bool)"), self, SLOT("printID(bool)"))


        self.name = QAction("name",self)
        self.name.setCheckable(True)
        self.name.setChecked(True)
        self.connect(self.name, SIGNAL("triggered(bool)"), self, SLOT("printNAME(bool)"))


        self.username = QAction("username",self)
        self.username.setCheckable(True)
        self.username.setChecked(True)
        self.connect(self.username, SIGNAL("triggered(bool)"), self, SLOT("printUSERNAME(bool)"))

    def ctxMenu(self, point):
        menu = QMenu(self)
        self.currentSection = self.logicalIndexAt(point)
        menu.addAction(self.id)
        menu.addAction(self.name)
        menu.addAction(self.username)
        menu.exec_(self.mapToGlobal(point))


class Table(QTableWidget):
    def __init__(self, parent=None):
        super(Table, self).__init__(parent)
        self.setHorizontalHeader(Header(self))
        self.setColumnCount(3)
        self.setHorizontalHeaderLabels(['id', 'name', 'username'])
        self.populate()

    def populate(self):
        self.setRowCount(10)
        for i in range(10):
            for j,l in enumerate(string.ascii_letters[:3]):
                self.setItem(i, j, QTableWidgetItem(l)) 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    t = Table()
    t.show()
    app.exec_()
    sys.exit()
