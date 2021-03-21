# -*- coding: utf-8 -*-

import random
from individuo import Individuo

ind = Individuo()


class Populacao():

    def __init__(self):
        self.populacao = []

    def criar_populacao(self, tamanho_populacao, tamanho_cromossomo):
        for i in range(tamanho_populacao):
            self.populacao.append([random.randint(0, 1) for i in range(
                tamanho_cromossomo)])
        return self.populacao

    def fitness_populacao(self, cromossomo_original, populacao):
        valores = []
        for i in range(len(populacao)):
            valores.append(ind.fitness(cromossomo_original, populacao[i]))
        return valores

    def mutacao(self, populacao, porcentagem):
        for i in range(len(populacao)):
            mutado = populacao[i]
            for j in range(len(mutado)):
                comp = round(random.random(), 2)
                if comp <= porcentagem:
                    if mutado[j] == 1:
                        mutado[j] = 0
                    else:
                        mutado[j] = 1
            populacao[i] = mutado
        return populacao

    def torneio(self, cromossomo_original, populacao, valor_k, quantidade_individuos):
        x = 0
        comp = round(random.random(), 2)
        escolhidos, valor = [], []
        while x < quantidade_individuos:
            numero = random.randint(0, len(populacao) - 1)
            if numero not in escolhidos:
                escolhidos.append(numero)
                x += 1
        for i in range(quantidade_individuos):
            valor.append(ind.fitness(
                cromossomo_original, populacao[escolhidos[i]]))
        if comp < valor_k:
            return populacao[valor.index(max(valor))]
        else:
            return populacao[valor.index(min(valor))]

    def gerar(self, cromossomo_original, populacao, prole, valor_k, quantidade_individuos):
        x = 0
        filhos_gerados = []
        while x < prole:
            gene1 = self.torneio(cromossomo_original,
                                 populacao, valor_k, quantidade_individuos)
            gene2 = self.torneio(cromossomo_original,
                                 populacao, valor_k, quantidade_individuos)
            numero = random.randint(0, len(gene1) - 1)
            escolha = random.randint(1, 2)
            if escolha == 1:
                filho = gene1[0:numero] + gene2[numero:len(gene1)]
            elif escolha == 2:
                filho = gene2[0:numero] + gene1[numero:len(gene1)]
            filhos_gerados.append(filho)
            x += 1
        return filhos_gerados

    def selecao_melhores(self, cromossomo_original, populacao, quantidade_individuos):
        melhores = []
        valores = self.fitness_populacao(cromossomo_original, populacao)
        peoples = populacao[:]
        for i in range(quantidade_individuos):
            pos = valores.index(max(valores))
            melhores.append(peoples[pos])
            peoples.pop(pos)
            valores.pop(pos)
        return melhores

    def verificar_solucao(self, cromossomo_original, populacao):
        for i in range(len(populacao)):
            if populacao[i] == cromossomo_original:
                print('Solucao encontrada: ')
                return True
        return False
