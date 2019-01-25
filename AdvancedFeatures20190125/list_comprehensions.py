import os

a = list(range(1, 11))
print(a)

b = [x * x for x in range(1, 11)]
print(b)

c = [x * x for x in range(1, 11) if x % 2 == 0]
print(c)

d = [m + n for m in 'ABC' for n in 'XYZ']
print(d)

e = [d for d in os.listdir('.')]  # os.listdir可以列出文件和目录
print(e)

d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
    print(k, '=', v)

f = [k + '=' + v for k, v in d.items()]
print(f)

L = ['Hello', 'World', 'IBM', 'Apple']
g = [s.lower() for s in L]
print(g)







