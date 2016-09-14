import sys

from ui import recipe_ui
from ui import variables_ui

#from current_conf import conf.txt
from ui.mainwindow_ui import Ui_MainWindow


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,  QFileDialog, QTextEdit, QDialog, \
                            QPushButton, QListWidget, QListWidgetItem, QAbstractItemView, QMouseEventTransition, QAction,QDialog, QComboBox
from PyQt5.QtCore import QFile, QFileDevice, QFileSelector, QFileInfo, QDirIterator, pyqtWrapperType, qDebug, Qt
from PyQt5.QtGui import QIcon


# <<< SETTINGS Variables >>> # 
data_of_list=[]
class CurrentConfig():
    
    def __init__(self):
        super(CurrentConfig, self).__init__()
        File = open("conf.txt", "r+")
        self.load_conf(File)
        
    def load_conf(self, File):
        
        pass

    def save_conf(self,File):
        pass

# <<< END of: SETTINGS Variables >>> # 


        
    

# <<< MAINWINDOW >>> #

class MainWindow(QMainWindow, Ui_MainWindow):

 # Lista plikow 
       	
    def __init__(self, app, parent=None):
        super(MainWindow, self).__init__(parent)
        
        Ui_MainWindow.setupUi(self, self)

        self.push_button_1.clicked.connect(self.load_files)
        self.push_button_4.clicked.connect(self.clear_selected_items)
        self.push_button_5.clicked.connect(self.clear_all_items)
        self.push_button_2.clicked.connect(self.select_recipe)
        self.push_button_3.clicked.connect(self.config_output)
        self.show()
                   
        self.list_widget_1.setAcceptDrops(True)
        self.list_widget_1.setMouseTracking(True)
        self.list_widget_1.setDragDropMode(QAbstractItemView.InternalMove)
        self.list_widget_1.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.list_widget_1.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)

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
        self.list_widget_1.setToolTip("Aby dodać pliki skorzystaj z przycisku wybierz. \nAby wyświetlić szybkie menu kliknij prawym przyciskiem. ")
	


 # << Listwidget handling >> #

    # clear current selected item
    def clear_selected_items(self):
        for selected_item in self.list_widget_1.selectedItems():
            self.list_widget_1.takeItem(self.list_widget_1.row(selected_item))
          #  data_of_list.
         

    # clear all files on the list
    def clear_all_items(self):
        self.list_widget_1.clear()
        data_of_list.clear()

    # select all files on the list
    def select_items(self):
        self.list_widget_1.selectAll();
        qDebug("\n" + str(data_of_list)) # chcek list values: data_of_list 

    
   # EVENT: drag item on list
   # def dragEnterEvent(self, event):
   #     if event.mimeData().hasUrls():
   #         event.acceptProposedAction()
   #    else:
   #         super(self.list_widget_1, self).dragEnterEvent(event)

   #  EVENT: move item on list
   # def dragMoveEvent(self, event):
   #     super(self.list_widget_1, self).dragMoveEvent(event)


   # EVENT: Put elements on the list 
   # def dropEvent(self, event):
   #     if event.mimeData().hasUrls():
   #         for url in event.mimeData().urls():
   #             self.list_widget_1.addItem(url.path())
		

   #         event.acceptProposedAction()
   #     else:
   #         super(self.list_widget_1, self).dropEvent(event)

 # << END of: Listwidget handling >> #


	
 # << ADD paths on list_widget_1 from list_of_paths used pop()  >> #
    def add_to_list_widget(self, list_of_paths):
     while list_of_paths:
             self.list_widget_1.addItem(list_of_paths.pop())


	
 # << Load files on >> #
    def load_files(self):
        list_of_paths = []
        file_paths, _ = QFileDialog.getOpenFileNames(self, "Wybierz pliki", '',"Documents(*.txt *.doc, *.docx, *.pdf);; Markdown (*.md);; Mobi (*.mobi);; All Files (*)")

        for file_path in file_paths:
            list_of_paths.append(file_path)
            data_of_list.append(file_path)
        print(list_of_paths)
        self.add_to_list_widget(list_of_paths)
   
 # << END of: Load files on >> #
    


 # << Select recipe - handling >> # 
    def select_recipe(self):
        recipe_dialog = QtWidgets.QDialog()
        recipe_dialog.ui = recipe_ui.Ui_Dialog()
        recipe_dialog.ui.setupUi(recipe_dialog)
	
        recipe_dialog.exec_()

 # << END of: Select recipe - handling >> #

    def config_output(self):
        config_dialog = VariablesDialog()
        config_dialog.exec_()


