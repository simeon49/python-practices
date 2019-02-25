#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    python 自带的 asyncio 库,实现了单线程的io并发操作, 实现了如TCP, UDP, SSL等协议,
    aiohttp 是基于asyncio实现的http框架

    pip install aiohttp
'''

import asyncio

from aiohttp import web

async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>')

async def hello(request):
    await asyncio.sleep(0.5)
    text = '<div>Hi, {}!</div>'.format(request.match_info.get('name', 'Anonymous'))
    return web.Response(body=text.encode('utf-8'))

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    srv = await loop.create_server(app.make_handler(), '0.0.0.0', 8000)
    print('Server started at http://0.0.0.0:8000 ....')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
