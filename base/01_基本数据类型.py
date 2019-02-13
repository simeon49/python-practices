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

#############################
#  迭代 range
#############################
range(100)
for x in range([1,2,3]):
    print(x)
