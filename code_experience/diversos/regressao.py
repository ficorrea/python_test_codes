import random as rd

b, y = [], []
t = 0
for i in range(1, 101):
    x = rd.random()
    b.append(t)
    y.append(x*3+1)
    t += 1+x

import matplotlib.pyplot as plt

plt.scatter(b, y)
plt.show()
