# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created: Mon Apr  3 04:10:37 2017
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(372, 396)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton1_on = QtGui.QPushButton(self.centralwidget)
        self.pushButton1_on.setGeometry(QtCore.QRect(100, 90, 110, 29))
        self.pushButton1_on.setObjectName(_fromUtf8("pushButton1_on"))
        self.pushButton2_on = QtGui.QPushButton(self.centralwidget)
        self.pushButton2_on.setGeometry(QtCore.QRect(100, 150, 110, 29))
        self.pushButton2_on.setObjectName(_fromUtf8("pushButton2_on"))
        self.pushButton1_off = QtGui.QPushButton(self.centralwidget)
        self.pushButton1_off.setGeometry(QtCore.QRect(230, 90, 110, 29))
        self.pushButton1_off.setObjectName(_fromUtf8("pushButton1_off"))
        self.pushButton2_off = QtGui.QPushButton(self.centralwidget)
        self.pushButton2_off.setGeometry(QtCore.QRect(230, 150, 110, 29))
        self.pushButton2_off.setObjectName(_fromUtf8("pushButton2_off"))
        self.pushButton3_on = QtGui.QPushButton(self.centralwidget)
        self.pushButton3_on.setGeometry(QtCore.QRect(100, 210, 110, 29))
        self.pushButton3_on.setObjectName(_fromUtf8("pushButton3_on"))
        self.pushButton3_off = QtGui.QPushButton(self.centralwidget)
        self.pushButton3_off.setGeometry(QtCore.QRect(230, 210, 110, 29))
        self.pushButton3_off.setObjectName(_fromUtf8("pushButton3_off"))
        self.pushButton4_on = QtGui.QPushButton(self.centralwidget)
        self.pushButton4_on.setGeometry(QtCore.QRect(100, 270, 110, 29))
        self.pushButton4_on.setObjectName(_fromUtf8("pushButton4_off"))
        self.pushButton4_off = QtGui.QPushButton(self.centralwidget)
        self.pushButton4_off.setGeometry(QtCore.QRect(230, 270, 110, 29))
        self.pushButton4_off.setObjectName(_fromUtf8("pushButton4_off_2"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 30, 171, 19))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 71, 19))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 210, 71, 19))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 160, 71, 19))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 270, 71, 19))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 340, 71, 19))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.pushButton_on = QtGui.QPushButton(self.centralwidget)
        self.pushButton_on.setGeometry(QtCore.QRect(100, 330, 110, 29))
        self.pushButton_on.setObjectName(_fromUtf8("pushButton_on"))
        self.pushButton_off = QtGui.QPushButton(self.centralwidget)
        self.pushButton_off.setGeometry(QtCore.QRect(230, 330, 110, 29))
        self.pushButton_off.setObjectName(_fromUtf8("pushButton_off"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Relés", None))
        self.pushButton1_on.setText(_translate("MainWindow", "Ligar", None))
        self.pushButton2_on.setText(_translate("MainWindow", "Ligar", None))
        self.pushButton1_off.setText(_translate("MainWindow", "Desligar", None))
        self.pushButton2_off.setText(_translate("MainWindow", "Desligar", None))
        self.pushButton3_on.setText(_translate("MainWindow", "Ligar", None))
        self.pushButton3_off.setText(_translate("MainWindow", "Desligar", None))
        self.pushButton4_on.setText(_translate("MainWindow", "Ligar", None))
        self.pushButton4_off.setText(_translate("MainWindow", "Desligar", None))
        self.label.setText(_translate("MainWindow", "Acionamento Relés", None))
        self.label_2.setText(_translate("MainWindow", "Relé 1", None))
        self.label_3.setText(_translate("MainWindow", "Relé 3", None))
        self.label_4.setText(_translate("MainWindow", "Relé 2", None))
        self.label_5.setText(_translate("MainWindow", "Relé 4", None))
        self.label_6.setText(_translate("MainWindow", "Todos", None))
        self.pushButton_on.setText(_translate("MainWindow", "Ligar", None))
        self.pushButton_off.setText(_translate("MainWindow", "Desligar", None))

