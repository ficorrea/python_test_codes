# Criação de arquivo csv estabelecendo número de linhas e colunas,
# além dos elementos que comporão os dados.


import csv
import random
import pandas as pd


colunas = ['col' + str(i) for i in range(10)]
data = list(range(100))
lines = list(range(100))
for i in range(100):
    data[i] = (str(random.randint(-1, 1)) for line in range(10))
for i in range(100):
    lines[i] = (line for line in data[i])
with open('table.csv', 'w') as table:
    writer = csv.writer(table)
    writer.writerow(colunas)
    writer.writerows(lines)


dataset = pd.read_csv('table.csv')
x = dataset.iloc[:, 0:5].values
