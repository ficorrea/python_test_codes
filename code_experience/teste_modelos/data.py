""" import pandas as pd

df = pd.read_csv('data.csv')

def soma(a, b):
    return a + b

df['soma'] = df.apply(lambda row: row['num1'] * row['num2'], axis=1)
print(df) """


""" import numpy as np
np.random.seed(1)
data = np.random.randn(50000, 2) * 20 + 20

from sklearn.cluster import DBSCAN
od = DBSCAN(min_samples=2, eps=3)
cl = od.fit_predict(data)
print(list(cl).count(-1))

from sklearn.ensemble import IsolationForest
clf = IsolationForest(behaviour='new', max_samples=100, random_state=1, contamination='auto')
pred = clf.fit_predict(data)
print(list(pred).count(-1)) """

""" import random as rd

x = [rd.randint(1, 6) for i in range(0, 1000000)]
print('1: {}\n2: {}\n3: {}\n4: {}\n5: {}\n6: {}'.format(x.count(1), x.count(2), x.count(3), \
                                                        x.count(4), x.count(5), x.count(6))) """

def gera():
    valor = 0
    while True:
        yield valor        
        valor += 1

g = gera()

print(next(g))
print(next(g))
print(next(g))