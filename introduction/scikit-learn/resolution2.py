# Reference: 
# https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html
# Aprendizado supervisionado - KNN

import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from scipy.stats import mode

# X is iris.data
# y is iris.targedistanciat
# X contains the features and y contains the labels
(X, y) = load_iris(return_X_y=True)

# Usa 80% dos dados para treinar o modelo
# Os 20% restantes são usados para testar o modelo
# x_train e x_test é oque eu conheço.
# y_train e y_test é o que quero descobrir
(X_train, X_test, y_train, y_test) = train_test_split(X, y, test_size=0.2, random_state=42)
# classify(k=5, train=(X_train, y_train), X_test=X_test)

k = 5
predicoes = []
for i in range(len(X_test)):
  # pega uma linha e diminui de uma matriz
  # tira a raiz quadrada
  distances = np.square(X_test[i, :] - X_train)
  # soma os valores da matriz, coluna por coluna
  distances = np.sum(distances, axis=1)

  # Ordena da menor para a maior distância e pega as primeiras "k" distâncias
  indices = np.argsort(distances)
  top_k = indices[:k]

  labels = y_train[top_k]
  # Pega o valor mais frequente (moda)
  moda = mode(labels)
  predicoes.append(moda.mode[0])

print(f'Predições: ', predicoes)