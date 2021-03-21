# -*- coding: utf-8 -*-

import socket
from threading import Thread

lista_cliente = []


class Servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host_name = '127.0.0.1'
    porta = 8888
    max_conexoes = 10
    client = None
    user_conectados = 0

    def __init__(self):
        self._bind_socket(self.host_name, self.porta)

    def _bind_socket(self, host_name, porta):
        if host_name:
            self.host_name = host_name
        if porta:
            self.porta = int(porta)
        self.servidor.bind((self.host_name, self.porta))

    def start(self):
        self.servidor.listen(self.max_conexoes)
        self.status_servidor()
        self.monitorar_clientes()

    def status_servidor(self):
        print('Servidor iniciado...')
        print('HOST: ' + self.host_name)
        print('IP: ' + str(self.porta))
        print('Usuários conectados: ', self.user_conectados)

    def monitorar_clientes(self):
        while True:
            conexao_client, cliente_ip = self.servidor.accept()
            self._novo_cliente(conexao_client)
            lista_cliente.append(conexao_client)
            thread = ThreadConexoes(conexao_client)
            thread.start()
        self.servidor.close()

    def _novo_cliente(self, conexao_client):
        if conexao_client not in lista_cliente:
            self._enviar_mensagem('Você está conectado ao servidor!\n',
                                  conexao_client)
            self.user_conectados += 1
            print('Usuários conectados: ', self.user_conectados)

    def _enviar_mensagem(self, mensagem, conexao_client):
        conexao_client.sendall(mensagem.encode('utf-8'))


class ThreadConexoes(Thread):

    def __init__(self, conexao_client):
        Thread.__init__(self)
        self.conexao_client = conexao_client

    def conexoes(self):
        while True:            
            dados = self.conexao_client.recv(1024).decode('utf-8')
            reply = dados
            for conexao in lista_cliente:
                conexao.sendall(reply.encode('utf-8'))
        self.conexao_client.close()

    def run(self):
        while True:
            self.conexoes()

servidor = Servidor()
servidor.start()
