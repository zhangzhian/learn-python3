import logging


try:
    print('try...')
    # r = 10 / 0
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
except BaseException as e:
    print('except:', e)
finally:
    print('finally...')
print('END')

# Python所有的错误都是从BaseException类派生的，常见的错误类型和继承关系看这里：
#
# https://docs.python.org/3/library/exceptions.html#exception-hierarchy


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
        # logging.exception(e)
    finally:
        print('finally...')

main()


# def main():
#     bar('0')
#
# main()

class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n


# foo('0')


def foo1(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n


def bar():
    try:
        foo1('0')
    except ValueError as e:
        print('ValueError!')
        raise

bar()





















