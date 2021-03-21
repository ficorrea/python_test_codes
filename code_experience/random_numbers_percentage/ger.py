# -*- coding: utf-8 -*-

import random

num = []
t = int(input('total de numeros: '))
p = int(input('Porcentagem de números 1: '))

lista = [0 for i in range(t)]
print(lista)

p = p / 100
per = int(t * p)
print(per)

x = 0
while x < per:
    valor = random.randint(0, t - 1)
    if valor not in num:
        num.append(valor)
        lista[valor] = 1
        x += 1

print(num)

'''for i in range(t):
    if lista[i] is None:
        lista[i] = 1
    else:
        pass'''


print(lista)
