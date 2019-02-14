class Animal(object):
    def run(self):
        print("Animal is running....")


class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


dog = Dog()
dog.run()
dog.eat()
cat = Cat()
cat.run()


a = list() # a是list类型
b = Animal() # b是Animal类型
c = Dog() # c是Dog类型

r1 = isinstance(a, list)
r2 = isinstance(b, Animal)
r3 = isinstance(c, Dog)
r4 = isinstance(c, Animal)
print(r1, r2, r3, r4)

