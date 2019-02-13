#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 在python中 所有类型的数据都可以看做是对象
# 123 是 <class 'int'> 的实例
# def foo():
#     pass
# foo 是 <class 'function'> 的实例

###################################################
#  type: 返回对象的类型(class)
###################################################
type(123) # <class 'int'>
type('123') # <class 'str'>
type(None) # <class 'NoneType'>

type('abc')(123) # '123'

# types
import types
type(lambda x: x) == types.FunctionType # True
type(lambda x: x) == types.LambdaType # True
type((x for x in range(100))) == types.GeneratorType # True


###################################################
#  dir: 获取对象所有属性和方法
###################################################
dir('abc') # ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', ....]


###################################################
# hasattr, getattr, setattr
###################################################
class MyObject(object):
    def __init__(self):
        self.num = 7

    def power(self):
        return self.num * self.num

obj = MyObject()

hasattr(obj, 'num') # True
hasattr(obj, 'abc') # False
hasattr(obj, 'power') # True
# getattr(obj, 'asdf') # AttibuteError: 'MyObject' object has no attribute 'asdf'

setattr(obj, 'abc', 'abc')
getattr(obj, 'abc') # 'abc'
