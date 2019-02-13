#!/usr/bin/env python
# -*- coding: utf-8 -*-

###################################################
# __call__: 使得对象可以像函数一样调用
###################################################

class MyObj(object):

    def __call__(self, *args, **kw):
        print('object is called')

obj = MyObj()
print(callable(obj)) # True
obj()
