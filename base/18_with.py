#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
logging.basicConfig(level=logging.DEBUG)

###################################################
# with: 基本用法
###################################################
print('========== with 基本用法1 ==========')
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
# 让自己写的类的对象可以使用with
###################################################
print('========== 让自己写的类的对象可以使用with ==========')
class Query(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...' % self.name)

with Query('Tom') as q:
    q.query()


###################################################
# contextmanager
###################################################
print('========== contextmanager ==========')

class Query(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)

from contextlib import contextmanager

@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')


with create_query('Tom') as q:
    q.query()


###################################################
# closing
###################################################
from contextlib import closing
from urllib.request import urlopen

# 自己实现closing
# @contextmanager
# def closing(obj):
#     try:
#         yield obj
#     finally:
#         obj.close()

print('========== closing ==========')
with closing(urlopen('http://www.baidu.com')) as page:
    for line in page:
        print(line)
