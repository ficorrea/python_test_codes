# -*- coding: utf-8 -*-

import threading
import random
import time


class Pista():
    escuderia = None
    pista = None

    def __init__(self):
        self.pista = threading.Semaphore(5)
        self.escuderia1 = Escuderia(self.pista)
        self.escuderia2 = Escuderia(self.pista)
        self.escuderia3 = Escuderia(self.pista)
        self.escuderia4 = Escuderia(self.pista)
        self.escuderia5 = Escuderia(self.pista)
        self.escuderia6 = Escuderia(self.pista)
        self.escuderia7 = Escuderia(self.pista)


class Escuderia():
    car1 = None
    car2 = None
    sem = None
    pst = None

    def __init__(self, pista):
        self.sem = threading.Semaphore(1)
        self.pst = pista
        self.car1 = Carro(1, 0, self.sem, self.pst)
        self.car2 = Carro(2, 0, self.sem, self.pst)
        self.car1.start()
        self.car2.start()


class Carro(threading.Thread):
    carro = None
    situacao = 0
    sem_escuderia = None
    sem_pista = None

    def __init__(self, carro, situacao, escud, pista):
        threading.Thread.__init__(self)
        self.carro = carro
        self.situacao = situacao
        self.sem_escuderia = escud
        self.sem_pista = pista

    def sorteio(self):
        valor = random.randint(1, 2)
        return valor

    def run(self):
        while True:
            time.sleep(2)
            sorteio = self.sorteio()
            if sorteio == 1 and self.situacao == 0:
                self.situacao = 2
                self.sem_escuderia.acquire()
                self.sem_pista.acquire()
                self.situacao = 1
            if sorteio == 2 and self.situacao == 1:
                self.situacao = 0
                self.sem_pista.release()
                self.sem_escuderia.release()
