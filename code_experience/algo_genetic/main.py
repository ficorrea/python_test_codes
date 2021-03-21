# -*- coding: utf-8 -*-

from individuo import Individuo
from populacao import Populacao
import matplotlib.pyplot as graf
from os import system

ind = Individuo()
pop = Populacao()

opc, x = 0, 0
cro, vy = [], []
geracao_maxima = 10000

'''opc = int(input('[1]Digitar genes\n[2]Gerar automático\n[3]Gerar automático,'
                ' mas definindo a porcentagem de números 1\n\n'
                'Escolha: '))

if opc == 1:
    cromossomo = str(input('Digite sequencia de genes: '))
    tam = len(cromossomo)
    cro = ind.criar_digitado(cromossomo)
elif opc == 2:
    tam = int(input('Tamanho do cromossomo: '))
    cro = ind.criar_aleatorio(tam)
elif opc == 3:
    tam = int(input('Tamanho do cromossomo: '))
    pct = int(input('Porcentagem de números 1: '))
    pct = int(pct / 100 * tam)
    cro = ind.criar_porcentagem(tam, pct)'''

tamanho_populacao = 10
tam = 30

cro = ind.criar_aleatorio(tam)
print('Sequencia gerada: \n', cro)
peoples = pop.criar_populacao(tamanho_populacao, tam)

# tamanho_populacao = int(input('Tamanho da população: '))
# peoples = pop.criar_populacao(tamanho_populacao, tam)


def imprimir(x, cromossomo_original, popul):
    pop = Populacao()
    valores = pop.fitness_populacao(cromossomo_original, popul)
    maior = valores.index(max(valores))
    print('Geração', x, ' : ->', popul[maior])

while x < geracao_maxima:
    imprimir(x, cro, peoples)
    peoples = pop.selecao_melhores(cro, peoples, tamanho_populacao)
    valores = pop.fitness_populacao(cro, peoples)
    vy.append(max(valores))
    filhos = pop.gerar(cro, peoples, tamanho_populacao // 2, 0.75, 3)
    filhos = pop.mutacao(filhos, 0.05)
    peoples = peoples + filhos
    solucao = pop.verificar_solucao(cro, peoples)
    if solucao is True:
        system('clear')
        print('Original: ', cro)
        imprimir(x, cro, peoples)
        break
    elif x > geracao_maxima:
        print('Valor não alcançado!!!')
        break
    x += 1

vx = list(range(len(vy)))
graf.plot(vx, vy)
graf.show()
