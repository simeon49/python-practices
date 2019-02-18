#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, queue
from multiprocessing.managers import BaseManager

###################################################
#  worker: 执行任务
###################################################
print('============= worker =============')

PORT = 5000

class QuequeManager(BaseManager):
    pass

QuequeManager.register('get_task_queue')
QuequeManager.register('get_result_queue')

server_addr = input('请输入master服务器ip: ')
print('Connenct to server %s:%s...' % (server_addr, PORT))
m = QuequeManager(address=(server_addr, PORT), authkey=b'secret_world')
m.connect()

task = m.get_task_queue()
result = m.get_result_queue()
while True:
    try:
        n = task.get(timeout=1)
        print('run taks %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n * n)
        time.sleep(1)
        result.put(r)
    except queue.Empty:
        print('task is empty.')
        break
    except EOFError:
        print('master is exit.')
        break

print('worker exit.')
