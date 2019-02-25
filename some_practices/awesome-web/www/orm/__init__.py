#!/usr/bin/env python
# -*- coding: utf-8 -*

import time
import asyncio
import aiomysql
import itertools

import logging; logging.basicConfig(level=logging.DEBUG)

from pymysql.err import ProgrammingError

__pool = None


async def create_pool(minsize=1, maxsize=10, loop=None, echo=False, **kw):
    """
    参考: https://aiomysql.readthedocs.io/en/latest/pool.html
    """
    global __pool
    __pool = await aiomysql.create_pool(
        host=kw.get('host', 'localhost'),
        port=kw.get('port', 3306),
        user=kw['user'],
        password=kw.get('password', ''),
        db=kw['db'],
        charset=kw.get('charset', 'utf8'),
        autocommit=kw.get('autocommit', True),
        minsize=minsize,
        maxsize=maxsize,
        loop=loop,
        echo=echo
    )

def close():
    global __pool
    __pool.close()

async def wait_closed():
    global __pool
    await __pool.wait_closed()

async def select(query, args=None, size=None):
    global __pool
    async with __pool.acquire() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cur:
            await cur.execute(query.replace('?', '%s'), args or ())
            if size:
                rs = await cur.fetchmany(size)
            else:
                rs = await cur.fetchall()
    return rs

async def execute(query, args=None):
    global __pool
    async with __pool.acquire() as conn:
        auto_commit = conn.get_autocommit()
        if not auto_commit:
            conn.begin()
        async with conn.cursor() as cur:
            try:
                await cur.execute(query.replace('?', '%s'), args or ())
                affected = cur.rowcount
                rs = await cur.fetchone()
                if not auto_commit:
                    await conn.commit()
            except ProgrammingError as e:
                if not auto_commit:
                    await conn.rollback()
                raise
        return (affected, rs)

class Field(object):

    def __init__(self, column_type, primary_key, auto_increment=False, default=None, unique=False):
        self.column_type = column_type
        self.primary_key = primary_key
        self.auto_increment = auto_increment
        self.default = default
        self.unique = unique

    def __str__(self):
        return '<%s, %s>' % (self.__class__.__name__, self.column_type)


class AutoIncrementPrimaryField(Field):

    def __init__(self):
        super().__init__('int', primary_key=True, auto_increment=True)


class IntegerField(Field):

    def __init__(self, primary_key=False, default=0, **kw):
        super().__init__('bigint', primary_key, default=default, **kw)


class StringField(Field):

    def __init__(self, primary_key=False, default='', ddl='varchar(100)', **kw):
        super().__init__(ddl, primary_key, default=default, **kw)


class FloatField(Field):

    def __init__(self, primary_key=False, default=0.0, **kw):
        super().__init__('real', primary_key, default=default, **kw)


class BooleanField(Field):

    def __init__(self, default=False):
        super().__init__('boolean', False, default=default)


class TextField(Field):

    def __init__(self, default=None):
        super().__init__('text', False, default=default)


