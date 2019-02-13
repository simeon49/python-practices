#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Iterable, Iterator

###################################################
# __getattr__: 获取属性
###################################################
class MyObj(object):
    def __getattr__(self, attr):  # 只有属性找不到时会被调用 __getattribute__ 每次都会被调用
        if attr == 'default':
            return 'default'
        raise AttributeError('MyObj has no attribute %s' % attr)

obj = MyObj()
obj.default
try:
    obj.not_exsit_method
except AttributeError as e:
    print('AttributeError:', e)


# 练习: 链式调用
class Chain(object):
    def __init__(self, path):
        self._path = path

    def __getattr__(self, attr):
        return Chain(r'%s/%s' % (self._path, attr))

    def __str__(self):
        return self._path

print(Chain('').Users.simeon.WorkSpace.Practices.python_practices) # /Users/simeon/WorkSpace/Practices/python_practices
