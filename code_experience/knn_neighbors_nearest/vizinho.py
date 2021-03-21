from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import matplotlib


# help(pd)
data = pd.read_csv('dados.csv')
print(data)

x = data.iloc[:, [1, 2]].values
y = data.iloc[:, 3].values

#print(x)
print(y)

'''xtrain, xtest, ytrain, ytest = train_test_split(
    x, y, test_size=0.2, random_state=0)

classificador = KNeighborsClassifier(n_neighbors=5)
classificador.fit(xtrain, ytrain)

pred = classificador.predict(xtest)

from sklearn.metrics import confusion_matrix
matrix = confusion_matrix(ytest, pred)

print(matrix)'''