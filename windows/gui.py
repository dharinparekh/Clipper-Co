from PyQt4 import QtCore, QtGui
from homeform import Ui_Form as homeUI
from loginform import Ui_Form as loginUI
from regform import Ui_Form as regUI
import sys
import threading
import os

running = False
th = None
app = None

def show_login_form():
    Form = QtGui.QWidget()
    login_ui = loginUI()
    login_ui.setupUi(Form)
    login_ui.setEvents(Form)
    Form.show()

def show_home_form():
    global running, th
    th = threading.Thread(target = run_copy_clip)
    th.start()
    Form = QtGui.QWidget()
    home_ui = homeUI()
    home_ui.setupUi(Form)
    home_ui.setEvents(Form)
    Form.show()

def run_copy_clip():
    import copy_clip
    copy_clip.main()
    #while True:
        #pass

def show_reg_form():
    Form = QtGui.QWidget()
    reg_ui = regUI()
    reg_ui.setupUi(Form)
    reg_ui.setEvents(Form)
    Form.show()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    show_login_form()
    try:
        sys.exit(app.exec_())
    except:
        os._exit(0)

def exit_all():
    os._exit(0)