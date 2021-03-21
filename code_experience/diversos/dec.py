# Ex 1:
""" def decorator(funcao):
    def wrapper():
        print("Estou antes da execução da função passada como argumento")
        funcao()
        print("Estou depois da execução da função passada como argumento")
    return wrapper


def outra_funcao():
    print("Sou um belo argumento!")


funcao_decorada = decorator(outra_funcao)
funcao_decorada() """


# Ex 2
import time


def calc_time(funcao):
    def tempo():
        inicio = time.time()
        funcao()
        fim = time.time()
        print('Tempo total {}'.format(fim - inicio))
    return tempo


def descansa(funcao):
    def dormir():
        time.sleep(1)
        funcao()
    return dormir


@calc_time
@descansa
def gera_somas():
    for i in range(1000):
        print(i * (i+10))


gera_somas()
