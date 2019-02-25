# -*- coding: utf-8 -*

import re
import os
import json
import inspect
import asyncio
import functools
import logging; logging.basicConfig(level=logging.DEBUG)

from urllib import parse
from aiohttp import web

def get(path):
    '''Get'''
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kw):
            return fn(*args, **kw)
        wrapper.__method__ = 'GET'
        wrapper.__route__ = path
        return wrapper
    return decorator

def post(path):
    '''Post'''
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kw):
            return fn(*args, **kw)
        wrapper.__method__ = 'POST'
        wrapper.__route__ = path
        return wrapper
    return decorator

def add_route(app, handler):
    method = getattr(handler, '__method__', None)
    path = getattr(handler, '__route__', None)
    if method is None or path is None:
        raise ValueError(f'@get or @post not defined in {str(handler.__name__)}')
    if not inspect.iscoroutinefunction(handler) and not inspect.isgeneratorfunction(handler):
        handler = asyncio.coroutine(handler)
    logging.info(f'add route {method} {path} => {handler.__name__}({", ".join(inspect.signature(handler).parameters.keys())})')
    app.router.add_route(method, path, handler=RequestHandler(app, handler))

def add_routers(app, model_names):
    for model_name in model_names:
        index = model_name.rfind('.')
        if index == -1:
            model = __import__(model_name)
        else:
            name = model_name[index+1:]
            model = getattr(__import__(model_name[:index], fromlist=[name]), name)

        for method in dir(model):
            if method.startswith('_'):
                continue
            fn = getattr(model, method)
            if callable(fn):
                if hasattr(fn, '__method__') and hasattr(fn, '__route__'):
                    add_route(app, fn)

def add_static(app, path):
    if not os.path.isdir(path):
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), path)
    app.router.add_static('/static/', path)
    logging.info(f'add static "/static/" => "{path}"')


class APIError(Exception):

    def __init__(self, error, data='', message=''):
        super().__init__(message)
        self.error = error
        self.data = data
        self.message = message


def get_required_kw_args(fn):
    args = []
    params = inspect.signature(fn).parameters
    for name, param in params.items():
        if param.kind == inspect.Parameter.KEYWORD_ONLY and param.default == inspect.Parameter.empty:
            args.append(name)
    return tuple(args)


def get_named_kw_args(fn):
    args = []
    params = inspect.signature(fn).parameters
    for name, param in params.items():
        if param.kind == inspect.Parameter.KEYWORD_ONLY:
            args.append(name)
    return tuple(args)


def has_named_kw_args(fn):
    params = inspect.signature(fn).parameters
    for name, param in params.items():
        if param.kind == inspect.Parameter.KEYWORD_ONLY:
            return True


def has_var_kw_arg(fn):
    params = inspect.signature(fn).parameters
    for name, param in params.items():
        if param.kind == inspect.Parameter.VAR_KEYWORD:
            return True


def has_request_arg(fn):
    sig = inspect.signature(fn)
    params = sig.parameters
    found = False
    for name, param in params.items():
        if name == 'request':
            found = True
            continue
        if found and (param.kind != inspect.Parameter.VAR_POSITIONAL and param.kind != inspect.Parameter.KEYWORD_ONLY and param.kind != inspect.Parameter.VAR_KEYWORD):
            raise ValueError('request parameter must be the last named parameter in function: %s%s' % (
                fn.__name__, str(sig)))
    return found

class RequestHandler(object):
    '''
    从url函数中分析其需要的参数, 并从request中获取必要的参数, 调用url函数, 然后把结果转换为web.Request对象
    '''

    # ROUTE_RE = re.compile(r'\{([_a-zA-Z][_a-zA-Z0-9]*?)\}')

    def __init__(self, app, handler):
        self._app = app
        self._handler = handler
        self._has_request_arg = has_request_arg(handler)
        self._has_var_kw_arg = has_var_kw_arg(handler)
        self._has_named_kw_args = has_named_kw_args(handler)
        self._named_kw_args = get_named_kw_args(handler)
        self._required_kw_args = get_required_kw_args(handler)


    async def __call__(self, request):
        kw = None
        if self._has_var_kw_arg or self._has_named_kw_args or self._required_kw_args:
            if request.method == 'POST':
                if not request.content_type:
                    return web.HTTPBadRequest(text='Missing Content-Type.')
                ct = request.content_type.lower()
                if ct.startswith('application/json'):
                    try:
                        kw = await request.json()
                    except json.decoder.JSONDecodeError:
                        return web.HTTPBadRequest(text='JSON body must be object.')
                elif ct.startswith('application/x-www-form-urlencoded') or ct.startswith('multipart/form-data'):
                    kw = await request.post()
                else:
                    return web.HTTPBadRequest(text=f'Unsupported Content-Type: {request.content_type}')
            elif request.method == 'GET':
                qs = request.query_string
                if qs:
                    kw = dict()
                    for k, v in parse.parse_qs(qs, True).items():
                        kw[k] = v[0]

        if kw is None:
            kw = dict(**request.match_info)
        else:
            if not self._has_var_kw_arg and self._named_kw_args:
                # remove all unamed kw:
                copy = dict()
                for name in self._named_kw_args:
                    if name in kw:
                        copy[name] = kw[name]
                kw = copy
            # check named arg:
            for k, v in request.match_info.items():
                if k in kw:
                    logging.warning(
                        'Duplicate arg name in named arg and kw args: %s' % k)
                kw[k] = v
        if self._has_request_arg:
            kw['request'] = request
        # check required kw:
        if self._required_kw_args:
            for name in self._required_kw_args:
                if not name in kw:
                    return web.HTTPBadRequest(text='Missing argument: %s' % name)
        logging.info(f'call with args: {str(kw)}')
        try:
            res = await self._handler(**kw)
            return res
        except APIError as e:
            return dict(error=e.error, data=e.data, message=e.message)
