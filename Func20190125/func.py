import math

print(abs(-123))

b = max(2, 3, 5, 0, 999)
print(b)

print(int('2222'))

print(float('12.22'))

print(int(12.22))

print(hex(123))


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-99))

# 如果想定义一个什么事也不做的空函数，可以用pass语句：
def nop():
    pass


nop()

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# my_abs('A')


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x1, y1 = move(100, 100, 60, math.pi / 6)
print(x1, y1)

r1 = move(100, 100, 60, math.pi / 6)
print(r1)


def power(x, n=2):
    i = n
    s = 1
    while i > 0:
        i = i - 1
        s = s * x
    return s


print(power(5))

print(power(5, 3))


def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


enroll('Sarah', 'F')

enroll('Adam', 'M', city='Tianjin')

def add_end(L=[]):
    L.append('END')
    return L

print(add_end([1, 2, 3]))

print(add_end())

print(add_end())
# 定义默认参数要牢记一点：默认参数必须指向不变对象！


def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

print(add_end())
print(add_end())

# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

calc_num = calc(1, 2)
print(calc_num)

nums = [1, 2, 3]
print(calc(*nums))


def calc2(*numbers):
    for n in numbers:
        print(n)

calc2(1, '23324', 12.2)

# 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30)
person('Adam', 45, gender='M', job='Engineer')

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])
person('Jack', 24, **extra)


# 命名关键字参数
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        print('city:',kw.get('city'))
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)

person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)


def person(name, age, *, city, job):
    print(name, age, city, job)

person('Jack', 24, city='Beijing', job='Engineer')


def person(name, age, *args, city, job):
    print(name, age, args, city, job)
# person('Jack', 24, 'Beijing', 'Engineer')

def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)

person('Jack', 24, job='Engineer')

# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
# 这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

print(fact(50))


def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


print(fact(10))












