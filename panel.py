# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'panel.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(815, 478)
        Form.setFixedSize(815,478)
        self.button1 = QtWidgets.QPushButton(Form)
        self.button1.setGeometry(QtCore.QRect(530, 60, 111, 41))
        self.button1.setObjectName("button1")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 60, 501, 41))
        self.lineEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lineEdit.setObjectName("lineEdit")
        self.button2 = QtWidgets.QPushButton(Form)
        self.button2.setGeometry(QtCore.QRect(650, 60, 151, 41))
        self.button2.setObjectName("button2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 120, 501, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.button3 = QtWidgets.QPushButton(Form)
        self.button3.setGeometry(QtCore.QRect(570, 120, 161, 41))
        self.button3.setObjectName("button3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(100, 170, 211, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(460, 170, 211, 41))
        self.label_2.setObjectName("label_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(400, 210, 411, 261))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_3.setGeometry(QtCore.QRect(10, 210, 371, 261))
        self.textBrowser_3.setObjectName("textBrowser_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Extract the Information  (Created By N0body)"))
        self.button1.setText(_translate("Form", "Single File"))
        self.lineEdit.setText(_translate("Form", "Click the button you want to operate."))
        self.button2.setText(_translate("Form", "Multiple Files"))
        self.lineEdit_2.setText(_translate("Form", "Input the key words you want to extract."))
        self.button3.setText(_translate("Form", "extract"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\">The File(s) You Choose</p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\">Operation Status</p></body></html>"))
