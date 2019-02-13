#!/usr/bin/env python
# -*- coding: utf-8 -*-

###################################################
# __getitem__: 使得对象可以向列表一样访问 arr[1]=200 or arr[:]
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

arr = MyArray()
arr.push(100)
arr.push(200)
arr.push(300)
print('len(arr)=', len(arr)) # 3
print('arr[1]=', arr[1]) # 200
arr[1] = 2
print('arr[:]=', arr[:])
del arr[1]
print('len(arr)=', len(arr)) # 2
