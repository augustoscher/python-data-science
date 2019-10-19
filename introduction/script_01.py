print('hello')

for i in [450, 3, 8, 932, 3]:
    print(i)

print()
for i in range(0, 5):
    print(i)

print()

arr = list(range(0, 5))
print(len(arr))

print()

dic = {'v1': [0, 1, 2, 3], 'v2': 'teste'}
print(dic)

print()


while True:
    valor = input('Digite um número: ')
    try:
        valor = int(valor)
    except ValueError:
        print("Valor inválido: {}".format(valor))
        break

    is_pair = lambda p : p % 2 == 0
    print("Digitou: {}".format(valor))
    if (is_pair(valor)):
        print(f"O valor {valor} é par")

print()
print('Generators')

def pair(v):
    return v % 2 == 0

def ler_valor():
    while True:
        valor = input('Digite um número: ')
        try:
            yield int(valor)
        except:
            raise StopIteration()

for valor in ler_valor():
    if pair(valor):
        print(f'{valor} é par')
    else:
        print(f'{valor} não é par')


