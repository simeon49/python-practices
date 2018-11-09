# coding=utf-8
import time

# 方法1: 协程
# def consumer():
#     print('Consumer is running..')
#     while True:
#         n = yield
#         if not n:
#             return
#         print('consuming {}'.format(n))


# def produce(c):
#     c.send(None)
#     times = 5
#     while times:
#         times -= 1
#         print('producing {}'.format(times))
#         r = c.send(times)
#     c.close()

# produce(consumer())

# 方法2: 多线程
import threading

def consumer(cond):
    with cond:
        cond.wait()
        print('consuming by {}'.format(threading.current_thread()))

def produce(cond):
    with cond:
        print('producing by {}'.format(threading.current_thread()))
        cond.notifyAll()

condition = threading.Condition()

c1 = threading.Thread(target=consumer, args=(condition,))
c2 = threading.Thread(target=consumer, args=(condition,))
p1 = threading.Thread(target=produce, args=(condition,))
c1.start()
c2.start()
p1.start()

c1.join()
c2.join()
p1.join()