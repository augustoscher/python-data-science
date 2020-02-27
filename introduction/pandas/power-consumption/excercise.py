import pandas as pd

dataset = 'household_power_consumption.txt'
df = pd.read_csv(dataset, delimiter=';', na_values=['?'])
df['ano'] = df.Date.apply(lambda x: int(x.split('/')[-1]))
# print(df.ano)

df_2006_2009 = df[df.ano < 2010]
df_2010 = df[df.ano == 2010]

mean = df_2006_2009.Voltage.mean()
std = df_2006_2009.Voltage.std()

# Pega a diferença da media de voltagem entre 2010 e 2006 ate 2010
# Pega somente valores absolutos
# Filtra somente itens com voltagem maiores que duas vezes o desvio padrão
# Gera uma lista de boolean usada para filtrar os itens.
anomalias = (df_2010.Voltage - mean).abs() > (2 * std)

# Print dos itens com anomalias utilizando a lista de boolean
print('Itens com anomalias considerando Voltagem: ')
print(df_2010[anomalias])
print()

print('Itens sem anomalias considerando Voltagem: ')
print(df_2010[~anomalias])
