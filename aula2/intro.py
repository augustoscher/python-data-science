import numpy as np

np.random.seed(1)
a = np.random.normal(size=10)
print(a)
print()

print(a > 0)
print()

print(a + 10)
print()

print(a[3:8])
print()

print(a[[3, 5, 6]])
print()

print(a[[True, False, False, False, False, False, False, False, False, False]])
print()

x = a > 0
print(x)
print(a[x])
# print(a[a > 0])
print()


print(a[(a > -0.5) & (a < 0.5)])
