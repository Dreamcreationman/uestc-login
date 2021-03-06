# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import ctypes

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(527, 388)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(80, 40, 363, 302))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.container = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.container.setContentsMargins(20, 30, 20, 30)
        self.container.setHorizontalSpacing(15)
        self.container.setVerticalSpacing(20)
        self.container.setObjectName("container")
        self.username_label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.username_label.setFont(font)
        self.username_label.setObjectName("username_label")
        self.container.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.username_label)
        self.username = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.username.setFont(font)
        self.username.setMaxLength(12)
        self.username.setObjectName("username")
        self.username.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]{14}"), self.username))
        self.container.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.username)
        self.passwd_label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.passwd_label.setFont(font)
        self.passwd_label.setObjectName("passwd_label")
        self.container.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.passwd_label)
        self.password = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.password.setFont(font)
        self.password.setMaxLength(100)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.container.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.password)
        self.ok = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.ok.setFont(font)
        self.ok.setObjectName("ok")
        self.container.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.ok)
        self.positionContainer = QtWidgets.QHBoxLayout()
        self.positionContainer.setContentsMargins(10, 5, 10, 5)
        self.positionContainer.setSpacing(5)
        self.positionContainer.setObjectName("positionContainer")
        self.mainbuilding = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.mainbuilding.setChecked(True)
        self.mainbuilding.setObjectName("mainbuilding")
        self.positionContainer.addWidget(self.mainbuilding)
        self.dorm = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.dorm.setObjectName("dorm")
        self.positionContainer.addWidget(self.dorm)
        self.container.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.positionContainer)
        self.exit = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.exit.setFont(font)
        self.exit.setObjectName("exit")
        self.container.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.exit)
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "电子科技大学自动登录"))
        self.username_label.setText(_translate("mainWindow", "学号"))
        self.username.setToolTip(_translate("mainWindow", "你的学号"))
        self.username.setPlaceholderText(_translate("mainWindow", "请输入学号"))
        self.passwd_label.setText(_translate("mainWindow", "密码"))
        self.password.setToolTip(_translate("mainWindow", "服务大厅的密码"))
        self.password.setPlaceholderText(_translate("mainWindow", "请输入服务大厅密码"))
        self.ok.setText(_translate("mainWindow", "确定"))
        self.mainbuilding.setText(_translate("mainWindow", "主楼"))
        self.dorm.setText(_translate("mainWindow", "寝室（硕丰）"))
        self.exit.setText(_translate("mainWindow", "退出程序"))
