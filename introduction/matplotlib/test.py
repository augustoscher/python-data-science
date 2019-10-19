import numpy as np
import matplotlib.pyplot as plt

idades = np.random.randint(24, 50, size=1000)
idades2 = np.random.randint(20, 60, size=1000)

# Histogram
(_, ax) = plt.subplots(1, 1, figsize=(15, 10))
ax.hist(idades, bins=26)
ax.set_title('Histograma')
ax.set_xlabel('Idades')
ax.set_ylabel('Qtd Pessoas')
plt.savefig('grafico.png')

# Scatter
(_, ax2) = plt.subplots(1, 1, figsize=(15, 10))
ax2.scatter(idades, idades2)
ax2.set_title('Scatter')
ax2.set_xlabel('Idades')
ax2.set_ylabel('Qtd Pessoas')
plt.savefig('grafico2.png')

