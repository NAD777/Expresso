# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'part.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(648, 476)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 621, 451))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.size_text = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.size_text.setObjectName("size_text")
        self.gridLayout.addWidget(self.size_text, 4, 0, 1, 1)
        self.degree_text = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.degree_text.setObjectName("degree_text")
        self.gridLayout.addWidget(self.degree_text, 0, 0, 1, 1)
        self.price_text = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.price_text.setObjectName("price_text")
        self.gridLayout.addWidget(self.price_text, 3, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 2, 0, 1, 1)
        self.type_text = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.type_text.setObjectName("type_text")
        self.gridLayout.addWidget(self.type_text, 1, 0, 1, 1)
        self.edit_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.edit_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("edit(1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit_btn.setIcon(icon)
        self.edit_btn.setObjectName("edit_btn")
        self.gridLayout.addWidget(self.edit_btn, 0, 1, 1, 1)
        self.delete_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.delete_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_btn.setIcon(icon1)
        self.delete_btn.setObjectName("delete_btn")
        self.gridLayout.addWidget(self.delete_btn, 1, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.degree_text, self.type_text)
        Form.setTabOrder(self.type_text, self.textEdit)
        Form.setTabOrder(self.textEdit, self.price_text)
        Form.setTabOrder(self.price_text, self.size_text)
        Form.setTabOrder(self.size_text, self.edit_btn)
        Form.setTabOrder(self.edit_btn, self.delete_btn)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
