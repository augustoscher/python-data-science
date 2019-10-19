import pandas as pd

# DataFrame reading csv file
df = pd.read_csv('household_power_consumption.txt', delimiter=';', na_values=['?'])
print(df.info())
print()

# Gerando uma nova coluna em dataframe
df['ano'] = df.Date.apply(lambda x: int(x.split('/')[-1]))

# Retorna todos os anos
print(df.ano)

# Retorna somente os itens de 2010
print(df.ano < 2010)
