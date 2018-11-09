# -*- coding: utf8 -*-

class Database(object):

    def __init__(self, *args, **kwargs):
        self._connected = False

    def connect(self):
        self._connected = True

    def close(self):
        self._connected = False

    def query(self, query=''):
        assert self._connected, 'DB not connenctd'
        return 'query data'

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

# 1.普通方式
def handle_query_01():
    db = Database()
    db.connect()
    print('handle 01 ->: {}'.format(db.query()))
    db.close()

# 2.使用装饰器
def dbconn(fn):
    def wrapper(*args, **kwargs):
        db = Database()
        db.connect()
        ret = fn(db, *args, **kwargs)
        db.close()
        return ret
    return wrapper

@dbconn
def handle_query_02(db):
    print('handle 02 ->: {}'.format(db.query()))

# 3.使用with as 方式
def handle_query_03():
    with Database() as db:
        print('handle 03 ->: {}'.format(db.query()))

if __name__ == '__main__':
    handle_query_01()
    handle_query_02()
    handle_query_03()
