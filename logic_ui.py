import io
import os
import sys
import glob
import shutil
import recipe
import zipfile
import pypandoc
import datetime
import configparser

import subprocess
from os import path
from zipfile import ZipFile
from subprocess import call
from PIL import Image, ImageQt

import ui
import zips
import outputs
import settings

from ui import about_ui
from ui import settings_ui
from ui import howToUse_ui
from ui import recipe_ui
from ui import variables_ui
from ui.mainwindow_ui import Ui_MainWindow

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon,QPixmap,QRegExpValidator, QFont, QFontDatabase
from PyQt5.QtCore import QFile,QFileDevice, QFileSelector, QFileInfo, QDirIterator, qDebug, Qt, QEvent,QRegExp, QCoreApplication
from PyQt5.QtWidgets import QApplication, QFontDialog, QMainWindow,  QFileDialog, QSlider, QTextEdit, QDialog, QDialogButtonBox, \
                            QPushButton, QListWidget, QListWidgetItem, QAbstractItemView,QMouseEventTransition, QSizePolicy, \
                            QSpacerItem, QAction, QDialog, QComboBox, QListView


# <<< SETTINGS Variables >>> #
pathDirectory = os.path.dirname(__file__)
sets = configparser.ConfigParser()
sets = settings.loadConf()
zipsFolder="/zips/"
defaultRecipe=""
listPaths=[]

def saveConf():
    pass
def loadConf():
    pass
# <<< END of: SETTINGS Variables >>> #

class AboutDialog(QtWidgets.QDialog, about_ui.Ui_Dialog):
    def __init__(self):
        super(AboutDialog, self).__init__()
        self.dialog = QtWidgets.QDialog()
        about_ui.Ui_Dialog.setupUi(self, self)
        self.dialog.ui = about_ui.Ui_Dialog()
        self.dialog.ui.setupUi(self.dialog)
        self.buttonBox.accepted.connect(self.accept)
        self.show()

    def accept(self):
        super(AboutDialog, self).accept()

class UseDialog(QtWidgets.QDialog, howToUse_ui.Ui_Dialog):
    def __init__(self):
        super(UseDialog, self).__init__()
        self.dialog = QtWidgets.QDialog()
        howToUse_ui.Ui_Dialog.setupUi(self, self)
        self.dialog.ui = howToUse_ui.Ui_Dialog()
        self.dialog.ui.setupUi(self.dialog)
        self.buttonBox.accepted.connect(self.accept)
        self.show()

    def accept(self):
        super(UseDialog, self).accept()

class SettingsDialog(QtWidgets.QDialog, settings_ui.Ui_Dialog):
    def __init__(self, loadedRecipe):
        super(SettingsDialog, self).__init__()
        self.dialog = QtWidgets.QDialog()
        settings_ui.Ui_Dialog.setupUi(self, self)
        self.dialog.ui = settings_ui.Ui_Dialog()
        self.dialog.ui.setupUi(self.dialog)

        self.spin_box_1.valueChanged.connect(self.setFontOnDialog)
        self.font_box_1.currentFontChanged.connect(self.setFontOnDialog)
        self.buttonBox.button(QDialogButtonBox.Apply).clicked.connect(self.accept)
        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.reject)
        QFontDatabase().Latin

        path = os.path.dirname(__file__)
        self.zipPackages  = [os.path.basename(x) for x in glob.glob(path+'/zips/'+'*.zip')]
        self.combo_box_1.addItems(self.zipPackages)

        #print(sets.sections()) # for debugging
        sets = settings.loadConf()
        self.combo_box_1.setCurrentText(sets['user']['default-recipe'])
        self.font_box_1.setCurrentFont(QFont(sets['user']['font-name']))
        self.spin_box_1.setValue(int(sets['user']['font-size']))
        font = QFont.fromString(QFont(),sets['user']['font-name'])

        rx =QRegExp("(([\w\d])+([ ]||[-]||[_]))*");
        self.reg = QRegExpValidator(rx)
        self.line_edit_1.setValidator(self.reg)
        self.line_edit_1.setText(sets['user']['default-book-name'])
        self.show()

    def setFontOnDialog(self):
        self.setFont(QFont(self.font_box_1.currentText(),int(self.spin_box_1.value())))

    def accept(self):
        settings.saveConf(self.combo_box_1.currentText(), self.font_box_1.currentText(),self.spin_box_1.value(), self.line_edit_1.text())
        global defaultRecipe
        global path
        global zips

        defaultRecipe=str(pathDirectory + zipsFolder + self.combo_box_1.currentText())
        self.setFont(QFont(sets['user']['font-name'],int(sets['user']['font-size'])))
        super(SettingsDialog, self).accept()

    def reject(self):
        settings.loadConf()
        super(SettingsDialog, self).reject()


