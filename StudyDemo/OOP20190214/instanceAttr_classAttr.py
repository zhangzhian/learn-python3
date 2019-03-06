class Student(object):

    name = 'Student'

    # def __init__(self, name):
    #     self.name = name


# s = Student('Bob')
# s.score = 90
s = Student()
print(s.name)
print(Student.name)
s.name = "hello"
print(s.name)
print(Student.name)
del s.name  # 如果删除实例的name属性
print(s.name)

















