# Reference: 
# https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html
# Aprendizado supervisionado - Regressão Linear
# Tem uma entrada esperada como expected

import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# X é uma matriz
# y é um vetor/equação
(X, y) = load_diabetes(return_X_y=True)

# Pega 20% dos dados e joga para teste
data = train_test_split(X, y, test_size=0.2, random_state=1)
(X_train, X_test, y_train, y_test) = data

# Cria modelo de regressão linear
modelo = LinearRegression()

# Treina o modelo
modelo.fit(X_train, y_train)

# Predições das informações com aproximação
y_hat = modelo.predict(X_test)

# Quanto meu algoritmo é bom em relação ao que eu esperava
print(modelo.score(X_test, y_test))

# Erro quadrado médio. Quanto meu algoritmo em média, erra :/
# Desempenho
# y_hat = previsão
# y_test = o que era esperado
print(np.square(y_hat - y_test).mean())