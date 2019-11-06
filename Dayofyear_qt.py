# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dy.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(340, 120, 111, 16))
        self.label_4.setObjectName("label_4")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(240, 160, 273, 123))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.pushButton)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "流水日计算器"))
        self.label.setText(_translate("MainWindow", "年"))
        self.label_2.setText(_translate("MainWindow", "月"))
        self.label_3.setText(_translate("MainWindow", "日"))
        self.pushButton.setText(_translate("MainWindow", "计算"))

    def setupFunction(self):
        self.pushButton.clicked.connect(self.dayofyear)
#计算一年的第几天
    def dayofyear(self):
        year = int(self.lineEdit.text())
        month = int(self.lineEdit_2.text())
        day = int(self.lineEdit_3.text())
        sum = 0
        months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
        leap = 0
        #判断是否闰年
        if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
            leap = 1
        #判断月和日输入是否正确
        if 0 < month <= 12 and (
                (( month == 1 or month == 3 or month == 4 or month == 7 or month == 8 or month == 10 or  month == 12) and 0 < day <= 31)
                or (( month == 4 or month == 6 or month == 9 or month == 11 ) and 0 < day <= 30)
                or ( month == 2 and ((leap == 0 and 0 < day <= 28) or (leap == 1 and 0 < day <= 29) ))):
            sum = months[month - 1]
            sum += day
            #闰年二月份以上则日期加1
            if (leap == 1) and (month > 2):
                sum += 1
            self.lineEdit_4.setText(str(sum))
        elif month <= 0 or month > 12:
            self.lineEdit_4.setText("月份输入错误")
        else:
            self.lineEdit_4.setText("日期输入错误")
if __name__=="__main__":
    import sys
    from PyQt5.QtGui import QIcon
    app=QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui=Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.setupFunction()  # 执行类中的setupFunction方法
    MainWindow.show()
    sys.exit(app.exec_())