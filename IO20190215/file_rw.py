
# f = open("/Users/zhangzhian/Desktop/PycharmProjects/IO20190215/test.txt", "r")

f = open("test.txt", "r")

s = f.read()
print(s)

f.close()

try:
    f = open('/Users/zhangzhian/Desktop/PycharmProjects/IO20190215/test.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()

with open('test.txt', 'r') as f:
    print(f.read())

f = open("test.txt", "r")
print("-------------------")
for line in f.readlines():
    print(line.strip())  # 把末尾的'\n'删掉
print("-------------------")

f = open("test.txt", "rb")
print(f.read())

f = open("test.txt", "w")
f.write("hello world")
f.close()

with open('test.txt', 'w') as f:
    f.write('Hello, world2!\n')

with open('test.txt', 'a') as f:
    f.write('Hello, world3!')


















