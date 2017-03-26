from PyQt4.QtCore import QTimer
from PyQt4 import QtCore, QtGui
import pyperclip
import login_backend
from threading import *
import sys

og_name = ""
og_passw = ""
t_name = ""
t_passw = ""

mins = 1*float(60)

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(320, 480)
        Form.setFixedSize(Form.size())
        Form.move(200, 150)
        Form.setStyleSheet(_fromUtf8("/* QWidget */\n"
"QWidget {\n"
"    background: #1565c0;\n"
"}\n"
"\n"
"/* Text Edit */\n"
"QTextEdit, QTextEdit:hover {\n"
"    padding-bottom: 2px;\n"
"    color: #dddddd;\n"
"    background-color:rgba(0,0,0,0);\n"
"}\n"
"/* Line Edit */\n"
"QLineEdit, QLineEdit:hover {\n"
"    border: none;\n"
"    padding-bottom: 2px;\n"
"    border-bottom: 1px solid #dddddd;\n"
"    color: #dddddd;\n"
"    background-color:rgba(0,0,0,0);\n"
"}\n"
"\n"
"QLineEdit:editable{\n"
"    border: none;\n"
"    padding-bottom: 2px;\n"
"    border-bottom: 2px solid #b2dfdb;\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"QLineEdit:disabled{\n"
"    border: 0px solid white;\n"
"    padding-bottom: 2px;\n"
"    border-bottom: 2px solid #eeeeee;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 0px solid white;\n"
"    padding-bottom: 2px;\n"
"    border-bottom: 2px solid #ff9800;\n"
"    color: #eeeeee;\n"
"}\n"
"QLineEdit:pressed {\n"
"    border: none;\n"
"    padding-bottom: 2px;\n"
"    border-bottom: 2px solid #ff9800;\n"
"}\n"
"\n"
"/* Push Button */\n"
"\n"
"QPushButton, QPushButton:focus, QPushButton:focus {\n"
"  background-color: #ff9800;\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 3px 20px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover, QPushButton:hover:focus {\n"
"  background-color: #ff9800;\n"
"  border-color: #ff9800;\n"
"  border: none;\n"
"}\n"
"\n"
"QPushButton:selected { \n"
"    border:none;\n"
"}\n"
"\n"
"QPushButton:pressed,\n"
"QPushButton:pressed:focus {\n"
"  background-color: #ee7700;\n"
"  border: none;\n"
"  color: white;\n"
"}\n"
"\n"
""))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(80, 420, 151, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.pushButton2 = QtGui.QPushButton(Form)
        self.pushButton2.setGeometry(QtCore.QRect(80, 250, 151, 31))
        self.pushButton2.setObjectName(_fromUtf8("pushButton2"))

        self.pushButton3 = QtGui.QPushButton(Form)
        self.pushButton3.setGeometry(QtCore.QRect(80, 350, 151, 31))
        self.pushButton3.setObjectName(_fromUtf8("pushButton3"))

        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 140, 231, 51))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.textEdit = QtGui.QLineEdit(Form)
        self.textEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.textEdit.setGeometry(QtCore.QRect(85, 290, 141, 40))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 210, 161, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(60, -20, 191, 191))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8("images/logo.png")))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_4.raise_()
        self.label_3.raise_()
        self.pushButton.raise_()
        self.pushButton2.raise_()
        self.pushButton3.raise_()
        self.textEdit.raise_()
        self.label.raise_()

        self.label_msg = QtGui.QLabel(Form)
        self.label_msg.setGeometry(QtCore.QRect(90, 390, 131, 20))
        self.label_msg.setObjectName(_fromUtf8("label_msg"))
        self.label_msg.raise_()

        self.retranslateUi(Form)                        
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", "Logout", None))
        self.pushButton2.setText(_translate("Form", "Generate OTP", None))
        self.pushButton3.setText(_translate("Form", "Connect To OTP", None))
        self.label_3.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ffffff;\"> Welcome </span></p></body></html>", None))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\"></span></p></body></html>", None))


    def setEvents(self, Form):
        import functools        
        self.pushButton.clicked.connect(lambda: self.logButtonPress(Form))
        self.pushButton2.clicked.connect(lambda: self.button1Press(Form))
        self.pushButton3.clicked.connect(lambda: self.button2Press(Form))
        Form.setWindowTitle(_translate("CClipper", "CClipper", None))
    
    
    def logButtonPress(self, Form):
        print "Button Pressed"        

        try:
            import gui
            gui.running = True
            print "Opening file.."
            f = open("credentials.txt","w") 
            f.write("")
            f.close()
            Form.hide()
            print "Showing login form.."
            gui.exit_all()

        except Exception as e:
            print e
        
    # Generate otp
    def button1Press(self, Form):
        print "Button 1 Pressed"        
        otp = login_backend.requestotp("0")
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">"+otp+"</span></p></body></html>", None))
        self.pushButton2.setEnabled(False)
        #self.pushButton3.setEnabled(False)
        self.timer = QTimer()
        self.timer.timeout.connect(self.enableStuff)
        self.timer.start(1000 * mins) # 5 min

    def enableStuff(self):
        global og_name, og_passw
        self.pushButton2.setEnabled(True)
        self.pushButton3.setEnabled(True)
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\"></span></p></body></html>", None))
        if og_name != "" and og_passw != "":
            f = open("credentials.txt","w") 
            f.write(og_name) 
            f.write("\n")
            f.write(og_passw) 
            f.close()
            og_name = ""
            og_passw = ""

    # connect to otp
    def button2Press(self, Form):
        global og_name, og_passw, t_name, t_passw
        print "Button 2 Pressed"        
        try:
            otp = str(self.textEdit.text())
            if len(otp) == 6:
                topic, time = login_backend.checkotp(otp)
                name = topic.split("/")[0]
                passw = topic.split("/")[1]
                

                if name == "error" and passw == "error":
                    self.label_msg.setText(_translate("Form", "<html><head/><body><b><p align=\"center\"><span style=\" color:#ff9800;\">Invalid OTP</span></p></b></body></html>", None))            
                else:
                    t_name = name
                    t_passw = passw
                    og_name, og_passw = open('credentials.txt','r').read().split('\n')
                    self.pushButton2.setEnabled(False)
                    self.pushButton3.setEnabled(False)
                    self.label_msg.setText(_translate("Form", "<html><head/><body><b><p align=\"center\"><span style=\" color:#ff9800;\">Successful!</span></p></b></body></html>", None))
                    self.timer = QTimer()
                    self.timer.timeout.connect(self.enableStuff)
                    self.timer.start(1000 * (mins - time))
                    print (mins - time) / float(60)       
                    f = open("credentials.txt","a") 
                    f.write("\n")
                    f.write(name) 
                    f.write("\n")
                    f.write(passw) 
                    f.close()

            else:
                self.label_msg.setText(_translate("Form", "<html><head/><body><b><p align=\"center\"><span style=\" color:#ff9800;\">Invalid OTP</span></p></b></body></html>", None))                       
        except:
            self.label_msg.setText(_translate("Form", "<html><head/><body><b><p align=\"center\"><span style=\" color:#ff9800;\">Invalid OTP</span></p></b></body></html>", None))                       
            