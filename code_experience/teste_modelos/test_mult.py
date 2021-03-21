from multiprocessing import Process, Lock, current_process
from time import sleep
import os

def soma_persiste(x):
    with open('result.csv', 'a+') as file:
        file.write('{},{},{}\n'.format(x, x+x, x*x))


def terminate(processo):
    processo.join()
    processo.terminate()
    print(p, p.is_alive())
    processo.close()


if __name__ == "__main__":
    for i in range(100):
        p = Process(target=soma_persiste, args=(i,))
        p.start()
        terminate(p)