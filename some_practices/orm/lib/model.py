#!/usr/bin/env python
# -*- coding: utf-8 -*-

from copy import deepcopy

from .field import Field
from .utils import camel2underline

class ORMMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)

        print('Found model: %s' % name)
        mappings = {}
        for key, value in list(attrs.items()):
            if isinstance(value, Field):
                mappings[key] = value
                del attrs[key]
        attrs['__mappings__'] = mappings
        attrs['__table__'] = camel2underline(name)
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ORMMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError('\'%s\' object has no attribute \'%s\'!' % (self.__class__.__name__, key))

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for key, filed in self.__mappings__.items():
            fields.append(filed.name)
            params.append('?')
            args.append(getattr(self, key, None))

        sql = 'insert into table `%s` (%s) values(%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL:', sql)
        print('ARGS:', args)
