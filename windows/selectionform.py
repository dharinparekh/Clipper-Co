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
        Form.move(500, 150)
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
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(80, 250, 151, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 350, 151, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 140, 231, 51))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.label_logo = QtGui.QLabel(Form)
        self.label_logo.setGeometry(QtCore.QRect(60, -20, 191, 191))
        self.label_logo.setText(_fromUtf8(""))
        self.label_logo.setPixmap(QtGui.QPixmap(_fromUtf8("images/logo.png")))
        self.label_logo.setScaledContents(True)
        self.label_logo.setObjectName(_fromUtf8("label_4"))
        
        self.label_logo.raise_()
        self.label_3.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Clipper Co.", "Clipper Co.", None))
        self.pushButton.setText(_translate("Form", "Interactive Mode", None))
        self.pushButton_2.setText(_translate("Form", "Clipboard Share", None))
        self.label_3.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ffffff;\"> Welcome! </span></p></body></html>", None))

    def setEvents(self, Form):
        import functools
        self.pushButton.clicked.connect(lambda: self.interButtonPress(Form))
        self.pushButton_2.clicked.connect(lambda: self.clipButtonPress(Form))

    def interButtonPress(self, Form):
        print "Inter button pressed"
        import gui
        Form.hide()
        gui.show_interactive_form()

    def clipButtonPress(self, Form):
        print "Clip thing pressed"
        import gui
        Form.hide()
        gui.show_home_form()
