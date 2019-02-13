#!/usr/bin/env python
# -*- coding: utf-8 -*-

###################################################
#  __slots__: 限制实例的属性(减少ARM内存的使用)
###################################################
class B1(object):
    pass

b1 = B1()
b1.abc = 123

# 使用 __slots__
class B2(object):
    __slots__ = ('num',)

    def __init__(self):
        self.num = 123

b2 = B2()
b2.num = 456
try:
    b2.abc = 'abc'
except AttributeError as e:
    print('AttributeError:', e)

class C2(B2):
    pass

c2 = C2()
c2.abc = 'abc'
