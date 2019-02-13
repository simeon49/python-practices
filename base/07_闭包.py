#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 利用闭包返回一个计数器函数，每次调用它返回递增整数：

def createCounter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

countterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
