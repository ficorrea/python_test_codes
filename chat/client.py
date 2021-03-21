# -*- coding: utf-8 -*-

import socket
import time


class Cliente():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    porta = None
    host = None
    mensagem = None

    def __init__(self, interface):
        self.interface = interface

    def montar(self, user, msg):
        self.mensagem = user + ' diz: ' + msg

    def conectar(self, port):
        self.porta = int(port)
        self.host = 'localhost'
        try:
            self.cliente.connect((self.host, self.porta))
            self.interface.listWidget_view.addItem('Conectado ao servidor')
        except Exception as e:
            print(e)
            time.sleep(1)
            self.conectar()
        return True

    def enviar_mensagens(self):
        self.cliente.sendall(self.mensagem.encode('utf-8'))

    def recebe_mensagens(self):
        while True:
            mensagem = self.cliente.recv(1024)
            msg = str(mensagem.decode('utf-8'))
            self.interface.listWidget_view.addItem(msg)
            msg = ''

    def iniciar_chat(self):
        self.enviar_mensagens()
