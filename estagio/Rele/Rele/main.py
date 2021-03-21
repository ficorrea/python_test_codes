# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import interface
import sys
import time
import threading
from rele import Rele


class tela(QtGui.QMainWindow, interface.Ui_MainWindow):

	sair = 0
	rl = 0
	
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self)
		self.rele = Rele()
		self.sair = 0
		self.rl= 0
		self.pushButton1_on.setEnabled(True)
		self.pushButton1_off.setEnabled(False)
		self.pushButton2_on.setEnabled(True)
		self.pushButton2_off.setEnabled(False)
		self.pushButton3_on.setEnabled(True)
		self.pushButton3_off.setEnabled(False)
		self.pushButton4_on.setEnabled(True)
		self.pushButton4_off.setEnabled(False)
		self.pushButton_on.setEnabled(True)
		self.pushButton_off.setEnabled(True)
		self.pushButton1_on.clicked.connect(self.r1_on)
		self.pushButton1_off.clicked.connect(self.r1_off)
		self.pushButton2_on.clicked.connect(self.r2_on)
		self.pushButton2_off.clicked.connect(self.r2_off)
		self.pushButton3_on.clicked.connect(self.r3_on)
		self.pushButton3_off.clicked.connect(self.r3_off)
		self.pushButton4_on.clicked.connect(self.r4_on)
		self.pushButton4_off.clicked.connect(self.r4_off)
		self.pushButton_on.clicked.connect(self.r_on)
		self.pushButton_off.clicked.connect(self.r_off)
		self.r_off()


	def r1_on(self):
		self.rele.liga(1)
		self.pushButton1_on.setEnabled(False)
		self.pushButton1_off.setEnabled(True)
			
	def r1_off(self):
		self.rele.desliga(1)
		self.pushButton1_off.setEnabled(False)
		self.pushButton1_on.setEnabled(True)

	def r2_on(self):
		self.rele.liga(2)
		self.pushButton2_on.setEnabled(False)
		self.pushButton2_off.setEnabled(True)
			
	def r2_off(self):
		self.rele.desliga(2)
		self.pushButton2_off.setEnabled(False)
		self.pushButton2_on.setEnabled(True)

	def r3_on(self):
		self.rele.liga(3)
		self.pushButton3_on.setEnabled(False)
		self.pushButton3_off.setEnabled(True)
			
	def r3_off(self):
		self.rele.desliga(3)
		self.pushButton3_off.setEnabled(False)
		self.pushButton3_on.setEnabled(True)

	def r4_on(self):
		self.rele.liga(4)
		self.pushButton4_on.setEnabled(False)
		self.pushButton4_off.setEnabled(True)
			
	def r4_off(self):
		self.rele.desliga(4)
		self.pushButton4_off.setEnabled(False)
		self.pushButton4_on.setEnabled(True)

	def r_on(self):
		self.rele.liga(8)
		self.pushButton_on.setEnabled(False)
		self.pushButton1_on.setEnabled(False)
		self.pushButton2_on.setEnabled(False)
		self.pushButton3_on.setEnabled(False)
		self.pushButton4_on.setEnabled(False)
		self.pushButton_off.setEnabled(True)
		self.pushButton1_off.setEnabled(True)
		self.pushButton2_off.setEnabled(True)
		self.pushButton3_off.setEnabled(True)
		self.pushButton4_off.setEnabled(True)
			
	def r_off(self):
		self.rele.desliga(8)
		self.pushButton_off.setEnabled(False)
		self.pushButton1_off.setEnabled(False)		
		self.pushButton2_off.setEnabled(False)
		self.pushButton3_off.setEnabled(False)
		self.pushButton4_off.setEnabled(False)
		self.pushButton_on.setEnabled(True)
		self.pushButton1_on.setEnabled(True)
		self.pushButton2_on.setEnabled(True)
		self.pushButton3_on.setEnabled(True)
		self.pushButton4_on.setEnabled(True)
			

def main():
	app = QtGui.QApplication(sys.argv)
	form = tela()
	form.show()
	app.exec_()

if __name__ == '__main__':
	main()

