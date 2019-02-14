#!/usr/bin/env python
# -*- coding: utf-8 -*-

###################################################
#  异常
#       异常参考表: https://docs.python.org/3/library/exceptions.html#exception-hierarchy
###################################################

# 正常执行
try:
    print('===== Start(Nomal) =====')
    r = 1 / 10
except ZeroDivisionError as e:
    print('except: ', e)
else:
    print('result: %s' % r)
finally:
    print('finally...')
print('===== End(Nomal) =====')

# 异常
try:
    print('===== Start(Exception) =====')
    r = 1 / 00
except ZeroDivisionError as e:
    print('except: ', e)
else:
    print('result: %s' % r)
finally:
    print('finally...')
print('===== Start(Exception) =====')


# 捕获多个异常
try:
    # do some things here
    pass
except ValueError as e:
    print('ValueError:', e)
except KeyError as e:
    print('KeyError:', e)


# 使用logging记录异常
import logging

try:
    1/0
except ZeroDivisionError as e:
    logging.exception(e)


# 自定义异常
class CustomerError(Exception):
    pass

try:
    raise CustomerError('an error')
except CustomerError as e:
    print('CustomerError:', e)