# <<< MAINWINDOW >>> #

class MyListWidgetItem(QListWidgetItem):
    # << Custom Main Widget >> #
    def __init__(self, text):
        super(MyListWidgetItem, self).__init__()
        self.path=""
        self.ext=""
        self.setPath(text);
        self.setExtension(text);

    def setExtension(self, text):
        self.ext = text
        self.ext = self.ext.split('.')
        self.ext = self.ext[-1]

    def setPath(self,text):
        self.path = text

    def showPath(self):
        return self.path

    def showExtension(self):
        return self.ext


class MainWindow(QMainWindow, Ui_MainWindow):
  # << Custom Main Widget >> #
    def __init__(self, app):
        super(MainWindow, self).__init__()
        Ui_MainWindow.setupUi(self, self)
        self.setWindowIcon(QIcon("ui/sealcode-logo.ico"))
        self.actionUstawienia.triggered.connect(self.settings)
        self.actionO_GPandoc.triggered.connect(self.aboutGPadnoc)
        self.actionInstrukcja_uzycia.triggered.connect(self.instruction)

        global zipsFolder
        global sets
        self.setFont(QFont(sets['user']['font-name'],int(sets['user']['font-size'])))
        rx =QRegExp("(([\w\d])+([ ]||[-]||[_]))*");
        self.reg = QRegExpValidator(rx)
        self.line_edit_1.setValidator(self.reg)
        self.line_edit_1.setText(sets['user']['default-book-name'])
        self.line_edit_1.setToolTip("Wynik konwersji zostanie zapisany w folderze\"/outputs\". "+
                                    "Przy odznaczonej opcji \"łącz dokumenty\",\n"+
                                    "do nazw plików wynikowych dopisywany jest numer porządkowy według listy.")

        self.push_button_1.clicked.connect(self.load_files)
        self.push_button_2.clicked.connect(self.select_recipe)
        self.push_button_3.clicked.connect(self.conf_variables)
        self.push_button_4.clicked.connect(self.clear_selected_items)
        self.push_button_5.clicked.connect(self.clear_all_items)
        self.show()

        self.list_widget_1.setAcceptDrops(True)
        self.list_widget_1.setMouseTracking(True)
        self.list_widget_1.verticalScrollBar()
        self.list_widget_1.horizontalScrollBar()
        self.list_widget_1.setDragDropMode(QAbstractItemView.InternalMove)
        self.list_widget_1.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.list_widget_1.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.list_widget_1.currentItemChanged.connect(self.items_changed)

    # Actions for mouse right click #
        quit_action_1 = QAction("Zamknij", self, shortcut="Ctrl+Q", triggered=QApplication.instance().quit)
        quit_action_2 = QAction("Czyść", self, triggered=self.clear_all_items)
        quit_action_3 = QAction("Zaznacz wszystko", self, shortcut="Ctrl+A", triggered=self.select_items)
        quit_action_4 = QAction("Usuń zaznaczone", self, shortcut="Del", triggered=self.clear_selected_items)
        self.list_widget_1.addAction(quit_action_4)
        self.list_widget_1.addAction(quit_action_3)
        self.list_widget_1.addAction(quit_action_2)
        self.list_widget_1.addAction(quit_action_1)

    # Info for users how to add files
        self.list_widget_1.setContextMenuPolicy(Qt.ActionsContextMenu)

        self.push_button_1.setToolTip("Kliknij, aby dodać pliki do listy")
        self.push_button_2.setToolTip("Kliknij, aby wybrać przepis")

        self.push_button_3.setToolTip("Kliknij, aby przejść do wygenerowania dokumentu")
        self.push_button_4.setToolTip("Kliknij, aby usunać zaznaczone elementy")
        self.push_button_5.setToolTip("Kliknij, aby wyczyścić liste")
        sets = configparser.ConfigParser()
        sets = settings.loadConf()
        global pathDirectory
        global zipsFolder

        self.returnedFiles = []
        self.boxIsChecked = False
        self.selectedRecipe = str(pathDirectory+zipsFolder+sets['user']['default-recipe'])
        self.items_changed()

 # << END of: Custom Main Widget >> #
    def aboutGPadnoc(self):
        dialog = AboutDialog()
        dialog.exec_()

    def instruction(self):
        dialog = UseDialog()
        dialog.exec_()

    def settings(self,loadedRecipe):
        dialog = SettingsDialog(loadedRecipe)
        self.setFont(QFont(sets['user']['font-name'],int(sets['user']['font-size'])))
        dialog.exec_()
 # << Listwidget handling >> #

    # clear current selected item
    def clear_selected_items(self):
        for select in self.list_widget_1.selectedItems():
            self.list_widget_1.takeItem(self.list_widget_1.row(select))
        self.items_changed()

    def check_extensions(self):
        if (self.list_widget_1.count()):
            ext = self.list_widget_1.item(0).showExtension()
            for x in range (self.list_widget_1.count()):
                if(str(ext) != str(self.list_widget_1.item(x).showExtension())):
                    #print ("check_extension return: \nFalse, because list included different extensions.\nDisable checkBox")  # for debugging
                    self.check_box_1.setChecked(False)
                    self.check_box_1.setEnabled(False)
                    return False
            #print ("check_extension return: \nTrue, because list included the same extensions.\nEnable checkBox")   # for debugging

            self.check_box_1.setEnabled(True)
        self.check_box_1.setEnabled(True)
        return True

    def items_changed(self):
        if (self.selectedRecipe == None and defaultRecipe==None or self.list_widget_1.count()==0):
            self.push_button_3.setEnabled(False)
            self.check_extensions()
        else:
            self.push_button_3.setEnabled(True)
            self.check_extensions()




    # clear all files on the list
    def clear_all_items(self):
        self.list_widget_1.clear()
        self.items_changed()

    # select all files on the list
    def select_items(self):
        self.list_widget_1.selectAll()
        #print("\n" + str(listPaths)) # chcek list values: listPaths
        for x in range(self.list_widget_1.count()):
            print(self.list_widget_1.item(x).showPath())

    def print_extensions(self):
        for x in range (self.list_widget_1.count()):
            print(self.list_widget_1.item(x).showExtension())

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        self.items_changed()

 # << ADD paths on list_widget_1 from listPaths used pop()  >> #
    def add_to_list_widget(self, listPaths):
        for path in listPaths:
            fileName = str(path).split("/")
            item = MyListWidgetItem(path)
            item.setText(fileName[-1])
            item.setPath(str(path))
            self.list_widget_1.addItem(item)
        self.print_extensions() # for debugging
        self.check_extensions()

 # << Load files on >> #



    def load_files(self):
        listPaths = []
        files, _ = QFileDialog.getOpenFileNames(self, "Wybierz pliki", '',
                                                "wszystkie (*);;"+"commonmark (*.commonmark);;"+
                                                "docbook (*.docbook);;"+"docx (*.docx);;"+"epub (*.epub);;"+
                                                "haddock (*.haddock);;"+"html (*.html);;"+"json (*.json);;"+
                                                "latex (*.latex);;"+"markdown (*.markdown *.md);;"+"markdown_github (*.markdown_github);;"+
                                                "markdown_mmd (*.markdown_mmd);;"+"markdown_phpextra (*.markdown_phpextra);;"+
                                                "markdown_strict (*.markdown_strict);;"+"mediawiki (*.mediawiki);;"+
                                                "native (*.native);;"+"odt (*.odt);;"+"opml (*.opml);;"+"org (*.org);;"+
                                                "rst (*.rst);;"+"t2t (*.t2t);;"+"textile (*.textile);;"+"twiki (*.twiki)")

        for file in files:
            listPaths.append(file)
        print(listPaths)  # for debugging
        self.add_to_list_widget(listPaths)
        self.items_changed()

 # << END of: Load files on >> #
    def return_boxIsChecked(self):
        self.isChecked =  self.check_box_1.checkState()
        return self.isChecked

    def return_files(self):
        self.returnedFiles = []
        for x in range(self.list_widget_1.count()):
            self.returnedFiles.append(self.list_widget_1.item(x).showPath())
        return self.returnedFiles
 # << >>

 # << Select recipe - handling >> #
    def select_recipe(self):
        global zipsFolder
        recipeDialog=None
        recipeDialog = RecipeDialog(recipeDialog, self.selectedRecipe,zipsFolder)
        self.selectedRecipe = recipeDialog.retRecipe()
        self.items_changed()
        print(self.selectedRecipe)   # for debugging

 # << END of: Select recipe - handling >> #with ZipFile('spam.zip') as myzip:


    def conf_variables(self):
        bookName = str(self.line_edit_1.text())
        variablesDialog = VariablesDialog(self.selectedRecipe, self.return_files(), self.return_boxIsChecked(), bookName)
        variablesDialog.exec_()
        self.shellCommand()

    def shellCommand(self):
        command = None


