import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('megac.csv')

# print(dataset)


x = dataset.iloc[:, 2:8].values
print(x)
y = list(range(1, 7))

plt.scatter(x[0], y)
plt.show()