# coding=utf-8

import time
import threading

def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        print('time use: {}'.format(end - start))
        return ret
    return wrapper

def fib(n, show=True):
    if n <= 2:
        return 1
    ret = fib(n - 1, False) + fib(n - 2, False)
    if show:
        print(ret)
    return ret

@timeit
def no_thread():
    fib(35)
    fib(35)

@timeit
def use_thread():
    for i in range(2):
        t = threading.Thread(target=fib, args=(35,))
        t.start()
    main_thread = threading.current_thread()
    for t in threading.enumerate():
        if t is main_thread:
            continue
        t.join()


no_thread()
use_thread()

time.sleep(20)
