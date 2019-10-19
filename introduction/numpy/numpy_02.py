import numpy as np

print('Lista random de idades')
idades = np.random.randint(24, 50, size=30)
print(idades)
print()

print('Lista random de idades')
idades = np.random.randint(24, 50, size=30)

# Desconstroi a tupla retornada pelo enumerate e pega o indice e valor
for (i, idade) in enumerate(idades):
  print(f"Idx: {i}, Idade: {idade}")

print()
idades2 = np.random.randint(24, 50, size=30)
for (idade, idade2) in zip(idades, idades2):
  print(idade, idade2)

print()
idades2 = np.random.randint(24, 50, size=30)
for (i, (idade, idade2)) in enumerate(zip(idades, idades2)):
  print(i, idade, idade2)

print()

print('List comprehensions')
media = idades.mean()
diffs = []
for idade in idades:
  diffs.append(idade - media)
print(diffs)
print()

# Em list comprehension
diffs = [idade - media for idade in idades]
print(diffs)
print()

# Map/Filter são lazy, só executam quando são evaluadas
# Em filter
diffs2 = filter(lambda idade: idades % 2 == 0, idades)
print(diffs2)
print()

# Em map - Ainda não executou
diffs3 = map(lambda idade : idade - media, diffs)
# Agora processa a lambda e retorna 
print(list(diffs3))

