# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import interface
import sys
import threading
from led_cube import Cubo


class tela(QtGui.QMainWindow, interface.Ui_MainWindow):

    sair = 0

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.cubo = Cubo()
        self.sair = 0
        self.radioButton_randomico.setEnabled(False)
        self.radioButton_randcol.setEnabled(False)
        self.radioButton_mix.setEnabled(False)
        self.radioButton_espiral.setEnabled(False)
        self.radioButton_none.setEnabled(False)
        self.radioButton_randcam.setEnabled(False)
        self.pushButton_ini.clicked.connect(self.inicia)
        self.pushButton_close.clicked.connect(self.fechar)
        self.radioButton_randomico.clicked.connect(self.randomico)
        self.radioButton_randcol.clicked.connect(self.randcol)
        self.radioButton_mix.clicked.connect(self.mix)
        self.radioButton_espiral.clicked.connect(self.espiral)
        self.radioButton_randcam.clicked.connect(self.randcam)
        self.radioButton_none.clicked.connect(self.none)

    def inicia(self):
        atualiza_tela = threading.Thread(target=self.update_tela)
        atualiza_tela.start()
        self.lineEdit.setText('Pronto')
        self.radioButton_randomico.setEnabled(True)
        self.radioButton_randcol.setEnabled(True)
        self.radioButton_mix.setEnabled(True)
        self.radioButton_espiral.setEnabled(True)
        self.radioButton_none.setEnabled(True)
        self.radioButton_randcam.setEnabled(True)
        self.pushButton_ini.setEnabled(False)

    def fechar(self):
        self.sair = 1
        exit()

    def randomico(self):
        self.lineEdit.setText('Modo Randômico')
        self.cubo.randomico()

    def none(self):
        self.lineEdit.setText('Nenhum')
        self.cubo.setup()

    def randcol(self):
        self.lineEdit.setText('Modo Randômico Colunas')
        self.cubo.random_colunas()

    def mix(self):
        self.lineEdit.setText('Modo Mix')
        self.cubo.mix()

    def espiral(self):
        self.lineEdit.setText('Modo Espiral')
        self.cubo.espiral_led()

    def randcam(self):
        self.lineEdit.setText('Modo Randômico Camadas')
        self.cubo.random_camadas()

    # Atualização de telas
    def update_tela(self):
        while self.sair != 1:
            if self.radioButton_randomico.isChecked():
                self.randomico()
            if self.radioButton_none.isChecked():
                self.none()
            if self.radioButton_randcol.isChecked():
                self.randcol()
            if self.radioButton_mix.isChecked():
                self.mix()
            if self.radioButton_espiral.isChecked():
                self.espiral()
            if self.radioButton_randcam.isChecked():
                self.randcam()


def main():
    app = QtGui.QApplication(sys.argv)
    form = tela()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