class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)

        table_name = attrs['__table__'] if '__table__' in attrs else name
        mappings = dict()
        fields = []
        primary_key = None
        for key, item in attrs.items():
            if not isinstance(item, Field):
                continue
            mappings[key] = item
            if item.primary_key:
                if primary_key:
                    raise Exception(f'Duplicate primary key for field: {key}')
                primary_key = key
            else:
                fields.append(key)
        if not primary_key:
            raise Exception('Primary key not found.')
        for key in mappings.keys():
            attrs.pop(key)
        attrs['__mappings__'] = mappings
        attrs['__fields__'] = fields
        attrs['__primary_key__'] = primary_key
        attrs['__table__'] = table_name

        attrs['__select__'] = 'select `%s`, %s from `%s`' % (primary_key, ', '.join(fields), table_name)
        attrs['__insert__'] = f'insert into `{table_name}` ({primary_key}, {", ".join(fields)}) values ({", ".join(["?" for i in range(len(fields) + 1)])}); SELECT @@IDENTITY;'
        attrs['__update__'] = 'update `%s` set %s where `%s`=?' % (table_name, ', '.join(map(lambda key: '`%s`=?' % key, fields)), primary_key)
        attrs['__delete__'] = 'delete from `%s` where `%s`=?' % (table_name, primary_key)
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(f'"{self.__class__.__name__}" object has no attribute "{key}"')

    def __setitem__(self, key, value):
        self[key] = value

    def getValue(self, key):
        return getattr(self, key, None)

    def get_value_or_default(self, key):
        '''获取key的值或默认值'''

        if hasattr(self, key):
            return getattr(self, key)
        value = None
        field = self.__mappings__[key]
        if field.default is not None:
            value = field.default() if callable(field.default) else field.default
            setattr(self, key, value)
        return value

    @classmethod
    async def create_table_if_not_exists(cls):
        '''创建表'''

        fields_sqls = [
            f'{key} {item.column_type} not null {"auto_increment" if item.auto_increment else ""} {"unique" if item.unique else ""}' for key, item in cls.__mappings__.items()]
        primary_key_sql = f'primary key (`{cls.__primary_key__}`)'
        query = f'create table if not exists {cls.__table__}({", ".join(fields_sqls)}, {primary_key_sql}) engine=innodb default charset=utf8;'
        # logging.debug(query)
        await execute(query)

    @classmethod
    async def findAll(cls, where=None, args=None, **kw):
        ' find objects by where clause. '
        sql = [cls.__select__]
        if where:
            sql.append('where')
            sql.append(where)
        if args is None:
            args = []
        orderBy = kw.get('orderBy', None)
        if orderBy:
            sql.append('order by')
            sql.append(orderBy)
        limit = kw.get('limit', None)
        if limit is not None:
            sql.append('limit')
            if isinstance(limit, int):
                sql.append('?')
                args.append(limit)
            elif isinstance(limit, tuple) and len(limit) == 2:
                sql.append('?, ?')
                args.extend(limit)
            else:
                raise ValueError('Invalid limit value: %s' % str(limit))
        rs = await select(' '.join(sql), args)
        return [cls(**r) for r in rs]

    @classmethod
    async def findNumber(cls, selectField, where=None, args=None):
        ' find number by select and where. '
        sql = ['select %s _num_ from `%s`' % (selectField, cls.__table__)]
        if where:
            sql.append('where')
            sql.append(where)
        rs = await select(' '.join(sql), args, 1)
        if len(rs) == 0:
            return None
        return rs[0]['_num_']

    @classmethod
    async def find(cls, pk):
        ' find object by primary key. '
        rs = await select('%s where `%s`=?' % (cls.__select__, cls.__primary_key__), [pk], 1)
        if len(rs) == 0:
            return None
        return cls(**rs[0])

    async def save(self):
        affected, rs = await execute(self.__insert__, list(map(self.get_value_or_default, [self.__primary_key__, *self.__fields__])))
        if affected != 1:
            logging.warn(f'failed to insert record: affected ${affected}')

    async def update(self):
        args = list(map(self.getValue, self.__fields__))
        args.append(self.getValue(self.__primary_key__))
        rows = await execute(self.__update__, args)
        if rows != 1:
            logging.warn(
                'failed to update by primary key: affected rows: %s' % rows)

    async def remove(self):
        args = [self.getValue(self.__primary_key__)]
        rows = await execute(self.__delete__, args)
        if rows != 1:
            logging.warn(
                'failed to remove by primary key: affected rows: %s' % rows)


if __name__ == '__main__':
    class User(Model):
        __table__ = 'user'

        id = AutoIncrementPrimaryField()
        email = StringField(ddl='varchar(50)')
        name = StringField(ddl='varchar(50)')
        password = StringField(ddl='varchar(50)')
        avatar = StringField(ddl='varchar(500)')
        create_date = FloatField(default=time.time)

    async def test():
        await create_pool(host='localhost', user='root', password='123456', db='my_test', echo=True)
        _, rs = await execute('SELECT @@IDENTITY;select 42; ')
        await User.create_table_if_not_exists()

        user = User(email='qixiyi@yeah.net', name='Simeon',
                    password='pwd123', avatar='https://www.xxxx.com/ssssss.jpg')
        await user.save()
        print(await User.find(pk=1))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(test())
