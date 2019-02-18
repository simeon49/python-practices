#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 日期与时间处理

###################################################
#  datetime 获取当前日期和时间
###################################################
print('============= datetime.datetime =============')
from datetime import datetime
now = datetime.now()
print(now)          # 2019-02-18 17:16:38.635506
print(type(now))    # <class 'datetime.datetime'>

# 创建日期
dt = datetime(2019, 2, 17, 12, 30)
print(dt)               # 2019-02-17 12:30:00

# timestamp
print(dt.timestamp())   # 1550377800.0

# timestamp 转datetime
# 2019-02-17 12:30:00  (东8区时间 UTC+8:00)
print(datetime.fromtimestamp(1550377800.0))

# UTC 标准市区的时间
print(datetime.utcfromtimestamp(1550377800.0))  # 2019-02-17 04:30:00

# str转换为datetime
print(datetime.strptime('2019-02-17 12:30:00',
                        '%Y-%m-%d %H:%M:%S'))  # 2019-02-17 12:30:00

# datetime转换为str
print(now.strftime('%a, %b %d %H:%M'))  # Mon, Feb 18 17:25

# datetime加减
from datetime import timedelta
print(dt + timedelta(hours=10))  # 2019-02-17 22:30:00
print(dt + timedelta(days=2, hours=12))  # 2019-02-20 00:30:00

# 设置时区
from datetime import timezone
tz_utc_8 = timezone(timedelta(hours=8))  # 创建时区UTC+8:00
print('now: ', now)                      # 2019-02-18 17:30:32.241769
# 2019-02-18 17:30:32.241769+08:00
print('utc8: ', now.replace(tzinfo=tz_utc_8))


# 练习: 假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，
# 均是str，请编写一个函数将其转换为timestamp：
import re
def to_timestamp(dt_str, tz_str):
    tz_number = int(re.match(r'UTC([-\+]\d{1,2}):00', tz_str).groups()[0])
    # print(tz_number)
    tz = timezone(timedelta(hours=tz_number))
    d = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    d = d.replace(tzinfo=tz)
    return d.timestamp()


# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')
