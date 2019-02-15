#!/usr/bin/env python
# -*- coding: utf-8 -*-

###################################################
#  超级dict
###################################################

class SupperDict(dict):

    def __init__(self, **kw):
       super(SupperDict, self).__init__(**kw)

    def __getattr__(self, attr):
        try:
            return self[attr]
        except KeyError:
            raise AttributeError('\'%s\' object has no attribute \'%s\'' % (self.__class__.__name__, attr))

    def __setattr__(self, attr, value):
        self[attr] = value
