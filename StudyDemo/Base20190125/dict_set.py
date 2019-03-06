d = {'a': 95, 'b': 75, 'c': 85}

print(d['a'])

d['a'] = 79

print(d['a'])

if 'a' in d:
    print("123")

num = d.get('a')
print(num)

print(d.get('e'))

d.pop('a')
print(d)

s = set([1, 2, 3])
print(s)

d.setdefault('d', 123)
print(d)

s.add(7)

print(s)

a = [1, 4, 6, 11, 0, 99]
a.sort()
print(a)




























