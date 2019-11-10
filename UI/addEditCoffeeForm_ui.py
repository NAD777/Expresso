# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(625, 561)
        Form.setStyleSheet("background-color: rgb(242, 243, 245)")
        self.reject_btn = QtWidgets.QPushButton(Form)
        self.reject_btn.setGeometry(QtCore.QRect(180, 517, 89, 25))
        self.reject_btn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:8px;\n"
"")
        self.reject_btn.setObjectName("reject_btn")
        self.accept_btn = QtWidgets.QPushButton(Form)
        self.accept_btn.setGeometry(QtCore.QRect(310, 517, 89, 25))
        self.accept_btn.setStyleSheet("color:white;\n"
"border-radius:8px;\n"
"background-color:rgb(43, 112, 246);")
        self.accept_btn.setObjectName("accept_btn")
        self.degree_text = QtWidgets.QLineEdit(Form)
        self.degree_text.setGeometry(QtCore.QRect(20, 47, 585, 25))
        self.degree_text.setObjectName("degree_text")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(20, 109, 585, 325))
        self.textEdit.setObjectName("textEdit")
        self.size_text = QtWidgets.QLineEdit(Form)
        self.size_text.setGeometry(QtCore.QRect(20, 471, 585, 25))
        self.size_text.setObjectName("size_text")
        self.type_text = QtWidgets.QLineEdit(Form)
        self.type_text.setGeometry(QtCore.QRect(20, 78, 585, 25))
        self.type_text.setObjectName("type_text")
        self.price_text = QtWidgets.QLineEdit(Form)
        self.price_text.setGeometry(QtCore.QRect(20, 440, 585, 25))
        self.price_text.setObjectName("price_text")
        self.name_text = QtWidgets.QLineEdit(Form)
        self.name_text.setGeometry(QtCore.QRect(20, 10, 585, 25))
        self.name_text.setObjectName("name_text")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.name_text, self.degree_text)
        Form.setTabOrder(self.degree_text, self.type_text)
        Form.setTabOrder(self.type_text, self.textEdit)
        Form.setTabOrder(self.textEdit, self.price_text)
        Form.setTabOrder(self.price_text, self.size_text)
        Form.setTabOrder(self.size_text, self.accept_btn)
        Form.setTabOrder(self.accept_btn, self.reject_btn)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.reject_btn.setText(_translate("Form", "Отменить"))
        self.accept_btn.setText(_translate("Form", "Изменить"))
        self.degree_text.setPlaceholderText(_translate("Form", "Степень обжарки"))
        self.textEdit.setPlaceholderText(_translate("Form", "Описание"))
        self.size_text.setPlaceholderText(_translate("Form", "Объем"))
        self.type_text.setPlaceholderText(_translate("Form", "Тип"))
        self.price_text.setPlaceholderText(_translate("Form", "Цена"))
        self.name_text.setPlaceholderText(_translate("Form", "Имя"))
