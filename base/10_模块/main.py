#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import my_module

print(my_module.__doc__)  # this is a test module
print(my_module.__author__) # Simeon
print(my_module.__name__) # my_module
print(my_module.__file__) # /Users/simeon/WorkSpace/Practices/python-practices/base/10_模块/my_module/__init__.py
print(my_module.__package__) # my_module

my_module.say_hi()
my_module.say_hi('simeon')
