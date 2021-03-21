class Limite:

    def __init__(self, valor):
        self.valor = valor

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        num = self.a
        if num > self.valor:
            raise StopIteration
        self.a += 1
        return num


def main():
    for i in Limite(1024):
        print('Número:', i)

if __name__ == '__main__':
    main()
