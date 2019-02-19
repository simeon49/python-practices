#!/usr/bin/env python
# -*- coding: utf-8 -*-
import functools

###################################################
#  装饰器: 本质上就是一个返回为函数的高阶函数
###################################################
def log(fun):
    @functools.wraps(fun)  # 此处如果注释  则 add.__name__ 的值将会为 '_'
    def _(*args, **kw):
        print('call %s()' % fun.__name__)
        return fun(*args, **kw)
    return _

@log        # 等价于 foo = log(foo)
def foo():
    pass

foo() # call foo()

# 升级版
def log1(text):
    def decorator(fun):
        @functools.wraps(fun)
        def _(*args, **kw):
            print('call %s()' % fun.__name__)
            return fun(*args, **kw)
        return _

    return decorator if isinstance(text, str) else decorator(text)

@log1('some text ....')
def foo1():
    pass

@log1
def foo2():
    pass

foo1()  # call foo1()
foo2()  # call foo2()
