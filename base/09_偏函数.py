#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import partial

###################################################
#  偏函数
###################################################
int('123456', base=8) # 42798
int('123456', base=16) # 1193046
int('123456', base=10) # 123456

int8 = partial(int, base=8)
int16 = partial(int, base=16)

int8('123456') # 42798
int16('123456') # 1193046
