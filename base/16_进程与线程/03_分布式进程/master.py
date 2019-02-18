#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random, time, queue, json
from urllib.request import urlopen
from multiprocessing.managers import BaseManager

PORT = 5000

###################################################
#  master: 发布任务
###################################################
print('============= master =============')
print('get warn ip...')
IP = json.load(urlopen('http://jsonip.com'))['ip']
print('IP: %s Port: %s' % (IP, PORT))


# 发送任务的队列
task_queue = queue.Queue()
# 接收结果的队列
result_queue = queue.Queue()

class QueueManager(BaseManager):
    pass

# 将队列暴露到网络中
QueueManager.register('get_task_queue', lambda: task_queue)
QueueManager.register('get_result_queue', lambda: result_queue)

# 绑定端口5000, 验证码 b'secret_world'
manager = QueueManager(address=('', PORT), authkey=b'secret_world')
manager.start()

task = manager.get_task_queue()
result = manager.get_result_queue()

for i in range(10):
    n = random.randint(0, 10000)
    print('Put task %d' % n)
    task.put(n)

print('Try get results...')
try:
    for i in range(10):
        r = result.get(timeout=3)
        print('Result: %s' % r)
except queue.Empty:
    print('error: timeout, get nothing.')
finally:
    manager.shutdown()
    print('master exit.')
