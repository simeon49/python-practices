#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from collections import Iterable, Iterator

###################################################
# 高级使用
###################################################

class MyArray(object):
    def __init__(self):
        super(MyArray, self).__init__()
        self._arry = []
        self._cur_index = 0

    def push(self, o):
        self._arry.append(o)

    def __str__(self):  # 用于 print (返回用户看到的字符串)
        return 'MyArray object len: %d' % len(self._arry)

    def __repr__(self): # 返回程序开发者看到的字符串
        return 'MyArray object'

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

    def __getitem__(self, index):   # 使得对象可以向列表一样访问 arr[1]=200 or arr[:]
        if isinstance(index, int):
            return self._arry[index]
        # 切片
        elif isinstance(index, slice):
            start = index.start if index.start else 0
            stop = index.stop if index.stop else len(self._arry)
            step = index.step if index.step else 1
            print(start, stop, step)
            return self._arry[start:stop:step]

    def __setitem__(self, index, o):
        self._arry[index] = o

    def __delitem__(self, index):
        del self._arry[index]

    def __getattr__(self, attr):  # 只有属性找不到时会被调用 __getattribute__ 每次都会被调用
        try:
            index = int(re.findall(r'^index_([0-9]+)$', attr)[0])
            return self._arry[index]
        except:
            raise AttributeError('MyArray object has no attr %s' % attr)

    def __call__(self, *args, **kw): # 使得对象可以像函数一样调用
        print('object is called')

arr = MyArray()
print('print(arr)=', arr)    # MyArray object len: 0
arr           # MyArray object
arr.push(100)
arr.push(200)
arr.push(300)
print('len(arr)=', len(arr)) # 3
print('isinstance(arr, Iterable)=', isinstance(arr, Iterable)) # True
for i, n in enumerate(arr):
    print('  (%s)->(%s)' %(i, n))
print('arr[1]=', arr[1]) # 200
arr[1] = 2
print('arr[:]=', arr[:])

try:
    arr.not_exist_method
except AttributeError as e:
    print('AttributeError:', e)

print(arr.index_0) # 100
arr()
