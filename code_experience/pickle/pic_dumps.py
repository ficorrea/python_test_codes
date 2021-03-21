import pickle as pic
from pickle import Pickler, Unpickler
import io
from collections import namedtuple

a = [1, 2, 3]
b = ('a', 'b', 'c')

""" pic.dump(a,  open('arquivo_a.txt', 'wb'))
c = pic.dumps(b, 2)
print(c)

d = pic.loads(c)
print(d)

e = pic.load(open('arquivo_a.txt', 'rb'))
print(e) """

""" Pickler(open('arquivo_a.sav', 'wb')).dump(a)
Pickler(file=open('arquivo_txt', 'wb')).dump(b)

c = Unpickler(open('arquivo_a.sav', 'rb')).load()
print(c) """

""" user = namedtuple('User', ['nome', 'sobrenome', 'idade'])
user_1 = user('Felipe', 'Corrêa', 33)
user_2 = user('Samanta', 'Kido', 33)
user_3 = user_1 + user_2
print(user_3.count(33)) """

""" from sklearn.datasets import make_regression
a, b = make_regression(n_samples=10, n_features=5, n_targets=3)
print(a)
print(b)
 """


import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
import numpy as np

df = pd.read_csv('data.csv')
#le = LabelEncoder()
#df['categoria'] = le.fit_transform(df['categoria'])

""" ohe = OneHotEncoder(categorical_features=[0], handle_unknown='ignore')
df.iloc[:, 0:] = ohe.fit_transform(df)
print(df) """

enc = OneHotEncoder(handle_unknown='ignore')
X = [['Male', 1], ['Female', 3], ['Female', 2]]
enc.fit(X)
print(X)

""" from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(df[:, 0:4], df[:, -1])

val = ohe.transform(6)
print(model.predict(val))
print(ohe.active_features_)
print(ohe.n_values_)
print(ohe.feature_indices_)
print(ohe.n_values)
print(ohe.handle_unknown) """
