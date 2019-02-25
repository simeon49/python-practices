#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    WSGI: web server gateway interface
    一个web应用的本质就是:
        1.浏览器发送一个http请求
        2.服务器收到请求, 生成一个HTML文档
        3.服务器把HTML文档作为http响应的body发送给浏览器
        4.浏览器收到http响应, 显示html文档

    如果要从底层实现web server 需要从TCP链接开始,并处理http请求和响应格式...

    wsgi帮助我们实现上面的功能
'''

from wsgiref.simple_server import make_server
from app import say_hi

httpd = make_server('', 8000, say_hi)
print('Serving http on port 8000...')
httpd.serve_forever()
