#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 注意: 这里的练习不能再调试中测试!!!!!

import os
import time
import random

print('Cur pid is %s' % os.getpid())

#############################
#  os.fork 系统提供的接口(只在unix/linx)上有该接口
#############################
print('====== os.fork ======')
pid = os.fork()
if pid == 0:
    print('  > child process %s.' % os.getpid())
    exit()  # 让子进程退出
else:
    print('  > parent process %s' % os.getpid())


#############################
#  multiprocessing.Process:  python封装的一个进程库
#############################
from multiprocessing import Process

def run_proc(*args, **kw):
    print('child process %s, args=%s kw=%s' % (os.getpid(), args, kw))

print('====== multiprocessing.Process ======')
p = Process(target=run_proc, args=(1,2,3), kwargs={'a': 1})
p.start()
p.join()


#############################
#  multiprocessing.Pool 进程池
#############################
from multiprocessing import Pool

def run_proc_1(*args, **kw):
    start = time.time()
    time.sleep(random.random() * 2)
    print('  [%s] job done, time used %s' % (os.getpid(), time.time() - start))

print('====== multiprocessing.Pool ======')
p = Pool(3)
start = time.time()
for i in range(5):
    p.apply_async(run_proc_1)
p.close()   # 调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
p.join()
print('time used: %s' % (time.time() - start))


#############################
#  subporcess: 用于调用外部程序
#############################
import subprocess

print('====== subprocess ======')
# 查询 baidu ip
print('$ nslookup www.baidu.com')
r = subprocess.call(['nslookup', 'www.baidu.com'])
print('Exit code:', r)

# 如果子进程需要输入
print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\nwww.baidu.com\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)

#############################
#  进程间通信: Queue 消息队列
#############################
from multiprocessing import Process, Queue

print('====== multiprocessing.Queue ======')
def producer(q):
    for fruit in ['apple', 'tangerine', 'orange', 'banana']:
        print('  > produce "%s"' % fruit)
        q.put(fruit)
        time.sleep(random.random())

def consumer(q):
    while True:
        fruit = q.get(True)
        print('  < eat "%s"' % fruit)

q = Queue()
p1 = Process(target=producer, args=(q,))
c1 = Process(target=consumer, args=(q,))
c2 = Process(target=consumer, args=(q,))
p1.start()
c1.start()
c2.start()
p1.join()       # 等待生产者结束
c1.terminate()  # 进程里是死循环，无法等待其结束，只能强行终止:
c2.terminate()  # 进程里是死循环，无法等待其结束，只能强行终止:

#############################
#  进程间通信: Pipes 管道
#############################
