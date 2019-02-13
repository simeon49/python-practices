#!/usr/bin/env python
# -*- coding: utf-8 -*-

###################################################
# __len__: 长度
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

arr = MyArray()
arr.push(100)
arr.push(200)
arr.push(300)
print('len(arr)=', len(arr)) # 3
