import threading
import asyncio
# 参考 http://python.jobbole.com/87310/

# python 3.4 写法
@asyncio.coroutine
def foo():
    print('start {}'.format(threading.current_thread()))
    yield from asyncio.sleep(3)
    print('end {}'.format(threading.current_thread()))

coroutines = [foo(), foo(), foo()]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(coroutines))
loop.close()


# python 3.5以后 写法
async def foo():
    print('start {}'.format(threading.current_thread()))
    r = await asyncio.sleep(3)
    print('end {}'.format(threading.current_thread()))

coroutines = [foo(), foo(), foo()]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(coroutines))
loop.close()

# 获取返回结果
async def foo():
    return 'ok'

coroutine = foo()
task = asyncio.ensure_future(coroutine)
loop = asyncio.get_event_loop()
loop.run_until_complete(task)
task.result()

# 绑定回调
async def foo():
    return 'ok'

def call_back(future):
    print('call back: {}'.format(future.result()))

coroutine = foo()
task = asyncio.ensure_future(coroutine)
task.add_done_callback(call_back)
loop =asyncio.get_event_loop()
loop.run_until_complete(task)

# 协程嵌套
async def foo(time):
    await asyncio.sleep(time)
    return time

async def do_all():
    coroutine1 = foo(1)
    coroutine2 = foo(2)
    coroutine3 = foo(4)

    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3)
    ]
    dones, pendings = await asyncio.wait(tasks)
    for task in dones:
        print('task result: {}'.format(task.result()))

loop = asyncio.get_event_loop()
loop.run_until_complete(do_all)

# 不同线程的事件循环

import threading
import asyncio

def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()

async def foo(time):
    print('start () {}'.format(time, threading.current_thread()))
    await asyncio.sleep(time)
    print('end () {}'.format(time, threading.current_thread()))

new_loop = asyncio.new_event_loop()
t = threading.Thread(target=start_loop, args=(new_loop,))
t.setDaemon(True)
t.start()

asyncio.run_coroutine_threadsafe(foo(1), new_loop)
asyncio.run_coroutine_threadsafe(foo(2), new_loop)
asyncio.run_coroutine_threadsafe(foo(4), new_loop)
t.join()



# 实例1: 网络请求
async def wget(host):
    print('wget {}...'.format(host))
    connect = await asyncio.open_connection(host, 80)
    reader, writer = counnet
    header = 'GET / HTTP/1.0\r\nHost: {}\r\n\r\n'.format(host)
    writer.write(header.encode('utf-8'))
    await writer.drain()
    while True:
        line = await reader.readline()
        if line == bbb'\r\n':
            break
        print('{} header > {}'.format(host, line.decode('utf-8').rstrip()))
    writer.close()
    return '{} ok'.format(host)
loop = asyncio.get_event_loop()
coroutines = [wget(host) for host in ('www.baidu.com', 'www.sina.com', 'www.163.com')]

loop.run_until_complete(asyncio.wait(coroutines))



async def foo1():
    print('start foo')
    await time.sleep(3)
    print('end foo')
    return 'foo ok'

async def foo2():
    print('start foo1')
    await asyncio.sleep(3)
    print('end foo1')
    return 'foo1 ok'

coroutine1 = foo1()
coroutine2 = foo2()
loop = asyncio.get_event_loop()
task1 = asyncio.create_task(coroutine1)
task2 = asyncio.create_task(coroutine2)

loop.run_until_complete(task1)


# ================= 实现原理参考 =================

# task 实现模型
class Task(asyncio.futures.Future):
    def __init__(self, gen, *, loop):
        super(Task, self).__init__(loop=loop)
        self._gen = gen
        self._loop.call_soon(self._step)

    def _step(self, val=None, exc=None):
        try:
            if exc:
                f = self._gen.throw(exc)
            else:
                f = self._gen.send(val)
        except StopIteration as e:
            self.set_result(e.value)
        except Exception as e:
            self.set_exception(e)
        else:
            f.add_done_callback(self.wakeup)

    def _wakeup(self, fut):
        try:
            ret = fut.result()
        except Exception as e:
            self._setp(None, e)
        else:
            self._setp(ret, None)


# loop 实现模型
def done_callback(fut):
    fut._loop.stop()


class Loop:
    def __init__(self):
        self._ready = deque()
        self._stopping = False

    def create_task(self, coro):
        Task = asyncio.tasks.Task
        task = Task(coro, loop=self)
        return task

    def run_until_complete(self, fut):
        tasks = asyncio.tasks
        # 获取任务
        fut = tasks.ensure_future(
                    fut, loop=self)
        # 增加任务到self._ready
        fut.add_done_callback(done_callback)
        # 跑全部任务
        self.run_forever()
        # 从self._ready中移除
        fut.remove_done_callback(done_callback)

    def run_forever(self):
        try:
            while 1:
                self._run_once()
                if self._stopping:
                    break
        finally:
            self._stopping = False

    def call_soon(self, cb, *args):
        self._ready.append((cb, args))

    def _run_once(self):
        ntodo = len(self._ready)
        for i in range(ntodo):
            t, a = self._ready.popleft()
            t(*a)

    def stop(self):
        self._stopping = True

    def close(self):
        self._ready.clear()

    def call_exception_handler(self, c):
        pass

    def get_debug(self):
        return False


async def foo():
    print('Hello Foo')


async def bar():
    print('Hello Bar')

loop = Loop()
tasks = [loop.create_task(foo()),
         loop.create_task(bar())]
loop.run_until_complete(
        asyncio.wait(tasks))
loop.close()