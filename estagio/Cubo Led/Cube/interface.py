# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created: Sun Apr  2 23:37:44 2017
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
        MainWindow.resize(416, 379)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton_ini = QtGui.QPushButton(self.centralwidget)
        self.pushButton_ini.setGeometry(QtCore.QRect(140, 30, 110, 29))
        self.pushButton_ini.setObjectName(_fromUtf8("pushButton_ini"))
        self.radioButton_randomico = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_randomico.setGeometry(QtCore.QRect(30, 190, 125, 24))
        self.radioButton_randomico.setObjectName(_fromUtf8("radioButton_randomico"))
        self.radioButton_randcol = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_randcol.setGeometry(QtCore.QRect(30, 220, 201, 24))
        self.radioButton_randcol.setObjectName(_fromUtf8("radioButton_randcol"))
        self.radioButton_mix = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_mix.setGeometry(QtCore.QRect(30, 280, 125, 24))
        self.radioButton_mix.setObjectName(_fromUtf8("radioButton_mix"))
        self.radioButton_espiral = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_espiral.setGeometry(QtCore.QRect(30, 250, 125, 24))
        self.radioButton_espiral.setObjectName(_fromUtf8("radioButton_espiral"))
        self.radioButton_none = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_none.setGeometry(QtCore.QRect(30, 130, 125, 24))
        self.radioButton_none.setObjectName(_fromUtf8("radioButton_none"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 80, 351, 31))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton_close = QtGui.QPushButton(self.centralwidget)
        self.pushButton_close.setGeometry(QtCore.QRect(140, 320, 110, 29))
        self.pushButton_close.setObjectName(_fromUtf8("pushButton_close"))
        self.radioButton_randcam = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_randcam.setGeometry(QtCore.QRect(30, 160, 211, 24))
        self.radioButton_randcam.setObjectName(_fromUtf8("radioButton_randcam"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Cubo de Led 3^3", None))
        self.pushButton_ini.setText(_translate("MainWindow", "Iniciar", None))
        self.radioButton_randomico.setText(_translate("MainWindow", "Randômico", None))
        self.radioButton_randcol.setText(_translate("MainWindow", "Colunas Randômicas", None))
        self.radioButton_mix.setText(_translate("MainWindow", "Mix", None))
        self.radioButton_espiral.setText(_translate("MainWindow", "Espiral", None))
        self.radioButton_none.setText(_translate("MainWindow", "Nenhum", None))
        self.pushButton_close.setText(_translate("MainWindow", "Fechar", None))
        self.radioButton_randcam.setText(_translate("MainWindow", "Camadas Randômicas", None))

