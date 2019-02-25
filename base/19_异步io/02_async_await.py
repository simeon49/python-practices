#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio
import random


'''
    了简化并更好地标识异步IO，从Python 3.5开始引入了新的语法async和await，可以让coroutine的代码更简洁易读
'''

async def producer(queue, id):
    for n in range(10):
        print('{} produce {}'.format(id, n))
        await queue.put(n)
        await asyncio.sleep(random.random())
    print('=========== {} is end =============='.format(id))

async def consumer(queue, id):
    times = 0
    while True:
        try:
            n = queue.get_nowait()
        except asyncio.QueueEmpty:
            times += 1
            if times > 3:
                break
        else:
            times = 0
            print('  {} consume {}'.format(id, n))
        await asyncio.sleep(random.random())
    print('=========== {} is end =============='.format(id))


queue = asyncio.Queue()
p1 = producer(queue, 'Producer A')
p2 = producer(queue, 'Producer B')

c1 = consumer(queue, 'Consumer 1')
c2 = consumer(queue, 'Consumer 2')
c3 = consumer(queue, 'Consumer 3')

loop = asyncio.get_event_loop()
producers = (p1, p2)
consumers = (c1, c2, c3)
tasks = [*producers, *consumers]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
