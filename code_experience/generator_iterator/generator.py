import os

def limite(num):
    a = 0
    while a <= num:
        yield a
        a += 1

'''for i in limite(10):
	print(i)'''


# generator comprehension

quadrado = (i**2 for i in limite(10))
for i in quadrado:
    print(i)

os.system('stop')