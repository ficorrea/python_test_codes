# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat.ui'
#
# Created: Sun Dec  4 18:26:23 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(338, 354)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget_view = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_view.setGeometry(QtCore.QRect(10, 10, 321, 192))
        self.listWidget_view.setObjectName("listWidget_view")
        self.pushButton_enviar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_enviar.setGeometry(QtCore.QRect(240, 210, 85, 27))
        self.pushButton_enviar.setObjectName("pushButton_enviar")
        self.pushButton_conectar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_conectar.setGeometry(QtCore.QRect(10, 300, 151, 27))
        self.pushButton_conectar.setObjectName("pushButton_conectar")
        self.lineEdit_msg = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_msg.setGeometry(QtCore.QRect(10, 210, 221, 27))
        self.lineEdit_msg.setObjectName("lineEdit_msg")
        self.lineEdit_usuario = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_usuario.setGeometry(QtCore.QRect(72, 250, 261, 27))
        self.lineEdit_usuario.setObjectName("lineEdit_usuario")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 260, 56, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 310, 41, 17))
        self.label_2.setObjectName("label_2")
        self.lineEdit_porta = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_porta.setGeometry(QtCore.QRect(220, 300, 113, 27))
        self.lineEdit_porta.setObjectName("lineEdit_porta")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Chat"))
        self.pushButton_enviar.setText(_translate("MainWindow", "Enviar"))
        self.pushButton_conectar.setText(_translate("MainWindow", "Conectar"))
        self.label.setText(_translate("MainWindow", "Usuário:"))
        self.label_2.setText(_translate("MainWindow", "Porta:"))

