#!/usr/bin/env python
# -*- coding: utf-8 -*-

###################################################
# __new__: 创建实例
###################################################

class MyObj(object):
    def __new__(cls, *args, **kw):
        print('__new__')
        return object.__new__(cls, *args, **kw)

    def __init__(self):
        print('__init__')

obj = MyObj()


# 练习: 单例模式
class Single(object):
    instance = None
    def __new__(cls, *args, **kw):
        if not cls.instance:
            cls.instance = super(cls, *args, **kw)
        return cls.instance

obj1 = Single()
obj2 = Single()

print(id(obj1))
print(id(obj2))


# 练习: 工厂模式
class Fruit(object):
    def say_hi(self):
        print('I am %s' % self.__class__.__name__)

class Apple(Fruit):
    pass

class Orange(Fruit):
    pass

class FruitFactory(object):
    fruits = {'apple': Apple, 'orange': Orange}

    def __new__(cls, name):
        assert isinstance(name, str), 'name is not str'
        name = name.lower()
        if name in cls.fruits:
            return cls.fruits[name]()
        else:
            return Fruit()

apple = FruitFactory('apple')
orange = FruitFactory('orange')
other = FruitFactory('other')

apple.say_hi()
orange.say_hi()
other.say_hi()
