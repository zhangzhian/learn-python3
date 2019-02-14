
print(123)


class Student(object):
    # 特殊方法“__init__”前后分别有两个下划线！！！
    # def __init__(self, name, score):
    #     self.name = name
    #     self.score = score

    # 让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，
    # 实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'


bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
print(bart.get_name())
print(bart._Student__name)
bart.print_score()
lisa.print_score()
a = bart.get_grade()
b = lisa.get_grade()
print(a)
print(b)







































