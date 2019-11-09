# Reference: 
# https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html
# Aprendizado supervisionado - KNN

import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from scipy.stats import mode


# def classify(k, train, X_test):

#   # X_train contains the training features
#   # X_test contains the testing features
#   # y_train contains the training label
#   # y_test contains the testing labels
#   (X_train, y_train) = train

#   classifier = KNeighborsClassifier(n_neighbors=k)
#   classifier.fit(X_train, y_train)
#   y_pred = classifier.predict(X_test)

#   for i in range(len(X_test)):
#         # Busca linha por linha da matriz
#         x = X_test[i, :]

#         # ** 2 é ao quadrado
#         # distancia = np.sum((p1 - p2) ** 2)
#         # print(distancia)

#         # calcula distância euclidiana
#         diff_quadrado = (X_train - x) ** 2
#         distancia = diff_quadrado.sum(axis=1)
#         # print(distancia)

#         # ordena da menor para a maior distância e pega as primeiras "k" distâncias
#         min_k = distancia.argsort()[:k]
#         # pega o valor mais frequente (moda)
#         label = mode(y_train[min_k]).mode[0]
#         yield label

# ================================================================================================

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

  # Retorna os indices ordenados
  indices = np.argsort(distances)
  top_k = indices[:k]

  labels = y_train[top_k]
  moda = mode(labels)
  predicoes.append(moda.mode[0])

print(f'Predições: ', predicoes)

