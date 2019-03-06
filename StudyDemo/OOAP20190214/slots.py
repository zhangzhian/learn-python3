from types import MethodType


class Student(object):
    pass


def set_age(self, age): # 定义一个函数作为实例方法
    self.age = age


s = Student()
s.name = 'Michael' # 动态给实例绑定一个属性
print(s.name)

s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
s.set_age(25) # 调用实例方法
s.age # 测试结果


s2 = Student() # 创建新的实例
# s2.set_age(25) # 尝试调用方法


def set_score(self, score):
    self.score = score


Student.set_score = set_score

s.set_score(100)
s2.set_score(99)
print(s.score)
print(s2.score)

# __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称


s = Student() # 创建新的实例
s.name = 'Michael' # 绑定属性'name'
s.age = 25 # 绑定属性'age'
# s.score = 99 # 绑定属性'score'






















