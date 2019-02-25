#!/usr/bin/env python
# -*- coding: utf-8 -*-

def say_hi(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<div> Hello, %s</div>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]
