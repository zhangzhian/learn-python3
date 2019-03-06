from datetime import datetime, timedelta, timezone

now = datetime.now()
print(now)

print(type(now))

dt = datetime(2019, 4, 19, 12, 20, 33) # 用指定日期时间创建datetime
print(dt)

ts = dt.timestamp() # 把datetime转换为timestamp

print(ts)

t = 1555647633.0
print(datetime.fromtimestamp(t))

cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))

print(now + timedelta(hours=10))
print(now - timedelta(days=1))
print(now + timedelta(days=2, hours=12))

tz_utc_8 = timezone(timedelta(hours=8)) # 创建时区UTC+8:00
dt = now.replace(tzinfo=tz_utc_8) # 强制设置为UTC+8:00

print(dt)

# 把时间从UTC+0时区转换为UTC+8:
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
utc8_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print('UTC+0:00 now =', utc_dt)
print('UTC+8:00 now =', utc8_dt)


















