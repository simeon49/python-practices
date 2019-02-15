#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import logging

logging.basicConfig(level=logging.DEBUG)


###################################################
#  读文件
###################################################
# 写法1
try:
    f = open('./base/15_io/random.txt', 'r', encoding='utf-8', errors='ignore')
except Exception as e:
    logging.error(e)
else:
    for s in f.readlines():
        logging.info('-> %s' % s)
finally:
    if f:
        f.close()  # 使用后关闭文件

# 写法2
try:
    with open('./base/15_io/random.txt', 'r') as f:
        for s in f.readlines():
            logging.info('-> %s' % s)
except Exception as e:
    logging.error(e)


###################################################
#  写文件
###################################################
# 写法1:
try:
    f = open('./base/15_io/random.txt', 'w', encoding='utf-8')
except Exception as e:
    logging.error(e)
else:
    for i in range(3):
        f.write(str(random.random()) + '\n')
finally:
    if f:
        f.close()

# 写法2:
try:
    with open('./base/15_io/random.txt', 'w', encoding='utf-8') as f:
        for i in range(3):
            f.write(str(random.random()) + '\n')
except Exception as e:
    logging.error(e)
