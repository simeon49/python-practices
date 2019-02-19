#!/usr/bin/env python
# -*- coding: utf-8 -*-

# collections是Python内建的一个集合模块，提供了许多有用的集合类。

###################################################
#  namedtuple: 命名tuple
###################################################
print('============= collections.nametuple =============')
from collections import namedtuple
Point = namedtuple('Point', ('x', 'y'))
p = Point(1, 2)
print(p.x, p.y)
print('isinstance(p, Point): ', isinstance(p, Point)) # True
print('isinstance(p, tuple): ', isinstance(p, tuple)) # True


###################################################
#  deque: 双向列表, 在插入和删除时比线性存储的list快, 适用于需要插入
# 删除频繁的list
###################################################
print('============= collections.deque =============')
from collections import deque
q1 = deque(['a', 'b', 'c'])
q1.append('x')
q1.appendleft('y')
q1.insert(1, 'z')
q1.remove('a')
print(q1)


###################################################
#  defaultdict: 使用dict时，如果引用的Key不存在，就会抛出KeyError。
# 如果希望key不存在时，返回一个默认值，就可以用defaultdict
###################################################
print('============= collections.defaultdict =============')
from collections import defaultdict
d1 = defaultdict(lambda: 'N/A')
d1['a'] = 123
print(d1['a'])          # 123
print(d1['no_exist'])   # N/A


###################################################
#  OrderedDict: dict的key是无序的, OrderDict的key是有序的
###################################################
print('============= collections.OrderedDict =============')
from collections import OrderedDict
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)


###################################################
#  ChainMap: 可以把一组dict串起来并组成一个逻辑上的dict。ChainMap本身也是一个dict，
# 但是查找的时候，会按照顺序在内部的dict依次查找。
###################################################
print('============= collections.ChainMap =============')
import os, argparse
from collections import ChainMap

defaults = {
    'user': 'guest',
    'color': 'red'
}

# 构造命令行参数
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = { k: v for k, v in vars(namespace).items() if v }

# 组合成ChainMap
combined = ChainMap(command_line_args, os.environ, defaults)

# $ python ./inner_models/lean_collections.py
# $ python ./inner_models/lean_collections.py -c green -u root
# $ user=admin color=blue python ./inner_models/lean_collections.py
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])


###################################################
#  Counter: 计数器
###################################################
print('============= collections.Counter =============')
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] += 1

print(c)
