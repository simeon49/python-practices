#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle

###################################################
#  序列化: 把变量从内存中变成可存储或传输的过程
###################################################
d = dict(name='Tom', age='21', score=99)

# dumps 将对象转换为二进制内容
bts = pickle.dumps(d)

# dump 将对象转换为二级制内容后写入 file-like(有read write 方法的对象) 中
with open('./base/15_io/dump.txt', 'bw') as f:
    pickle.dump(d, f)

###################################################
#  反序列化: 把存储中的内容转换为内存中的变量
###################################################
d1 = pickle.loads(bts)
print(d1)

with open('./base/15_io/dump.txt', 'br') as f:
    d2 = pickle.load(f)
    print(d2)



import json

###################################################
#  JSON
###################################################
s = json.dumps(d)
print(s)
d3 = json.loads(s)
print(d3)

# json class 对象
class Student(object):

    def __init__(self, name, age, score):
        super(Student, self).__init__()
        self.name = name
        self.age = age
        self.score = score

std1 = Student('Jack', 7, 77)
s = json.dumps(std1, default=lambda o: {
    'name': o.name,
    'age': o.age,
    'score': o.score
})
print(s)
std2 = json.loads(s, object_hook=lambda d: Student(d['name'], d['age'], d['score']))
print(std2.name)
