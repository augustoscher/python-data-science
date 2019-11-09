import numpy as np
from scipy.stats import mode

class KNN:

  def __init__(self, k):
    self._k = k
  
  def fit(self, X, y):
    self._X = X
    self._y = y

  def predict(self, X):
    predicoes = []
    for i in range(len(X)):
      distance = X[i, :] - self._X
      distance = np.square(distance)
      distance = np.sum(distance, axis=1)

      indices = np.argsort(distance)
      top_k = indices[self._k]
      moda = mode(self._y[top_k])
      predicoes.append(moda.mode[0])
    
    return predicoes