# <<< END OF MAINWINDOW >>> #


# <<< CONFIG VARIABLES >>> #


class Table(QtWidgets.QTableWidget):

    def __init__(self):
        super(Table, self).__init__()
        self.rows_number = 0
        self.columns_number = 1
        self.setRowCount(self.rows_number)
        self.setColumnCount(self.columns_number)
        self.setup_empty_table()

        # < ADD PushButton and connect with function add_cell > #
        self.button_form = QtWidgets.QPushButton()
        self.button_form.setText("Nowe pole")
        self.button_form.clicked.connect(self.add_cell)

        self.button_form2 = QtWidgets.QPushButton()
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


class RecipeDialog(QtWidgets.QDialog, recipe_ui.Ui_Dialog):
    def __init__(self,app,selectedRecipe,zipsFolder):
        super(RecipeDialog, self).__init__()
        recipe_ui.Ui_Dialog.setupUi(self, self)
        self.zipPackages =[]
        self.loadedRecipe = selectedRecipe
        self.path = os.path.dirname(__file__)
        self.dialog = QtWidgets.QDialog()
        self.dialog.ui = recipe_ui.Ui_Dialog()
        self.dialog.ui.setupUi(self.dialog)
        self.dialog.ui.label_1.setScaledContents(True);

        self.zipPackages  = [os.path.basename(x) for x in glob.glob(self.path+zipsFolder+'*.zip')]

        self.dialog.ui.combo_box_1.addItems(self.zipPackages)
        self.dialog.ui.combo_box_1.currentIndexChanged[str].connect(self.changeRecipe)
        self.dialog.ui.button_box_1.accepted.connect(self.accept)
        self.dialog.ui.button_box_1.rejected.connect(self.reject)
        self.showPreviewOfRecipe()
        self.dialog.exec_()

    def accept(self):
        self.loadedRecipe = str(self.path+ zipsFolder+ str(self.dialog.ui.combo_box_1.currentText()))
        print("Current loaded recipe: "+ self.loadedRecipe)   # for debugging
        self.retRecipe()
        super().accept()

    def reject(self):
        super().reject()

    def retRecipe(self):
        return (self.loadedRecipe)

    def setRecipe(self):
        self.dialog.ui.combo_box_1.setCurrentText(str(self.loadedRecipe))

    def showPreviewOfRecipe(self):
        zippedImgs = ZipFile(self.path+zipsFolder+str(self.dialog.ui.combo_box_1.currentText()))

        for i in range(len(zippedImgs.namelist())):

            file_in_zip = zippedImgs.namelist()[i]
            self.dialog.ui.label_2.setText("Brak podglądu")
            self.dialog.ui.label_2.setScaledContents(True)

            if ("preview" in file_in_zip):
                print ("Found image: ", file_in_zip, " -- ")  # for debugging
                data = zippedImgs.read(file_in_zip)       # read bits to variable
                dataEnc = io.BytesIO(data)                # save bytes like io
                dataImgEnc = Image.open(dataEnc)          # convert bytes on Image file
                qimage = ImageQt.ImageQt(dataImgEnc)      # create QtImage from Image
                pixmap = QtGui.QPixmap.fromImage(qimage)  # convert QtImage to QPixmap
                print(pixmap)     # for debugging
                self.dialog.ui.label_2.setPixmap(pixmap)

    def changeRecipe(self):
        print(self.dialog.ui.combo_box_1.currentText())
        self.showPreviewOfRecipe()

