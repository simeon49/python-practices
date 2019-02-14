#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 最简单的函数
def foo():
    print('hi')
foo() # hi

# 返回值
def foo2():
    return 1, 2
a, b = foo2()

# 参数
def foo3(a):
    print(a)
foo3('test')

# 参数(默认参数)
def power(x, n=2):
    s = 1
    while n > 0:
        s *= x
        n -= 1
    return s

power(5) # 25
power(3, 4) # 81

# 参数(注意 这个会有问题, Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。)
# 定义默认参数要牢记一点：默认参数必须指向不变对象！
def foo4(s, l=[]):
    assert isinstance(l, list), 'l is not list'
    l.append(s)
    print(l)
    return l

foo4('A') # ['A']
foo4('B') # ['A', 'B']

# 解决办法
def foo4_new(s, l=None):
    if l is None:
        l = []
    assert isinstance(l, list), 'l is not list'
    l.append(s)
    print(l)
    return l

foo4_new('A') # ['A']
foo4_new('B') # ['B']


# 参数(可变参数)
def foo5(*args):
    for arg in args:
        print(arg)

foo5(1,2,3,4,5)
foo5(*['a', 'b', 'c'])

# 参数(关键字参数)
def foo6(**kw):
    for key, value in kw.items():
        print('%s = %s' % (key, value))

foo6(a=1, b=2)
foo6(**{'a': 1, 'b': 2})

# 参数(命名关键字参数)
def foo7(name, age, *, city, job): # city 和job 是必须参数
    pass

foo7('Tom', 12, city="shanghai", job="engineer")


# 递归
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

fact(5) # 120
try:
    fact(5000)
except RuntimeError as e:
    print('RuntimeError:', e)

# 尾递归(一些语言的解释器对尾递归做了优化, 调用栈不会增加, 可惜python没有做优化)
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


try:
    fact(5000)
except RuntimeError as e:
    print('RuntimeError:', e)
