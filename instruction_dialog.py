from ui.howto import Ui_HowTo

from PyQt5 import QtWidgets


class InstructionDialog(QtWidgets.QDialog, Ui_HowTo):
    def __init__(self):
        super(InstructionDialog, self).__init__()
        self.dialog = QtWidgets.QDialog()
        Ui_HowTo.setupUi(self, self)
        self.dialog.ui = Ui_HowTo()
        self.dialog.ui.setupUi(self.dialog)
        self.buttonBox.accepted.connect(self.accept)
        self.show()

    def accept(self):
        super(InstructionDialog, self).accept()