class VariablesDialog(QDialog, variables_ui.Ui_Dialog):
    def __init__(self, loadedRecipe, gfiles, boxIsChecked, bookName):
        super(VariablesDialog,  self).__init__()
        variables_ui.Ui_Dialog.setupUi(self,self)
        self.tempFolder="/temp/"
        self.form=[]
        self.bookName = bookName
        self.attributes = {}
        self.getFiles = gfiles
        global pathDirectory
        self.saveDir = pathDirectory
        self.boxIsChecked = boxIsChecked
        if (loadedRecipe==""):
            self.loadedRecipe = defaultRecipe
        else:
            self.loadedRecipe=loadedRecipe
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
                if isinstance (w, QtWidgets.QLabel):
                    self.getsTable = []
                    self.getsTable.append(w.text().encode('utf-8').decode('utf-8'))
                    key_value = True

                if isinstance (w, Table):
                    for i in range(w.rowCount()):
                        itm = w.item(i,0)
                        self.getsTable.append(itm.text().encode('utf-8').decode('utf-8'))

                    if key_value:
                        self.attributes[self.getsTable[0]] = self.getsTable[1:]
                        key_value = False

                if isinstance (w, QtWidgets.QLineEdit):
                    self.getsTable.append(w.text().encode('utf-8').decode('utf-8'))
                    if key_value:
                        self.attributes[self.getsTable[0]] = self.getsTable[1:]
                        key_value = False

                if isinstance (w, QtWidgets.QPlainTextEdit):
                    self.getsTable.append(w.toPlainText().encode('utf-8').decode('utf-8'))
                    if key_value:
                        self.attributes[self.getsTable[0]] = self.getsTable[1:]
                        key_value = False

    # << Set elements on form >> #
    def drawInterface(self):
        for elem in self.form:
            self.form_layout.addRow(elem)

    def load_table_of_lists(self,names_of_lists):
        #for element in name_of_lists:
        for name_of_list in names_of_lists:
            self.label= QtWidgets.QLabel(name_of_list)
            self.label.setMinimumWidth(100)
            self.label.setText(str(name_of_list))
            self.label.setObjectName(str(name_of_list) + "_label")

            self.table_widget = Table()
            self.table_widget.setHorizontalHeaderLabels([str(name_of_list)])
            self.table_widget.setObjectName(self.label.text() + "_table_widget")

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

            self.label= QtWidgets.QLabel(variable)
            self.label.setMinimumWidth(100)
            self.label.setText(str(variable))
            self.label.setObjectName(self.label.text()+ "_label")
            self.line_edit= QtWidgets.QLineEdit("Wartość")
            self.box = QtWidgets.QHBoxLayout()
            self.box.addWidget(self.label)
            self.box.addWidget(self.line_edit)
            self.form.append(self.box)

        self.drawInterface()

    def load_table_of_texts(self, names_of_texts):

        for text in names_of_texts:

            self.label= QtWidgets.QLabel(text)
            self.label.setText(str(text))
            self.label.setMinimumWidth(100)
            self.label.setMinimumHeight(100)
            self.label.setScaledContents(True)
            self.label.setObjectName(self.label.text()+ "_label")

            self.plain_text= QtWidgets.QPlainTextEdit("Wartość tekstowa")

            # create layout vertical for label and list(at the moment still combobox)
            self.box = QtWidgets.QHBoxLayout()
            self.box.addWidget(self.label)
            self.box.addWidget(self.plain_text)
            self.form.append(self.box)

            #self.form.append(self.combobox)

        self.drawInterface()

    def unzip(self):
        with zipfile.ZipFile(self.loadedRecipe) as zf:
            zf.extractall(self.saveDir+self.tempFolder)

    def clear_dir(self):
        shutil.rmtree(self.saveDir+self.tempFolder,True)

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
                inputFile.append(str(path))    #input file
            if(self.template_name): #template file
                templateFile='--template='+self.saveDir+self.tempFolder + str(self.template_name[0])
                print (templateFile)
            for attr in self.attributes.keys():
                for e in self.attributes[attr]:    #variables skime ex.: -V authors = "Szymborska"
                    variables.append('-V')
                    variables.append(attr+ '=' + e)

            outputFile+='--output='+ self.saveDir+'/outputs/'+self.bookName+'.'+self.output_format[0]

                #print([pandoc,inputFile,templateFile,variables,outputFile])

            if(templateFile!=""):
                try:
                    print (*[pandoc,*inputFile,templateFile,*variables,outputFile])  # for debagging
                    subprocess.run([pandoc,*inputFile,templateFile,*variables,outputFile])
                except subprocess.errno:
                    print("error until call to pandoc")
                print("[*] Done")  # for debugging
            else:
                try:
                    print (*[pandoc,*inputFile,*variables,outputFile])  # for debagging
                    subprocess.run([pandoc,*inputFile,*variables,outputFile])
                except subprocess.errno:
                    print("error until call to pandoc")
                print("[*] Done")  # for debugging

            inputFile = []
            templateFile = ""
            variables =[]
            outputFile=""

        else:

            num = 0
            inputFile =""
            for path in self.getFiles:
                num+=1
                inputFile=str(path)    #input file

                if(self.template_name): #template file
                    templateFile='--template='+self.saveDir+self.tempFolder + str(self.template_name[0])
                for attr in self.attributes.keys():
                    for e in self.attributes[attr]:    #variables skime ex.: -V authors = "Szymborska"
                        variables.append('-V')
                        variables.append(attr+ '=' + e)

                outputFile+='--output='+ self.saveDir+'/outputs/'+self.bookName+"_"+str(num)+'.'+self.output_format[0]

                if(templateFile!=""):
                    try:
                        #check is temaplate of pdf
                        print (*[pandoc,inputFile,templateFile,*variables,outputFile])  # for debagging
                        subprocess.run([pandoc,inputFile,templateFile,*variables,outputFile])
                    except subprocess.errno:
                        print("error until call to pandoc")
                    print("[*] Done")  # for debugging
                else:
                    try:
                        print (*[pandoc,inputFile,*variables,outputFile])  # for debagging
                        subprocess.run([pandoc,inputFile,*variables,outputFile])
                    except subprocess.errno:
                        print("error until call to pandoc")
                    print("[*] Done")  # for debugging

                templateFile = ""
                variables =[]
                outputFile=""

        super(VariablesDialog, self).accept()


# <<< END of: CONFIG VARIABLES >>> #
