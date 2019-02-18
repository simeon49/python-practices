#!/usr/bin/env python
# -*- coding: utf-8 -*-

# python 标准库提供了两个模块: _thread(低级模块) threading(高级模块 对_thread进行封装)

import time
import random
import _thread
import threading


def job(thread_type):
    start = time.time()
    thread_name = ''
    if thread_type == '_thread':
        thread_name = _thread.get_ident()
    else:
        thread_name = threading.current_thread().name
    print('thread %s is running...' % thread_name)
    time.sleep(random.random())
    print('thread %s is end. time used: %s' % (thread_name, time.time() - start))


###################################################
#  _thread
###################################################
print('============= _thread =============')
_thread.start_new_thread(job, ('_thread',))  # 如果主线程结束, 创建的子线程也会结束
time.sleep(1)


###################################################
#  threading
###################################################
print('============= threading =============')
t = threading.Thread(target=job, name='job_thread', args=('threading', ))
t.start()
t.join()    # 等待子线程结束

###################################################
#  threading 锁
###################################################
print('============= threading.Lock =============')
balance = 0
lock = threading.Lock()

def run_thread(n):
    for i in range(1000000):
        lock.acquire()
        try:
            global balance
            balance += n
            balance -= n
        finally:
            pass
            lock.release()

t = threading.Thread(target=run_thread, args=(3,))
t2 = threading.Thread(target=run_thread, args=(5,))
t.start()
t2.start()
t.join()
t2.join()
print('balance: %s' % balance)

###################################################
#  threading.local: 虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。
# ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。
###################################################
print('============= threading.Lock =============')
local_info = threading.local()

def printUserInfo():
    print(local_info.user)

def run_thread2(name, phone):
    local_info.user = {'name': name, 'phone': phone}
    printUserInfo()

t1 = threading.Thread(target=run_thread2, args=('Tom', '1364409918'))
t2 = threading.Thread(target=run_thread2, args=('Jack', '15828205867'))
t1.start()
t2.start()
t1.join()
t2.join()


###################################################
# GIL:  python的线程虽然是真正的线程, 但解释器(官方的CPython)有一个GIL锁(Golabel interpreter look)
# 在python任何线程执行前必须先获得GIL锁, 然后每执行100条字节码, 解释器就自动释放GIL锁, 让其它线程可以
# 执行, 所以在单个进程中即使有多个线程 这些线程也只能交替执行, 注意 每个进程有这个GIL锁
###################################################
import multiprocessing

def loop():
    x = 0
    while True:
        x = x ^ 1

# 多线程死循环在多核CPU下 只能占用100%左右
for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()

# 解决pyhon GIL问题的办法

# 1.使用用多进程: 多进程不存在这个问题 可以占到 CPU核数*100%
p = multiprocessing.Pool(multiprocessing.cpu_count())
for i in range(multiprocessing.cpu_count()):
    p.apply_async(loop)
p.close()
# p.join()

# 2.使用多线程load C modle 执行
import ctypes
lib = ctypes.cdll.LoadLibrary('./base/16_进程与线程/liba.so')
for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=lib.loop)
    t.start()
