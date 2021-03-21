import pandas as pd

dataset = pd.read_csv('dados.csv')

print(dataset)
# print(dataset.isnull().sum())

dataset.fillna(dataset['col1'].mean())

print(dataset)