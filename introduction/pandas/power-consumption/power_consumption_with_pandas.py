import pandas as pd

# DataFrame reading csv file
df = pd.read_csv('household_power_consumption.txt', delimiter=';', nrows=10000, na_values=['?'])
df.info()
print()

a = df.describe()
print(type(a))
print(a['Sub_metering_3'])
print(a['Sub_metering_3'].mean())
print(a['Sub_metering_3'].std())
print()

print(df.mean())
print()

coluna = 'Date'
print(df[coluna])









