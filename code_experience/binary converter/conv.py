# _*_ coding: utf-8 _*_


def converter(num):
    binario = []
    conv = gerar(num)
    i = 0
    soma = []
    while i < len(conv):
        valor = num - conv[i]
        if valor >= 0:
            binario.append(1)
            num = valor
            soma.append(conv[i])
        else:
            binario.append(0)
        i += 1
    binario = ''.join(map(str, binario))
    print('\nValor binario:', binario)
    soma = ','.join(map(str, soma))
    print('Números somados:', soma, '\n')


def gerar(num):
    ger = []
    tam = 1
    while num >= tam:
        ger.append(tam)
        tam *= 2
    ger.reverse()
    return ger


def main():
    while True:
        dec = int(input("Digite um numero: "))
        converter(dec)


if __name__ == '__main__':
    main()
