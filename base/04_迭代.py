#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 判断一个对象是可迭代对象
from collections import Iterable

isinstance('abc', Iterable) # str是否可迭代
isinstance([1,2,3], Iterable) # list是否可迭代
isinstance(123, Iterable) # 整数是否可迭代

# 字符串遍历
for ch in 'abc':
    print(ch)

# 数组遍历
for item in ['a', 'b', 'c']:
    print(item)

for i, item in enumerate(['a', 'b', 'c']):
    print(i, item)


# 字典遍历
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

for value in d.values():
    print(value)

for key, value in d.items():
    print(key, value)
