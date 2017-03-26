from PyQt4 import QtCore, QtGui

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
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setGeometry(QtCore.QRect(70, 160, 171, 27))
        self.lineEdit.setInputMask(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 240, 171, 27))
        self.lineEdit_2.setInputMask(_fromUtf8(""))
        self.lineEdit_2.setText(_fromUtf8(""))
        self.lineEdit_2.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(80, 320, 151, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 370, 131, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 400, 151, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(90, 160, 131, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(90, 240, 131, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        
        self.label_msg = QtGui.QLabel(Form)
        self.label_msg.setGeometry(QtCore.QRect(90, 285, 131, 20))
        self.label_msg.setObjectName(_fromUtf8("label_msg"))

        self.label_logo = QtGui.QLabel(Form)
        self.label_logo.setGeometry(QtCore.QRect(60, -20, 191, 191))
        self.label_logo.setText(_fromUtf8(""))
        self.label_logo.setPixmap(QtGui.QPixmap(_fromUtf8("images/logo.png")))
        self.label_logo.setScaledContents(True)
        self.label_logo.setObjectName(_fromUtf8("label_4"))
        self.label_logo.raise_()
        
        self.label_msg.raise_()
        self.label_4.raise_()
        self.label_3.raise_()
        self.label_2.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.pushButton.raise_()
        self.label.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", "Login", None))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#ffffff;\">Not a user?</span></p></body></html>", None))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; text-decoration: underline; color:#ffffff;\">Register Now!</span></p></body></html>", None))
        self.label_3.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">User Name</span></p></body></html>", None))
        self.label_4.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Password</span></p></body></html>", None))

    def setEvents(self, Form):
        import functools
        self.lineEdit.textChanged.connect(self.hideLabel1)
        self.lineEdit_2.textChanged.connect(self.hideLabel2)
        self.pushButton.clicked.connect(lambda: self.buttonPress(Form))
        self.label_2.mousePressEvent = functools.partial(self.labelPress, Form)
        Form.setWindowTitle(_translate("CClipper", "CClipper", None))

    def hideLabel1(self):
        self.label_3.setText("")

    def hideLabel2(self):
        self.label_4.setText("")
    
    def buttonPress(self, Form):
        import login_backend
        print "Login Button Pressed"
        print   "Name: " +  self.lineEdit.text()
        print   "Password: " + self.lineEdit_2.text()
        name = str(self.lineEdit.text())
        passw = str(self.lineEdit_2.text())
        val = login_backend.login(name, passw)
        print val
        if val:
            import gui
            f = open("credentials.txt","w")
            f.write(name)
            f.write("\n")
            f.write(passw)
            f.close()
            self.label_msg.setText(_translate("Form", "<html><head/><body><b><p align=\"center\"><span style=\" color:#ff9800;\">Login Successful!</span></p></b></body></html>", None))
            Form.hide()
            gui.show_home_form()
        else:
            self.label_msg.setText(_translate("Form", "<html><head/><body><b><p align=\"center\"><span style=\" color:#ff9800;\">Invalid Credentials!</span></p></b></body></html>", None))

    def labelPress(self, Form, event):
        import gui
        print "Registration thing pressed"
        Form.hide()
        gui.show_reg_form()