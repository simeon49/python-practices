#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import Iterable, Iterator

#############################
#  生成器: generator
#############################
# 1. 一个普通的列表
L1 = [x * x for x in range(10)] # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 2. 使用生成器
L2 = (x * x for x in range(10)) # <generator object <genexpr> at 0x10ce680f8>
# 使用next迭代 (注意: 能被next迭代的对象 必须是Iterator对象)
isinstance(L1, Iterable) # True
isinstance(L2, Iterable) # True
isinstance(L1, Iterator) # False  isinstance(iter(L1), Iterator)
isinstance(L2, Iterator) # True
while True:
    try:
        print(next(L2))
    except StopIteration:
        pass

# 等价于下面方式
for n in L2:
    print(n)


# 练习: 斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
def fib(max):
    n = 0
    a, b = 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1

for num in fib(7):
    print(num)

# 练习: 杨辉三角定义如下：
#           1
#          / \
#         1   1
#        / \ / \
#       1   2   1
#      / \ / \ / \
#     1   3   3   1
#    / \ / \ / \ / \
#   1   4   6   4   1
#  / \ / \ / \ / \ / \
# 1   5   10  10  5   1
def triangles(max):
    l = [1]
    n = 0
    while n < max:
        yield l
        l = [1] + [l[i] + l[i + 1] for i in range(n)] + [1]
        n += 1

for l in triangles(7):
    print(l)
