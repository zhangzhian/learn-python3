from collections.abc import Iterable
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print([L[0], L[1], L[2]])

print(L[0:3])

print(L[:3])

print(L[-2:])

print(L[-2:-1])

L = list(range(100))
print(L)

print(L[:10])

print(L[-10:])

print(L[::5])

print(L[:])

print('ABCDEFG'[:3])

print('ABCDEFG'[::2])

d = {'a': 1, 'b': 2, 'c': 3}

for key in d:
    print(key)
    print(d.get(key))

x = isinstance('abcd', Iterable)  # str是否可迭代

y = isinstance(123, Iterable)  # 整数是否可迭代

print(x)
print(y)

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)





















