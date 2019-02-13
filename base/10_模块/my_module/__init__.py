#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'this is a test module'

__author__ = 'Simeon'

def say_hi(*args):
    if len(args) == 0:
        print('Hi, world!')
    elif len(args) == 1:
        print('Hi, %s' % args[0])
    else:
        print('Too many argument!')

if __name__ == '__main__':
    say_hi()
    say_hi('Simeon')
