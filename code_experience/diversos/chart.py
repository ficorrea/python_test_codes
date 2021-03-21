import random


# total máximo dos pesos 81
peso = [16, 18, 1, 8, 12, 0, 5, 6, 2, 13]

# total máximo do benefício 306
beneficio = [32, 20, 25, 11, 35, 50, 47, 34, 19, 33]


def validar(ind, valor):
    u"""Valida o peso do indivíduo."""
    valido = 0
    for i in range(len(ind)):
        valido = valido + (peso[i] * ind[i])
    if valido <= valor:
        return True
    else:
        return None


def cria_individuo(genes, valor_peso):
    u"""Cria o indivíduo com base no peso."""
    individuo = []
    i = 0
    while i < 1:
        for i in range(genes):
            individuo.append(random.randint(0, 1))
        valido = validar(individuo, valor_peso)
        if valido is True:
            i += 1
            return individuo


def fitness(ind):
    u"""Calcula o fitness."""
    total = 0
    for i in range(len(ind)):
        total = total + (beneficio[i] * ind[i])
    return total


def sorteia_individuos(populacao, numero_individuos):
    u"""Escolhe uma quantidade de indivíduos aleatoriamente."""
    i = 0
    sorteados = []
    while i < numero_individuos:
        sorte = random.randint(0, len(populacao) - 1)
        if sorte not in sorteados:
            sorteados.append(sorte)
            i += 1
        else:
            pass
    return sorteados


print(cria_individuo(10, 50))
