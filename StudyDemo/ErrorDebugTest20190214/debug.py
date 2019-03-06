def foo(s):
    n = int(s)
    print('>>> n = %d' % n)
    return 10 / n


def main():
    foo('0')


def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n


def main():
    foo('0')


import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
# print(10 / n)

# 断点调试
s = '0'
n = int(s)
#print(10 / n)


import pdb

s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停
print(10 / n)









