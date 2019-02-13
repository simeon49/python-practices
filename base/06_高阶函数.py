#!/usr/bin/env python
# -*- coding: utf-8 -*-

###################################################
#  高阶函数: 函数接收的参数中包含函数
###################################################

#############################
#  map
#############################
r1 = map(lambda x: x * x, [1, 2, 3, 4, 5]) # <map object at 0x10cff1c50> 迭代器
list(r1) # [1, 4, 9, 16, 25]

#############################
#  reduce
#############################
from functools import reduce
reduce(lambda a, b: a + b, [1, 2, 3, 4, 5]) # 15

# 练习: str转换为int
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': None}
def str2int(s):
    s = s.strip()
    def char2num(ch):
        return DIGITS[ch]
    return reduce(lambda a, b: a * 10 + b, map(char2num, s))

str2int('12345678')

# 练习: str转float
def str2float(s):
    s = s.strip()
    tn = 0
    if '.' in s:
        tn = len(s) - s.index('.') - 1
        s = s.replace('.', '')

    def char2num(ch):
        return DIGITS[ch]

    return reduce(lambda  a, b: a * 10 + b, map(char2num, s)) / 10 ** tn


#############################
#  filter
#############################
# 基数判断
def is_odd(n):
    return n % 2 == 1

r2 = filter(is_odd, [1,2,3,4,5]) # <filter object at 0x10d13e860>
list(r2) # [1, 3, 5]

# 练习: 素数生成器
# 计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单：
# 首先，列出从2开始的所有自然数，构造一个序列：
# 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
# 取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：
# 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
# 取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：
# 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
# 取新序列的第一个数5，然后用5把序列的5的倍数筛掉：
# 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
# 不断筛下去，就可以得到所有的素数。
def primes():
    def all_nums(start):
        n = start
        while True:
            yield n
            n += 1

    def not_divisible(n):
        return lambda x: x % n > 0

    l = all_nums(2)
    while True:
        prime = next(l)
        yield prime
        l = filter(not_divisible(prime), l)

for i, prime in enumerate(primes()):
    print(prime)
    if i >= 10:
        break

#############################
#  sorted
#############################
sorted([4,2,5,6,1,3,7]) # [1, 2, 3, 4, 5, 6, 7]
sorted([4,2,5,6,1,3,7], reverse=True) # [7, 6, 5, 4, 3, 2, 1]
l = [4,2,5,6,1,3,7]
l.sort()    # l = [1, 2, 3, 4, 5, 6, 7]

l = [('Tom', 87), ('Jack', 98), ('Jany', 66), ('Sun', 90)]
sorted(l, key=lambda x: x[0]) # [('Jack', 98), ('Jany', 66), ('Sun', 90), ('Tom', 87)]
