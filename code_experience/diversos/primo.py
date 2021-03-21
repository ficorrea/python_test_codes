from time import sleep

def ehprimo(numero):
    fator = 2
    while numero % fator != 0 and fator < numero // 2:
        fator += 1
    if numero % fator == 0:
        return False
    else:
        return True


numero = 1
while(True):
    print(numero, ehprimo(numero))
    sleep(1)
    numero += 1

        
