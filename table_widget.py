import PyQt5
from PyQt5 import QtWidgets

from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QListView
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QPlainTextEdit
from PyQt5.QtWidgets import QTableWidgetItem


class Table(QtWidgets.QTableWidget):

    def __init__(self):
        super(Table, self).__init__()
        self.rows_number = 0
        self.columns_number = 1
        self.setRowCount(self.rows_number)
        self.setColumnCount(self.columns_number)
        self.setup_empty_table()

        # < ADD PushButton and connect with function add_cell > #
        self.button_form = QPushButton()
        self.button_form.setText("Nowe pole")
        self.button_form.clicked.connect(self.add_cell)

        self.button_form2 = QPushButton()
        self.button_form2.setText("Usuń pole")
        self.button_form2.clicked.connect(self.remove_cell)

    def setup_empty_table(self):
        self.horizontalHeader().setStretchLastSection(True)
        self.setMinimumHeight(120)
        self.setMaximumHeight(180)
        self.add_cell()
        for x in range(self.rows_number):
            self.setRowHeight(x, 30)

    def add_cell(self):
        self.rows_number = (self.rowCount())
        self.insertRow(self.rows_number)
        self.setItem(self.rows_number, 0, QtWidgets.QTableWidgetItem(""))
        if int(self.rows_number) > 3:
            self.setMinimumHeight(150)
            self.setMaximumHeight(300)
            for x in range(self.rowCount()):
                self.setRowHeight(x, 20)
        self.show()

    def remove_cell(self):
        self.current_row = self.currentRow()
        self.removeRow(self.currentRow())
        self.show()
