import pandas as pd

df = pd.read_csv('abalone.data', header=None)
nome_colunas = ['sex', 'length', 'diameter', 'height', 'whole_h', 'shucked_w', 'viscera_w', 'shell_w', 'rings']
df.columns = nome_colunas

df.to_csv('data_abalone.csv', index=False, encoding='utf-8')