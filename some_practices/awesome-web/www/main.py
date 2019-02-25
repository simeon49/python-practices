#!/usr/bin/env python
# -*- coding: utf-8 -*

import json
import asyncio
import logging; logging.basicConfig(level=logging.DEBUG)

from aiohttp import web
from setting import config  # 配置
from orm import create_pool
from models import User, Blog  # 模型
from core_web import add_routers, add_static


@web.middleware
async def response_middelware(request, handler):
    r = await handler(request)
    if isinstance(r, web.StreamResponse):
        return r
    elif isinstance(r, bytes):
        resp = web.Response(body=r)
        resp.content_type = 'application/octet-stream'
    elif isinstance(r, str):
        if r.startswith('redirect:'):
            return web.HTTPFound(r[9:])
        resp = web.Response(body=r.encode('utf-8'))
        resp.content_type = 'text/html;charset=utf-8'
        return resp
    if isinstance(r, dict):
        template = r.get('__template__')
        if template is None:
            resp = web.Response(body=json.dumps(
                r, ensure_ascii=False, default=lambda o: o.__dict__).encode('utf-8'))
            resp.content_type = 'application/json;charset=utf-8'
            return resp
        else:
            r['__user__'] = request.__user__
            resp = web.Response(body=app['__templating__'].get_template(
                template).render(**r).encode('utf-8'))
            resp.content_type = 'text/html;charset=utf-8'
            return resp
    if isinstance(r, int) and t >= 100 and t < 600:
        return web.Response(text=t)
    if isinstance(r, tuple) and len(r) == 2:
        t, m = r
        if isinstance(t, int) and t >= 100 and t < 600:
            return web.Response(t, str(m))
    # default:
    resp = web.Response(body=str(r).encode('utf-8'))
    resp.content_type = 'text/plain;charset=utf-8'
    return resp

async def init_db():
    await create_pool(**config['db'])
    await User.create_table_if_not_exists()
    await Blog.create_table_if_not_exists()

async def init_routers(app):
    add_routers(app, ['views.blog'])
    add_static(app, 'static')

async def get_server(loop):
    app = web.Application(loop=loop)
    await init_db()
    await init_routers(app)

    # 添加中间件
    app.middlewares.append(response_middelware)

    HOST = config['server']['host']
    PORT = config['server']['port']
    server = await loop.create_server(app.make_handler(), HOST, PORT)
    logging.info(f'Server started at {HOST}:{PORT}...')
    return server

loop = asyncio.get_event_loop()
loop.run_until_complete(get_server(loop))
loop.run_forever()
