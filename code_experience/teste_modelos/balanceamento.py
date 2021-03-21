import pandas as pd

df = pd.read_csv('winequality-red.csv', sep=';')

df['quality'] = df.apply(lambda row: 1 if row['quality'] > 5 else 0, axis=1)

dfz = df[df.quality == 0]
dfo = df[df.quality == 1]

dfo = dfo.sample(744)

df = pd.concat([dfo, dfz], axis=0, ignore_index=True)
x = df.iloc[:, 0:-1].values
y = df.iloc[:, -1].values

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3) 

from sklearn.svm import SVC

svc = SVC()

model = svc.fit(x_train, y_train)
pred = model.predict(x_test)

from sklearn.metrics import confusion_matrix 

cm = confusion_matrix(y_test, pred)

###############################################################################

du = df[df.quality == 1]
dd = df[df.quality == 0]
dd = dd.sample(74)
df = pd.concat([du, dd], axis=0, ignore_index=True)

x = df.iloc[:, 0:-1].values
y = df.iloc[:, -1].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3) 

model = svc.fit(x_train, y_train)
pred = model.predict(x_test)

cmu = confusion_matrix(y_test, pred)

###############################################################################


svc_aj = SVC(class_weight='balanced')

model_aj = svc_aj.fit(x_train, y_train)
pred_aj = model_aj.predict(x_test)

cmu_aj = confusion_matrix(y_test, pred_aj)

###############################################################################

from sklearn.utils.class_weight import compute_class_weight
import numpy as np

un = compute_class_weight(class_weight=None, classes=np.unique(y), y=y)
bl = compute_class_weight(class_weight='balanced', classes=np.unique(y), y=y)
dc = compute_class_weight(class_weight={0: 2.5, 1: 2.5}, classes=np.unique(y), y=y)
