import sys

from ui import recipe_ui
from ui.mainwindow_ui import Ui_MainWindow
from ui import variables_ui

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,  QFileDialog, QTextEdit, QDialog, \
                            QPushButton, QListWidget, QListWidgetItem, QAbstractItemView, QMouseEventTransition, QAction,QDialog, QComboBox
from PyQt5.QtCore import QFile, QFileDevice, QFileSelector, QFileInfo, QDirIterator, pyqtWrapperType, qDebug, Qt
from PyQt5.QtGui import QIcon

### Commented class current not used 
class ListWidget(QListWidget):

    def __init__(self, parent=None):
        super(ListWidget, self).__init__(parent)
        self.setAcceptDrops(True)
        self.setMouseTracking(True)
        self.setDragDropMode(QAbstractItemView.InternalMove)
        self.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)

        # Actions for mouse right click
        quit_action_1 = QAction("Zamknij", self, shortcut="Ctrl+Q", triggered=QApplication.instance().quit)
        quit_action_2 = QAction("Czyść", self, triggered=self.clearAllItems)
        quit_action_3 = QAction("Zaznacz wszystko", self, shortcut="Ctrl+A", triggered=self.select_items)
        quit_action_4 = QAction("Usuń zaznaczone", self, shortcut="Del",triggered=self.clear_selected_items)
        self.addAction(quit_action_4)
        self.addAction(quit_action_3)
        self.addAction(quit_action_2)
        self.addAction(quit_action_1)

        # Info for users how to add files
        self.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.setToolTip("Aby dodać pliki skorzystaj z przycisku wybierz, lub przeciągnij je i upuść na liście")

    # clear current selected item
    def clear_selected_items(self):
        for selected_item in self.selectedItems():
            self.takeItem(self.row(selected_item))

    # clear all files on the list
    def clear_all_items(self):
        self.clear()

    # select all files on the list
    def select_items(self):
        self.selectAll();

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            super(ListWidget, self).dragEnterEvent(event)

    # event
    def dragMoveEvent(self, event):
            super(ListWidget, self).dragMoveEvent(event)
    # event
    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                self.addItem(url.path())
            event.acceptProposedAction()
        else:
            super(ListWidget, self).dropEvent(event)


# <<< SETTINGS Variables >>> # 

data_of_list = [] 
join_files = False
allow_repeat = False

# <<< END of: SETTINGS Variables >>> # 
  


# <<< MAINWINDOW >>> #

class MainWindow(QMainWindow, Ui_MainWindow):

 # Lista plikow 
       	
    def __init__(self, app, parent=None):
        super(MainWindow, self).__init__(parent)
        
        Ui_MainWindow.setupUi(self, self)

        self.push_button_1.clicked.connect(self.load_files)
        self.push_button_2.clicked.connect(self.clear_selected_items)
        self.push_button_3.clicked.connect(self.clear_all_items)
        self.push_button_4.clicked.connect(self.select_recipe)
        self.push_button_5.clicked.connect(self.config_output)
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

class VariablesDialog(QDialog, variables_ui.Ui_Dialog):

    names_of_lists = [ 'Lista1',{"value1", "Value2" },'Lista2','Lista3']
    def __init__(self):
        super(VariablesDialog,  self).__init__()
        
        variables_ui.Ui_Dialog.setupUi(self,self)
        

        self.load_table_of_lists(self.names_of_lists)
    
    def load_table_of_lists(self,names_of_lists):
              
        #for element in name_of_lists:
        for name_of_list in names_of_lists: 

            auto_label = QtWidgets.QLabel()
            auto_label.setText(str(name_of_list))
            auto_label.setObjectName(auto_label.text()+ "_label")

            auto_combobox = QtWidgets.QComboBox()
            auto_combobox.setObjectName(auto_label.text()+ "_combobox")

            auto_layout = QtWidgets.QVBoxLayout()
            auto_layout.setObjectName(auto_label.text() + "_layout")
            
            #auto_layout.addWidget(auto_label)
            #auto_layout.addWidget(auto_combobox)
            for elements in name_of_list:
                auto_combobox.addItem(elements)

            self.form_layout.addRow(auto_label, auto_combobox)
                

    def load_table_of_variables(self, names_of_variables):
        pass

    def load_table_of_text(self, _of_variables):
        pass
    
    def bulid_menu(self):
        
        pass
        
        
# <<< END of: CONFIG VARIABLES >>> #




