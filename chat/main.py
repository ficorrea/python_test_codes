# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore
import chat
from client import Cliente
import sys
import time
import threading


class tela(QtWidgets.QMainWindow, chat.Ui_MainWindow):
    porta = None
    mensagem = None
    user = None
    cliente = None
    evento = None
    imp = None

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        QtCore.QCoreApplication.processEvents()
        self.cliente = Cliente(self)
        self.evento = threading.Event()
        self.imp = threading.Thread(target=self.imprimir)
        self.imp.start()
        self.pushButton_enviar.clicked.connect(self.enviar)
        self.pushButton_conectar.clicked.connect(self.conectar)

    def conectar(self):
        self.porta = self.lineEdit_porta.text()
        if self.porta == '':
            self.porta = 8888
        self.cliente.conectar(self.porta)
        self.evento.set()

    def enviar(self):
        self.mensagem = self.lineEdit_msg.text()
        self.user = self.lineEdit_usuario.text()
        self.cliente.montar(self.user, self.mensagem)
        self.cliente.enviar_mensagens()

    def imprimir(self):
        self.evento.wait()
        self.cliente.recebe_mensagens()


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('cleanlooks')
    form = tela()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
