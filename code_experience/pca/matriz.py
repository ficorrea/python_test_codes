import numpy as np
import numpy.linalg as la
import pandas as pd
from sklearn.decomposition import PCA

df = pd.read_csv('iris.csv')
data = df.iloc[:, 1:5].values

print(df.head())

# myarray = [0.251, 0.309, -0.253, -0.275, -0.289, 0.183, -0.227, -0.206, -0.234,
#           0.259, 0.282, -0.259, 0.232, 0.230, 0.169, -0.164, -0.229, 0.087]

# Necessária transposição da matriz por causa da função
cov_data = np.cov(np.transpose(data))

x, y = la.eig(cov_data)
# print(x) -> autovetores
# print(y) -> autovalores
# print(x/np.sum(x))

# Método com scikit
pca = PCA(n_components=3)
pca.fit(data)
print(pca.components_)
print(pca.explained_variance_)  # -> autovalores
#print(pca.explained_variance_ratio_)  # -> proporção da variância
