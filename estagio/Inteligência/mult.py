# Multi-regressão

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv('data.csv')

px = data.iloc[:, :-1].values
py = data.iloc[:, 1].values

'''print(len(px))
print(px)
print(py)'''

px_train, px_test, py_train, py_test = train_test_split(
    px, py, test_size=0.2, random_state=0)

# print(px_train)
# print(py_train)

regressor = LinearRegression()
regressor.fit(px_train, py_train)

y_pred = regressor.predict(px_test)
# y_pred = regressor.predict(101)

# print(y_pred)

plt.plot(px, py)
plt.scatter(px_test, y_pred, color='red')
plt.show()
