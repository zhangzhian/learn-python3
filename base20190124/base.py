# -*- coding: utf-8 -*-
a = 10
if a >= 0:
    print(a)
else:
    print(-a)

print("I'am OK ... 123")
print('I\'am \"Ok\"')

print('''line1
line2 
line3''')

print('\\\t\\')
# Python还允许用r''表示''内部的字符串默认不转义
print(r'\\\t\\')

print(r'''hello,\n
world''')

True

False

print(3 > 2)
print(2 > 3)

# 布尔值可以用and、or和not运算。

print(True and False)

print(True or False)

print(not False)

# 空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。

print(None)

a = 1

b = '123'

c = True

print(a, b, c)


a = 'ABC'
b = a
a = 'XYZ'
print(b)
print(a)

PI = 3.14159265359
print(PI)

print(10/3)
print(10//3)

print("你好")


print(ord('a'))
print(chr(97))

print('\u4e2d\u6587')

print('ABC'.encode('ascii'))

print('中文'.encode('utf-8'))

# print('中文'.encode('ascii'))

print(b'ABC'.decode('ascii'))

print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))

print(len('ABC'))

print(len('中文'))

print('Hello, %s' % 'world')

print('Hi, %s, you have $%d.' % ('zza', 1000000))

# 占位符	替换内容
# %d	整数
# %f	浮点数
# %s	字符串
# %x	十六进制整数

print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

print('Age: %s. Gender: %s' % (25, True))

print('growth rate: %d%%' % 7)














