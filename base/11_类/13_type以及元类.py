#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# python是动态语言, 所有的类型都是对象, 所有的对象都可以在运行时创建包括 class
#
###################################################
# type: 是一切对象的最基础类型
###################################################
type(123)               # <class 'int'>
type(type(123))         # <class 'type'>

type('abc')             # <class 'str'>
type(type('abc'))       # <class 'type'>

type(True)              # <class 'bool'>
type(type(True))        # <class 'type'>

type({'a': 1})          # <class 'dict'>
type(type({'a': 1}))    # <class 'type'>

type((x * x for x in range(10)))        # <class 'generator'>
type(type((x * x for x in range(10))))  # <class 'type'>

def foo():
    pass

type(foo)               # <class 'function'>
type(type(foo))         # <class 'type'>

class Base(object):
    pass

class Child(Base):
    pass

c1 = Child()
type(c1)                # <class '__main__.Child'>
type(type(c1))          # <class 'type'>


###################################################
# type: 用于创建类 class
###################################################
# 正常情况下
class ObjectA(object):
    def foo(self):
        print('fooA')

o1 = ObjectA()
o1.foo() # 'fooA'

# 使用type创建
def foo(self):
    print('fooB')

# type() 函数参数
#     1.object_or_name: class的名称 or 对象, 如果是对象则返回创建这个对象的类
#     2.bases: 继承的父类集合, 注意python支持多继承
#     3.dict: class的方法字典
ObjectB = type('ObjectB', (object,), {'foo': foo})
o2 = ObjectB()
o2.foo() # 'fooB'


###################################################
# metaclass: 用于改变类的创建行为
###################################################
class ToLowerMetaclass(type):  # 元类必须继承type
    def __new__(cls, name, bases, attrs):
        # 将所有方法变为小写
        for key, value in list(attrs.items()):
            if key.startswith('_'):
                continue
            print(key, '->', key.lower())
            attrs[key.lower()] = value
            del attrs[key]
        return type.__new__(cls, name, bases, attrs)

class ObjectC(object, metaclass=ToLowerMetaclass):
    def __init__(self):
        self.NUM = 123

    def FOO(self):
        print('fooC')

o3 = ObjectC()
try:
    o3.FOO()
except AttributeError as e:
    print('AttributeError:', e)
o3.foo()           # fooC
print(o3.NUM)      # 123       # metaclass 只改变 类ObjectC的属性 而不改变 ObjectC的实例的属性
