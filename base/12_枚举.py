#!/usr/bin/env python
# -*- coding: utf-8 -*-

###################################################
#  Enum: 枚举
###################################################

from enum import Enum, unique

# @unique装饰器可以帮助我们检查保证没有重复值
@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon
print(day1) # Weekday.Mon
print(day1.value) # 1

day2 = Weekday(2)
print(day2) # Weekday.Tue
print(day2.value) # 2

try:
    Weekday(7)
except ValueError as e:
    print('ValueError:', e)


# 也可以这样写
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
print(Month.Jan.value) # 1 默认从1开始
