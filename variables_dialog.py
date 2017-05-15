import shutil
import zipfile
import subprocess

import pypandoc
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMessageBox

import recipe
import settings
from ui.variables import Ui_Variables
from table_widget import Table


class VariablesDialog(QDialog, Ui_Variables):
    def __init__(self, loadedRecipe, gfiles, boxIsChecked, bookName):
        super(VariablesDialog,  self).__init__()
        Ui_Variables.setupUi(self, self)
        settings.sets = settings.loadConfiguration()
        settings.localPath
        self.setFont(QFont(settings.sets['user']['font-name'],
                     int(settings.sets['user']['font-size'])))

        self.form = []
        self.bookName = bookName
        self.attributes = {}
        self.getFiles = gfiles
        self.boxIsChecked = boxIsChecked
        if (loadedRecipe == ""):
            self.loadedRecipe = defaultRecipe
        else:
            self.loadedRecipe = loadedRecipe
        self.names_of_lists = recipe.Recipe(loadedRecipe).list
        self.names_of_texts = recipe.Recipe(loadedRecipe).text
        self.names_of_variables = recipe.Recipe(loadedRecipe).string
        self.template_name = recipe.Recipe(loadedRecipe).template
        self.output_format = recipe.Recipe(loadedRecipe).outputFormat

        self.load_table_of_lists(self.names_of_lists)
        self.load_table_of_variables(self.names_of_variables)
        self.load_table_of_texts(self.names_of_texts)
        self.unzip()

    def get_values(self):
        self.getsTable = []
        for box in self.form:
            items = (box.itemAt(i).widget() for i in range(box.count()))

            for w in items:
                if isinstance(w, QtWidgets.QLabel):
                    self.getsTable = []
                    self.getsTable.append(
                        w.text().encode('utf-8').decode('utf-8'))

                    key_value = True

                if isinstance(w, Table):
                    for i in range(w.rowCount()):
                        itm = w.item(i, 0)
                        self.getsTable.append(
                            itm.text().encode('utf-8').decode('utf-8'))

                    if key_value:
                        self.attributes[self.getsTable[0]] = self.getsTable[1:]
                        key_value = False

                if isinstance(w, QtWidgets.QLineEdit):
                    self.getsTable.append(
                        w.text().encode('utf-8').decode('utf-8'))
                    if key_value:
                        self.attributes[self.getsTable[0]] = self.getsTable[1:]
                        key_value = False

                if isinstance(w, QtWidgets.QPlainTextEdit):
                    self.getsTable.append(
                        w.toPlainText().encode('utf-8').decode('utf-8'))
                    if key_value:
                        self.attributes[self.getsTable[0]] = self.getsTable[1:]
                        key_value = False

    # << Set elements on form >> #
    def drawInterface(self):
        for elem in self.form:
            self.form_layout.addRow(elem)

    def load_table_of_lists(self, names_of_lists):
        # for element in name_of_lists:
        for name_of_list in names_of_lists:
            self.label = QtWidgets.QLabel(name_of_list)
            self.label.setMinimumWidth(100)
            self.label.setText(str(name_of_list))
            self.label.setObjectName(str(name_of_list) + "_label")

            self.table_widget = Table()
            self.table_widget.setHorizontalHeaderLabels([str(name_of_list)])
            self.table_widget.setObjectName(
                self.label.text() + "_table_widget")

            self.box = QtWidgets.QHBoxLayout()
            self.box.addWidget(self.label)
            self.box.addWidget(self.table_widget)

            self.b_box = QtWidgets.QHBoxLayout()
            self.b_box.addSpacing(108)
            self.b_box.addWidget(self.table_widget.button_form)
            self.b_box.addWidget(self.table_widget.button_form2)
            self.form.append(self.box)
            self.form.append(self.b_box)

        self.drawInterface()

    def load_table_of_variables(self, names_of_variables):
        for variable in names_of_variables:

            self.label = QtWidgets.QLabel(variable)
            self.label.setMinimumWidth(100)
            self.label.setText(str(variable))
            self.label.setObjectName(self.label.text() + "_label")
            self.line_edit = QtWidgets.QLineEdit("Wartość")
            self.box = QtWidgets.QHBoxLayout()
            self.box.addWidget(self.label)
            self.box.addWidget(self.line_edit)
            self.form.append(self.box)

        self.drawInterface()

    def load_table_of_texts(self, names_of_texts):

        for text in names_of_texts:

            self.label = QtWidgets.QLabel(text)
            self.label.setText(str(text))
            self.label.setMinimumWidth(100)
            self.label.setMinimumHeight(100)
            self.label.setScaledContents(True)
            self.label.setObjectName(self.label.text() + "_label")

            self.plain_text = QtWidgets.QPlainTextEdit("Wartość tekstowa")

            # create layout vertical for label and list(at the moment still
            # combobox)
            self.box = QtWidgets.QHBoxLayout()
            self.box.addWidget(self.label)
            self.box.addWidget(self.plain_text)
            self.form.append(self.box)

            # self.form.append(self.combobox)

        self.drawInterface()

    def unzip(self):
        with zipfile.ZipFile(self.loadedRecipe) as zf:
            zf.extractall(settings.localPath+settings.tempFolder)

    def clear_dir(self):
        shutil.rmtree(settings.localPath+settings.tempFolder, True)

    def reject(self):
        self.clear_dir()
        super(VariablesDialog, self).reject()

    def accept(self):
        variables = []
        outputFile = ""
        templateFile = ""
        self.get_values()
        pandoc = pypandoc.get_pandoc_path()

        if(self.boxIsChecked):
            inputFile = []
            for path in self.getFiles:
                inputFile.append(str(path))  # input file
            if(self.template_name):  # template file
                templateFile = '--template=' \
                               + settings.localPath \
                               + settings.tempFolder \
                               + self.template_name[0]
                print(templateFile)
            for attr in self.attributes.keys():
                for e in self.attributes[attr]:
                    # variables skime ex.: -V authors = "Szymborska"
                    variables.append('-V')
                    variables.append(attr + '=' + e)

            outputFile += '--output=' \
                          + settings.localPath \
                          + '/outputs/' \
                          + self.bookName \
                          + '.' \
                          + self.output_format[0]

            print([pandoc, inputFile, templateFile, variables, outputFile])
            if(templateFile != ""):
                try:
                    # for debagging
                    print(*[pandoc, *inputFile, templateFile, *variables,
                            outputFile])
                    subprocess.run([pandoc, *inputFile, templateFile,
                                    *variables, outputFile])
                except subprocess.errno:
                    print("error until call to pandoc")
                    messageBox = QMessageBox.error(self, 'Napotkano problem!',
                                                   "Podczas odwołania do"
                                                   + " programu Pandoc "
                                                   + " wystapił błąd: \n"
                                                   + str(subprocess.errno),
                                                     QMessageBox.Ok)

                messageBox = QMessageBox.information(self, 'Informacja',
                                                     "Konwersja przebiegła"
                                                     + " pomyślnie!\n Sprawdź"
                                                     + " folder \'outputs\'",
                                                     QMessageBox.Ok)
                # print("[*] Done")
                # for debugging
            else:
                try:
                    print(*[pandoc, *inputFile, *variables, outputFile])
                    # for debagging
                    subprocess.run([pandoc, *inputFile, *variables,
                                    outputFile])

                except subprocess.errno:
                    print("error until call to pandoc")
                    messageBox = QMessageBox.error(self, 'Napotkano problem!',
                                                   "Podczas odwołania do"
                                                   + " programu Pandoc "
                                                   + " wystapił błąd: \n"
                                                   + str(subprocess.errno),
                                                     QMessageBox.Ok)

                messageBox = QMessageBox.information(self, 'Informacja',
                                                     "Konwersja przebiegła"
                                                     + " pomyślnie!\n Sprawdź"
                                                     + " folder \'outputs\'",
                                                     QMessageBox.Ok)
            # print("[*] Done")  # for debugging
            inputFile = []
            templateFile = ""
            variables = []
            outputFile = ""

        else:

            num = 0
            inputFile = ""
            for path in self.getFiles:
                num += 1
                inputFile = str(path)  # input file

                if(self.template_name):  # template file
                    templateFile = '--template=' \
                                   + settings.localPath \
                                   + settings.tempFolder \
                                   + self.template_name[0]

                for attr in self.attributes.keys():
                    for e in self.attributes[attr]:
                        # variables skime ex.: -V authors = "Szymborska"
                        variables.append('-V')
                        variables.append(attr + '=' + e)

                outputFile += str('--output=' + settings.localPath
                                  + '/outputs/' + self.bookName + "_"
                                  + str(num) + '.' + self.output_format[0])

                if(templateFile != ""):
                    try:
                        if (templateFile.split('.')[1].lower() == "pdf"):
                            print("PDF !")

                        # check is temaplate of pdf [*]
                        print(*[pandoc, inputFile, templateFile, *variables,
                                outputFile])  # for debagging
                        subprocess.run([pandoc, inputFile, templateFile,
                                        *variables, outputFile])
                    except subprocess.errno:
                        print("error until call to pandoc")
                        messageBox = QMessageBox.error(self,
                                                       'Uwaga wykryto błąd!',
                                                       "Błąd podczas konwersji"
                                                       + " tego dokumentu:\n"
                                                       + str(inputFile)
                                                       + " napotkano n błąd:\n"
                                                       + str(subprocess.errno),
                                                       QMessageBox.Ok)

                    print("[*] Done for "+str(inputFile))
                else:
                    try:
                        print(*[pandoc, inputFile, *variables, outputFile])
                        # for debagging
                        subprocess.run([pandoc, inputFile, *variables,
                                        outputFile])

                    except subprocess.errno:
                        print("error until call to pandoc")
                        messageBox = QMessageBox.error(self,
                                                       'Uwaga wykryto błąd!',
                                                       "Błąd podczas konwersji"
                                                       + " tego dokumentu:\n"
                                                       + str(inputFile)
                                                       + " napotkano n błąd:\n"
                                                       + str(subprocess.errno),
                                                       QMessageBox.Ok)

                    print("[*] Done for "+str(inputFile))  # for debugging

                # print("[*] Done")  # for debugging
                templateFile = ""
                variables = []
                outputFile = ""
            messageBox = QMessageBox.information(self, 'Informacja',
                                                 "Konwersja przebiegła"
                                                 + " pomyślnie!\n Sprawdź"
                                                 + " folder \'outputs\'",
                                                 QMessageBox.Ok)

        super(VariablesDialog, self).accept()
