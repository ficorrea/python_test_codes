import random


def rand(a, b):
    num = random.randint(a, b)
    return num


def gender():
    num = rand(0, 1)
    if num == 1:
        return 'male'
    elif num == 0:
        return 'female'


def category():
    num = rand(0, 1)
    return num


def salary(min, max):
    num = rand(min, max)
    return num


def age():
    num = rand(18, 65)
    return num


def individuo():
    genero = gender()
    idade = age()
    if idade <= 25:
        sal = salary(1000, 5000)
        categoria = 0
    elif idade > 25 and idade < 40:
        sal = salary(6000, 15000)
        categoria = 1
    elif idade >= 40:
        sal = salary(16000, 30000)
        categoria = 2
    ind = genero, idade, sal, categoria
    return ind

def main(limite):
    lista = list(range(limite))
    i = 0
    while i < limite:
        lista[i] = individuo()
        i += 1
    for i in range(limite):
        print(lista[i])

if __name__ == '__main__':
    main(300)
