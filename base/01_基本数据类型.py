#!/usr/bin/env python
# -*- coding: utf-8 -*-

#############################
#  整数 int
#############################
a1 = 1234
print('a1=%d' % a1)

#############################
#  浮点数 float
#############################
f1 = 12.34
f2 = -9.123
f3 = 1.2e-5
print('f1=%f f2=%f f3=%f' % (f1, f2, f3))

#############################
#  字符串 str
#############################
s1 = 'abc'
s2 = 'abc\n'
s3 = r'abc\n'   # 不转义
s4 = '''这是一个多行文本:
    第一行
    第二行
'''
print('s1=%s' % s1)
print('s2=%s' % s2)
print('s3=%s' % s3)
print('s4=%s' % s4)
# python 默认使用unicode编码
ord('A') # 65
ord('中') # 20013
chr(66) # 'B'
chr(25991) # '文'
'\u4e2d\u6587' # 等价于 '中文'

#############################
#  布尔 bool
#############################
b1 = True
b2 = False
print('b1={} b2={}'.format(b1, b2))

#############################
#  空值 NoneType
#############################
a1 = None
a1 is None

#############################
#  列表 list
#############################
lst = ['Michael', 'Bob', 'Tracy']
# 第一个元素
lst[0]  # 'Michael'
# 倒数第一个
lst[-1] # 'Tracy'
# 添加元素
lst.append('Admin') # 'Michael', 'Bob', 'Tracy', 'Admin'
# 出栈
lst.pop() # 'Admin'

#############################
#  元组 tuple
#############################
l = ('Michael', 'Bob', 'Tracy') # ('Michael', 'Bob', 'Tracy')
l = (1,) # (1)

#############################
#  字典/map dict
#############################
d = {'a': 1, 'b': 2}

#############################
#  集合 set
#############################
s1 = {1,2,3,3,2,1,4} # {1, 2, 3, 4}
s2 = {3,4,5,6}

s1 & s2 # {3, 4}
s1 | s2 # {1, 2, 3, 4, 5, 6}

# -------------------------------- 下面的不属于基本类型 --------------------------------

#############################
#  迭代 range
#############################
range(100)
for x in range(100):
    print(x)

# 注意 range() 对象是可迭代的 但不是可迭代对象
from collections import Iterable, Iterator
print(isinstance(range(100), Iterable)) # True
print(isinstance(range(100), Iterator)) # False
try:
    next(range(100))
except TypeError as e:
    print('TypeError:', e)


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


#############################
#  还有很多....
#############################
