from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from  caclulator_Vlad_Derkach import  Ui_Dialog

app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()



def action_plus():
    text=ui.lable_output.text()
    ui.lable_output.setText(text+"+")

def pushbutton_one():
    text = ui.lable_output.text()
    ui.lable_output.setText(text + "1")
ui.pushButton_one.clicked.connect(pushbutton_one)
ui.pushButton_plus.clicked.connect(action_plus)
sys.exit(app.exec_())