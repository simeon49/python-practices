#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    协程: Coroutine [,kəuru:'ti:n]

'''

def consumer():
    r = '200 OK'
    while True:
        n = yield r
        print('[CONSUMER] Consuming %s...' % n)


def producer(c):
    c.send(None)
    for n in range(10):
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
    c.close()

c = consumer()
producer(c)
