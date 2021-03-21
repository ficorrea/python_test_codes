# -*- coding: utf-8 -*-

import random


class Individuo():

    def __init__(self):
        self.cromossomo = []
        self.temp = []

    def criar_digitado(self, tamanho_cromossomo):
        for i in range(len(tamanho_cromossomo)):
            self.cromossomo.append(int(tamanho_cromossomo[i]))
        return self.cromossomo

    def criar_aleatorio(self, tamanho_cromossomo):
        self.cromossomo = [random.randint(0, 1)
                           for i in range(tamanho_cromossomo)]
        return self.cromossomo

    def criar_porcentagem(self, tamanho_cromossomo, porcentagem):
        x = 0
        self.cromossomo = [0 for i in range(tamanho_cromossomo)]
        while x < porcentagem:
            pos = random.randint(0, tamanho_cromossomo - 1)
            if pos not in self.temp:
                self.temp.append(pos)
                self.cromossomo[pos] = 1
                x += 1
        return self.cromossomo

    def fitness(self, individuo_original, individuo):
        valor = 0
        for i in range(len(individuo)):
            if individuo[i] == individuo_original[i]:
                valor += 1
        return valor
