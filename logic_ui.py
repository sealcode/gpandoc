import io
import os
import sys
import glob
import recipe
import configparser

from os import path
from subprocess import call
from zipfile import ZipFile


from PIL import Image,ImageQt
from ui import recipe_ui
from ui import variables_ui
from ui.mainwindow_ui import Ui_MainWindow

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtCore import QFile, QFileDevice, QFileSelector, QFileInfo, QDirIterator, pyqtWrapperType, qDebug, Qt, QEvent
from PyQt5.QtWidgets import QApplication, QMainWindow,  QFileDialog, QSlider, QTextEdit, QDialog, QDialogButtonBox, \
                            QPushButton, QListWidget, QListWidgetItem, QAbstractItemView,QMouseEventTransition, QSizePolicy,QSpacerItem, QAction, QDialog, QComboBox



# <<< SETTINGS Variables >>> # 
list_of_paths=[]
class CurrentConfig():
    
    def __init__(self):
        super(CurrentConfig, self).__init__()
        File = open("conf.py", "r+")
        self.load_conf(File)
        
    def load_conf(self, File):  
        pass

    def save_conf(self,File):
        pass

# <<< END of: SETTINGS Variables >>> # 

        
# <<< MAINWINDOW >>> #

class MainWindow(QMainWindow, Ui_MainWindow):
    

  # << Custon Main Widget >> #
    def __init__(self, app):
        super(MainWindow, self).__init__()
            
        
        Ui_MainWindow.setupUi(self, self)
        self.push_button_1.clicked.connect(self.load_files)
        self.push_button_4.clicked.connect(self.clear_selected_items)
        self.push_button_5.clicked.connect(self.clear_all_items)
        self.push_button_2.clicked.connect(self.select_recipe)
        self.push_button_3.clicked.connect(self.conf_variables)
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
     #  self.list_widget_1.setToolTip("Aby dodać pliki skorzystaj z przycisku wybierz pliki." +
                                   #   "\nAby wyświetlić szybkie menu kliknij prawym przyciskiem. ")
        self.ret_files = []
        self.loadedRecipe = None
        self.items_changed()

    # << END of: Custom Main Widget >> #
 # << Listwidget handling >> #2

    def update_python_list(self):
        list_of_paths.clear()
        for x in range(self.list_widget_1.count()):
            list_of_paths.append(self.list_widget_1.item(x).text())

    # clear current selected item
    def clear_selected_items(self):
        for selected_item in self.list_widget_1.selectedItems():    
            self.list_widget_1.takeItem(self.list_widget_1.row(selected_item))
        self.update_python_list()
        self.items_changed()
       
    
         
    def items_changed(self):
        self.update_python_list()

        if self.loadedRecipe == None or self.list_widget_1.count()==0:
            self.push_button_3.setEnabled(False)
        else:
            self.push_button_3.setEnabled(True)

   
    # clear all files on the list
    def clear_all_items(self):
        self.list_widget_1.clear()
        list_of_paths.clear()
        self.items_changed()

    # select all files on the list
    def select_items(self):
        self.list_widget_1.selectAll();
        print("\n" + str(list_of_paths)) # chcek list values: list_of_paths

    def dragEnterEvent(self, e):
        e.accept()
        self.update_python_list()

    def dropEvent(self, e):
        self.items_changed()

 # << ADD paths on list_widget_1 from list_of_paths used pop()  >> #
    def add_to_list_widget(self, list_of_paths):
        for path in list_of_paths:
            self.list_widget_1.addItem(str(path))
        count = self.list_widget_1.count()
        for x in range(count):
            name_of_file = self.list_widget_1.item(x).text().split("/")
            self.list_widget_1.item(x).setToolTip(name_of_file[-1])

 # << Load files on >> #
    def load_files(self):
        list_of_paths = []
        file_paths, _ = QFileDialog.getOpenFileNames(self, "Wybierz pliki", '',"Dokumenty (*.txt *.odt *.doc *.docx *.pdf) "+
                                                           ";; Markdown (*.md);; pdf (*.pdf);; txt (*.txt);; doc (*.doc);; docx (*.docx);; Mobi (*.mobi);; Wszystkie (*)")
        for file_path in file_paths:
            list_of_paths.append(file_path)
        print(list_of_paths)
        self.add_to_list_widget(list_of_paths)
        self.items_changed()
   
 # << END of: Load files on >> #
    
    def return_files(self):
        self.ret_files = []
        for i in range (self.list_widget_1.count()):
            self.ret_files.append(self.list_widget_1.item(i).text().encode('utf-8').decode('utf -8'))
        print("Return files: ", self.ret_files)
        return self.ret_files
 # << >>
  
 # << Select recipe - handling >> # 
    def select_recipe(self):
        recipeDialog=None
        recipeDialog = RecipeDialog(recipeDialog, self.loadedRecipe) 
        self.loadedRecipe = recipeDialog.retRecipe()
        self.items_changed()
        print(self.loadedRecipe)
        
 # << END of: Select recipe - handling >> #

    def conf_variables(self):
        variablesDialog = VariablesDialog(self.loadedRecipe, self.return_files())
        variablesDialog.exec_()
        self.shellCommand()
    
    def shellCommand(self):
        call(["echo", "SHELL COMMAND"])

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
    def __init__(self,app,loadedRecipe):
        super(RecipeDialog, self).__init__()
        recipe_ui.Ui_Dialog.setupUi(self, self)
        
        self.zipPackages =[]
        self.loadedRecipe = loadedRecipe
        self.path = os.path.dirname(__file__)     
        self.dialog = QtWidgets.QDialog()
        self.dialog.ui = recipe_ui.Ui_Dialog()
        self.dialog.ui.setupUi(self.dialog)
        self.dialog.ui.label_1.setScaledContents(True);
        
        self.zipPackages  = [os.path.basename(x) for x in glob.glob(self.path+'/zips/*.zip')]
        print (self.zipPackages)
        
        self.dialog.ui.combo_box_1.addItems(self.zipPackages)
        print(self.dialog.ui.combo_box_1.currentText())
        self.changeRecipe()
        self.dialog.ui.combo_box_1.currentIndexChanged[str].connect(self.changeRecipe)   
        self.dialog.ui.button_box_1.accepted.connect(self.accept)
        self.dialog.ui.button_box_1.rejected.connect(self.reject)
        self.dialog.exec_()
        
    def accept(self): 
        self.loadedRecipe = str(self.path+ "/zips/" + str(self.dialog.ui.combo_box_1.currentText()))
        print("Current loaded recipe: "+ self.loadedRecipe)
        self.retRecipe()
        super().accept()
    
    def reject(self):
        super().reject()
    
    def retRecipe(self):
        return (self.loadedRecipe)
       
    def changeRecipe(self): 
        print(self.dialog.ui.combo_box_1.currentText()) 
        print (str('zips/'+self.dialog.ui.combo_box_1.currentText()))
        zippedImgs = ZipFile(self.path+'/zips/'+str(self.dialog.ui.combo_box_1.currentText()))
        for i in range(len(zippedImgs.namelist())):
            file_in_zip = zippedImgs.namelist()[i]
            if (".png" in file_in_zip or ".PNG" in file_in_zip):
                print ("Found image: ", file_in_zip, " -- ")
                data = zippedImgs.read(file_in_zip)       # read bits to variable                                                      
                dataEnc = io.BytesIO(data)                # save bytes like io              
                dataImgEnc = Image.open(dataEnc)          # convert bytes on Image file            
                qimage = ImageQt.ImageQt(dataImgEnc)      # create QtImage from QImage
                pixmap = QtGui.QPixmap.fromImage(qimage)  # convert QtImage to QPixmap      
                print(pixmap)
                self.dialog.ui.label_2.setPixmap(pixmap)  
                self.dialog.ui.label_2.setScaledContents(True)
            else:
                self.dialog.ui.label_2.setText("Brak podglądu")
                 
        
