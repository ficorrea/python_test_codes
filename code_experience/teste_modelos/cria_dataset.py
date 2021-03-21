#!/usr/bin/env python3

import numpy as np
import pandas as pd

COLS = 10
ROWS = 1000

colunas = ['col_{}'.format(i) for i in range(COLS)]

data = pd.DataFrame(data=np.random.rand(ROWS, COLS), columns=colunas)

a = np.random.randint(0, 2, 1000)

data['target'] = a

data.to_csv('data_criada.csv', index=False)
