# -*- coding: utf8 -*-

import tornado.ioloop
import tornado.stack_context
import functools

ioloop = tornado.ioloop.IOLoop.instance()

def job():
    print('do job.')
    raise ValueError('except in job')


def warrper(fun):
    try:
        return fun()
    except Exception as e:
        print('warrper exception: {}'.format(e))


def async_task():
    print('run async task')
    ioloop.add_callback(callback=functools.partial(warrper, job))


if __name__ == '__main__':
    async_task()
    print('end')
    ioloop.start()
