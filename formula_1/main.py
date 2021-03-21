# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QThread, SIGNAL
import view.interface
import threading
import sys
import time
from controller.classe_controle import Pista


class tela(QtGui.QMainWindow, view.interface.Ui_Form):
    pista = None
    ciclo = 0
    qtd_pista = 0
    qtd_wait = 0
    qtd_box = 0
    
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.ciclo = 0
        self.pista = Pista()
        self.thread_loop = threading.Thread(target=self.start)
        self.pushButton_ini.clicked.connect(self.begin)
        self.qtd_pista = 0
        self.qtd_wait = 0
        self.qtd_box = 0

    def begin(self):
        self.thread_loop.start()
        
    def upt_ciclo(self):
        self.ciclo += 1
        self.label_ciclo.setText(str(self.ciclo))

    def upt_status(self, situacao):
        if situacao == 0:
            self.qtd_box += 1
            return 'Box'
        if situacao == 1:
            self.qtd_pista += 1
            return 'Pista'
        if situacao == 2:
            self.qtd_wait += 1
            return 'Aguardando'

    def upt_quantidade(self):
        self.label_car_pista.setText(str(self.qtd_pista))
        self.label_car_box.setText(str(self.qtd_box))
        self.label_car_wait.setText(str(self.qtd_wait))
        self.qtd_pista = 0
        self.qtd_wait = 0
        self.qtd_box = 0

    def upt_carros(self):
        self.label_car11.setText(self.upt_status(self.pista.escuderia1.car1.situacao))
        self.label_car12.setText(self.upt_status(self.pista.escuderia1.car2.situacao))
        self.label_car21.setText(self.upt_status(self.pista.escuderia2.car1.situacao))
        self.label_car22.setText(self.upt_status(self.pista.escuderia2.car2.situacao))
        self.label_car31.setText(self.upt_status(self.pista.escuderia3.car1.situacao))
        self.label_car32.setText(self.upt_status(self.pista.escuderia3.car2.situacao))
        self.label_car41.setText(self.upt_status(self.pista.escuderia4.car1.situacao))
        self.label_car42.setText(self.upt_status(self.pista.escuderia4.car2.situacao))
        self.label_car51.setText(self.upt_status(self.pista.escuderia5.car1.situacao))
        self.label_car52.setText(self.upt_status(self.pista.escuderia5.car2.situacao))
        self.label_car61.setText(self.upt_status(self.pista.escuderia6.car1.situacao))
        self.label_car62.setText(self.upt_status(self.pista.escuderia6.car2.situacao))
        self.label_car71.setText(self.upt_status(self.pista.escuderia7.car1.situacao))
        self.label_car72.setText(self.upt_status(self.pista.escuderia7.car2.situacao))


    def start(self):
        while True:
            time.sleep(1.8)
            self.upt_carros()
            self.upt_quantidade()
            time.sleep(0.1)
            self.upt_ciclo()

def main():
    app = QtGui.QApplication(sys.argv)
    form = tela()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
