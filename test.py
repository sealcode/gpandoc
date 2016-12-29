     def changeRecipe(self): 
        print (str('zips/'+self.dialog.ui.combo_box_1.currentText()))
        zippedTemp = ZipFile(self.path+'/zips/'+str(self.dialog.ui.combo_box_1.currentText()))
        for i in range(len(zippedTemp.namelist())):
            file_in_zip = zippedTemp.namelist()[i]
            if ("template." in file_in_zip):
                print ("Found template: ", file_in_zip, " -- ")
                data = zippedTemp.read(file_in_zip)       # read bits to variable                                                      
                dataEnc = io.BytesIO(data)                # save bytes like io              
                dataImgEnc = File.open(dataEnc)          # convert bytes on Image file            
                qimage = ImageQt.ImageQt(dataImgEnc)      # create QtImage from QImage
                pixmap = QtGui.QPixmap.fromImage(qimage)  # convert QtImage to QPixmap      
                print(pixmap)
                self.dialog.ui.label_2.setPixmap(pixmap)  
                self.dialog.ui.label_2.setScaledContents(True)
            else:
                self.dialog.ui.label_2.setText("Brak podglądu")
                 