import numpy as np

print(np.sum([1, 2, 3, 4, 5]))
print()

idades = np.random.randint(24, 50, size=30)
print(idades)
print()

# Media: soma todos e divide pela qtd de elementos
print(int(idades.mean()))

# Mediana: ordena a lista e pega o valor do meio.
# Se a lista conter qtd impar de elementos, pega os dois do meio, soma e divide por 2
print(np.median(idades))
print()

# Operações vetorizadas
idades1 = np.random.randint(24, 50, size=31).astype(np.int)
idades2 = np.random.randint(24, 50, size=31).astype(np.int)

diff = idades1 - idades2
print(diff)

# Media de idade da subtração de idades1 - idades2
# Sabemos que a diferença da media de idades é
print(np.round(diff.mean(), 3))
print()

# Normal: gera números aleatórios com a mesma probabilidade de aparecerem
idades3 = np.random.normal(30, 3, size=10)
print(np.round(idades3, 3))
print()

# Gera array de boleanos com considerando a regra para cada posição
array = np.random.randint(0, 50, size=30).astype(np.int)
v = array > 15
print(v)
print()

# Retorna so os itens que são true
print(array[v])
print()

