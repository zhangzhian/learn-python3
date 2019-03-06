import psutil

print(psutil.cpu_count()) # CPU逻辑数量
print(psutil.cpu_count(logical=False))  # CPU物理核心

print(psutil.cpu_times())

# for x in range(10):
#     a = psutil.cpu_percent(interval=1, percpu=True)
#     print(a)

print(psutil.virtual_memory())
print(psutil.swap_memory())


a = psutil.disk_partitions() # 磁盘分区信息
b = psutil.disk_usage('/') # 磁盘使用情况
c = psutil.disk_io_counters() # 磁盘IO
print(a)
print(b)
print(c)

a = psutil.net_io_counters() # 获取网络读写字节／包的个数
b = psutil.net_if_addrs() # 获取网络接口信息
c = psutil.net_if_stats() # 获取网络接口状态
print(a)
print(b)
print(c)

a = psutil.pids() # 所有进程ID
print(a)
p = psutil.Process(a[0]) # 获取指定进程ID=3776，其实就是当前Python交互环境
print(p.name())
print(p.exe())

print(psutil.test())

