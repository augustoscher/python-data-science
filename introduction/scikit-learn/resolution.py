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
    distances = np.square(X_test[i, :] - X_train)
    distances = np.sum(distances, axis=1)

    # ordena da menor para a maior distância e pega as primeiras "k" distâncias
    indices = np.argsort(distances)
    top_k = indices[:k]
    # pega o valor mais frequente (moda)
    label = mode(y_train[top_k]).mode[0]
    yield label

# TODO Carregar e Splitar os dados em teste e treino e chamar a function