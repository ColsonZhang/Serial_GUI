# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\pyqt_file\untitled_2.ui'
#
# Created: Sat Apr 15 09:51:16 2017
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!
import sys
import serial
import threading
import binascii 
from PyQt5 import QtCore, QtGui, QtWidgets
import serial.tools.list_ports

class Ui_MainWindow(object):
    ser = serial.Serial()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(579, 369)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 141, 311))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 31, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 41, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 41, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 41, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 140, 41, 16))
        self.label_5.setObjectName("label_5")
        self.comboBox_4 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_4.setGeometry(QtCore.QRect(60, 20, 71, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(60, 50, 71, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(60, 80, 71, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_2.setGeometry(QtCore.QRect(60, 110, 71, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_3.setGeometry(QtCore.QRect(60, 140, 71, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(10, 240, 51, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 240, 51, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 200, 61, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(10, 170, 41, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(70, 170, 54, 16))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(160, 10, 411, 181))
        self.groupBox_2.setObjectName("groupBox_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser.setGeometry(QtCore.QRect(10, 20, 391, 151))
        self.textBrowser.setObjectName("textBrowser")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(160, 200, 261, 121))
        self.groupBox_3.setObjectName("groupBox_3")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 241, 91))
        self.textEdit.setObjectName("textEdit")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(430, 210, 61, 16))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(500, 210, 61, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(430, 240, 61, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(430, 280, 61, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 579, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height());  
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Serial_gui"))
        self.groupBox.setTitle(_translate("MainWindow", "串口设置"))
        self.label.setText(_translate("MainWindow", "串 口"))
        self.label_2.setText(_translate("MainWindow", "波特率"))
        self.label_3.setText(_translate("MainWindow", "校验位"))
        self.label_4.setText(_translate("MainWindow", "数据位"))
        self.label_5.setText(_translate("MainWindow", "停止位"))
        self.lineEdit_3.setText(_translate("MainWindow", "9600"))
        self.comboBox.setItemText(0, _translate("MainWindow", "8"))
        self.comboBox.setItemText(1, _translate("MainWindow", "7"))
        self.comboBox.setItemText(2, _translate("MainWindow", "6"))
        self.comboBox.setItemText(3, _translate("MainWindow", "5"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "N"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "E"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "O"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "M"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "S"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "1.5"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "2"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "COM1"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "COM2"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "COM3"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "COM4"))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "COM5"))
        self.comboBox_4.setItemText(5, _translate("MainWindow", "COM6"))
        self.comboBox_4.setItemText(6, _translate("MainWindow", "COM7"))
        self.comboBox_4.setItemText(7, _translate("MainWindow", "COM8"))
        self.comboBox_4.setItemText(8, _translate("MainWindow", "COM9"))
        self.comboBox_4.setItemText(9, _translate("MainWindow", "COM10"))
        self.pushButton.setText(_translate("MainWindow", "打开"))
        self.pushButton.clicked.connect(self.port_open)

        self.pushButton_2.setText(_translate("MainWindow", "关闭"))
        self.pushButton_2.clicked.connect(self.port_close)

        self.pushButton_3.setText(_translate("MainWindow", "检测串口"))
        self.pushButton_3.clicked.connect(self.port_cheak)

        self.label_11.setText(_translate("MainWindow", "状 态："))
        self.label_12.setText(_translate("MainWindow", "串口状态"))
        self.groupBox_2.setTitle(_translate("MainWindow", "接收区"))
        self.groupBox_3.setTitle(_translate("MainWindow", "发送区"))
        self.checkBox.setText(_translate("MainWindow", "Hex显示"))
        self.checkBox_2.setText(_translate("MainWindow", "Hex发送"))
        self.pushButton_4.setText(_translate("MainWindow", "清除"))
        self.pushButton_4.clicked.connect(self.clean_data)

        self.pushButton_5.setText(_translate("MainWindow", "发送"))
        self.pushButton_5.clicked.connect(self.send_data)

    def port_open(self):

        self.ser.port = self.comboBox_4.currentText()
        self.ser.baudrate = int(self.lineEdit_3.text())
        self.ser.bytesize = int(self.comboBox.currentText()) 
        self.ser.stopbits = int(self.comboBox_3.currentText())
        self.ser.parity = self.comboBox_2.currentText()
        self.ser.open()
        if(self.ser.isOpen()):
            self.pushButton.setEnabled(False)
            self.label_12.setText("打开成功")
            self.t1 = threading.Thread(target=self.receive_data)
            self.t1.setDaemon(True)
            self.t1.start()
        else:
            self.label_12.setText("打开失败")

    def port_close(self):
        self.ser.close()
        if(self.ser.isOpen()):
            self.label_12.setText("关闭失败")
        else:
            self.pushButton.setEnabled(True)
            self.label_12.setText("关闭成功")


    def send_data(self):
        if(self.ser.isOpen()):
            if(self.checkBox_2.isChecked()):
                 self.ser.write(binascii.a2b_hex(self.textEdit.toPlainText()))
            else:
                self.ser.write(self.textEdit.toPlainText().encode('utf-8'))
            self.label_12.setText("发送成功")
    #       self.ser.flushOutput()
        else:
            self.label_12.setText("发送失败")

    def receive_data(self):
        print("The receive_data threading is start")
        res_data = '' 
        num = 0
        while (self.ser.isOpen()):
            size = self.ser.inWaiting()
            if size:
                res_data = self.ser.read_all()
                if(self.checkBox.isChecked()):
                    self.textBrowser.append(binascii.b2a_hex(res_data).decode())
                else:
                    self.textBrowser.append(res_data.decode())
                self.textBrowser.moveCursor(QtGui.QTextCursor.End)
                self.ser.flushInput()               
                num +=1
                self.label_12.setText("接收："+str(num))

    def clean_data(self):
        self.textBrowser.setText("")
        self.label_12.setText("接收清空")

    def port_cheak(self):
        Com_List=[]
        port_list = list(serial.tools.list_ports.comports())
        self.comboBox_4.clear()
        for port in port_list:
            Com_List.append(port[0])
            self.comboBox_4.addItem(port[0])
        if(len(Com_List) == 0):
            self.label_12.setText("没串口")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow) 


    MainWindow.show()
    sys.exit(app.exec_())