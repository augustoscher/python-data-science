import numpy as np
print('--- Testing ---')

a = np.arange(0, 10, 1)
l = lambda param : param ** 2
print(l(a))

l = list(range(0, 5))
print(l)
print()

print('Invertendo array')
print(l[::-1])
print()

print('Slice')
print(l[2:3])
print()

print('Set - Conjunto de elementos únicos')
s = {1, 2, 3, 4}
print(s)
print()

print('Soma ambos conjuntos')
s2 = s | {2, 5}
print(s2)
print()

print('Dictionaries')
pessoas = {'id1': 'Augusto', 'id2': 'Joao', 'id3': 'Outro'}
print(pessoas)

if 'id2' in pessoas:
    print(pessoas['id2'])
else:
    print('Não tem a chave')
print()

print('Functions')
is_pair = lambda x, y, z=10 : (x + y - z) % 2 == 0
print(is_pair(2, 3, 9))
print(is_pair(2, 3))
print()

print('Var args')
def somaaae(*args):
    res = 0
    for v in args:
        res += v
    return res

print(somaaae(1, 3, 4, 5))
print()

