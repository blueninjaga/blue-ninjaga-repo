from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from  caclulator_Vlad_Derkach import  Ui_Dialog

app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()


def action_equals():
    text=ui.lable_output.text()
    ans = eval(text)
    ui.lable_output.setText(text+"=")


def action_plus():
    text=ui.lable_output.text()
    ui.lable_output.setText(text+"+")

def action_minus():
    text = ui.lable_output.text()
    ui.lable_output.setText(text + "-")

def pushbutton_one():
    text = ui.lable_output.text()
    ui.lable_output.setText(text + "1")
def pushbutton_two():
    text = ui.lable_output.text()
    ui.lable_output.setText(text + "2")
def pushbutton_three():
    text = ui.lable_output.text()
    ui.lable_output.setText(text + "3")
def pushbutton_four():
    text = ui.lable_output.text()
    ui.lable_output.setText(text + "4")
def pushbutton_five():
    text = ui.lable_output.text()
    ui.lable_output.setText(text + "5")
def pushbutton_six():
    text = ui.lable_output.text()
    ui.lable_output.setText(text + "6")
def pushbutton_seven():
    text = ui.lable_output.text()
    ui.lable_output.setText(text + "7")
def pushbutton_eight():
    text = ui.lable_output.text()
    ui.lable_output.setText(text + "8")
def pushbutton_nine():
    text = ui.lable_output.text()
    ui.lable_output.setText(text + "9")
def pushbutton_zero():
    text = ui.lable_output.text()
    ui.lable_output.setText(text + "0")

ui.pushButton_plus.clicked.connect(action_plus)
ui.pushButton_equals.clicked.connect(action_equals)
ui.pushButton_one.clicked.connect(pushbutton_one)
ui.pushButton_two.clicked.connect(pushbutton_two)
ui.pushButton_three.clicked.connect(pushbutton_three)
ui.pushButton_four.clicked.connect(pushbutton_four)
ui.pushButton_five.clicked.connect(pushbutton_five)
ui.pushButton_six.clicked.connect(pushbutton_six)
ui.pushButton_seven.clicked.connect(pushbutton_seven)
ui.pushButton_eight.clicked.connect(pushbutton_eight)
ui.pushButton_nine.clicked.connect(pushbutton_nine)
ui.pushButton_zero.clicked.connect(pushbutton_zero)
ui.pushButton_minus.clicked.connect(action_minus)
sys.exit(app.exec_())