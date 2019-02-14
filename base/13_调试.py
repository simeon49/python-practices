#!/usr/bin/env python
# -*- coding: utf-8 -*-

###################################################
#  断言
###################################################
def toUpper(s):
    assert isinstance(s, str), 's is not str!'
    return s.upper()

try:
    toUpper(123)
except AssertionError as e:
    print('AssertionError:', e)


###################################################
#  logging
###################################################
import logging
logging.basicConfig(level=logging.DEBUG)

logging.debug('debug here')
logging.info('info here')
logging.warn('warn here')
logging.error('error here')


###################################################
#  pdb: 设置断点
###################################################
import pdb
# pdb.set_trace()
