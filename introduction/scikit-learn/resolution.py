# Reference: 
# https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html
# Aprendizado supervisionado - KNN

import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from scipy.stats import mode


def classify(k, train, X_test):

  # X_train contains the training features
  # X_test contains the testing features
  # y_train contains the training label
  # y_test contains the testing labels
  (X_train, y_train) = train

  for i in range(len(X_test)):
    # Busca linha por linha da matriz
    x = X_test[i, :]

    # Potencia de 2
    distancia = np.sum((p1 - p2) ** 2)
    print(distancia)

    # calcula distância euclidiana
    diff_quadrado = (X_train - x) ** 2
    distancia = diff_quadrado.sum(axis=1)
    # print(distancia)

    # ordena da menor para a maior distância e pega as primeiras "k" distâncias
    min_k = distancia.argsort()[:k]
    # pega o valor mais frequente (moda)
    label = mode(y_train[min_k]).mode[0]
    yield label

# TODO Carregar e Splitar os dados em teste e treino e chamar a function