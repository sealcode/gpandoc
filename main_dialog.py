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
        dialog = InstructionDialog()
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
        recipeDialog.exec_()
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
