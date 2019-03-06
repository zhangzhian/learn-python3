import os

print(os.name)  # 是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
print(os.uname())  # 详细的系统信息
print(os.environb)  # 环境变量

print(os.environb.get(b'PATH'))

print("------------------------")
print(os.path.abspath('.'))

print(os.path.join('/Users/zhangzhian/Desktop/PycharmProjects/IO20190215', 'test'))
print(os.mkdir('/Users/zhangzhian/Desktop/PycharmProjects/IO20190215/test'))
print(os.rmdir('/Users/zhangzhian/Desktop/PycharmProjects/IO20190215/test'))

print(os.path.split('/Users/zhangzhian/Desktop/PycharmProjects/IO20190215/test.txt'))
print(os.path.splitext('/Users/zhangzhian/Desktop/PycharmProjects/IO20190215/test.txt'))

# os.rename('test2.txt', 'test.py')

# os.remove('test.py')
# 列出当前目录下的所有目录
f = [x for x in os.listdir('.') if os.path.isdir(x)]
print(f)
# 列出所有的.py文件
p = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
print(p)

