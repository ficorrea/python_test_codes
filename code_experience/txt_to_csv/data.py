# -*- coding: utf-8 -*-

import csv
import pandas as pd
import random

with open('dados.txt', 'r') as data:
    dataset = ('-1 ' + line.strip() for line in data)
    lines = (line.split() for line in dataset)
    with open('dados.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(('col1', 'col2', 'col3', 'col4', 'col5'))
        writer.writerows(lines)


d = pd.read_csv('dados.csv')
treinamento = d.iloc[:, 0:4].values
print(treinamento)
target = d.iloc[:, -1].values