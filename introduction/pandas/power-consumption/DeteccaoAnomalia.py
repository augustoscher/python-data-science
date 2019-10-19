import numpy as np
import pandas as pd

class DeteccaoAnomalia:

  def __init__(self, df, coluna):
    self._coluna = coluna
    self._mean = df[coluna].mean()
    self._std = df[coluna].std()

  def detectar(self, df):
    return np.abs(df[self._coluna] - self._mean) > (2 * self._std)

if __name__ == '__main__':
  dataset = 'household_power_consumption.txt'
  df = pd.read_csv(dataset, delimiter=';', na_values=['?'])
  df['ano'] = df.Date.apply(lambda x: int(x.split('/')[-1]))

  df_2006_2009 = df[df.ano < 2010]
  df_2010 = df[df.ano == 2010]

  mean = df_2006_2009.Voltage.mean()
  std = df_2006_2009.Voltage.std()

  # Pega a diferença da media de voltagem entre 2010 e 2006 ate 2010
  # Pega somente valores absolutos
  # Filtra somente itens com voltagem maiores que duas vezes o desvio padrão
  # Gera uma lista de boolean usada para filtrar os itens.
  modelo = DeteccaoAnomalia(df_2006_2009, coluna='Voltage')
  anomalias = modelo.detectar(df_2010)

  # Print dos itens com anomalias utilizando a lista de boolean
  print('Itens com anomalias considerando Voltagem: ')
  print(df_2010[anomalias])
  print()

  print('Itens sem anomalias considerando Voltagem: ')
  print(df_2010[~anomalias])
