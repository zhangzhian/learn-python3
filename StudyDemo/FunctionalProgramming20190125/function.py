from functools import reduce
import functools

f = abs
x = f(-20)
print(x)

# 一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数


def add(x, y, f):
    return f(x) + f(y)


z = add(-5, 6, abs)


print(z)


def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6])
# print(r)
print(list(r))


y = list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(y)


def add(x, y):
    return x + y


z = reduce(add, [1, 3, 5, 7, 9])
print(z)


def fn(x, y):
    return x * 10 + y


z = reduce(fn, [1, 3, 5, 7, 9])
print(z)


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


z = reduce(fn, map(char2num, '123456'))
print(z)


DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))


print(str2int('9090'))


def char2num(s):
    return DIGITS[s]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


def is_odd(n):
    return n % 2 == 1


z = list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
print(z)


def not_empty(s):
    return s and s.strip()


z = list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
print(z)


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列


# 打印1000以内的素数:
for n in primes():
    if n < 100:
        print(n)
    else:
        break


z = sorted([36, 5, -12, 9, -21])
print(z)

z = sorted([36, 5, -12, 9, -21], key = abs)
print(z)

z = sorted(['bob', 'about', 'Zoo', 'Credit'])
print(z)

z = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
print(z)

z = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
print(z)


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum


f = lazy_sum(1, 3, 5, 9)
print(f())


def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())


def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())


f = lambda x: x * x
print(f(9))


def now():
    print('2015-3-25')


f = now
f()

name = now.__name__
print(name)

print(f.__name__)


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


print('---------------------------')


@log
def now():
    print('2015-3-25')


now()


def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log('execute')
def now():
    print('2015-3-25')


now()


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now():
    print('2015-3-25')


now()


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log('execute')
def now():
    print('2015-3-25')


now()


print(int('12345'))

print(int('12345', base=8))

print(int('12345', base=16))


def int2(x, base=2):
    return int(x, base)


x = int2('1010001010101')
print(x)

int2 = functools.partial(int, base=2)
x = int2('100101')
print(x)





