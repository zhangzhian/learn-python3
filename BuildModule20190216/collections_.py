from collections import namedtuple, deque, defaultdict, OrderedDict, ChainMap, Counter
import os, argparse

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)

print(isinstance(p, Point))
print(isinstance(p, tuple))

# namedtuple('名称', [属性list]):
Circle = namedtuple('Circle', ['x', 'y', 'r'])

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)
q.pop()
print(q)

# 默认值是调用函数返回的，而函数在创建defaultdict对象时传入。
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
a = dd['key1']
b = dd['key2'] # key2不存在，返回默认值
print(a)
print(b)


d = dict([('a', 1), ('b', 2), ('c', 3)])
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(d)
print(od)
# OrderedDict的Key会按照插入的顺序排列，不是Key本身排序
od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print(list(od.keys())) # 按照插入的Key的顺序返回

# 构造缺省参数:
defaults = {
    'color': 'red',
    'user': 'guest'
}
print('-----------------------------------------------------------')
# 构造命令行参数:
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = { k: v for k, v in vars(namespace).items() if v }
# 组合成ChainMap:
combined = ChainMap(command_line_args, os.environ, defaults)

# 打印参数:
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])

c = Counter()
for ch in 'prggramming':
    c[ch] = c[ch]+1
print(c)









