#!/usr/bin/env python
# -*- coding: utf-8 -*-

###################################################
#  多继承
###################################################
class AMaxIn(object):
    def fooCom(self):
        print('fooCom in A')

    def fooA(self):
        print('fooA')

class BMaxIn(object):
    def fooCom(self):
        print('fooCom in B')

    def fooB(self):
        print('fooB')

class SubC(AMaxIn, BMaxIn):
    def fooC(self):
        print('fooC')

c = SubC()
c.fooA()    # fooA
c.fooB()    # fooB
c.fooC()    # fooC
c.fooCom()  # fooCom in A   # 参考: https://kevinguo.me/2018/01/19/python-topological-sorting/
