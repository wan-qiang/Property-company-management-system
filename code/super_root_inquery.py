# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'super_root_inquery.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import image.super_root

class Ui_super_root_inquery(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(731, 642)
        Form.setMinimumSize(QtCore.QSize(731, 642))
        Form.setMaximumSize(QtCore.QSize(731, 642))
        icon = QtGui.QIcon.fromTheme("D:\\python_projects\\DataBase\\image\\logo.png")
        Form.setWindowIcon(icon)
        Form.setWindowOpacity(0.85)
        Form.setStyleSheet("background-image: url(:/background/7.jpg);")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(380, 200, 181, 51))
        self.pushButton_4.setStyleSheet("font: 16pt \"Arial\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(370, 280, 191, 51))
        self.pushButton_6.setStyleSheet("font: 16pt \"Arial\";")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 200, 171, 51))
        self.pushButton_3.setStyleSheet("font: 16pt \"Arial\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(130, 370, 171, 51))
        self.pushButton_7.setStyleSheet("font: 16pt \"Arial\";")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(130, 280, 171, 51))
        self.pushButton_5.setStyleSheet("font: 16pt \"Arial\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(130, 110, 171, 51))
        self.pushButton.setStyleSheet("font: 16pt \"Arial\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 110, 181, 51))
        self.pushButton_2.setStyleSheet("font: 16pt \"Arial\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(380, 370, 181, 51))
        self.pushButton_8.setStyleSheet("font: 16pt \"Arial\";")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_10 = QtWidgets.QPushButton(Form)
        self.pushButton_10.setGeometry(QtCore.QRect(380, 460, 181, 51))
        self.pushButton_10.setStyleSheet("font: 16pt \"Arial\";")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(120, 460, 181, 51))
        self.pushButton_9.setStyleSheet("font: 16pt \"Arial\";")
        self.pushButton_9.setObjectName("pushButton_9")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(190, 30, 371, 51))
        self.label.setStyleSheet("font: 18pt \"Arial\";\n"
"color: rgb(255, 0, 0);\n"
"font: 24pt \"Arial\";")
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "超级管理员"))
        self.pushButton_4.setText(_translate("Form", "楼栋信息"))
        self.pushButton_6.setText(_translate("Form", "车辆信息"))
        self.pushButton_3.setText(_translate("Form", "员工信息"))
        self.pushButton_7.setText(_translate("Form", "宠物信息"))
        self.pushButton_5.setText(_translate("Form", "停车位信息"))
        self.pushButton.setText(_translate("Form", "小区信息"))
        self.pushButton_2.setText(_translate("Form", "家庭信息"))
        self.pushButton_8.setText(_translate("Form", "户主信息"))
        self.pushButton_10.setText(_translate("Form", "退出系统"))
        self.pushButton_9.setText(_translate("Form", "返回"))
        self.label.setText(_translate("Form", "欢迎登入超级管理员"))