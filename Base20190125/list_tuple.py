classmates = ['a', 'b', 'c']
print(classmates)

print(len(classmates))

print(classmates[0])

print(classmates[-1])

print(classmates[-2])

classmates.append('d')

print(classmates)

classmates.insert(1, 'g')

print(classmates)

classmates.pop(2)

print(classmates)

classmates.pop()

print(classmates)

classmates[1] = 'b'

print(classmates)

classmates[2] = 123

print(classmates)

classmates[1] = [1, 2]

print(classmates)

# 元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改

classmates = (1, 2, 3)

print(classmates)

t = (1)

print(t)

t = (1,)

print(t)

t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'

print(t)
