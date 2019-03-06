from collections.abc import Iterable
from collections.abc import Iterator

# 可迭代对象
a = isinstance([], Iterable)

b = isinstance({}, Iterable)

c = isinstance('abc', Iterable)

d = isinstance((x for x in range(10)), Iterable)

print(a)
print(b)
print(c)
print(d)

# 迭代器
a = isinstance([], Iterator)

b = isinstance({}, Iterator)

c = isinstance('abc', Iterator)

d = isinstance((x for x in range(10)), Iterator)

print('-----------------------')
print(a)
print(b)
print(c)
print(d)

e = isinstance(iter(()), Iterator)

f = isinstance(iter('abc'), Iterator)
print('-----------------------')
print(e)
print(f)









