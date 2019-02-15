#!/usr/bin/env python
# -*- coding: utf-8 -*-

###################################################
#  文档测试
#     参考: https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319170285543a4d04751f8846908770660de849f285000
###################################################


class SupperDict(dict):
    '''
    Simple dict but also support access x.y style.

    >>> d1 = SupperDict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = SupperDict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'SupperDict' object has no attribute 'empty'
    '''

    def __init__(self, **kw):
       super(SupperDict, self).__init__(**kw)

    def __getattr__(self, attr):
        try:
            return self[attr]
        except KeyError:
            raise AttributeError('\'%s\' object has no attribute \'%s\'' % (
                self.__class__.__name__, attr))

    def __setattr__(self, attr, value):
        self[attr] = value

if __name__ == '__main__':
    import doctest
    doctest.testmod()
