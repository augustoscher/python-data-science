import csv

f = open('household_power_consumption.txt')
r = csv.DictReader(f, delimiter=';')
print(next(r))

