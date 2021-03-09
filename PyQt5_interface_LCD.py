from PyQt5 import QtCore, QtGui, QtWidgets
from time import sleep
import serial
port = serial.Serial("COM3",baudrate=9600)

class Ui_Form():
        def setupUi(self, Form):
                Form.setObjectName("Form")
                Form.resize(1050, 600)

                self.digit1 = QtWidgets.QLineEdit(Form)
                self.digit1.setGeometry(QtCore.QRect(40, 20, 40, 60))
                self.digit1.setObjectName("digit1")

                self.digit2 = QtWidgets.QLineEdit(Form)
                self.digit2.setGeometry(QtCore.QRect(100, 20, 40, 60))
                self.digit2.setObjectName("digit2")

                self.digit3 = QtWidgets.QLineEdit(Form)
                self.digit3.setGeometry(QtCore.QRect(160, 20, 40, 60))
                self.digit3.setObjectName("digit3")

                self.digit4 = QtWidgets.QLineEdit(Form)
                self.digit4.setGeometry(QtCore.QRect(220, 20, 40, 60))
                self.digit4.setObjectName("digit4")

                self.digit5 = QtWidgets.QLineEdit(Form)
                self.digit5.setGeometry(QtCore.QRect(280, 20, 40, 60))
                self.digit5.setObjectName("digit5")

                self.digit6 = QtWidgets.QLineEdit(Form)
                self.digit6.setGeometry(QtCore.QRect(340, 20, 40, 60))
                self.digit6.setObjectName("digit6")

                self.digit7 = QtWidgets.QLineEdit(Form)
                self.digit7.setGeometry(QtCore.QRect(400, 20, 40, 60))
                self.digit7.setObjectName("digit7")

                self.digit8 = QtWidgets.QLineEdit(Form)
                self.digit8.setGeometry(QtCore.QRect(460, 20, 40, 60))
                self.digit8.setObjectName("digit8")

                self.digit9 = QtWidgets.QLineEdit(Form)
                self.digit9.setGeometry(QtCore.QRect(520, 20, 40, 60))
                self.digit9.setObjectName("digit9")

                self.digit10 = QtWidgets.QLineEdit(Form)
                self.digit10.setGeometry(QtCore.QRect(580, 20, 40, 60))
                self.digit10.setObjectName("digit10")

                self.digit11 = QtWidgets.QLineEdit(Form)
                self.digit11.setGeometry(QtCore.QRect(640, 20, 40, 60))
                self.digit11.setObjectName("digit11")

                self.digit12 = QtWidgets.QLineEdit(Form)
                self.digit12.setGeometry(QtCore.QRect(700, 20, 40, 60))
                self.digit12.setObjectName("digit12")

                self.digit13 = QtWidgets.QLineEdit(Form)
                self.digit13.setGeometry(QtCore.QRect(760, 20, 40, 60))
                self.digit13.setObjectName("digit13")

                self.digit14 = QtWidgets.QLineEdit(Form)
                self.digit14.setGeometry(QtCore.QRect(820, 20, 40, 60))
                self.digit14.setObjectName("digit14")

                self.digit15 = QtWidgets.QLineEdit(Form)
                self.digit15.setGeometry(QtCore.QRect(880, 20, 40, 60))
                self.digit15.setObjectName("digit15")

                self.digit16 = QtWidgets.QLineEdit(Form)
                self.digit16.setGeometry(QtCore.QRect(940, 20, 40, 60))
                self.digit16.setObjectName("digit16")

                self.digit1_2 = QtWidgets.QLineEdit(Form)
                self.digit1_2.setGeometry(QtCore.QRect(40, 90, 40, 60))
                self.digit1_2.setObjectName("digit1_2")
                
                self.digit2_2 = QtWidgets.QLineEdit(Form)
                self.digit2_2.setGeometry(QtCore.QRect(100, 90, 40, 60))
                self.digit2_2.setObjectName("digit2_2")

                self.digit3_2 = QtWidgets.QLineEdit(Form)
                self.digit3_2.setGeometry(QtCore.QRect(160, 90, 40, 60))
                self.digit3_2.setObjectName("digit3_2")

                self.digit4_2 = QtWidgets.QLineEdit(Form)
                self.digit4_2.setGeometry(QtCore.QRect(220, 90, 40, 60))
                self.digit4_2.setObjectName("digit4_2")

                self.digit5_2 = QtWidgets.QLineEdit(Form)
                self.digit5_2.setGeometry(QtCore.QRect(280, 90, 40, 60))
                self.digit5_2.setObjectName("digit5_2")

                self.digit6_2 = QtWidgets.QLineEdit(Form)
                self.digit6_2.setGeometry(QtCore.QRect(340, 90, 40, 60))
                self.digit6_2.setObjectName("digit6_2")

                self.digit7_2 = QtWidgets.QLineEdit(Form)
                self.digit7_2.setGeometry(QtCore.QRect(400, 90, 40, 60))
                self.digit7_2.setObjectName("digit7_2")

                self.digit8_2 = QtWidgets.QLineEdit(Form)
                self.digit8_2.setGeometry(QtCore.QRect(460, 90, 40, 60))
                self.digit8_2.setObjectName("digit8_2")

                self.digit9_2 = QtWidgets.QLineEdit(Form)
                self.digit9_2.setGeometry(QtCore.QRect(520, 90, 40, 60))
                self.digit9_2.setObjectName("digit9_2")
                
                self.digit10_2 = QtWidgets.QLineEdit(Form)
                self.digit10_2.setGeometry(QtCore.QRect(580, 90, 40, 60))
                self.digit10_2.setObjectName("digit10_2")
                
                self.digit11_2 = QtWidgets.QLineEdit(Form)
                self.digit11_2.setGeometry(QtCore.QRect(640, 90, 40, 60))
                self.digit11_2.setObjectName("digit11_2")

                self.digit12_2 = QtWidgets.QLineEdit(Form)
                self.digit12_2.setGeometry(QtCore.QRect(700, 90, 40, 60))
                self.digit12_2.setObjectName("digit12_2")
                
                self.digit13_2 = QtWidgets.QLineEdit(Form)
                self.digit13_2.setGeometry(QtCore.QRect(760, 90, 40, 60))
                self.digit13_2.setObjectName("digit13_2")
               
                self.digit14_2 = QtWidgets.QLineEdit(Form)
                self.digit14_2.setGeometry(QtCore.QRect(820, 90, 40, 60))
                self.digit14_2.setObjectName("digit14_2") 
                
                self.digit15_2 = QtWidgets.QLineEdit(Form)
                self.digit15_2.setGeometry(QtCore.QRect(880, 90, 40, 60))
                self.digit15_2.setObjectName("digit15_2") 

                self.digit16_2 = QtWidgets.QLineEdit(Form)
                self.digit16_2.setGeometry(QtCore.QRect(940, 90, 40, 60))
                self.digit16_2.setObjectName("digit16_2") 

                self.children = Form.findChildren(QtWidgets.QLineEdit)
                self.children = self.children[:32]
                self.children2 = self.children[16:32]

                digitSet = (".setStyleSheet(" '"' + "{}" + '"' ")").format(r"color: rgb(252, 252, 252);\n""background-color: rgb(33, 92, 255);font: 24pt 'Arial';")       
                for child in self.children:
                        eval("self." + child.objectName() + str(digitSet))
                        eval("self." + child.objectName() + ".setEnabled(False)")
                        eval("self." + child.objectName() + ".setAlignment(QtCore.Qt.AlignCenter)")
               

                self.text_1 = QtWidgets.QLineEdit(Form)
                self.text_1.setGeometry(QtCore.QRect(160, 180, 821, 55))
                self.text_1.setStyleSheet("background-color: rgb(221, 255, 237);font: 22pt 'Arial';")
                self.text_1.setMaxLength(40)

                self.text_2 = QtWidgets.QLineEdit(Form)
                self.text_2.setGeometry(QtCore.QRect(160, 260, 821, 55))
                self.text_2.setStyleSheet("background-color: rgb(221, 255, 237);font: 22pt'Arial';")
                self.text_2.setMaxLength(40)

                self.lbl = QtWidgets.QLabel(Form)
                self.lbl.setGeometry(QtCore.QRect(40, 180, 91, 55))
                self.lbl.setStyleSheet("background-color: rgb(137, 137, 255);font: bold 16pt'Arial';")

                self.lbl_2 = QtWidgets.QLabel(Form)
                self.lbl_2.setGeometry(QtCore.QRect(40, 260, 91, 55))
                self.lbl_2.setStyleSheet("background-color: rgb(137, 137, 255);font: bold 16pt'Arial';")

                self.lbl_3 = QtWidgets.QLabel(Form)
                self.lbl_3.setGeometry(QtCore.QRect(40, 340, 161, 31))
                self.lbl_3.setStyleSheet("background-color: rgb(137, 137, 255);font: bold 16pt'Arial';")

                self.lbl_4 = QtWidgets.QLabel(Form)
                self.lbl_4.setGeometry(QtCore.QRect(10, 150, 991, 16))
                self.lbl_4.setStyleSheet("color: rgb( 0, 10, 0);font: bold 40pt'Arial';")

                self.lbl_length_err = QtWidgets.QLabel(Form)
                self.lbl_length_err.setGeometry(QtCore.QRect(580,340,380,35))
                self.lbl_length_err.setStyleSheet("background-color: rgb(255,5,5);color: rgb( 0, 10, 0);font: bold 16pt'Arial';")
                self.lbl_length_err.setText("Longer than 16 characters !!!")
                self.lbl_length_err.hide()

                self.lbl_1_length = QtWidgets.QLabel(Form)
                self.lbl_1_length.setGeometry(QtCore.QRect(990, 182, 45, 50))
                self.lbl_1_length.setStyleSheet("background-color: rgb(137, 137, 255);font: bold 23pt'Arial';")
                self.lbl_1_length.setObjectName("lbl_1_length")
                self.lbl_1_length.setText("0")
                self.lbl_1_length.setAlignment(QtCore.Qt.AlignCenter)

                self.lbl_2_length = QtWidgets.QLabel(Form)
                self.lbl_2_length.setGeometry(QtCore.QRect(990, 262, 45, 50))
                self.lbl_2_length.setStyleSheet("background-color: rgb(137, 137, 255);font: bold 23pt'Arial';")
                self.lbl_2_length.setObjectName("lbl_2_length")
                self.lbl_2_length.setText("0")
                self.lbl_2_length.setAlignment(QtCore.Qt.AlignCenter)

                self.animationComboBox = QtWidgets.QComboBox(Form)
                self.animationComboBox.setGeometry(QtCore.QRect(230, 340, 331, 31))
                self.animationComboBox.setStyleSheet("background-color: rgb(221, 255, 237);font: 14pt 'Arial';")
                self.animationComboBox.addItem("Direct Text")
                self.animationComboBox.addItem("Centered Screen Text")
                self.animationComboBox.addItem("Right Scrolling Text")
                self.animationComboBox.addItem("One by One Written Text")
                self.animationComboBox.addItem("Left Scrolling Text")
                self.animationComboBox.addItem("Flashing Text")
               
                self.butt_serial_write = QtWidgets.QPushButton(Form)
                self.butt_serial_write.setGeometry(QtCore.QRect(320, 450, 351, 51))
                self.butt_serial_write.setStyleSheet("background-color: rgb(65, 65, 255);\n""color: rgb(255, 247, 7);font: bold 20pt'Arial';")

                self.butt_clear = QtWidgets.QPushButton(Form)
                self.butt_clear.setGeometry(QtCore.QRect(320, 510, 351, 31))
                self.butt_clear.setStyleSheet("background-color: rgb(255, 33, 33);\n""color: rgb(255, 174, 174);font: 12pt'Arial';")

                self.butt_apply = QtWidgets.QPushButton(Form)
                self.butt_apply.setGeometry(QtCore.QRect(320, 390, 351, 31))
                self.butt_apply.setStyleSheet("background-color: rgb(5, 147, 255);font: bold 12pt'Arial';")

                self.retranslateUi(Form)
                QtCore.QMetaObject.connectSlotsByName(Form)

                self.text_1.textChanged.connect(lambda: self.digitsWrite(self.children[:16],self.text_1.text(),1))
                self.text_2.textChanged.connect(lambda: self.digitsWrite(self.children2,self.text_2.text(),2))
                
                self.butt_apply.clicked.connect(self.animationApply)
                self.butt_clear.clicked.connect(self.Clear)
                self.butt_serial_write.clicked.connect(self.serialWrite)

                
        def retranslateUi(self, Form):
                _translate = QtCore.QCoreApplication.translate
                Form.setWindowTitle(_translate("Form", "LCD Serial Control"))
                self.lbl.setText(_translate("Form", "1.Line"))
                self.lbl_2.setText(_translate("Form", "2.Line"))
                self.lbl_3.setText(_translate("Form", "Animation"))
                self.butt_serial_write.setText(_translate("Form", "Serial Write"))
                self.butt_clear.setText(_translate("Form", "CLEAR"))
                self.lbl_4.setText(_translate("Form", "---------------------------------------------------------"))
                self.butt_apply.setText(_translate("Form", "Animation Apply"))

        def digitsWrite(self,child_list,text,number):
                x = 0
                text = list(text)
                if(len(text)<17):
                        for child in child_list[:len(text)]:
                                eval("self." + str(child.objectName()) + ".setText('{}')".format(text[x]))
                                x += 1
                        for child in child_list[len(text):]:
                                eval("self." + str(child.objectName()) + ".setText('')")
                        
                        if (number == 1):
                                self.lbl_1_length.setStyleSheet("background-color: rgb(137, 137, 255);font: bold 23pt'Arial';")
                                self.lbl_1_length.setText(str(len(self.text_1.text())))
                        else:
                                self.lbl_2_length.setStyleSheet("background-color: rgb(137, 137, 255);font: bold 23pt'Arial';")
                                self.lbl_2_length.setText(str(len(self.text_2.text())))

                else:
                        if (number == 1):
                                self.lbl_1_length.setStyleSheet("background-color: rgb(255, 20, 30);font: bold 23pt'Arial';")
                                self.lbl_1_length.setText(str(len(self.text_1.text())))
                        else:
                                self.lbl_2_length.setStyleSheet("background-color: rgb(255, 20, 30);font: bold 23pt'Arial';")
                                self.lbl_2_length.setText(str(len(self.text_2.text())))


        def animationApply(self):
                if(self.animationComboBox.currentIndex()==1):
                        if(self.text_length()>16):self.serial_length_error(1)
                        else:self.textMiddPrint()
                elif(self.animationComboBox.currentIndex()==2):
                        if(self.text_length()>16):self.serial_length_error(1)
                        else:self.textScrllRigth()
                elif(self.animationComboBox.currentIndex()==3):
                        if(self.text_length()>16):self.serial_length_error(1)
                        else:self.textOnebyOnePrint()     
                elif(self.animationComboBox.currentIndex()==4):
                        if(self.text_length()>16):self.serial_length_error(2)
                        else:self.textScrllLeft()
                elif(self.animationComboBox.currentIndex()==5):
                        if(self.text_length()>16):self.serial_length_error(1)
                        else:self.textFlashingPrint()
                else:
                        if(self.text_length()>16):self.serial_length_error(1)
                
        def text_length(self):
                length = len(self.text_1.text())
                if(len(self.text_2.text())>length):length = len(self.text_2.text())
                return length

        def serial_length_error(self,number):
                if (number == 1):
                        self.lbl_length_err.setText("Longer than 16 characters !!!")
                else:
                        self.lbl_length_err.setText("Shorter than 16 characters !!!")                  
                self.lbl_length_err.show()
                QtWidgets.QApplication.processEvents()
                sleep(2)
                self.lbl_length_err.hide()
               
        def Clear(self):                     # Screen Clear
                self.text_1.setText("")
                self.text_2.setText("")
                self.digitsWrite(self.children,self.text_1.text(),1)
                self.digitsWrite(self.children2,self.text_2.text(),2)
                self.animationComboBox.setCurrentIndex(0)
                port.write(str.encode((" " + "^" + " " +"^" + "7")))

        def serialWrite(self):                   # Sends texts via serial port
                if(self.text_length()<17):
                        if((self.animationComboBox.currentIndex()==4)):self.serial_length_error(2)
                        else:port.write(str.encode((self.text_1.text() + "^" + self.text_2.text() + "^" + str(self.animationComboBox.currentIndex()+1))))   
                else:
                        if((self.animationComboBox.currentIndex()==4)):
                                port.write(str.encode((self.text_1.text() + "^" + self.text_2.text() + "^" + str(self.animationComboBox.currentIndex()+1))))
                        else:
                                self.serial_length_error(1)
                                
        def textMiddPrint(self):
                self.text_1.setText(str(int((16-len(self.text_1.text()))/2) * " " + self.text_1.text()))
                self.digitsWrite(self.children,self.text_1.text(),1)
                self.text_2.setText(str(int((16-len(self.text_2.text()))/2) * " " + self.text_2.text()))
                self.digitsWrite(self.children2,self.text_2.text(),2)

        def textScrllRigth(self):                   #scrolls the text to the right and the text goes back to the screen from the left
                txt_list1 = []
                txt_list2 = []
                for child in self.children[:16]:
                        txt_list1.append(eval("self." + str(child.objectName()) + ".text()"))
                for child in self.children2:
                        txt_list2.append(eval("self." + str(child.objectName()) + ".text()"))
                for i in range(0,16):
                        del txt_list1[-1]
                        del txt_list2[-1]
                        txt_list1.insert(0," ")
                        txt_list2.insert(0," ")
                        self.digitsWrite(self.children,txt_list1,1)
                        self.digitsWrite(self.children2,txt_list2,2)
                        QtWidgets.QApplication.processEvents()
                        sleep(0.7)
                for i in range(0,self.text_length()):
                        if(i<len(self.text_1.text())):
                                del txt_list1[-1]
                                txt_list1.insert(0,self.text_1.text()[::-1][i])
                                self.digitsWrite(self.children[:len(self.text_1.text())],txt_list1,1)
                        if(i<len(self.text_2.text())):
                                del txt_list2[-1]
                                txt_list2.insert(0,self.text_2.text()[::-1][i])
                                self.digitsWrite(self.children2[:len(self.text_2.text())],txt_list2,2)
                        QtWidgets.QApplication.processEvents()
                        sleep(0.7)

        def textOnebyOnePrint(self):             #prints text by adding letters one by one to the screen
                txt_list1 = list(16 * "")
                txt_list2 = list(16 * "")
                text = list(self.text_1.text())
                text2 = list(self.text_2.text())
                for i in range(0,self.text_length()-1):
                        if(i<len(text)):
                                txt_list1.insert(i,text[i])
                        if(i<len(text2)):
                                txt_list2.insert(i,text2[i])
                        self.digitsWrite(self.children[:16],(''.join([str(arr) for arr in txt_list1])),1)
                        self.digitsWrite(self.children2[:16],(''.join([str(arr) for arr in txt_list2])),2)
                        QtWidgets.QApplication.processEvents()
                        sleep(0.7)
                self.textFlashingPrint()

        def textScrllLeft(self):                 #shifts the text to the left to fit the lcd.
                txt_list1 = self.text_1.text()
                txt_list2 = self.text_2.text()
                num1 = num2 = 0
                for i in range(0,self.text_length()-15):
                        if(i < len(self.text_1.text())-15):
                                txt_list1 = self.text_1.text()[0+i:i+16]
                                num1 = i
                        if(i < len(self.text_2.text())-15):
                                txt_list2 = self.text_2.text()[0+i:i+16]
                                num2 = i
                        self.digitsWrite(self.children[:16],txt_list1,1)
                        self.digitsWrite(self.children2[:16],txt_list2,2)
                        QtWidgets.QApplication.processEvents()
                        sleep(0.7)
                self.digitsWrite(self.children,self.text_1.text()[:len(self.text_1.text())-num1],1)
                self.digitsWrite(self.children2,self.text_2.text()[:len(self.text_2.text())-num2],2)
        
        def textFlashingPrint(self):        #flashing intermittently
                for i in range(0,4):
                        self.digitsWrite(self.children[:len(self.text_1.text())],len(self.text_1.text()) * " ",1)
                        self.digitsWrite(self.children2[:len(self.text_2.text())],len(self.text_2.text()) * " ",2)
                        QtWidgets.QApplication.processEvents()
                        sleep(0.4)
                        self.digitsWrite(self.children[:len(self.text_1.text())],self.text_1.text(),1)
                        self.digitsWrite(self.children2[:len(self.text_2.text())],self.text_2.text(),2)
                        QtWidgets.QApplication.processEvents()
                        sleep(0.7)


if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = Ui_Form()
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec_())