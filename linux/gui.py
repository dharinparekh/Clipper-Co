from PyQt4 import QtCore, QtGui
from homeform import Ui_Form as homeUI
from loginform import Ui_Form as loginUI
from regform import Ui_Form as regUI
import sys
import subprocess
import thread
import os
import signal

dat = [1]
procc = None
running = False
pid= -1
test = 0

def _kill_all():
    try:
        fil = open('pid.txt','r')
        pid = int(fil.read())
    except:
        pass
    if(pid != -1):
        cpid = os.popen("pgrep -P "+str(pid)).readlines()
        cpid = cpid[0].strip("\n")
        os.system("kill -9 %s"%pid)
        if(cpid):
            os.system("kill -9 %s"%cpid)

def show_login_form():
    Form = QtGui.QWidget()
    login_ui = loginUI()
    login_ui.setupUi(Form)
    login_ui.setEvents(Form)
    Form.show()

def show_home_form():
    global running
    if not running:
        run_copy_clip()
        running = True
    Form = QtGui.QWidget()
    home_ui = homeUI()
    home_ui.setupUi(Form)
    home_ui.setEvents(Form)
    Form.show()

def run_copy_clip():
    global procc
    global pid, test
    test = 100
    procc = subprocess.Popen("python copy_clip.py",shell=True)
    pid = procc.pid
    fil = open('pid.txt','w')
    fil.write(str(pid))
    fil.close()

    # while True:
        # pass

def show_reg_form():
    Form = QtGui.QWidget()
    reg_ui = regUI()
    reg_ui.setupUi(Form)
    reg_ui.setEvents(Form)
    Form.show()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    show_login_form()
    # if procc:
    #     procc.terminate()
    #     procc.kill()
    try:
        sys.exit(app.exec_())
    except SystemExit as ex:
            pid = -1
            _kill_all()
            # os.system("killall -9 python")
