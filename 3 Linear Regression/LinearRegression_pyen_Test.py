import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt

X, y = datasets.make_regression(n_samples =100, n_features=1, noise=20, random_state=4)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

from LinearRegression_pyen import LinearRegression

reg = LinearRegression()
reg.fit(X_train, y_train)
predicted = reg.predict(X_test)

def mse(y_true, y_predicted):
    return np.mean((y_true - y_predicted)**2)

accur = mse(y_test, predicted)
print("Accuracy: ",accur)
#========================================================
reg1 = LinearRegression(lr=0.001)
reg1.fit(X_train, y_train)
predicted = reg1.predict(X_test)


accur = mse(y_test, predicted)
print("Accuracy: ",accur)

import matplotlib.pyplot as plt
y_pred_line = reg1.predict(X)
cmap = plt.get_cmap("viridis")
fig = plt.figure(figsize=(8, 6))
m1 = plt.scatter(X_train, y_train, color=cmap(0.9), s=10)
m2 = plt.scatter(X_test, y_test, color=cmap(0.5), s=10)
plt.plot(X, y_pred_line, color="black", linewidth=2, label="Prediction")
plt.show()