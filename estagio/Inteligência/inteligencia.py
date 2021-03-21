
def gera(x):
    a = list(range(4))
    if x % 2 == 0:
        a[0] = 1
    else:
        a[0] = 0

    if x % 3 == 0 or x % 5 == 0:
        a[1] = 1
    else:
        a[1] = 0

    if x % 7 == 0 or x % 11 == 0:
        a[2] = 1
    else:
        a[2] = 0

    if x % 13 == 0 or x % 17 == 0:
        a[3] = 1
    else:
        a[3] = 0

    total = (8 * a[0]) + (4 * a[1]) + (2 * a[2]) + (1 * a[3])
    print(x, ':', a, '=', total)
    return total

num = []
for i in range(5000):
    numero = gera(i)
    if numero not in num:
        num.append(numero)
print(num)
