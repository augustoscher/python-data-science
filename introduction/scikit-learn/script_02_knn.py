# Reference: 
# https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html
# Aprendizado supervisionado - Regressão Linear
# Tem uma entrada esperada como expected

import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# X é uma matriz
# y é um vetor/equação
(X, y) = load_iris(return_X_y=True)
# print(X)
# print(y)

# Usa 80% dos dados para treinar o modelo
# Os 20% restantes são usados para testar o modelo
data = train_test_split(X, y, test_size=0.2, random_state=1)
(X_train, X_test, y_train, y_test) = data

# KNN
classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
print(y_pred)
print(y_pred.shape)

# print(X_train.shape)
p1 = X_train[0, :]
p2 = X_test[0, :]

# ** 2 é ao quadrado
distancia = np.sum((p1 - p2) ** 2)
print(distancia)
