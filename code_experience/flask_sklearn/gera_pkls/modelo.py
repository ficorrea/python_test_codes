import pandas as pd
import numpy as np

data = pd.read_csv('iris.csv')
data.Species = data.Species.apply(str.lower)

from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(handle_unknown='ignore')
species = ohe.fit_transform(data.Species.values.reshape(-1, 1)).toarray()

ohe.transform(np.reshape('iris-setosa', (-1, 1))).toarray()[0]

from sklearn.model_selection import train_test_split
x = data.iloc[:, 1:5].values
y = species[:, 1:]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=30, random_state=42)
classifier.fit(x_train, y_train)

pred = classifier.predict([[5.1, 0.2, 0.9, 1]])
pred = np.insert(pred, 0, values=float(0))
np.sum(pred)
ohe.inverse_transform([pred])[0][0]

from sklearn.externals import joblib
joblib.dump(classifier, 'class.pkl')
joblib.dump(ohe, 'ohe.pkl')

# Cria meio que um json
print(ohe.__dict__)
print(classifier.__dict__)