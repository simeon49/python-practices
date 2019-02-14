#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import Iterable, Iterator

###################################################
# __iter__, __next__: 迭代
###################################################

class MyArray(object):
    def __init__(self):
        super(MyArray, self).__init__()
        self._arry = []
        self._cur_index = 0

    def push(self, o):
        self._arry.append(o)

    def __len__(self):  # 用于len
        return len(self._arry)

    def __iter__(self): # __iter__ 与 __next__ 使得对象可以迭代
        return self

    def __next__(self):
        if self._cur_index == len(self._arry):
            raise StopIteration
        res = self._arry[self._cur_index]
        self._cur_index += 1
        return res

arr = MyArray()
arr.push(100)
arr.push(200)
arr.push(300)
print('len(arr)=', len(arr)) # 3
print('isinstance(arr, Iterable)=', isinstance(arr, Iterable)) # True
print('isinstance(arr, Iterator)=', isinstance(arr, Iterator)) # True
for i, n in enumerate(arr):
    print('  (%s)->(%s)' %(i, n))