class VariablesDialog(QDialog, variables_ui.Ui_Dialog):
    def __init__(self, loadedRecipe, gfiles):
        super(VariablesDialog,  self).__init__()
        variables_ui.Ui_Dialog.setupUi(self,self)
      
        self.form=[]
        self.attributes = {}   
        self.get_files = gfiles
        self.names_of_lists = recipe.Recipe(loadedRecipe).lists
        self.names_of_variables = recipe.Recipe(loadedRecipe).strings
        self.names_of_texts = recipe.Recipe(loadedRecipe).texts         
        self.load_table_of_lists(self.names_of_lists)
        self.load_table_of_variables(self.names_of_variables)
        self.load_table_of_texts(self.names_of_texts)

    def print_ok(self):
        print(str("O.K"))     
        
    def accept(self):
        self.get_values()    
        ret ={ "all-attributes": self.attributes, "all-files": self.get_files }
        
        ## Place where is generate otuput for pandoc
        
        print(ret)
        super(VariablesDialog, self).accept()

    
    def reject(self):
        super(VariablesDialog, self).reject()
    
  

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
    def draw_lists(self):
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
          
            
        self.draw_lists()   

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

        self.draw_lists()

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

        self.draw_lists()

    
        
# <<< END of: CONFIG VARIABLES >>> #




