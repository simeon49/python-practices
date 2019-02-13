#!/usr/bin/env python
# -*- coding: utf-8 -*-

###################################################
# __str__, __repr__: 打印
###################################################

class MyArray(object):
    def __init__(self):
        super(MyArray, self).__init__()
        self._arry = []
        self._cur_index = 0

    def __str__(self):  # 用于 print (返回用户看到的字符串)
        return 'MyArray object len: %d' % len(self._arry)

    def __repr__(self): # 返回程序开发者看到的字符串
        return 'MyArray object'


arr = MyArray()
print('print(arr)=', arr)    # MyArray object len: 0
arr           # MyArray object
