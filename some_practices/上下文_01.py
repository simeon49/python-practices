# -*- coding: utf8 -*-

import tornado.ioloop
import tornado.stack_context

ioloop = tornado.ioloop.IOLoop.instance()

def job():
    print('do job.')
    raise ValueError('except in job')

def async_task():
    print('run async task')
    ioloop.add_callback(callback=job)

if __name__ == '__main__':
    try:
        async_task()
    except Exception as e:
        print('main exception: {}'.format(e))
    print('end')
    ioloop.start()
