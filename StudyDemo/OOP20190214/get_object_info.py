import types

print(type(123))
a = type('str')
print(a)
print(type(abs))
print(type(a))

print(type(123) == type(456))


def fn():
    pass


b1 = type(fn) == types.FunctionType

b2 = type(abs) == types.BuiltinFunctionType

b3 = type(lambda x: x) == types.LambdaType

b4 = type((x for x in range(10))) == types.GeneratorType

print(b1, b2, b3, b4)


class Animal(object):
    pass


class Dog(Animal):
    pass


class Husky(Dog):
    pass


c1 = Animal()
c2 = Dog()
c3 = Husky()

print(isinstance(c2, Husky))
print(isinstance(c2, Animal))
print(isinstance(c3, Dog) and isinstance(c3, Animal))

print(isinstance([1, 2, 3], (list, tuple)))

d = dir('ABC')

for i in d:
    print(i)

print(len('abc'))
print('ABC'.__len__())


class MyDog(object):
    def __len__(self):
        return 100


e = MyDog()
print(len(e))


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()
print(hasattr(obj, 'x')) # 有属性'x'吗？
print(hasattr(obj, 'y')) # 有属性'x'吗？
setattr(obj, 'y', 19) # 设置一个属性'y'
print(hasattr(obj, 'y')) # 有属性'y'吗？
print(getattr(obj, 'y')) # 获取属性'y'
print(obj.y) # 获取属性'y'

print(getattr(obj, 'z', 404)) # 获取属性'z'，如果不存在，返回默认值404
