# <<< END OF MAINWINDOW >>> #




# <<< CONFIG VARIABLES >>> #

import recipe
import string
import logging
import configparser
from zipfile import ZipFile



class Table(QtWidgets.QTableWidget):
    def __init__(self, parent=None):
        super(Table, self).__init__(parent)
        
        self.setColumnCount(1)

        self.button_form = QtWidgets.QPushButton()
        self.button_form.setText("Nowe pole")
        self.button_form.clicked.connect(self.add_cell)

        self.row = self.currentRow()
        self.col = self.currentColumn()
        self.count = 1
        self.populate()
        

    def populate(self):
        self.setRowCount(self.count)
        self.setItem(self.count, 0, QtWidgets.QTableWidgetItem("standard")) 
        self.horizontalHeader().setStretchLastSection(True)
   

    def c_current(self):
        self.row = self.currentRow()
        self.col = self.currentColumn()
        print("Current row is ", self.row)
        print("In this cell we have: ", self.value)

    def add_cell(self):
        
        self.count = self.count+1
        self.setRowCount(self.count)
        self.setItem(self.count,0, QtWidgets.QTableWidgetItem())
        self.show()
        
class VariablesDialog(QDialog, variables_ui.Ui_Dialog):
    
   
    def __init__(self):
        super(VariablesDialog,  self).__init__()
        
        variables_ui.Ui_Dialog.setupUi(self,self)

        self.names_of_lists = ['list', 'list2']
        self.names_of_variables = ['var1','var2']
        self.form=[]

        self.load_table_of_lists(self.names_of_lists)
        self.load_table_of_variables(self.names_of_variables)

        qDebug(str(self.form[0]))
    
    # << Set elements on form >> #
    def draw_lists(self):
        for elem in self.form:
            self.form_layout.addRow(elem)
    
    def load_table_of_lists(self,names_of_lists):
              
        #for element in name_of_lists:

        for name_of_list in names_of_lists: 
            
            self.label= QtWidgets.QLabel(name_of_list)

            self.label.setText(str(name_of_list))
            self.label.setObjectName(str(name_of_list) + "_label")
           
            self.table_widget = Table()

            self.table_widget.setHorizontalHeaderLabels([str(name_of_list)])
            self.table_widget.setObjectName(self.label.text() + "_table_widget")
       
            self.Hbox = QtWidgets.QHBoxLayout()
            self.Hbox.addWidget(self.label)
            self.Hbox.addWidget(self.table_widget)
            
            self.Vbox = QtWidgets.QVBoxLayout()
            self.Vbox.addLayout(self.Hbox)
            self.Vbox.addWidget(self.table_widget.button_form)

            #self.form.append(self.button_form)
            self.form.append(self.Vbox)
            #self.form.append(self.combobox)

        self.draw_lists()   
    def add_cell(self):
        pass

    def load_table_of_variables(self, names_of_variables):
            
        for variable in names_of_variables: 
            
            self.label= QtWidgets.QLabel(variable)
            self.label.setText(str(variable))
            self.label.setObjectName(self.label.text()+ "_label")
            
            self.line_edit= QtWidgets.QLineEdit("Wartość")     

            # create layout vertical for label and list(at the moment still combobox)
            self.box = QtWidgets.QHBoxLayout()
            self.box.addWidget(self.label)
            self.box.addWidget(self.line_edit)
        
            self.form.append(self.box)
            #self.form.append(self.combobox)

        self.draw_lists()

    def load_table_of_text(self, _of_variables):
        pass
    
    def bulid_menu(self):
        pass
        
        
# <<< END of: CONFIG VARIABLES >>> #




