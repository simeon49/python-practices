#!/usr/bin/env python
# -*- coding: utf-8 -*

# itertools: 迭代工具库
import itertools

###################################################
#  count
###################################################
# 奇数
print('============ itertools.count ============')
odds = itertools.count(start=1, step=2)
times = 0
for n in odds:
    print(n)
    times += 1
    if times > 10:
        break


###################################################
#  cycle
###################################################
# 循环打印"ABC""
print('============ itertools.cycle ============')
cs = itertools.cycle("ABC")
times = 0
for c in cs:
    print(c)
    times += 1
    if times > 10:
        break


###################################################
#  repeat
###################################################
print('============ itertools.repeat ============')
ns = itertools.repeat('A', times=5)
for n in ns:
    print(n)


###################################################
#  chain
###################################################
print('============ itertools.chain ============')
cs = itertools.chain('ABC', '123')
for c in cs:
    print(c)


###################################################
#  groupby: 把迭代器中相邻的重复元素挑出来放在一起：
###################################################
print('============ itertools.groupby ============')
for key, group in itertools.groupby('AAaaBBCAAAAAAA', key=lambda x: x.upper()):
    print(key, list(group))


# 练习: 技术算pi
from functools import reduce
def pi(N):
    '''
    step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    step 4: 求和:
    '''
    odds = itertools.count(start=1, step=2)
    # 一行的写法
    # pi = sum([4 / (2 * n - 1) * (-1) ** (n + 1) for n in range(1, N + 1)])

    # 使用itertools
    ns = itertools.count(start=1, step=2)
    ns = itertools.takewhile(lambda x: x <= 2 * N - 1, ns)
    cs = itertools.cycle([1, -1])
    l = [4 / n * next(cs) for n in ns]
    pi = sum(l)
    return pi

print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
