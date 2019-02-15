#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

###################################################
#  os: 与操作系统相关的库, 不同的操作系统提供的方法会有区别
#      比如 window 上不提供 'uname', 'fork' 等方法
###################################################

# 练习: 能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
CURPATH = os.path.abspath('.')
name = input('输入要查找的文件名: ')

def find_file(name, dir):
    for f in os.listdir(dir):
        f = os.path.join(dir, f)
        if os.path.isfile(f) and name in f:
            print(f)
        elif os.path.isdir(f):
            find_file(name, f)

print('find \'%s\' i    n \'%s\'' % (name, CURPATH))
find_file(name, CURPATH)
