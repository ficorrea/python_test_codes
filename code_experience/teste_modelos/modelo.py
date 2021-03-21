#!/usr/bin/env python3

import pandas as pd

df = pd.read_csv('data_criada.csv')
x = df.iloc[:, 0:-1].values
y = df.iloc[:, -1].values

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

from sklearn.ensemble import RandomForestClassifier

rfor = RandomForestClassifier(n_estimators=100, n_jobs=-1, criterion='entropy')
rfor.fit(x_train, y_train)
pred = rfor.predict(x_test)

from sklearn.metrics import accuracy_score

accuracy_score(y_test, pred)
