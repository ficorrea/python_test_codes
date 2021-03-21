import random as rd
import pandas as pd
import numpy as np

colunas = ['col' + str(i) for i in range(5)]
dataset = pd.read_table('bl.data', sep='\,', engine='python', names=colunas)
x = dataset.iloc[:, 1:5].values
y = dataset.iloc[:, 0]

b = list(range(len(x)))
a = rd.sample(b, int(len(x) * 0.8))
c = [item for item in b if item not in a]

x_train = np.asarray([x[i] for i in a])
y_train = np.asarray([y[i] for i in a])

x_train = np.asarray(x_train)
# print(x_train)
# print(y_train)

# print(x[x_train[0]], y[y_train[0]])

t = [[rd.randint(0, 1000) for i in range(10)] for j in range(3)]
print(t)
